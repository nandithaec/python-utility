#!/usr/bin/env python


#Example usage: python python_compare_3rd_edge.py -m decoder_op_ip -f /home/users/nanditha/Documents/utility/65nm/F0_expt/decoder_65nm 

import optparse
import re,os
import csv, re,time
import random,shutil

#import python_compare_remote

from optparse import OptionParser


parser = OptionParser("This script reads in the <path>/spice_results/final_results_spice_outputs_%d.csv (spice output Flip-flop values at 3rd rising edge) and <path>/<module>_reference_out/RTL.csv (RTL reference output values) to compare the spice simulation (with glitch) output with the original RTL simulation (no glitch) output. Two files are written out:\n1. <path>/spice_results/spice_rtl_difference_%d.csv and\n2.<path>/spice_results/spice_rtl_diff_testing_%d.csv.\n Both contain essentially same data but the _testing file has both spice and RTL outputs so that the result in the other file can be verified by us.\nIt then counts the number of flips- single/double etc., each time this script is executed (for a group of simulations) and then backs up few decks randomly for each case- no_flip case, single,double flip and triple flip case. These decks are saved in backup_spice_decks_3rd_edge folder and a separate folder is created for each of the no flip, single, double flips etc.,\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n")

parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")

(options, args) = parser.parse_args()


module=options.module
path=options.path




##########################################################################################
##########################Find the difference between the two#############################
##########################################################################################

f = open('%s/%s_reference_out/F0_obtained.csv' %(path,module), 'rb')
frtl = open('%s/%s_reference_out/RTL_expected.csv' %(path,module), 'rb')
fout = open('%s/spice_results/F0_rtl_difference_3rd_edge.csv' %(path), 'wb')


reader = csv.reader(f)
reader_rtl = csv.reader(frtl)
writer = csv.writer(fout)


headers_F0 = reader.next() #RTL F0 headers

print "\nF0 Headers:", headers_F0

print "\nHeader len:\n", (len(headers_F0)) #length



column = {}
for h in headers_F0:
	column[h] = []
	print "\nColumn inside for:\n", column

print "\nF0 Column:\n", column
#print "\nColumn 1:\n",column['output_dec_7_']

num_of_rows=0
for row in reader:
	num_of_rows=num_of_rows+1
	for h, v in zip(headers_F0, row):
		column[h].append(v)

print "\n column[headers_F0[0]]:\n", column[headers_F0[0]]  #This means, column[output_dec_7_], where output_dec_7_ is the headers[0]
#print "\nSpice Column:\n", column

####################################################################################
headers_rtl = reader_rtl.next() #RTL headers

print "\nRTL Headers:\n", headers_rtl
print "\nRTL Headers[0]:\n", headers_rtl[0]

column_rtl = {}
for h2 in headers_rtl:
	column_rtl[h2] = []

print "\nRTL Column:\n", column_rtl
#print "\nColumn 1:\n",column_rtl['input_dec_2_']

for row2 in reader_rtl:
	for h2, v2 in zip(headers_rtl, row2):
		column_rtl[h2].append(v2)

print "\nColumn :\n", column_rtl[headers_rtl[0]]

####################################################################################


km=[]

#Take difference between the 2 files
for r in range(len(headers_rtl)):
		
	k= [] ##Empty the temporary List before starting to append a new column
	#print "\n\nMatch found!! \n spice Header: %s \n RTL header: %s\nspice column: %s \nRTL column: %s:\n" %(headers[s],headers_rtl[r],column[headers[s]],column_rtl[headers_rtl[r]])
	
	k.append('diff_'+headers_rtl[r]) #Append header

	sp= column[headers_F0[r]] #Get the entire column in the F0 file. This excludes the header
	#Each item in the column is referenced as sp[0], sp[1] etc
	print "Next row: Header: k",k
	print "\nF0 is:\n",sp[0] #This is the first line- excluding the header

	rt= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file
	#Each item in the column is referenced as rt[0], rt[1] etc as many are the number of rows
	print "\nrtl is:\n",rt[0]

	for num_rows in range(0,num_of_rows): 
		print "inside for", num_rows
	
		F0_val=sp[num_rows]
		rtl_val=rt[num_rows]
		print "F0_val is",F0_val
		print "RTL_val is",rtl_val
		difference= abs(int(F0_val) - int(rtl_val))
		k.append(difference)
		print "\nk is\n",k
	

		
	print "\nk is\n", k  #All the data in the column is collected in k
	km.append(k) # appended to an empty list
	print "km is\n",km


