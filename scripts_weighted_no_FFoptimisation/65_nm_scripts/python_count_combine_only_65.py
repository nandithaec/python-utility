
#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Backup directories renamed to 'backup_spice_decks_3rd_edge' and 'backup_spice_decks_2nd_edge': feb 12 2014.
#Calling the python_FF_strike_taxonomy.py and python_gate_strike_taxonomy.py scripts explicitly, since calling it through a function did not run on the yuva cluster: Feb 11 2014
#Calling the python_taxonomy_gate_FF.py script to tabulate the gate and FF taxonomy and combine the resultant 2 pdf files: Feb 11 2014
#Backup directories etc created for the 2nd rise edge measurement backup. Other scripts which are being used to measure the 2nd rise edge data are being run from this script: Feb 7 2014
#This version of the script has the facility of selecting the gate based on the area of the gate. This version of the script uses another script python_weighted_gateselection.py to pick the random gate based on its area: Nov 17 2013
#Glitch insertion window is within the 2.5 cycles, and not the 6.5 cycles that is required for the case with intermediate FFs

#Example usage: python python_count_combine_only.py -m c432_clk_ipFF -p /home/nanditha/Documents/utility/design_cases_taxonomy/c432/2_cycles -d 2_cycles -t 180 -n 4000 --group 1000 --clk 200 --std_lib osu018_stdcells_correct_vdd_gnd.sp

import optparse
import re,os
import glob,shutil,csv
import random
import subprocess, time
import random,sys


from optparse import OptionParser

parser = OptionParser('This script reads in the template spice file and the inputs to the script are listed as arguments below, which are all necessary arguments.\nAfter a previous script has copied the current working directory to a remote cluster, this script invokes several scripts inturn:\n1.perl_calculate_gates_clk.pl\n2.perl_calculate_drain.pl\n3.deckgen_remote_seed.pl\n4.python_GNUparallel_ngspice_remote.py\n5.python_compare_remote_seed.py\n6.python_count_flips_remote_seed.py\n\nThe tasks of these scripts will be described in the help section of the respective scripts. The current script needs pnr/reports/5.postRouteOpt_mult/mult_postRoute.slk as an input. The current script will calculate the number of gates in the design(spice) file, pick a random gate, calculate the number of distinct drains for this gate and pick a drain to introduce glitch it.The location of the glitch is calculated based on the timing/slack information from the SoC encounter output: (pnr/reports/5.postRouteOpt_mult/mult_postRoute.slk) for the particular design, so that we introduce glitch only after the input has changed in the clk period, and before the next rising edge of the clk (when the latch is open). It then invokes deckgen.pl to modify the template spice file to introduce the glitched version of the gate in the spice file. The deckgen creates multiple spice files which will contain different input conditions since they are generated at different clk cycles.\nThe python_GNUparallel_ngspice_remote.py will then distribute these spice files across the different machines in the cluster and simulate these decks using ngspice. The results are csv files which contain output node values after spice simulation.\nThe results are then concatenated into one file and compared against the expected reference outputs that were obtained by the RTL simulation. If the results match, then it means that there was no bit-flip, so a 0 is reported, else a 1 is reported for a bit-flip. The number of flips in a single simulation is counted. Finally, if there are multiple flips given atleast one flip, it is reported as a percentage.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path to your design folder (your working dir)- either this machine or remote machine. IF remote machine, enter ~/simulations/<design_folder_name>")
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of your design folder")
parser.add_option("-t", "--tech",dest='tech', help='Enter the technology node-for eg., For 180nm, enter 180')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks to be simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
#parser.add_option("--backup",dest='backup',  help='Enter the number of spice decks you want to backup/save per run. For ef., if you entered -n 1000 and --group 100, and if you want to save 2 decks per 100, enter 2 ')
#parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')
parser.add_option("-c", "--clk",dest='clk', help='Enter the clk freq in MHz')
parser.add_option("-l", "--std_lib",dest='std_lib', help='Enter the file name of the standard cell library (sp file)')

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
std_lib = options.std_lib


clk_period = (1.0/float(clk))*(0.000001)
half_clk_period = clk_period/2.0
change_time= half_clk_period/3.0
end_PWL= half_clk_period + change_time #in ns generally

#To determine when the glitch needs to be introduced, depends on the slack information


########################################End of loop########################################################
"""
print "Combining all rtl diff files\n"
os.system('python  %s/python_count_flips_2nd_3rd_rise.py -f %s  -n %s  --group %s -s %s' %(path,path,num,num_at_a_time,seed))  #To save the seed to results file


#Add the details of number of DFFs
fa=open('/%s/subcktinstances.sp' %path, 'r')
fb=open('/%s/spice_results/count_flips_final_summary.csv' %path, 'a+')
read=fa.readlines()
filelen=len(read)
fb.writelines(read[filelen-3])
fb.writelines(read[filelen-2])
fb.writelines(read[filelen-1])
fa.close()
fb.close()
"""
#Doing the gate taxonomy and strike taxonomy functions through this script.
print "\nDoing the taxonomy for gates\n"

#Always run the gates first and then the FFs. FF script needs some outputs which are written out from the gates script.
os.system('python  %s/python_gate_strike_taxonomy.py  -p %s -m %s' %(path,path,module)) 
print "\nDoing the taxonomy for FFs\n"

os.system('python  %s/python_FF_strike_taxonomy.py  -p %s -m %s' %(path,path,module)) 

print "\nCombining the pdf reports\n"
os.system('python %s/python_combine_pdfs.py -p %s/spice_results -m %s' %(path,path,module))





