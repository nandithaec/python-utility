
#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: Without seed: python python_call_utility3.py -m decoder_behav_pnr -f /home/user1/simulations/decoder -d decoder -t 180 -n 100 --group 50 --backup 2


import optparse
import re,os
import glob,shutil,csv
import random
import subprocess, time
import random
#import python_compare_remote

from optparse import OptionParser

parser = OptionParser('Copy design folder to remote cluster, generate multiple decks and simulate. Obtain resutls and concatenate then')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder (your working dir)- either this machine or remote machine. IF remote machine, enter /home/user1/simulations/<design_folder_name>")
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of your design folder")
parser.add_option("-t", "--tech",dest='tech', help='Enter the technology node-for eg., For 180nm, enter 180')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks to be simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
parser.add_option("--backup",dest='backup',  help='Enter the number of spice decks you want to backup/save per run. For ef., if you entered -n 1000 and --group 100, and if you want to save 2 decks per 100, enter 2 ')
#parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()


module=options.module
num=options.num
path=options.path
design_folder=options.design_folder
tech=options.tech
num_at_a_time=options.group
backup_per_run=options.backup
#seed=int(options.seed)

#Whatever number of decks to be simulated- is assumed to be more than or equal to 1000.
#At a time, only 1000 are generated and run- to save disk space. After collecting results, they are deleted
num_of_loops=(int(num)/int(num_at_a_time))


#Clearing the results before starting off new simulatin
if os.path.exists('%s/spice_results' %path):
	os.chdir('%s/spice_results' %path)
	for f in glob.glob("count*.csv"):
		os.remove(f)

if os.path.exists('%s/spice_results' %path):
	os.chdir('%s/spice_results' %path)
	for f in glob.glob("spice_rtl_*.csv"):
		os.remove(f)

if os.path.isfile('%s/spice_results/result_summary_flipcount.csv' %(path)):
	os.remove('%s/spice_results/result_summary_flipcount.csv' %(path))


#Clear Back up directory

backup_dir = '%s/backup_spice_decks' %(path)

if os.path.exists(backup_dir):
	shutil.rmtree(backup_dir)
if not os.path.exists(backup_dir):
	os.mkdir(backup_dir)	



#Fresh simulation
for for_loop in range(1, (num_of_loops+1)): 

	
	print "Deleting the existing spice decks before creating new ones!\n"
	spice_dir = '%s/spice_decks' %(path)

	if os.path.exists(spice_dir):
		shutil.rmtree(spice_dir)

	#random.seed(seed*loop)
	#seed_new=random.randrange(354000000)
	#python python_utility3_remote.py -m decoder_behav_pnr -f /home/user1/simulations/decoder -d decoder -t 180 -n 100 --group 50 --backup 2
	proc= subprocess.Popen('python %s/python_utility3_remote.py  -m %s -f %s -d %s -t %s --group %s --backup %s -l %s' %(path,module,path,design_folder,tech,num_at_a_time,backup_per_run,for_loop), shell=True)
	
	status=proc.wait()
		
	
	if os.path.exists(spice_dir):
		shutil.rmtree(spice_dir)


########################################End of loop########################################################
#For validation of backup spice files

shutil.copy('%s/glitch_osu018_stdcells_correct_original.sp' %path, '%s/backup_spice_decks' %path )
shutil.copy('%s/tsmc018.m' %path, '%s/backup_spice_decks' %path )

print "Combining all rtl diff files\n"
os.system('python  %s/python_count_flips_remote.py -f %s  -n %s  --group %s' %(path,path,num,num_at_a_time))








