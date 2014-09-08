
#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage:  python python_utility3_remote_seed.py -m decoder_behav_pnr -p /home/user1/simulations/decoder -d decoder -t 180 -n 1000000 --group 10000 --clk 1000
#Example usage: python python_utility3_remote_seed.py -m decoder_behav_pnr -p /home/user1/simulations/decoder -d decoder -t 180 -n 540000 --group 10000 --clk 1000

#Example usage: python python_utility3_remote_seed.py -m decoder_behav_pnr -p /home/user1/simulations/decoder -d decoder -t 180 -n 10000 --group 1000 --clk 1000

import optparse
import re,os
import glob,shutil,csv
import random
import subprocess, time
import random,sys
#import python_compare_remote

from optparse import OptionParser

parser = OptionParser('Copy design folder to remote cluster, generate multiple decks and simulate. Obtain resutls and concatenate then')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path to your design folder (your working dir)- either this machine or remote machine. IF remote machine, enter ~/simulations/<design_folder_name>")
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of your design folder")
parser.add_option("-t", "--tech",dest='tech', help='Enter the technology node-for eg., For 180nm, enter 180')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks to be simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
#parser.add_option("--backup",dest='backup',  help='Enter the number of spice decks you want to backup/save per run. For ef., if you entered -n 1000 and --group 100, and if you want to save 2 decks per 100, enter 2 ')
#parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')
parser.add_option("-c", "--clk",dest='clk', help='Enter the clk freq in MHz')

(options, args) = parser.parse_args()


module=options.module
num=options.num
path=options.path
design_folder=options.design_folder
tech=options.tech
num_at_a_time=options.group
#backup_per_run=options.backup
#seed=int(options.seed)
clk=(options.clk)

#Whatever number of decks to be simulated- is assumed to be more than or equal to 1000.
#At a time, only 1000 are generated and run- to save disk space. After collecting results, they are deleted
num_of_loops=(int(num)/int(num_at_a_time))


if os.path.exists('%s/spice_results' %path):
	os.chdir('%s/spice_results' %path)
	for f in glob.glob("count*.csv"):
		os.remove(f)

if os.path.exists('%s/spice_results' %path):
	os.chdir('%s/spice_results' %path)
	for f in glob.glob("spice_rtl_*.csv"):
		os.remove(f)

if os.path.exists('%s/spice_results' %path):
	os.chdir('%s/spice_results' %path)
	for f in glob.glob("final_results_spice_outputs_*.csv"):
		os.remove(f)



if os.path.isfile('%s/spice_results/result_summary_flipcount.csv' %(path)):
	os.remove('%s/spice_results/result_summary_flipcount.csv' %(path))


#Clear Back up directory

backup_dir = '%s/backup_spice_decks' %(path)

if os.path.exists(backup_dir):
	shutil.rmtree(backup_dir)

if not os.path.exists(backup_dir):
	os.mkdir(backup_dir)	

print "Deleting the existing spice decks before creating new ones!\n"
os.system('rm -rf %s/spice_decks_*' %path)

start_loop=1

frand = open('%s/random_number_histogram.txt' %(path), 'w')

seed = random.randint(0, sys.maxint)
print "seed is: ", seed
frand.write("Seed:%d\n" %seed)

random.seed(seed) #Seeding the random number generator


clk_period = (1.0/float(clk))*(0.000001)

print "\nclk is ",clk
print "\nClk_period: ", clk_period

#Uncomment this for future designs. For decoder example, decoder folder has already been created on desktop
#os.system('ssh nanditha@10.107.90.52 mkdir /home/nanditha/simulations/%s' %(design_folder))
###########################################Comment this out if not using desktop to run##################################
"""
print "\nCopying a python script to desktop machine!\n"
		
os.system('scp %s/python_desktop_copy.py %s/glitch_osu018_stdcells_correct_original.sp %s/tsmc018.m nanditha@10.107.90.52:/home/nanditha/simulations/%s/' %(path,path,path,design_folder))
"""
######################################################################################################
#perl perl_calculate_gates_clk.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -m decoder_behav_pnr -f /home/user1/simulations/decoder

os.system('perl %s/perl_calculate_gates_clk.pl -s %s/reference_spice.sp -l %s/glitch_osu018_stdcells_correct_original.sp -r %s/%s_reference_out/tool_reference_out.txt -m %s -f %s ' %(path,path,path,path,module,module,path))

fg = open('%s/tmp_random.txt' %(path), 'r')
gate_clk_data = [line.strip() for line in fg]

num_of_gates=int(gate_clk_data[0])
print "\nnum of gates is %d" %num_of_gates

num_of_clks=int(gate_clk_data[1])
print "\nnum of clocks is %d" %num_of_clks

fg.close()


#Fresh simulation
for loop in range(start_loop, (num_of_loops+1)): 

		
	#time.sleep(2)
	#os.system('cd /home/user1/simulations/decoder ; ls; pwd;ls | wc -l' )
	#time.sleep(5)

	print "Now, creating multiple spice decks in spice_decks folder in current directory on the remote machine\n"
	
	#os.system('python %s/python_repeat_deckgen_remote_seed.py -m %s -n %s -f %s -o %s -s %d' %(path,module,num_at_a_time,path,loop,seed_new))

