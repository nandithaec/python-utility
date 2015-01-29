#!/usr/bin/env python

#Read in the pnr netlist, testbench and the entity name for the testbench, simulate it to create a file with FF outputs


#Modifications:
#Absolute paths introduced everywhere in the script, so that they can be run from one directory and no need of duplicating the scripts in all directories: June 25 2014

#1. Added an option to run Modelsim without invoking GUI. vsim -c. Errors will be written out to vsim.log file: 17th Dec 2013
##Example usage: python F0_python3_create_simdo_vsim_65.py -v F0_decoder_op_ip_modelsim.v -t /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm/test_decoder_opFF.vhd -b test_decoder_op_ip -r 200000ps -p /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm -d dec_0 -m decoder_op_ip -f outdecoder_reg_7_

##The pnr netlist is by default assumed to be in /pnr/op_data folder

import optparse
import re,os,csv
import time
import string
from optparse import OptionParser

parser = OptionParser("The script takes in the name of testbench, verilog pnr file, the DUT name and the name of the flip-flop that flipped at the 2nd rising edge of the clock. The clock cycle at which the flip-flop needs to be flipped needs to be known. Hence, the random clock cycle that was picked in the original simulation is taken as input. If clock cycle is 10, and if 1 clock period is 4000ps, then (10*4000)ps is the duration of the simulation. This clock cycle indicates the cycle in which the glitch injection takes place. The next rising edge is when the flip-flop needs to be fliiped. The simulation is stopped at this point, the value of the flip-flop is forced to its flipped value at the -ve edge of the 1st clk cycle, i.e., in this eg, at (10*4000)ps, and the simulation is continued for a clk cycle, so that the 2nd rising edge will clock-in the inverted value. Then the flip is released, by using 'noforce' command in modelsim and continued for another clock cycle. The values at the 3rd rising edge are stored.\n The files created are: F0_simulate_vsim.do and simdo.do file for modelsim.  The flip flop instance names (not the output names) are available in <path>_reference_out/flipflop_headers.csv. The flip-flop output which flipped is mapped to this flip-flop instance name inorder to freeze the value of the output.\n\n")


parser.add_option("-v","--rtl", help='Enter the post layout verilog netlist name along with its path that needs to be simulated',dest='rtl_pnr')
parser.add_option("-t","--test", help='Enter the path of the testbench (vhd/verilog) file for simulating the post layout RTL file, include the filename along with extension as part of this path',dest='test_path')
parser.add_option("-b","--tb_mod", help='Enter the test bench module name that needs to be simulated',dest='test_module')
parser.add_option("-r","--run", help='Enter the duration of the simulation run. e.g., 1us or 1 us',dest='runtime')
parser.add_option("-p", "--path", help="Enter the ENTIRE path to your design folder (your working dir)- /home/user1/simulations/<design_folder_name>",dest="path")
parser.add_option("-d", "--dut", help="Enter the DUT name in the test bench to which the entity is bound to the component",dest="dut")
parser.add_option("-m", "--module", help="Enter the main verilog/vhdl module name",dest="module")
parser.add_option("-f", "--flip", help="Enter the name of the flip-flop whose output flipped at 1st rising edge",dest="flip_ff")
parser.add_option("--period", help='Enter the clock period mentioned in the verilog testbench in ps',dest='period')

#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

rtl_pnr=options.rtl_pnr
test_path=options.test_path
test_module=options.test_module
runtime=options.runtime
path=options.path
dut=options.dut
module=options.module
flip_ff=options.flip_ff
period=int(options.period)

fl=open("%s/pnr/op_data/%s_final.v" %(path,module),"r")
lines=fl.readlines()

if 'q_reg' in open("%s/pnr/op_data/%s_final.v" %(path,module)).read():
	q_reg=1 #ISCAS
	print "ISCAS q_reg found"
else:
	q_reg=0	#ITC
	print "ITC q_reg not found"
	
fl.close()

Q_name=[]
for i in range(len(lines)):
	#print "Lines",lines[i]
	if q_reg==1: #ISCAS	
		if re.search("DFF",lines[i]): #This is for iscas
			words=lines[i].split()
			#print "**\n\n\nWords",words
			if words[2].startswith("(.q("): #3rd word is the Q node- capture the output node name- for iscas
				Q_name.append("q")
				#print "\nQ_name",Q_name
			
			#elif words[2].startswith("(.QN("): #3rd word is the QN node- capture the output node name- for ITC 
			elif words[2].startswith("(.QN("): #3rd word is the Q node- capture the output node name- for iscas
				Q_name.append("QN")
				#print "\nQ_name",Q_name

	elif q_reg==0: #ITC	
		if re.search("DFP",lines[i]): #This is for decoder
			words=lines[i].split()
			#print "**\n\n\nWords",words
			if words[2].startswith("(.Q("): #3rd word is the Q node- capture the output node name- for decoder and ITC 
				Q_name.append("Q")
				#print "\nQ_name",Q_name
			
			elif words[2].startswith("(.QN("): #3rd word is the QN node- capture the output node name- for ITC 
			#elif words[2].startswith("(.QN("): #3rd word is the Q node- capture the output node name- for iscas
				Q_name.append("QN")
				#print "\nQ_name",Q_name
			

fw = open('%s/F0_simulate_vsim.do' %path, 'w') ## This is the commands input file for modelsim
fdo = open('%s/simdo.do' %path, 'w') ## This is the do file for modelsim

