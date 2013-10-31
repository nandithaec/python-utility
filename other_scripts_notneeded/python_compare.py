#!/usr/bin/env python

#Compare results of spice and RTL

#Example usage: python python_compare.py -m decoder_behav_pnr -n 10

import optparse
import re,os
import csv, re

import python_compare

from optparse import OptionParser



#Defining a main function
def main():
	parser = OptionParser('Compare RTL and spice files')
	parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
	parser.add_option("-n", "--num",dest='number', help='Enter the number of spice outputs to be compared to RTL outputs')
	parser.add_option("-t", "--tech",dest='tech', help='Enter the technology node-for eg., For 180nm, enter 180')

	(options, args) = parser.parse_args()

	module=options.module
	num=options.number
	number=int(num)
	tech=options.tech


	if (tech == '180'):
		vdd_val=1.8
	elif (tech == '130'):
		vdd_val=1.5
	elif (tech == '90'):
		vdd_val=1.2
	elif (tech == '65'):
		vdd_val=1.1
	elif (tech == '45'):
		vdd_val=1.0
	elif (tech == '32'):
		vdd_val=0.9
	elif (tech == '22'):
		vdd_val=0.8
	
	print "vdd value is ",vdd_val

#Removing the existing combined results file in the results folder

	if os.path.isfile("./spice_decks/results/spice_rtl_difference.csv" ):
		print "****Removing the existing spice_rtl_difference.csv in results folder****\n"
		os.remove("./spice_decks/results/spice_rtl_difference.csv" )

	if os.path.isfile("./spice_decks/results/spice_rtl_diff_testing.csv" ):
		print "****Removing the existing spice_rtl_diff_testing.csv in results folder****\n"
		os.remove("./spice_decks/results/spice_rtl_diff_testing.csv" )

	if os.path.isfile("./spice_decks/results/count_flips.csv" ):
		print "****Removing the existing count_flips.csv in results folder****\n"
		os.remove("./spice_decks/results/count_flips.csv" )


	f = open('./spice_decks/results/final_results_spice_outputs.csv', 'rb')
	frtl = open('./%s_reference_out/RTL.csv' %module, 'rb')
	fout = open('./spice_decks/results/spice_rtl_difference.csv', 'wb')


	reader = csv.reader(f)  #spice output file
	reader_rtl = csv.reader(frtl) #RTL output file
	writer = csv.writer(fout) #Difference file


	headers = reader.next() #Spice file headers

	print "\nSpice Headers:%s", headers
	del headers[-1]
	print "\nSpice Headers after removing the extra last header:%s", headers
	print "\nHeader len:\n", range(len(headers)) #e.g.,[0, 1, 2, 3, 4, 5, 6, 7] 
	print "\nHeader len:\n", (len(headers)) #length

	print "\nSpice Headers[0]:\n", headers[0]



	column = {}
	for h in headers:
		column[h] = []
		print "\nSpice Column inside for:\n", column

	print "\nSpice Column:\n", column
	print "\nColumn 1:\n",column['output_dec_7_']

	for row in reader:
		for h, v in zip(headers, row):
			column[h].append(v)

	print "\n column[headers[0]]:\n", column[headers[0]]  #This means, column[output_dec_7_], where output_dec_7_ is the headers[0]
	print "\nSpice Column:\n", column

	####################################################################################
	headers_rtl = reader_rtl.next() #RTL headers

	print "\nRTL Headers:\n", headers_rtl
	print "\nRTL Headers[0]:\n", headers_rtl[0]

	column_rtl = {}
	for h2 in headers_rtl:
		column_rtl[h2] = []

	print "\nRTL Column:\n", column_rtl
	print "\nColumn 1:\n",column_rtl['output_dec_7_']

	for row2 in reader_rtl:
		for h2, v2 in zip(headers_rtl, row2):
			column_rtl[h2].append(v2)

	print "\nColumn :\n", column_rtl[headers_rtl[0]]

	####################################################################################
	#k= range(2000) ##List in python

	km=[]

	#For non-matching headers
	#Match the header in rtl file with that in every header in spice file
	for r in range(len(headers_rtl)):
		no_match_flag=1	 ##Reset this every r loop only
		for s in range(len(headers)):
			if (no_match_flag==1): # If a header match is found, stop looping
				if (re.match(headers[s], headers_rtl[r]) == None): ##That is, if the headers in spice file do not match with the rtl headers
					no_match_flag=1 #No match
				else:
					no_match_flag=0 #Match


		if (no_match_flag==1):	 #If at the end of the looping over all headers, still there is no match, then print out the header as it is		
			print "\n\nNo Match!! \nHeader: %s \nspice column: %s \nRTL column: %s:\n" %(headers_rtl[r],column[headers[s]],column_rtl[headers_rtl[r]])
			k1=[]
			k1.append(headers_rtl[r]) #Append header
			rt= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file

			for num_rows in range(0,(number)): # 10 rows. This will be a user in
				k1.append(rt[num_rows])
				print "\n rtl contents inside no match header is:", rt[num_rows]

			km.append(k1) # appended to an empty list
			print "km is\n",km
		


	#For matching headers
	for r in range(len(headers_rtl)):
		no_match_flag=0	 ##Reset this every r loop only
		for s in range(len(headers)):
			if (re.match(headers[s], headers_rtl[r]) != None): ##That is, if the headers in spice file match with the rtl headers

				k= [] ##Empty the temporary List before starting to append a new column
				print "\n\nMatch!! \nHeader: %s \nspice column: %s \nRTL column: %s:\n" %(headers[s],column[headers[s]],column_rtl[headers_rtl[r]])
				k.append('diff_'+headers_rtl[r]) #Append header

				sp= column[headers[s]] #Get the entire column in the spice file
				#Each item in the column is referenced as sp[0], sp[1] etc
				#print "\nspice is:\n",sp[0]

				rt= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file
				#Each item in the column is referenced as rt[0], rt[1] etc as many are the number of rows
				#print "\nrtl is:\n",rt[0]
			
				for num_rows in range(0,(number)): # 10 rows. This will be a user input: total num
								
					spice_val=sp[num_rows]
					if rt[num_rows] == '1': 
						rtl_val = vdd_val  #This will have to depend on the techn node
						print "\nrt val in rt[num_rows] == 1: is", rtl_val
					else: 
						rtl_val = 0
						print "\nrt val in else is", rtl_val
				
				
					ab=abs(float(spice_val) - float(rtl_val))
					print "\ndiff is\n",ab
					#print "\nab is\n", ab
					if ab <= 0.5: #This will have to depend on the techn node
						k.append('0')
						print "\nab in ab<0.5 is\n", ab
					else:
						#if ab > 1.2: #This will have to depend on the techn node
						k.append('1')
						print "\nab in > 1.2 is\n", ab
				
					print "\nk inside s\n", k
				print "\nk is\n", k  #All the data in the column is collected in k
				km.append(k) # appended to an empty list
				print "km is\n",km
		
					

	#Since we have collected data column-wise, and python has no way of writing out column wise to a csv,
	#We take a transpose of the list and print it out!!
	print "transpose:\n",zip(*km)
	writer.writerows(zip(*km))

	fout.close()

	################################# Validation file ###################################################

	fd = open('./spice_decks/results/spice_rtl_difference.csv', 'rb') #Open in read mode
	fv = open('./spice_decks/results/spice_rtl_diff_testing.csv', 'wb')

	diff_file = csv.reader(fd)
	validator= csv.writer(fv)


	####################################################################################
	headers_diff = diff_file.next() #Diff headers

	print "\nDiff Headers:\n", headers_diff
	print "\nDiff Headers[0]:\n", headers_diff[0]

	column_diff = {}
	for hd in headers_diff:
		column_diff[hd] = []

	print "\nColumn diff:\n", column_diff

	for row in diff_file:  
		for hd, v in zip(headers_diff, row):
			column_diff[hd].append(v)

	print "\nColumn 0:\n", column_diff[headers_diff[0]]

	####################################################################################

	test=[]

	#For all columns in RTL file
	for r in range(len(headers_rtl)):
		print "\n\nHeader: %s  \nRTL column: %s:\n" %(headers_rtl[r],column_rtl[headers_rtl[r]])
		k1=[]
		k1.append('rtl_'+headers_rtl[r]) #Append header
		rt= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file

		for num_rows in range(0,(number)): # 10 rows. This will be a user in
			k1.append(rt[num_rows])
			print "\n rtl contents in test file is:", rt[num_rows]

		test.append(k1) # appended to an empty list
		print "test array is\n",test


	#For all columns in spice file
	for s in range(len(headers)):
		print "\n\nHeader: %s \nspice column: %s\n" %(headers[s],column[headers[s]])
		k1=[]
		k1.append('spice_'+headers[s]) #Append header
		sp= column[headers[s]] #Get the entire column in the RTL file

		for num_rows in range(0,(number)): # 10 rows. This will be a user in
			k1.append(sp[num_rows])
			print "\n rtl contents in test file is:", sp[num_rows]

		test.append(k1) # appended to an empty list
		print "test array is\n",test

	print "diff file entering\n"


	#For all columns in diff file
	for s in range(len(headers_diff)):
		#pattern= re.compile('deck_num |clk |glitch')
		#if (pattern.match(headers_diff[s])): 
		#	print "Match found\n"
		if ((re.match(headers_diff[s], 'deck_num') == None) and (re.match(headers_diff[s], 'clk') == None) and (re.match(headers_diff[s], 'glitch') == None)):
			print "\n\nDiff Header: %s \nspice column: %s\n" %(headers_diff[s],column_diff[headers_diff[s]])
			k1=[]
			k1.append(headers_diff[s]) #Append header
			d= column_diff[headers_diff[s]] #Get the entire column in the RTL file

			for num_rows in range(0,(number)): # 10 rows including header. This will be a user in
				k1.append(d[num_rows])
				print "\n rtl contents in test file is:", d[num_rows]

			test.append(k1) # appended to an empty list
			print "test array is\n",test

	validator.writerows(zip(*test))

	fv.close()

	################################# Count the number of flips ###################################################
	#The final file which will have the count for multiple flips
	fflip = open('./spice_decks/results/count_flips.csv', 'wb')
	fd = open('./spice_decks/results/spice_rtl_difference.csv', 'rb') #Open in read mode
	diff_file = csv.reader(fd)
	flip_writer = csv.writer(fflip)

	diff_headers = diff_file.next() #Spice headers
	flip=[]
	k=[]

	print "diff_headers[0]= ",diff_headers[0]
	#Append header
	for i in range(3,len(diff_headers)):
		k.append(diff_headers[i])
		print "\nk in headers:",k

	k.append('flip_count')
	flip.append(k)
	print "flip header is\n:", flip

	num_col=len(diff_headers)
	last_col=num_col+1
	print "Column numbers total: %d, last col=%d" %(num_col,last_col)

	csv_rows=0
	num_of_zero_flips=0
	num_of_single_flips=0
	num_of_double_flips=0
	num_of_triple_flips=0
	num_of_four_flips=0

	for row in diff_file: #For every row in the diff file
		csv_rows=csv_rows+1 #This is excluding the header, since we have already done diff_file.next() to count the header
		k=[]
		count_num=0
	#column iteration - number of columns. Dont count first 3 columns- since they are deck_num, clk and glitch
		for i in (range(3,num_col)): #len is 11. so loop indexs stops at 10. So, if we want it to loop from 3 to 10, give range(3,11)
	
			print "\nRow in diff file is:", row
			print "\nindex i = %d" %(i)
			print "\nRow is:", row[i]  #Each value which is a string
			k.append(row [i])
			count_num = count_num + int(row[i])
			print "\n k is:",k

		#row[last_col]= count_num
		print "\nAt the end of the row, count is: ",count_num 
		if (count_num == 0):
			num_of_zero_flips=num_of_zero_flips+1
		elif (count_num == 1):
			num_of_single_flips=num_of_single_flips+1
		elif (count_num == 2):
			num_of_double_flips=num_of_double_flips+1
		elif (count_num == 3):
			num_of_triple_flips=num_of_triple_flips+1
		elif (count_num == 4):
			num_of_four_flips=num_of_four_flips+1
	
		k.append(str(count_num)) #Append to the last column thats newly added
		print "\n k with count is:",k

		flip.append(k)	
		print"\nflip is:",flip


	print"\nNumber of csv rows is:",csv_rows
	print "\nZero flips=%d, single flips=%d, Multiple flips=%d\nDouble flips=%d,triple flips=%d, four flips=%d\n" %(num_of_zero_flips,num_of_single_flips,(csv_rows-num_of_zero_flips-num_of_single_flips), num_of_double_flips,num_of_triple_flips,num_of_four_flips)

	per_0=float(num_of_zero_flips)/float(csv_rows)
	per_1=float(num_of_single_flips)/float(csv_rows)
	per_2=float(num_of_double_flips)/float(csv_rows)
	per_3=float(num_of_triple_flips)/float(csv_rows)
	per_4=float(num_of_four_flips)/float(csv_rows)
	per_multiple= (float(csv_rows)-float(num_of_zero_flips)-float(num_of_single_flips))/float(csv_rows)


	print "\nPercentage of zero flips=%f\nPercentage of single flips=%f\nPercentage of multiple flips=%f\n\nPercentage of double flips=%f\nPercentage of triple flips=%f\nPercentage of four flips=%f\n" %(per_0, per_1,per_multiple,per_2,per_3,per_4)
	print('\nNumber of random spice decks simulated:%d\n' %csv_rows)

	flip_writer.writerows(flip)


	fflip.write('\nPercentage of zero flips=%f\nPercentage of single flips=%f\nPercentage of multiple flips=%f\n\nPercentage of double flips=%f\nPercentage of triple flips=%f\nPercentage of four flips=%f\n' %(per_0, per_1,per_multiple,per_2,per_3,per_4))
	fflip.write('\nNumber of random spice decks simulated:%d\n' %csv_rows)

	fflip.close()
	
	return per_multiple



#Function call, returned value collected in x
if __name__ == "__main__":
    ret_multiple= main()
    print( ret_multiple )



	############################Flips have been counted#######################





















