
#!/usr/bin/env python
#Read in a RTL file, do synthesis and placement, route
#Example usage: python python_choose_subckts_library.py -m c432_clk_ipFF


import optparse
import re,os
import time
from optparse import OptionParser

parser = OptionParser('This script reads in the dspf file and adds \'gnd,gnds,vdd,vdds\' to the subckt instances and will show one instance per line (no + continuation of subckt): Mar 19 2014 .\n The output will be the same dspf with a "_new" suffix at the pnr/op_data location.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-m","--mod", help='Enter the entity name(vhdl) or module name (verilog) to be synthesised',dest='module_name')


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

module=options.module_name

f=open("faraday_umc90nm_std_cells.sp" ,"r")
#f=open("test.sp" ,"r")
fnew=open("faraday_umc90nm_selected_lib.sp" ,"w")

lib_data=f.readlines()

fsp=open("pnr/op_data/%s_final_new.dspf" %module ,"r")
data_dspf=fsp.readlines()

subckt1=[]
#Collect the subckt instance names in the current design

for i in range(0,len(data_dspf)):
	#Get each line
	current_line=data_dspf[i]
	#print "i=%d, current line=%s" %(i,current_line)
	if re.match("X",current_line):  #if it is a subckt instance
		#get the gate instance name	
		words=current_line.split()
		last_word=words[-1] #Save the last word	
		subckt1.append(last_word)		

		
print "Original Subckt list:",subckt1			
print "Length of original Subckt list:", len(subckt1)

###########################################################################

subckt=[]
#print "finding new subckt list"
for i in range(0,len(subckt1)):
	cur_elem=subckt1[i]
	#print "current elem:", cur_elem
	match=0
	for j in range(i+1,len(subckt1)):
		if (cur_elem==subckt1[j]):
			match=1
			#print "match=1, cur elem=%s, subckt1[%d]=%s ..exit while\n" %(cur_elem,j,subckt1[j])
	
	if match==0:
		subckt.append(cur_elem)
			

#Alternate option: subckt=set(subckt1)	
print "\n\nUnique Subckt list:",subckt			
print "Length of the unique subckt list:", len(subckt)
###########################################################################
#Parse the library file, match for "subckt" keyword and search for the desired instance name

fnew.writelines("\n***Library file consisting only the library cell instances in the /pnr/op_data/%s_final_new.dspf file\n\n" %module)
fnew.writelines("***Library cell instances: \n")
fnew.writelines("***Total number of cell instances: %d\n" %(len(subckt)))
for g in range(0,len(subckt)):
	fnew.writelines("**%s\n" %(subckt[g]))
	
fnew.writelines("\n\n")
for i in range(0,len(lib_data)):
	current_line=lib_data[i]
	#print "current line:%s, i=%d" %(current_line,i)
	if re.match(".SUBCKT",current_line):
		#print "subckt line:", current_line
		#found=0
#		while(found==0): #Stop searching in the current line, once the subckt instance is found
		for ii in range(0,len(subckt)):
			#print "subckt element searching:",subckt[ii]
		#Take each element of the subckt list, i.e., each library cell.Find a match in the library file
			if (re.search(subckt[ii],current_line)):
				#Save the subckt definition to a new file
				#print "match found searching:",subckt[ii]
				#print "inside if ,current line: %s, i=%d" %(current_line,i)
				 #The for loop starts from the current line where the subckt instance was found in the previous step
				for a in range(i,len(lib_data)):
				#Continue till .ENDS is found	
					if (re.match(".ENDS",lib_data[a])):
						fnew.writelines(lib_data[a]) #Write out .ENDS and then stop
						fnew.writelines("\n\n")
						stop=1
						break
					else:
						fnew.writelines(lib_data[a]) #Write out current line
				
				#print "done writing data"
		
		
