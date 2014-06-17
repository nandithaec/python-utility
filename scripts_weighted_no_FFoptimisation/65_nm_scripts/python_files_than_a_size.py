#!/usr/bin/env python
#Read in a RTL file, do synthesis and placement, route
#Example usage: python python_files_than_a_size.py -f /home/user1/simulations/65nm/LFSR/spice_decks_1


import optparse
import re,os,glob
import fileinput,shutil
import subprocess, time
from optparse import OptionParser
import sys

parser = OptionParser('This script makes converts the ngspice file into a hspice simulatable file.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-f","--path", help='Enter the RTL (verilog or vhdl) file path- THE ENTIRE PATH',dest='filepath')


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

path=options.filepath

#b=os.path.getsize("/home/users/nanditha/Documents/utility/65nm/LFSR/spice_decks_1/deck_158.sp")
#if b>200:
#	print "greate"
file_names=os.listdir('%s' %path)
num_of_files = len(file_names)
output_file=[]
files_copied=0
		
print "Num of files= %d" %num_of_files
print "File names", file_names

#Clear the selected decks directory
sel_dir = '%s/decks_to_be_run' %(path)


if os.path.exists(sel_dir):
	shutil.rmtree(sel_dir)

if not os.path.exists(sel_dir):
	os.mkdir(sel_dir)
	
	
for f in file_names:
	fullpath=os.path.join(path,f)
	if os.path.getsize(fullpath) < 20: #20 bytes
		print "files that did not run: ",fullpath
		print "\n"
		output_file.append(f)
		print "output file" ,output_file
		text = f #each file name
		m = re.search('glitch_report_outputs_new_(.+?).csv', text)
		if m:
			found_num=m.group(1)
			print "files less than 20b: ",f
			shutil.copy('%s/deck_%s.sp' %(path,found_num), '%s/decks_to_be_run' %path )
			shutil.copy('%s/glitch_report_outputs_new_%s.csv' %(path,found_num), '%s/decks_to_be_run' %path )
			print "copying file: %s/deck_%s.sp" %(path,found_num)
			files_copied=files_copied+1


print "Total number of files that did not run: ", files_copied



		

