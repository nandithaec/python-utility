#!/usr/bin/env python

#Spice flip count in 3rd edge is being calculated. Difference between RTL and spice 3rd edge flip count is now being calculated. Entire flow is automated. spice_results/F0_spice_rtl_difference_3rd_edge.csv - Nov 30th 2014

#Example usage: python python_compare_3rd_edge.py -m c432_clk_ipFF -f /home/users/nanditha/Documents/utility/65nm/c432 -t /home/users/nanditha/Documents/utility/65nm/c432/spice_results/c432_F0_3rd_edge.csv

import optparse
import re,os
import csv, re,time
import random,shutil

#import python_compare_remote

from optparse import OptionParser


parser = OptionParser("Calculates the difference in flip count between spice and RTL at the 3rd edge. Output is written out in spice_results/F0_spice_rtl_difference_3rd_edge.csv\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n")

parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-t", "--file2",dest='file2', help='Enter the path and the file name of the file that contains 3rd edge flip summary in csv format')

(options, args) = parser.parse_args()


module=options.module
path=options.path
file_edge3=options.file2


##########################################################################################
##########################Find the difference between the two#############################
##########################################################################################

f = open('%s/%s_reference_out/F0_obtained.csv' %(path,module), 'rb')
frtl = open('%s/%s_reference_out/RTL_expected.csv' %(path,module), 'rb')
fout = open('%s/spice_results/F0_spice_rtl_difference_3rd_edge.csv' %(path), 'wb')
#This file gives the flips after injecting the F0, in RTL

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

print "\n column[headers_F0[0]]:\n", column[headers_F0[0]]  #This means, column[output_dec_7_], where output_dec_7_ is the headers[0]- value is '0' or '1'
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


#################################Read 3rd edge file and sum up the number of flips##############################
f3 = open('%s' %(file_edge3), 'rb')
reader3 = csv.reader(f3)
#print "3rd edge file", reader3
headers_spice = reader3.next() #Spice headers

####################################################################################

km=[]

#Take difference between the 2 files to find the flips in RTL
for r in range(len(headers_rtl)):

	rows_number=0	
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
	
	#For all rows in that selected column.
	for num_rows in range(0,num_of_rows): 
		print "inside for", num_rows
	
		F0_val=sp[num_rows]
		rtl_val=rt[num_rows]
		print "F0_val is",F0_val
		print "RTL_val is",rtl_val
		difference= abs(int(F0_val) - int(rtl_val))
		k.append(difference)
		print "\nk is\n",k
		rows_number=rows_number+1

		
	print "\nk is\n", k  #All the data in the column is collected in k
	km.append(k) # appended to an empty list
	print "km is\n",km
	#transpose_row=zip(*km)
	#print "transpose_row:\n",transpose_row
#Since we have collected data column-wise, and python has no way of writing out column wise to a csv,
#We take a transpose of the list and print it out!!
flip=[]
flip.append("RTL_flip_count")

spice_flip=[]
spice_flip.append("Spice_flip_count")

spice_rtl_diff=[]
spice_rtl_diff.append("Spice_RTL_Diff_flips")

print "Num of rows",rows_number
transpose=zip(*km)
print "transpose:\n",transpose
print "transpose[0]:\n",transpose[0]  #header

#print "transpose[1]:\n",transpose[1]
mismatch=0

for b in range(1,rows_number+1):
	#For every row, excluding the header
	RTL_flip_sum=0
	print "RTL Row is ",transpose[b]
	for i in range(0,len(transpose[b])):
		RTL_flip_sum=RTL_flip_sum+transpose[b][i] #calculate the no. of flips
		#print "transpose[%d][%d]: %d\n" %(b,i,transpose[b][i])

	print "RTL_flip_sum of row %d: %d\n" %(b,RTL_flip_sum)
	flip.append(RTL_flip_sum)
	
	#Spice 3rd edge file
	row_spice = reader3.next() #Spice line
	print "Spice Row is",row_spice
	#Sum up the elements of the row excluding the first 6 elements- which are clk, deck_num etc.,
	spice_flip_sum=0
	sp_rt_diff=0
	for a in range(6,len(row_spice)):
		spice_flip_sum=spice_flip_sum+int(row_spice[a])

	spice_flip.append(spice_flip_sum)
	print "Spice flip sum is %d" %spice_flip_sum
	
	sp_rt_diff= abs(RTL_flip_sum - spice_flip_sum)
	spice_rtl_diff.append(sp_rt_diff)
	print "Spice - RTL flip diff is %d" %sp_rt_diff
	print "**************\n\n"
	
	
	if (sp_rt_diff>0):
		mismatch=mismatch+1
	
percent_mismatch= (float(mismatch)/float(rows_number))*100.0

print "Flip RTL",flip
print "Flip Spice",spice_flip
print "Diff is",spice_rtl_diff
print "Spice RTL mismatch is %d" %mismatch
print "Spice RTL mismatch is %f" %percent_mismatch

#Append this to the original list
km.append(flip)
km.append(spice_flip)
km.append(spice_rtl_diff)

print "km appended:\n",km 

transpose_new=zip(*km)
print "transpose_new:\n",transpose_new
writer.writerows(transpose_new)

fout.write("Num of rows: %d\n" %rows_number)
fout.write("Spice RTL mismatch cases is: %d\n" %mismatch)
fout.write("Percentage Spice RTL mismatch for F0 cases for design %s is %f percent" %(module,percent_mismatch))

fout.close()

