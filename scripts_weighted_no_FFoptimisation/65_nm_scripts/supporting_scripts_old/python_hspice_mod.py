#!/usr/bin/env python
#Read in a RTL file, do synthesis and placement, route
#Example usage: python python_hspice_mod.py -f /home/users/nanditha/Documents/utility/65nm/LFSR/spice_decks_1


import optparse
import re,os,glob
import fileinput
import subprocess, time
from optparse import OptionParser
import sys

parser = OptionParser('This script makes converts the ngspice file into a hspice simulatable file.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-f","--path", help='Enter the RTL (verilog or vhdl) file path- THE ENTIRE PATH',dest='filepath')


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

path=options.path

num_of_files = len(glob.glob('*.sp'))
file_names=os.listdir('%s' %path)

#Modify each file to be hspice compatible

for i in range(0,num_of_files):

	for line in fileinput.input('%s/%s' %(path,file_names[i])', inplace=1):
	if "glitch_CORE65GPSVT_selected_lib_vg.sp" in line:
		line = line.replace("glitch_CORE65GPSVT_selected_lib_vg.sp","hspice_glitch_CORE65GPSVT_selected_lib_vg.sp")
	if "gnd gnds vdd vdds" in line:
		line = line.replace("gnd gnds vdd vdds","gnd vdd")
	if ".control" in line:
		line = line.replace(".control",".option list measdgt=5 measform=3")
	if "tran 20ps" in line:
		line = line.replace("tran 20ps",".tran 20ps")
	if "meas tran " in line:
		line = line.replace("meas tran ",".measure tran ")
	if "quit\n\n.endc" in line:
		line = line.replace("quit\n\n.endc\n","\n")
		
		sys.stdout.write(line)
	
	else:
		if not "echo" in line:
			sys.stdout.write(line) 
	
	
