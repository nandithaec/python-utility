#!/usr/bin/env python

#ASSUMPTION: This will always be excecuted on the 48core cluster user1@10.107.105.201 and the design folder will be copied always to /home/user1/simulations folder and executed

# Code modified to do post processing of the result files for the 2nd rising edge. Last section of the code is added : Feb 7 2014
#Multiple spice decks that were generated using deckgen in the remote machine, will be run using ngspice and GNU Parallel on the cluster. We can also ssh to other machines which have GNU Parallel and ngspice installed. ssh-keygen should have been done so that it would not ask for ssh password everytime we ssh to the machines.

#Example usage: python python_GNUparallel_hspice_rise_local_mc_65 -n 1000 -d c432 -o 1 -p /home/users/nanditha/Documents/utility/65nm/c432


import optparse
import re,os
import fileinput
import glob
import shutil
import time,csv

from optparse import OptionParser

parser = OptionParser('This script will read in the path where multiple spice decks are present. This will generaloly be <path>/<spice_decks>. It reads in the total number of files to be simulated. It runs ngspice parallely on the multiple spice decks on the 48-core cluster machine, using an utility called GNU parallel. sshmachines.txt contains the IP Addresses of the machines to which you want to ssh and run parallel simulations\n#ASSUMPTION: This will always be excecuted on the 48core cluster user1@10.107.105.201 and the design folder will be copied always to <path> folder and executed\nMultiple spice decks that were generated using deckgen in the remote machine, will be run using ngspice and GNU Parallel on the cluster. We can also ssh to other machines which have GNU Parallel and ngspice installed. ssh-keygen should have been done so that it would not ask for ssh password everytime we ssh to the machines. IN case you want to add other machines, uncomment the commented part "Comment this out if not using desktop to run simulations" and include the machine names in the sshmachines.txt\n Once simulations are complete, the spice_decks folder contains glitch_report_outputs_%d.csv files which will all be combined into one output file:<path>/spice_results/final_results_spice_outputs_%d.csv, where %d will be the outloop variable\n Author:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')


parser.add_option("-n", "--num", type="int", dest="num_spice",help="Enter the number of spice decks to be simulated at a time")
parser.add_option("-p", "--path", dest="path",help="Enter the entire path to the design folder that is copied to remote machine")
parser.add_option("-d", "--dir", dest="folder",help="Enter the name of the design folder that is copied to remote machine")
parser.add_option("-o", "--outloop", dest="outloop",help="This is the number of times this script is executed in a loop. In case we are a lot of simulations, we can divide them into groups. For eg., if 10000 simulations need to be run, we can run only 1000 at a time. So we run this 10 times, and this becomes the outloop variable. This is passed from the top level script.")

(options, args) = parser.parse_args()

num_spice=int(options.num_spice)
folder=options.folder
path=options.path
outloop=int(options.outloop)


if os.path.exists('%s/spice_decks_%s' %(path,outloop)):
	os.chdir('%s/spice_decks_%s' %(path,outloop))
		
	for f in glob.glob("*.st0"):
		os.remove(f)
	
	for f in glob.glob("*.csv"):
		os.remove(f)
	
	for f in glob.glob(".nfs*"):
		os.remove(f)

	for f in glob.glob("*.ic0"):
		os.remove(f)
	
os.chdir("../")
print os.getcwd()

time.sleep(5)	
####################### NGSPICE SIMULATION RUN#######################
##seq 1 n - run n decks in current folder
# This is to execute GNU Parallel. +0 means utilise all cores in the processor.
#--sshloginfile file.txt uses the IP addresses of machines given the file.txt to ssh to them and run simulations. 
#THESE MACHINES SHOULD HAVE 'GNU Parallel' AND NGSPICE INSTALLED IN THEM. AND ALSO, SSH-KEY-GEN SHOULD BE DONE TO DO A PASSWORD-LESS LOGIN

print "\n****Launching GNU Parallel to run hspice simulations****\n"

start= ((outloop-1)*num_spice) + 1  # ((1-1)*10) +1 =1  , ((2-1)*10) +1 =11
end = (num_spice)*outloop  #(10*1) = 10, (10*2)=20

#ls | parallel --progress -j +0 -q bash -c "hspice {}"
os.chdir("%s/spice_decks_%s" %(path,outloop))
print "Changed to" , os.getcwd()
time.sleep(2)
os.system("ls hspice_*.sp | parallel --progress -j 3  -q bash -c 'hspice {};pwd;' " )

