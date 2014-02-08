#!/usr/bin/env python

#Compare results of spice and RTL

#Example usage: python python_count_flips_remote_seed.py -f /home/external/iitb/nanditha/simulations/decoder_ip_opFF_rise  -n 10 --group 10 -s 2594275917096658334

import optparse
import re,os
import csv, re,shutil
import math


from optparse import OptionParser


parser = OptionParser('This script counts the number of flips in each simulation result. It first combines all the <path>/spice_results/spice_rtl_difference_*.csv files into one file <path>/spice_results/spice_rtl_difference_summary.csv. This fils is then read and the number of flips is counted. If there is a flip, a \'1\' is reported for that output, and a \'0\' is reported for a no-flip case. \n\nThis information is written out in a table format into a file at <path>/spice_results/count_flips_summary.csv, in which the each row stands for one simulation, and each column contains the names of the output nodes\n This script reports the cases in which there was single flip, multiple flips, double flip, triple and atleast one flip. It calculates the probability of multiple flips given atleast one flip. So this means that, if there is a single particle strike causing a single glitch, and if it happens to cause a single bit-flip (fault), what is the probability that in such cases, more than one fault is likely to occur. If this probability is large, it indicates that, a single strike is likely to cause multiple faults at a high probability.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-n", "--num",dest='num',  help='Enter the total number of spice decks that were simulated')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks that were simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed so that it is saved in the result file, for future reference')

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


#Append header - start from 5- since we are omitting first 5 columns which have deck_num,clk,glitch,gate and subcktlinenum info
for i in range(5,len(diff_headers)):
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
more_than4_flips=0

for row in diff_file: #For every row in the diff file
	csv_rows=csv_rows+1 #This is excluding the header, since we have already done diff_file.next() to count the header
	k=[]
	count_num=0
#column iteration - number of columns. Dont count first 5 columns- since they are deck_num, clk, glitch, gate and subcktlinenum
	for i in (range(5,num_col)): #len is 11. so loop indexs stops at 10. So, if we want it to loop from 3 to 10, give range(3,11)

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
	elif (count_num > 4):
		more_than4_flips=more_than4_flips+1

	k.append(str(count_num)) #Append to the last column thats newly added
	#print "\n k with count is:",k

	flip.append(k)	
	#print"\nflip is:",flip


print"\nNumber of csv rows is:",csv_rows
num_of_multiple_flips = (csv_rows-num_of_zero_flips-num_of_single_flips)
atleast_one_flip = num_of_single_flips + num_of_multiple_flips  #(csv_rows-num_of_zero_flips)

print "\nZero flips=%d\nSingle flips=%d\nMultiple flips=%d\nDouble flips=%d\nTriple flips=%d\nFour flips=%d\nGreater than four flips=%d\nAtleast one flip=%d\n" %(num_of_zero_flips,num_of_single_flips,num_of_multiple_flips, num_of_double_flips,num_of_triple_flips,num_of_four_flips,more_than4_flips,atleast_one_flip)


print('\nNumber of random spice decks simulated:%d\n' %csv_rows)

if (num_of_multiple_flips > 0):
	probability=(float(num_of_multiple_flips)/float(atleast_one_flip))
else:
	probability=0.0
print '\nProbability of multiple flips given atleast one flip is:%d/%d = %f\nthat is: %f percent\n' %(num_of_multiple_flips,atleast_one_flip,probability,probability*100)


flip_writer.writerows(flip)

fflip.write("\nZero flips=%d\nSingle flips=%d\nMultiple flips=%d\nDouble flips=%d\nTriple flips=%d\nFour flips=%d\nGreater than four flips=%d\nAtleast one flip=%d\n" %(num_of_zero_flips,num_of_single_flips,(csv_rows-num_of_zero_flips-num_of_single_flips), num_of_double_flips,num_of_triple_flips,num_of_four_flips,more_than4_flips,atleast_one_flip))

print('\nSeed generated was:%d\n' %(int(seed)))
fflip.write('\nSeed passed into the main script was:%d\n' %(int(seed)))

