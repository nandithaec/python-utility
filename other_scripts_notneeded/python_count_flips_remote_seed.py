#!/usr/bin/env python

#Compare results of spice and RTL

#Example usage: python python_count_flips.py -f /home/user1/simulations/decoder  -n 100  --group 10

import optparse
import re,os
import csv, re,shutil


from optparse import OptionParser


parser = OptionParser('Count number of flips..')
parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-n", "--num",dest='num',  help='Enter the total number of spice decks that were simulated')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks that were simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()

num=options.num
num_at_a_time=options.group
path=options.path
seed=options.seed

num_of_loops=(int(num)/int(num_at_a_time))

print "\n****Counting flips****\n"

#Combine all the spice_rtl_difference_*.csv files into one file

fw = open('%s/spice_results/spice_rtl_difference_summary.csv' %(path), 'w')
summary_writer = csv.writer(fw)
fd = open('%s/spice_results/spice_rtl_difference_1.csv' %(path), 'r') #Open in read mode
diff_file = csv.reader(fd)

diff_headers = diff_file.next() #diff headers
summary=[]


#print "\ndiff headers:",diff_headers
#Append header
summary.append(diff_headers)
#print "\nsummary is", summary
#summary_writer.writerows(summary)

fd.close()

#Combine data from all csv files
#for the number of files that exist
for num in range(1,(num_of_loops+1)): 
	fr = open("%s/spice_results/spice_rtl_difference_%d.csv" %(path,num), "r")
	diff_file = csv.reader(fr)
	diff_headers = diff_file.next() #diff headers - exclude this. it has already been written

	for row in diff_file: #For every row in the diff file
		#print "\nRow in diff file is:", row
		summary.append(row) #rows in diff file

	fr.close()

summary_writer.writerows(summary)

fw.close()
################################# Count the number of flips ###################################################
#The final file which will have the count for multiple flips
fflip = open('%s/spice_results/count_flips_summary.csv' %path, 'wb')
fd = open('%s/spice_results/spice_rtl_difference_summary.csv' %path, 'rb') #Open in read mode
diff_file = csv.reader(fd)
flip_writer = csv.writer(fflip)

diff_headers = diff_file.next() #diff headers
#print "diff_headers[0]= ",diff_headers[0]

flip=[]
k=[]


#Append header
for i in range(3,len(diff_headers)):
	k.append(diff_headers[i])
	#print "\nk in headers:",k

k.append('flip_count')
flip.append(k)
#print "flip header is\n:", flip

num_col=len(diff_headers)
last_col=num_col+1
#print "Column numbers total: %d, last col=%d" %(num_col,last_col)

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

		#print "\nRow in diff file is:", row
		#print "\nindex i = %d" %(i)
		#print "\nRow is:", row[i]  #Each value which is a string
		k.append(row [i])
		count_num = count_num + int(row[i])
		#print "\n k is:",k

	#row[last_col]= count_num
	#print "\nAt the end of the row, count is: ",count_num 
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
	#print "\n k with count is:",k

	flip.append(k)	
	#print"\nflip is:",flip


print"\nNumber of csv rows is:",csv_rows
num_of_multiple_flips=(csv_rows-num_of_zero_flips-num_of_single_flips)
atleast_one_flip= num_of_single_flips + num_of_multiple_flips

print "\nZero flips=%d\nSingle flips=%d\nMultiple flips=%d\nDouble flips=%d\nTriple flips=%d\nFour flips=%d\nAtleast one flip=%d\n" %(num_of_zero_flips,num_of_single_flips,num_of_multiple_flips, num_of_double_flips,num_of_triple_flips,num_of_four_flips,atleast_one_flip)


print('\nNumber of random spice decks simulated:%d\n' %csv_rows)

probability=(float(num_of_multiple_flips)/float(atleast_one_flip))
print '\nProbability of multiple flips given atleast one flip is:%d/%d = %f\nthat is: %f percent\n' %(num_of_multiple_flips,atleast_one_flip,probability,probability*100)


flip_writer.writerows(flip)

fflip.write("\nZero flips=%d\nSingle flips=%d\nMultiple flips=%d\nDouble flips=%d\nTriple flips=%d\nFour flips=%d\nAtleast one flip=%d\n" %(num_of_zero_flips,num_of_single_flips,(csv_rows-num_of_zero_flips-num_of_single_flips), num_of_double_flips,num_of_triple_flips,num_of_four_flips,atleast_one_flip))

print('\nSeed generated was:%d\n' %(int(seed)))
fflip.write('\nSeed passed into the main script was:%d\n' %(int(seed)))

fflip.write('\nProbability of multiple flips given atleast one flip is:%d/%d = %f\nthat is: %f percent\n' %(num_of_multiple_flips,atleast_one_flip,probability,probability*100))

fflip.write('\nNumber of random spice decks simulated:%d\n' %csv_rows)

fflip.close()