os.chdir("../")
#time.sleep(2)
print os.getcwd()

print "\n****Completed hspice simulations****\n"
#print "****Resulting csv files are saved in the same folder in which the spice decks are****\n"

###################################################################################################################
#######################Now do the post processing of the result files#######################
"""
#Combine all the csv results files and place the resulting file in the results folder
#Creating results folder is done way back in the modperl2_outwrtr_new.pl script. The spice headers are also written out in that script.

fh = open("%s/spice_results/headers.csv" %(path),"r")
header=fh.read()

fw1 = open("%s/spice_results/final_results_spice_outputs_%d.csv" %(path,outloop),"w")
#Write the header first and then write the csv outputs of the rest of the files
fw1.write(header)

start= ((outloop-1)*num_spice) + 1  # ((1-1)*10) +1 =1  , ((2-1)*10) +1 =11
end = (num_spice)*outloop  #(10*1) = 10, (10*2)=20

########################################################################################################
#Individual echo statements will lead to a process id at the end of each file. Deleteting them and getting transpose of all glitch_*.csv files
#Loop over all existing csv files
print "****Deleting the process id at the end of each row in the result file and transposing the column to row****\n"
time.sleep(5)

for num in range(start,(end+1)):

	fr = open("%s/spice_decks_%s/glitch_report_outputs_%d.csv" %(path,outloop,num),"r")
	fout = open("%s/spice_decks_%s/glitch_report_outputs_new_%d.csv" %(path,outloop,num),"w")
	reader=csv.reader(fr)
	writer = csv.writer(fout)
	k=[]

	for row in reader:
		#print row
		del row[-1]
		#print "new row:\n" , row
		k.append(row)
		#print "k is", k

	writer.writerows(zip(*k))  #write transposed csv column into row format
	fr.close()
	fout.close()

###############Combine the results of all csv files into one file final_results_spice_outputs_ #############

for num in range(start,(end+1)):  #Always for loop takes max len + 1
	fr = open("%s/spice_decks_%s/glitch_report_outputs_new_%d.csv" %(path,outloop,num), "r")
	data=fr.read()
	fw1.write(data)
	fr.close()

fw1.close()
fh.close()
print "****Combined all csv files into a single file in the results folder along with the header****\n"


###################################################################################################################
###################################################################################################################
#######################Now do the post processing of the result files for the rise edge #######################

#Combine all the csv results files and place the resulting file in the results folder
#Creating results folder is done way back in the modperl2_outwrtr_new.pl script. The spice headers are also written out in that script.

fh = open("%s/spice_results/headers.csv" %(path),"r")
header=fh.read()


fw1_rise = open("%s/spice_results/final_results_spice_outputs_rise_%d.csv" %(path,outloop),"w")
#Write the header first and then write the csv outputs of the rest of the files
fw1_rise.write(header)


start= ((outloop-1)*num_spice) + 1  # ((1-1)*10) +1 =1  , ((2-1)*10) +1 =11
end = (num_spice)*outloop  #(10*1) = 10, (10*2)=20

########################################################################################################
#Individual echo statements will lead to a process id at the end of each file. Deleteting them and getting transpose of all glitch_*.csv files
#Loop over all existing csv files
print "****Deleting the process id at the end of each row in the result file and transposing the column to row****\n"
#time.sleep(5)

for num in range(start,(end+1)):

	fr = open("%s/spice_decks_%s/glitch_report_outputs_rise_%d.csv" %(path,outloop,num),"r")
	fout = open("%s/spice_decks_%s/glitch_report_outputs_rise_new_%d.csv" %(path,outloop,num),"w")
	reader=csv.reader(fr)
	writer = csv.writer(fout)
	k=[]

	for row in reader:
		#print row
		del row[-1]
		#print "new row:\n" , row
		k.append(row)
		#print "k is", k

	writer.writerows(zip(*k))  #write transposed csv column into row format
	fr.close()
	fout.close()

###############Combine the results of all csv files into one file final_results_spice_outputs_rise_ #############

for num in range(start,(end+1)):  #Always for loop takes max len + 1
	fr = open("%s/spice_decks_%s/glitch_report_outputs_rise_new_%d.csv" %(path,outloop,num), "r")
	data=fr.read()
	fw1_rise.write(data)
	fr.close()

fw1_rise.close()
print "****Combined all csv files into a single file in the results folder along with the header****\n"

"""