fflip.write('\nProbability of multiple flips given atleast one flip is:%d/%d = %f\nthat is: %f percent\n' %(num_of_multiple_flips,atleast_one_flip,probability,probability*100))

fflip.write('\nNumber of random spice decks simulated:%d\n' %csv_rows)

#Calculating statistics: mean, standard deviation, standard error and confidence intervals 
#Do this only if there is atleast one multiple flip. Else, there is no point in calculating it.
#And also, it will result in division by zero- for std_error_by_mean calculation

if (num_of_multiple_flips > 0):
	mean= (float(num_of_multiple_flips)/float(atleast_one_flip))

	variance_1st_term = (((1.0-mean)**2) * num_of_multiple_flips)  # number**2 indicates square of the number 
	variance_2nd_term = (((0.0-mean)**2) * (atleast_one_flip - num_of_multiple_flips))
	print "\nvariance 1st term ", variance_1st_term
	print "\nvariance 2nd term ", variance_2nd_term
	#N is made (N-1) when random sampling is involved. Hence we use (atleast_one_flip - 1)
	print "\n Atleast one flip:",atleast_one_flip
	if (atleast_one_flip >1):
		print "\n Atleast one flip:",atleast_one_flip
		variance = (variance_1st_term + variance_2nd_term) /(atleast_one_flip - 1) #no need to make atleast_one_flip as float
		print "\nvariance ", variance
		standard_deviation = math.sqrt(variance) #this returns a float
		print "\nstandard_deviation ", standard_deviation
		standard_error = standard_deviation/(math.sqrt(atleast_one_flip)) #float again
		print "\nstandard_error ", standard_error
		std_error_by_mean = standard_error/mean
		print "\nstd_error_by_mean ", std_error_by_mean
		#95% confidence intervals

		lower_limit = mean - (standard_error*1.96)
		upper_limit = mean + (standard_error*1.96)
	
		print "\nconfidence intervals: upper limit: %f, lower limit: %f\n " %(lower_limit,upper_limit)

		print('\n***STATISTICS FOR MULTIPLE BUT FLIPS, GIVEN THAT ATLEAST ONE FAULT (FLIP) HAS OCCURED***\n' )
		print('Mean of multiple flips given atleast one flip is: %f\n' %(mean))
		print('Variance is: %f\n' %variance)
		print('Standard deviation is: %f\n' %standard_deviation)
		print('Standard error is (sigma/sqrt(N)): %f\n' %standard_error)
		print('Standard error divided by mean is (sigma/sqrt(N)/mean): %f\n' %std_error_by_mean)
		print('95 percent Confidence interval is: %f to %f \n' %(upper_limit,lower_limit))
		print('95 percent Confidence interval in percent is: %f percent to %f percent \n' %(lower_limit*100,upper_limit*100))

		fflip.write('\n***STATISTICS*** for design at path %s:\n' %path )
		fflip.write('Mean of multiple flips given atleast one flip is: %f\n' %(mean))
		fflip.write('Variance is: %f\n' %variance)
		fflip.write('Standard deviation is: %f\n' %standard_deviation)
		fflip.write('Standard error is (sigma/sqrt(N)): %f\n' %standard_error)
		fflip.write('Standard error divided by mean is (sigma/sqrt(N)/mean): %f\n' %std_error_by_mean)
		fflip.write('95 percent Confidence interval is: %f to %f \n' %(lower_limit,upper_limit))
		fflip.write('95 percent Confidence interval in percent is: %f percent to %f percent \n' %(lower_limit*100,upper_limit*100))	

	else:
		fflip.write('\n Variance cannot be calculated since there is only one case of atleast one flip\n')
		fflip.write('\nHence the statistics for design at path %s: cannot be printed \n' %path )

fflip.close()



#Add the details of number of DFFs
fa=open('/%s/subcktinstances.sp' %path, 'r')
fb=open('/%s/spice_results/count_flips_summary.csv' %path, 'a+')
read=fa.readlines()
filelen=len(read)
fb.writelines(read[filelen-3])
fb.writelines(read[filelen-2])
fb.writelines(read[filelen-1])
fb.writelines("\n\n")
fa.close()
fb.close()











