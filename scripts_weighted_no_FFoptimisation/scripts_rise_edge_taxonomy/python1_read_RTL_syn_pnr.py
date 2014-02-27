#!/usr/bin/env python
#Read in a RTL file, do synthesis and placement, route
#Example usage: python python1_read_RTL_syn_pnr.py -f /home/users/nanditha/Documents/utility/b03/b03.vhd -m b03 -c 300

#Eliminated clock gating from synthesis: Feb 27 2014
#freq added to synthesis part: Nov 19 2013

import optparse
import re,os
import fileinput
import subprocess, time
from optparse import OptionParser

parser = OptionParser('This script reads in a vhdl or verilog file (RTL) and its test bench. It invokes rtl2gds utility to do synthesis and placement and route. The requirements of rtl2gds are the following tools: Design Compiler, SoC Encounter and Modelsim. The inputs to the script are listed as arguments below, which are all necessary arguments.\n The outputs of this script are same as the outputs of the rtl2gds utility. It creates varioous folders:man1, pnr, rtl, simulation, synthesis and template in the current working directory.\nThe files of interest to us are the following:\n1. pnr/op_data/$module_final.v - PNR verilog netlist\n2. pnr/op_data/$module_final.dspf - spice netlist \n3. pnr/reports/$module_summary.rpt - Cell area report - which will be used for optimisation later on.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-f","--path", help='Enter the RTL (verilog or vhdl) file path- THE ENTIRE PATH',dest='filepath')
parser.add_option("-m","--mod", help='Enter the entity name(vhdl) or module name (verilog) to be synthesised',dest='module_name')
parser.add_option("-c","--clk", help='Enter the clk frequency in MHz, for eg., if 900MHz, enter 900',dest='clkfreq')

#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

filepath=options.filepath
clkfreq=options.clkfreq
module=options.module_name

#Invoke rtl2gds and create directories in CURRENT WORKING DIRECTORY ONLY
os.system("rtl2gds -genScr=.")

#Run synthesis
os.system('rtl2gds -rtl=%s -rtl_top=%s -syn -frequency=%s' %(filepath,options.module_name,clkfreq))	

#These 3 commands also work
#os.system("rtl2gds -rtl={0} -rtl_top={1} -syn".format(options.filepath, options.module_name))
#os.system("rtl2gds -rtl={options.filepath} -rtl_top={options.module_name} -syn".format(args=args))
#subprocess.call(['rtl2gds', '-rtl=' + options.filepath, '-rtl_top=' + options.module_name, '-syn'])

fcr = open('synthesis/scripts/compile_dc.tcl', 'r') ## This is the tcl file for synthesis
data=fcr.readlines()
#print data
fcr.close()

fcw = open('synthesis/scripts/compile_dc_backup.tcl', 'w') ## This is the tcl file for synthesis- backup
fcw.writelines(data)
fcw.close()

os.remove('synthesis/scripts/compile_dc.tcl')

fin = open('synthesis/scripts/compile_dc_backup.tcl', 'r') 
fnew = open('synthesis/scripts/compile_dc.tcl', 'w') ## This is the new tcl file for synthesis


#Replace a current line
#with open('input') as fin, open('output','w') as fout:
for line in fin:
	if line == 'set_clock_gating_style  \\n':
		fnew.write('#set_clock_gating_style  \\n')
	elif line == 'insert_clock_gating > ../logs/insert_clock_gating.log\n':
		fnew.write('#insert_clock_gating > ../logs/insert_clock_gating.log\n')
	elif line == 'propagate_constraints -gate_clock\n':
		fnew.write('#propagate_constraints -gate_clock\n')
	elif line == 'identify_clock_gating\n':
		fnew.write('#identify_clock_gating\n')
	elif line == 'report_clock_gating -verbose > ../reports/clk_gate_verbose.rpt\n':
		fnew.write('#report_clock_gating -verbose > ../reports/clk_gate_verbose.rpt\n')
	else:
		fnew.write(line)

fnew.close()
fin.close()

fnew = open('synthesis/scripts/compile_dc.tcl', 'r') 
newdata=fnew.readlines()
#print (newdata)

f1 = open('synthesis/scripts/compile_dc_backup.tcl', 'w') 
#f1.writelines("This was the script compiled by the Design Compiler\n It gets overwritten in the pnr stepp. Hence saving a backup here\n\n")
f1.writelines(newdata)

f1.close()
fnew.close()

print "Done creating a new synthesis compile script \"synthesis/scripts/compile_dc.tcl\" \n"


if os.path.exists('synthesis/run/'):
	os.chdir('synthesis/run/')
	os.system('bash run_dc.bash')

os.chdir('../../')
print "...Pause...Done synthesis and optimisation of FF.. Starting pnr"


#Run place and route

os.system('rtl2gds -rtl=%s -rtl_top=%s -pnr -frequency=%s' %(filepath,options.module_name,clkfreq))	
print "\n ****Completed synthesis and place and route****\n"

print "\n***The worst case slack information for this frequency of operation (%s MHz) is given below:***\n" %clkfreq
print "***Make sure that the slack is positive enough, so that it is guaranteed that the spice simulation will operate at this frequency\n"



fo = open('./pnr/reports/5.postRouteOpt_%s/%s_postRoute.slk' %(module,module), 'r') 
#Has slack information
lines = fo.readlines()
print "Slack information:\n%s %s\n" %(lines[0],lines[1])
print "...Pause..."
time.sleep(5)

with open("./pnr/reports/5.postRouteOpt_%s/%s_postRoute.slk" %(module,module),"r") as f:
	words=map(str.split, f)

line1=words[1] #2nd line after header
slack_read=line1[2]
print "\nSlack is: %s" %slack_read
slack_string=slack_read.replace("*/","")
slack_time=float(slack_string)
print "\nSlack is: %f ns" %slack_time
print "...Pause..."
time.sleep(5)
if slack_time < 0 :
	print "WARNING: Slack is negative. Your design WILL NOT function at the frequency %s\n" %clkfreq
	time.sleep(30)
else:
	print "Slack is positive. Your design WILL function at the frequency %s MHz\n" %clkfreq
	time.sleep(5)


if '1\'b1' in open('./pnr/op_data/%s_final.v' %module).read():
	print "\n*******************WARNING******************\n"
	print "\n1'b1 is present in the verilog file and the corresponding nets should be manually tie it to vdd in the spice file\n"
	time.sleep(15)
else:
	print "\n1'b1 is NOT present in the verilog file and there is no need to manually tie it to vdd in the spice file\n"
	time.sleep(5)

if '1\'b0' in open('./pnr/op_data/%s_final.v' %module).read():
	print "\n*******************WARNING******************\n"
	print "\n1'b0 is present in the verilog file and the corresponding nets should be manually tie it to gnd in the spice file\n"
	time.sleep(15)
else:
	print "\n1'b0 is NOT present in the verilog file and there is no need to manually tie it to gnd in the spice file\n"
	time.sleep(5)

