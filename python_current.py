#!/usr/bin/env python

#Feb 9 2015

#Example usage: python python_current.py  -t /home/users/nanditha/sentaurus/65nm_mos/final/Monte_carlo -c template_sdev_nmos_des_ser_Vd_Vg.cmd -p /home/users/nanditha/sentaurus/65nm_mos/final/Monte_carlo/data_table.csv

import optparse,glob
import re,os
import csv, re
import random,shutil
import fileinput,sys


from optparse import OptionParser



parser = OptionParser('This script creates multiple sdevice command files from a template file for varying values of Vd,Vg,Vs,strike location and strike angle. It is assumed that the template sdevice cmd file has the tdr and parameter file paths correctly set,\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-t", "--tem",dest='temp_path', help='Enter the path of the template sdevice command file. This is the location where the multiple command files and results files will be created')
parser.add_option("-c", "--cmd",dest='cmd_file', help='Enter the name of the template sdevice command file, along with the file extension')
parser.add_option("-p", "--para",dest='parameter', help='Enter the path of the csv file that has parameters for the template file, along with the file and file extension')

(options, args) = parser.parse_args()


path=options.temp_path
cmd_file=options.cmd_file
parameter=options.parameter
"""
results_dir = '%s/results' %(path)


if os.path.exists(results_dir):
	shutil.rmtree(results_dir)

if os.path.exists('%s' %path):
	os.chdir('%s' %path)
	for f in glob.glob("sdev*.cmd"):
		os.remove(f)
	for f in glob.glob("*.plt"):
		os.remove(f)

f = open('%s/%s' %(path,cmd_file), 'rb')
template_data=f.readlines()
fpar = open('%s' %parameter, 'rb')

reader= csv.reader(fpar)

headers = reader.next() #parameter headers

print "\nHeaders", headers
print "\nHeader len:\n", (len(headers)) #length


row_num=0

for row in reader:
	row_num=row_num+1
	fout = open('%s/sdevice_command_%d.cmd' %(path,row_num), 'wb')
	fout.writelines(template_data)
	print "Row number is %d" %row_num
	#print "Row is", row
	#print "Row[2] is",row[2]
	fout.close()
	for k in range(0,len(headers)):

		#print "Replacing %s" %headers[k]
		word_to_replace="#"+headers[k]+"#"
		#print "word to replace", word_to_replace

		for line in fileinput.input('%s/sdevice_command_%d.cmd' %(path,row_num), inplace=1):
			if ("%s" %word_to_replace) in line:
				
				line = line.replace(word_to_replace,row[k])
				sys.stdout.write(line)

			else:
				sys.stdout.write(line)  #Write line in file as it is
		fileinput.close()
	print "\n\n******Done with the current file******\n\n"

####################################################################################
"""

row_num=320

#Run sdevice command files in sequence

for deck_number in range(1,row_num+1):
	print "Running sdevice_command_%d.cmd" %(deck_number)
	os.system("sdevice %s/sdevice_command_%d.cmd" %(path,deck_number))

	if os.path.exists('%s' %path):
		os.chdir('%s' %path)
		for f in glob.glob("*des*.tdr"):
			os.remove(f)















