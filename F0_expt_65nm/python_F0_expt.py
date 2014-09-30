#!/usr/bin/env python

# Sep 4 2014

#Example usage: python python_F0_expt.py -m decoder_op_ip -f /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm/spice_results/decoder_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm/spice_results/decoder_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm/test_decoder_opFF.vhd --tb_mod test_decoder_op_ip --period 4000

#Example usage: python python_F0_expt.py -m c432 -f /home/users/nanditha/Documents/utility/65nm/c432/spice_results/c432_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/c432/spice_results/c432_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/c432 -b des_c432 --test_path /home/users/nanditha/Documents/utility/65nm/c432/test_c432.vhd --tb_mod test_c432 --period 4000

#Example usage: python python_F0_expt.py -m c432_clk_ipFF -f /home/users/nanditha/Documents/utility/65nm/c432/spice_results/c432_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/c432/spice_results/c432_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/c432 -b u1 --test_path /home/users/nanditha/Documents/utility/65nm/c432/test_c432.v --tb_mod test_c432 --period 20000


import optparse
import re,os
import csv, re
import random,time

#import python_compare_remote

from optparse import OptionParser


parser = OptionParser('This script reads in the <path>/spice_results/final_results_spice_outputs_%d.csv (spice output Flip-flop values) and <path>/<module>_reference_out/RTL_2nd_edge.csv (RTL reference output values) to compare the spice simulation (with glitch) output with the original RTL simulation (no glitch) output. Two files are written out:\n1. <path>/spice_results/spice_rtl_difference_%d.csv and\n2.<path>/spice_results/spice_rtl_diff_testing_%d.csv.\n Both contain essentially same data but the _testing file has both spice and RTL outputs so that the result in the other file can be verified by us.\nIt then counts the number of flips- single/double etc., each time this script is executed (for a group of simulations) and then backs up few decks randomly for each case- no_flip case, single,double flip and triple flip case. These decks are saved in backup_spice_decks folder and a separate folder is created for each of the no flip, single, double flips etc.,\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--file1", dest="file1",help="Enter the path and the file name of the file that contains 2nd edge flip summary in csv format")
parser.add_option("-g", "--file2",dest='file2', help='Enter the path and the file name of the file that contains 3rd edge flip summary in csv format')
parser.add_option("-p", "--path",dest='path', help='Enter the path to the design folder')
parser.add_option("-b", "--dut",dest='dut', help='Enter the name of the DUT which is instantiated within the testbench, to which the entity is bound with the component. Say "NO_NAME" if there is no dut name')
parser.add_option("--test_path", help='Enter the path of the testbench (vhd/verilog) file for simulating the post layout RTL file, include the filename along with extension as part of this path',dest='test_path')
parser.add_option("--tb_mod", help='Enter the test bench module name that needs to be simulated',dest='test_module')
parser.add_option("--period", help='Enter the clock period mentioned in the verilog testbench in ps',dest='period')

(options, args) = parser.parse_args()


module=options.module
file_edge2=options.file1
file_edge3=options.file2
path=options.path
dutname=options.dut
test_path=options.test_path
test_module=options.test_module
period=int(options.period)

#Removing the existing combined results file in the results folder
#if os.path.isfile("%s/spice_decks/results/count_flips.csv" %path):
#	print "****Removing the existing count_flips.csv in results folder****\n"
#	os.remove("%s/spice_decks/results/count_flips.csv" %path)

########################################################################################################
#Simulation without the flip being injected. This is the reference output
"""
os.system('perl perl_write_simfile_65.pl -v %s/pnr/op_data/%s_final.v -m %s -p %s' %(path,module,module,path))
print('Done executing perl_write_simfile_65.pl.. created modelsim simulation file\n')
#time.sleep(2)


runtime="100us"

os.system('python python3_create_simdo_vsim_65.py -v %s/%s_modelsim.v -t %s -b %s -r %s -p %s' %(path,module,test_path,test_module,runtime,path))
print('Done executing python3_create_simdo_vsim_65.py.. and modelsim simulation\n')
#time.sleep(2)
"""
########################################################################################################
#Add XORs to FF outputs in the verilog file
os.system('python python_xors_DFF_output.py -p %s -m %s' %(path,module))
print('Done executing python_xors_DFF_output.py\n')
#time.sleep(5)

#Write out file I/O statements to the verilog file and header of tool_reference_out file	
os.system('perl F0_perl_write_simfile_65.pl -v %s/pnr/op_data/%s_final_xors.v -m %s -p %s' %(path,module,module,path))
print('Done executing F0_perl_write_simfile_65.pl\n')
print "%s/pnr/op_data/F0_%s_modelsim.v written out.." %(path,module)
#time.sleep(5)


#These files will be appended to, in the followin script after every simulation 
f = open('%s/%s_reference_out/F0_tool_reference_out.txt' %(path,module), 'rb')
fwr = open('%s/%s_reference_out/F0_obtained.csv' %(path,module), 'wb')
F0_data=f.readlines()
header = F0_data[0]
words=header.split()
header=",".join(words) #Making it csv
fwr.writelines(header)
fwr.writelines("\n")
f.close()
fwr.close()


f = open('%s/%s_reference_out/tool_reference_out.txt' %(path,module), 'rb')
fwr = open('%s/%s_reference_out/RTL_expected.csv' %(path,module), 'wb')
RTL_data=f.readlines()
header = RTL_data[0]
words=header.split()
header=",".join(words) #Making it csv
fwr.writelines(header)
fwr.writelines("\n")
f.close()
fwr.close()

###############################Read the spice 2nd edge file to pick the clk cycle and FF name to be flipped#################################
f2 = open('%s' %(file_edge2), 'rb')
f3 = open('%s' %(file_edge3), 'rb')
#This file was written out by previously run scripts: perl_write_simfile_65.pl. It contains the names of all input and output flip-flops
frtl = open('%s/%s_reference_out/flipflop_headers.csv' %(path,module), 'rb')  


reader2 = csv.reader(f2)
reader3 = csv.reader(f3)
ff_reader=csv.reader(frtl)



headers_spice = reader2.next() #Spice headers. 1st line.
ff_headers = ff_reader.next() #Flip flop names
print "\nHeader len:\n", (len(headers_spice)) #length
print "\nFlipflop Header len:\n", (len(ff_headers)) #this is the actual number of flip-flops present
#print "\nflip-flop Headers[0]:\n", ff_headers[0]
#print "\nflip-flop Headers[11]:\n", ff_headers[11]

summary=[]

#collect all the rows in the 2nd edge file excluding header. Header is already collected earlier in headers_spice
for row in reader2:
	summary.append(row) 

print "Number of rows:", len(summary)

#################################Run for all rows##########################################


for row_number in range(0,len(summary)):

	if os.path.isfile("%s/%s_reference_out/F0_tool_reference_out.txt" %(path,module)):
		print "****Removing the existing F0_tool_refout and our_ref_out****\n"
		os.remove("%s/%s_reference_out/F0_tool_reference_out.txt" %(path,module))
		os.remove("%s/%s_reference_out/F0_our_reference_out.txt" %(path,module))
	
	f1=open("%s/%s_reference_out/F0_tool_reference_out.txt" %(path,module),'w')
	f12=open("%s/%s_reference_out/F0_our_reference_out.txt" %(path,module),'w')
	f2=open("%s/%s_reference_out/F0_tool_reference_out_backup.txt" %(path,module),'r')
	f2_headers=f2.readlines()
	print "F2 headers", f2_headers
	f1.writelines(f2_headers)
	f1.close()
	f2.close()
	f12.close()
	
	print "Row number:",row_number
	print "Summary-line is", summary[row_number]

	#Random clk cycle that was picked for the glitch injection is being collected
	clk_cycle= summary[row_number][1] 
	print "clk number:", clk_cycle
	#For row 1 in this csv
	#This will have to go in a loop for as many number of rows are there in the F0 spice file
	for r in range(6,len(headers_spice)):
		print summary[row_number][r]
		#If there was a flip, it is denoted by '1': Collect that index and flipflop name
		if (summary[row_number][r] == '1'):
			index= r-6 #Data is present starting from 6th column. The 1st 6 contain deck num, clk etc
			print "One found at index %d" %index
			flipped_output= ff_headers[index]
			print "flipped output's flip-flop name is: ", flipped_output
		
	part=0.45*period
	print "Clk period is %d, part is %d\n" %(period,part)
	sim_time=int((int(clk_cycle)*period)-part) #So many picoseconds minus slightly less than half clk cycle
	print "sim time= %d" %sim_time
	#time.sleep(5)
	########################################################################################################
	
	#From here on, these scripts have to be executed in a loop,for as many number of rows are there in the F0 spice file
	#Write modelsim simulatable file and do file. This will change as per the clk cycle and the 
	if row_number==0: #Delete this work directory only first time.. else retain it as it is
		os.system('python F0_python3_create_simdo_vsim_65_1.py -v F0_%s_modelsim.v -t %s -b %s -r %dps -p %s -d %s -m %s -f %s --period %d' %(module,test_path,test_module,sim_time,path,dutname,module,flipped_output,period))
	else:
		os.system('python F0_python3_create_simdo_vsim_65.py -v F0_%s_modelsim.v -t %s -b %s -r %dps -p %s -d %s -m %s -f %s --period %d' %(module,test_path,test_module,sim_time,path,dutname,module,flipped_output,period))
	print('Done executing F0_python3_create_simdo_vsim_65.py\n')
	#time.sleep(5)
	
	os.system("python python_pick_3rd_edge_values.py -m %s -f %s -c %s" %(module,path,clk_cycle))
	print('Done executing python_pick_3rd_edge_values.py\n')
	#time.sleep(3)
######################################################################################################
	
	

#Get out of loop and run this comparison.
#The output of this script is <path>/spice_results/F0_rtl_difference_3rd_edge.csv
os.system("python python_compare_3rd_edge.py -m %s -f %s" %(module,path))
print('Done executing python_compare_3rd_edge.py\n')
#time.sleep(5)
