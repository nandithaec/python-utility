
#!/usr/bin/env python
#Example usage: python python_subckt_line_modify.py -m c432_clk_ipFF

#freq added to synthesis part: Nov 19 2013

import optparse
import re,os
import time
from optparse import OptionParser

parser = OptionParser('This script reads in the dspf file and adds \'gnd,gnds,vdd,vdds\' to the subckt instances and will show one instance per line (no + continuation of subckt): Mar 19 2014 .\n The output will be the same dspf with a "_new" suffix at the pnr/op_data location.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-m","--mod", help='Enter the entity name(vhdl) or module name (verilog) to be synthesised',dest='module_name')


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

module=options.module_name


f=open("pnr/op_data/%s_final.dspf" %(module),"r")
fnew=open("pnr/op_data/%s_final_new.dspf" %(module),"w")

#f=open("test.sp","r")
#fnew=open("test_final.sp","w")

lines=f.readlines()

#Write out all subckt definitions in one line.
for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	print "*****************\n"
	print "i is",i
	print "length of lines",len(lines)
	#last current line is the last line, then line+1 wont work.
	if (i < len(lines)-1):
		next_line=lines[i+1]
		print "Next line:",next_line
	print "Current line:",current_line


#There will be '+' in subckt definition as well. Print them out as it is
	if re.match(".SUBCKT",current_line) or re.match(".subckt",current_line):
		print "subckt line\n"
		flag=0
		fnew.writelines(current_line)
		while flag==0:
			i=i+1
			if re.match("\+",lines[i]): #If next line has +
				fnew.writelines(lines[i])
			else:
				flag=1 #When the next line is no longer a '+', the subckt has ended. So break the loop
				
	elif re.match("X",current_line):  #if it is a subckt instance
		#Check if next line is its continuation. Check for '+'
		print "match X\n"
		
		if re.search("FILL",current_line): #If there are FILLER cells, dont write them
			print "FILLER cells found\n"
		
		
		elif re.match("\+",next_line):
			print "match + next line\n"
			if current_line[-1]=='\n':
			#Remove \n from the current line before appending next line
				current_line=current_line[:-1] 
			#Eliminate the first character of next line which is '+' and append the rest
			for j in range(1,len(next_line)):  
				current_line=current_line+next_line[j] #append the 2 lines
		
			fnew.writelines(current_line)
			print "Modified line:",current_line
			#Do not write out the next line which starts with '+'
			#Hence increment the index. Doesnt work
			#i=i+2
			#print "i incremented is\n",i
			
		
		else: #If there is no continuation of subckt, print out the current subckt
		
			print "no continuation of subckt:",current_line
			fnew.writelines(current_line)
			print "Modified line:",current_line
		
			

			
	
	else: #If not a subckt instance, write as it is the non-subckt line.
		if (re.match("\+",current_line)==None): #If the line does not start with '+'
			fnew.writelines(current_line)
			print "not a subckt instance:",current_line
		else:
			print "starts with +. Hence omitting\n"
	

print "Done creating a new dspf file \"pnr/op_data/%s_final_new.dspf\" \n" %module