#Since we have collected data column-wise, and python has no way of writing out column wise to a csv,
#We take a transpose of the list and print it out!!
#print "transpose:\n",zip(*km)
writer.writerows(zip(*km))

fout.close()



################################# Validation file ###################################################
"""
fd = open('%s/spice_results/spice_rtl_difference_3rd_edge_%d.csv' %(path,int(outloop)), 'rb') #Open in read mode
fv = open('%s/spice_results/spice_rtl_diff_testing_3rd_edge_%d.csv' %(path,int(outloop)), 'wb')

diff_file = csv.reader(fd)
validator= csv.writer(fv)

a=[]
####################################################################################
headers_diff = diff_file.next() #Diff headers

#print "\nDiff Headers:\n", headers_diff
#print "\nDiff Headers[0]:\n", headers_diff[0]

a.append(headers_diff)
#print "a=\n",a

column_diff = {}
for hd in headers_diff:
	column_diff[hd] = []

#print "\nColumn diff:\n", column_diff

for row in diff_file:  
	for hd, v in zip(headers_diff, row):
		column_diff[hd].append(v)

#print "\nColumn 0:\n", column_diff[headers_diff[0]]

####################################################################################

test=[]

#For all columns in RTL file
for r in range(len(headers_rtl)):
	#print "\n\nHeader: %s  \nRTL column: %s:\n" %(headers_rtl[r],column_rtl[headers_rtl[r]])
	k1=[]
	k1.append('rtl_'+headers_rtl[r]) #Append header
	rt= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file

	for num_rows in range(0,int(num)): # This will be a user input
		k1.append(rt[num_rows])
		#print "\n rtl contents in test file is:", rt[num_rows]

	test.append(k1) # appended to an empty list
	#print "test array is\n",test


#For all columns in spice file
for s in range(len(headers)):
	#print "\n\nHeader: %s \nspice column: %s\n" %(headers[s],column[headers[s]])
	k1=[]
	k1.append('spice_'+headers[s]) #Append header
	sp= column[headers[s]] #Get the entire column in the RTL file

	for num_rows in range(0,int(num)): 
		k1.append(sp[num_rows])
		#print "\n rtl contents in test file is:", sp[num_rows]

	test.append(k1) # appended to an empty list
	#print "test array is\n",test

#print "diff file entering\n"


#For all columns in diff file
for s in range(len(headers_diff)):
	#pattern= re.compile('deck_num |clk |glitch')
	#if (pattern.match(headers_diff[s])): 
	#	print "Match found\n"
	#Ignore these headers
	if ((re.match(headers_diff[s], 'deck_num') == None) and (re.match(headers_diff[s], 'clk') == None) and (re.match(headers_diff[s], 'glitch') == None)and (re.match(headers_diff[s], 'gate') == None)and (re.match(headers_diff[s], 'subcktlinenum') == None)):
		#print "\n\nDiff Header: %s \nspice column: %s\n" %(headers_diff[s],column_diff[headers_diff[s]])
		k1=[]
		k1.append(headers_diff[s]) #Append header
		d= column_diff[headers_diff[s]] #Get the entire column in the RTL file

		for num_rows in range(0,int(num)): # 10 rows including header. This will be a user in
			k1.append(d[num_rows])
			#print "\n rtl contents in test file is:", d[num_rows]

		test.append(k1) # appended to an empty list
		#print "test array is\n",test

validator.writerows(zip(*test))

fv.close()
fd.close()

print "Ending compare\n"


"""
