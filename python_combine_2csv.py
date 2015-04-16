#!/usr/bin/env python

#Feb 9 2015

#Example usage: python python_combine_2csv.py  -t /home/users/nanditha/sentaurus/65nm_mos/final/Monte_carlo -f data_table -g result_combined

import optparse
import re,os
import csv, re
import random,shutil
import fileinput,sys


from optparse import OptionParser



parser = OptionParser('This script does post processing on the plot files obtained from sdevice simulation, to extract current pulse magnitude, rise and fall times, charge collected\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-t", "--tem",dest='temp_path', help='Enter the path of the results files')
parser.add_option("-f", "--fi1",dest='csv1', help='Enter the first csv file name')
parser.add_option("-g", "--fi2",dest='csv2', help='Enter the 2nd csv file name ')


(options, args) = parser.parse_args()


path=options.temp_path
csv1=options.csv1
csv2=options.csv2

fres = open('%s/csv_finalresult_combined.csv' %(path), 'wb')
writer = csv.writer(fres)

f1 = open('%s/%s.csv' %(path,csv1), 'rb') 
f2 = open('%s/%s.csv' %(path,csv2), 'rb') 

file1 = csv.reader(f1)
file2 = csv.reader(f2)

headers1 = file1.next()
headers2 = file2.next()


combined_csv=[]
row_csv=[]

for i in range(0,len(headers1)):
	row_csv.append(headers1[i])


for i in range(0,len(headers2)):
	row_csv.append(headers2[i])

combined_csv.append(row_csv)
print "\ncombined row:",combined_csv
csv_rows=0

for row in file1: #For every row in the diff file. There will be as many rows in diff_file_rise as well
	row_csv=[]
	csv_rows=csv_rows+1 
	for i in range(0,len(headers1)):
		row_csv.append(row[i])
	#print "\nrow file1:",row_csv
	row_file2= file2.next() 

	for i in range(0,len(headers2)):
		row_csv.append(row_file2[i])
	#print "\nrow file2:",row_csv

	combined_csv.append(row_csv)
	#print "\ncombined row:",combined_csv
	print"\nNumber of current row is:",csv_rows

writer.writerows(combined_csv)
print "\n combined row:",combined_csv
print "\nCombining done.\n"
f1.close()
f2.close()
fres.close()