#Write the following commands to this 'do' file
fw.write('set VLIB /home/users/nanditha/Documents/utility/65nm/CORE65GPSVT_nodelay.v\n\n')
if ".vhd" in test_path.lower():
	fw.write('set RTLLANG vhdl \nglobal toplevel \n')
else:
	fw.write('set RTLLANG verilog \nglobal toplevel \n')

fw.write('set TB %s \n' %test_path)

if ".vhd" in test_path.lower():
	fw.write('set LANG vhdl \n')
else:
	fw.write('set LANG verilog \n')

fw.write('set TB_TOP %s \n' %test_module)
fw.write('\n\nvlib work \n')
#fw.write('if { [string match "verilog" $LANG] == 1 } { \n')
fw.write('# TB and library inputs\n')

fw.write('vlog   $VLIB %s\n' %(rtl_pnr))

if ".vhd" in test_path.lower():
	fw.write('vcom $TB\n')
else:
	fw.write('vlog   $TB\n')


fw.write('# TB module name and THE simulate command\n')
fw.write('vsim -voptargs=+acc work.$TB_TOP -t 100ps \n\n')
fw.write('do simdo.do \n')
fw.write('\n\nquit -f \n ')
fw.close()
################################################################################

#Obtain the Flip-flop names
frtl = open('%s/%s_reference_out/flipflop_headers.csv' %(path,module), 'rb')
ff_reader=csv.reader(frtl)
ff_headers = ff_reader.next() #Flip flop names as obtained from the pnr file
print "\nFlipflop Header len:\n", (len(ff_headers)) #this is the actual number of flip-flops present
print "\nQ names len:\n", (len(Q_name)) #this is the actual number of flip-flop outputs present
print "\nflip-flop Headers[0]:", ff_headers[0]
print "\nflip-flop Headers:\n", ff_headers

for a in range(len(ff_headers)-1):
	print "Headers are: ",ff_headers[a]
	print "Q names are: ", Q_name[a]
	
	
frtl.close()


#Create the do file
fdo.write('.main clear\n')
fdo.write('add wave *\n')
for a in range(len(ff_headers)-1):
	ff_names=ff_headers[a]
	print "FF headers[a]",ff_names
	if dut=="NO_NAME":
		fdo.write("add wave {sim:/%s/%s/q}\n" %(test_module,ff_names))
		print "add wave {sim:/%s/%s/q}\n" %(test_module,ff_names)
	else:
		fdo.write("add wave {sim:/%s/%s/%s/%s}\n" %(test_module,dut,ff_names,Q_name[a])) #whether the output was Q or QN
		print "add wave {sim:/%s/%s/%s/%s}\n" %(test_module,dut,ff_names,Q_name[a])

if dut=="NO_NAME":
	fdo.write("add wave {sim:/%s/xor_%s/B}\n" %(test_module,flip_ff))
	fdo.write("add wave {sim:/%s/xor_%s/Z}\n" %(test_module,flip_ff))
else:
	fdo.write("add wave {sim:/%s/%s/xor_%s/B}\n" %(test_module,dut,flip_ff))
	fdo.write("add wave {sim:/%s/%s/xor_%s/Z}\n" %(test_module,dut,flip_ff))

fdo.write('run %s\n' %runtime)
#fdo.write('run 1.8ns\n')

#Force the 'B' input value of the XOR connected to the flip-flop to '1'.
#This will flip the flip-flop output
if dut=="NO_NAME":
	fdo.write('force -freeze sim:/%s/xor_%s/B St1 0\n' %(test_module,flip_ff))
else:
	fdo.write('force -freeze sim:/%s/%s/xor_%s/B St1 0\n' %(test_module,dut,flip_ff))

fdo.write('run %dps\n' %period) #This is because the clock period in the test bench was of 4000ps duration

#Release the flip by using no-force. Do not force it back to its previous value,since its value could be different in this clock cycle
if dut=="NO_NAME":
	fdo.write('noforce sim:/%s/xor_%s/B\n' %(test_module,flip_ff))
else:
	fdo.write('noforce sim:/%s/%s/xor_%s/B\n' %(test_module,dut,flip_ff))
	
multiple=int(1.5*period)
fdo.write('run %dps\n' %multiple) #This is because the clock period in the test bench was of 4000ps duration. Runningfor half clock cycle is good enough

################################################################################################

fdo.close()

os.chdir("%s" %path)

#Create the bash script to run modelsim with the above simulate_vsim.do file as the input
fw1 = open('%s/F0_run_sim.bash' %path, 'w') 
fw1.write('#!/bin/bash\n\n')
#Remove work directory if it exists
fw1.write('\\rm -rf %s/work\n' %path)

#Run simulation, do not invoke modelsim GUI
#fw1.write('vsim -c -do simulate_vsim.do >vsim.log\n')

#Run simulation, invoke modelsim
fw1.write('vsim -do %s/F0_simulate_vsim.do \n' %path)

fw1.close()
print "\n**DO FILE WRITTEN OUT***************INVOKING MODELSIM********************\n"
#time.sleep(3)

#Run the bash script
os.system('bash %s/F0_run_sim.bash' %path)	
#print "\n****Completed simulating the post layout verilog netlist.\n Reference FF outputs written\nCreated vsim.log..Check this file for log contents****"