#########################################repeat_deckgen copied starting from here#######################################

	if os.path.isfile("%s/%s_reference_out/RTL.csv" %(path,module)):
		print "****Removing the existing RTL.csv file in folder %s_reference_out ****\n" %(module)
		os.remove("%s/%s_reference_out/RTL.csv" %(path,module))


	#Now, we need the header in RTL.csv, so we create an RTL.csv and copy the headers from the RTL_backup.csv that we had saved from Netlstfrmt.pl
	fout = open('%s/%s_reference_out/RTL.csv' %(path,module), 'w')
	fin = open('%s/%s_reference_out/RTL_backup.csv' %(path,module), 'r')

	in_data=fin.read()
	fout.write(in_data)

	fout.close()
	fin.close()

	if not os.path.exists('%s/spice_decks_%s' %(path,loop)):
		os.mkdir('%s/spice_decks_%s' %(path,loop))

	
	start= ((loop-1)*int(num_at_a_time)) + 1  # ((1-1)*10) +1 =1  , ((2-1)*10) +1 =11
	end = (int(num_at_a_time))*loop  #(10*1) = 10, (10*2)=20

	print "***Inside repeat_deckgen. Executing deckgen to create decks and RTL.csv reference file\n***"
	for loop_var in range(start, end+1): 
		
		rand_gate= int(random.randrange(num_of_gates))  #A random gate picked
		#print "Random gate is: ",rand_gate
		rand_clk= int(random.randrange(num_of_clks))  #A random clk picked
		#print "Random clock cycle is: ",rand_clk
		#perl perl_calculate_drain.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -m decoder_behav_pnr -f /home/user1/simulations/decoder -g 27

		os.system('perl %s/perl_calculate_drain.pl -s %s/reference_spice.sp -l %s/glitch_osu018_stdcells_correct_original.sp -r %s/%s_reference_out/tool_reference_out.txt -m %s -f %s -g %d ' %(path,path,path,path,module,module,path,rand_gate))

		fg = open('%s/tmp_random.txt' %(path), 'r')
		drain_data = [line.strip() for line in fg]

		num_of_drains=int(drain_data[0])
		print "\nnum of drains is %d" %num_of_drains

		fg.close()
#If num of drains is 2, randrange(2) returns 0 or 1,where as we want drain number 1 or drain number 2. so, doing +1
		rand_drain= int(random.randrange(num_of_drains))+1  #A random drain picked. 

		unif=random.uniform(0,0.3*clk_period)
		rand_glitch= (1.2*clk_period) +  unif  #A random glitch picked
		print "\nglitch within clk cycle= ",unif
		print "\nRandom gate: %d\nRandom drain: %d\nRandom clock cycle:%d\nRandom glitch location:%e\n " %(rand_gate,rand_drain,rand_clk,rand_glitch)
		frand.write("%d, %d, %d,%e\n" %(rand_gate,rand_drain,rand_clk,rand_glitch))

#perl deckgen_remote_seed.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -n 1 -m decoder_behav_pnr -f /home/user1/simulations/decoder -g 27 -d 2 -c 10 -i 1.42061344093991e-09 -o 1 

		#deckgen.pl will need to be remotely executed through python_repeat_deckgen.py multiple number of times
		os.system('perl %s/deckgen_remote_seed.pl -s %s/reference_spice.sp -l %s/glitch_osu018_stdcells_correct_original.sp -r %s/%s_reference_out/tool_reference_out.txt -n %d -m %s -f %s  -o %s -g %s -d %s -c %s -i %s' %(path,path,path,path,module,loop_var,module,path,loop,rand_gate,rand_drain,rand_clk,rand_glitch))

##################Script repeat_deckgen copied ends here####################################
	
##################################Comment this out if not using desktop to run##################################
	#delete existing files on desktop machine and copy new files for simulation
	#os.system('ssh nanditha@10.107.90.52 python /home/nanditha/simulations/%s/python_desktop_copy.py -p %s -d %s -l %d' %(design_folder,path,design_folder,loop))
################################################################################################################

	#print "\nmaster machine.. listing the files and pausing\n"
	#os.system('cd /home/user1/simulations/decoder/spice_decks_%d ; ls; pwd;ls | wc -l' %loop)
	#time.sleep(1)
	#print "\nssh to slave.. listing the files and pausing\n"
	#os.system('ssh user1@192.168.1.8 pwd; cd /home/user1/simulations/decoder/spice_decks_%d; pwd;ls;pwd;ls | wc -l' %loop)
	#time.sleep(3)
	
	

	print "Running GNU Parallel and ngspice on the created decks\n"
	os.system('python %s/python_GNUparallel_ngspice_remote.py -n %s -d %s -o %s -p %s' %(path,num_at_a_time,design_folder,loop,path))

	seed_new= int(random.randrange(100000)*random.random())  #Used by compare script to backup random decks
	#seed_new=seed*loop
	print "New seed every outer loop is ", seed_new

	#python_results_compare.py will then need to be remotely executed
	#Might need to execute these last 3 in a loop till the results are acceptable
	print "Comparing the RTL and spice outputs\n"
	os.system('python %s/python_compare_remote_seed.py -m %s -f %s -n %s -t %s -l %d -s %s' %(path,module,path,num_at_a_time,tech,loop,seed_new))


##########################################################
	
	spice_dir = '%s/spice_decks_%s' %(path,loop)

	
	if os.path.exists(spice_dir):
		shutil.rmtree(spice_dir)


########################################End of loop########################################################
#For validation of backup spice files

shutil.copy('%s/glitch_osu018_stdcells_correct_original.sp' %path, '%s/backup_spice_decks' %path )
shutil.copy('%s/tsmc018.m' %path, '%s/backup_spice_decks' %path )

print "Combining all rtl diff files\n"
os.system('python  %s/python_count_flips_remote_seed.py -f %s  -n %s  --group %s -s %s' %(path,path,num,num_at_a_time,seed))  #To save the seed to results file








