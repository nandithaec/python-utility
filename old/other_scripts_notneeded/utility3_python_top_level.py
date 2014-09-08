
#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: python utility3_python_top_level.py -m decoder_behav_pnr -n 15 -p /home/user1/simulations/decoder -d decoder -t 180


import optparse
import re,os
import fileinput
import subprocess
import python_compare

from optparse import OptionParser

parser = OptionParser('Copy design folder to remote cluster, generate multiple decks and simulate. Obtain resutls and concatenate then')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("-p", "--path", dest="folder",help="Enter the ENTIRE path to your design folder (your working dir)- either this machine or remote machine. IF remote machine, enter /home/user1/simulations/<design_folder_name>")
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of your design folder")
parser.add_option("-t", "--tech",dest='tech', help='Enter the technology node-for eg., For 180nm, enter 180')

(options, args) = parser.parse_args()


module=options.module
num=options.num
path_folder=options.folder
design_folder=options.design_folder
tech=options.tech


##Generate multiple decks with the random gate and random clk cycle picked, with a glitch introduced at a random time instant in a clk cycle
#deckgen.pl will need to be remotely executed through python_repeat_deckgen.py multiple number of times
# python utility3_python_top_level.py -m decoder_behav_pnr -n 10 -f /home/user1/simulations/decoder -d decoder
print "Executing script on remote machine- to clear existing spice files, creating multiple spice decks in spice_decks folder, running ngspice and comparing RTL, spice values\n"
os.system('ssh user1@10.107.105.201 python %s/python_utility3_remote.py -n %s -m %s -f %s -d %s -t %s' %(path_folder,num,module,path_folder,design_folder,tech))

"""
#python python_utility3_testing.py -m decoder_behav_pnr -n 15 -f /home/user1/simulations/decoder
#os.system('ssh user1@10.107.105.201 python %s/python_repeat_deckgen_remote.py -n %s -m %s -f %s' %(path_folder,num,module,path_folder))

"""

















