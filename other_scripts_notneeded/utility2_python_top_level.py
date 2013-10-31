#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: python utility2_python_top_level.py -m decoder_behav_pnr -f decoder -c 1e9 -t 180 -n 10

import optparse
import re,os
import fileinput
import subprocess
import python_compare

from optparse import OptionParser

parser = OptionParser('Copy design folder to remote cluster, generate multiple decks and simulate. Obtain resutls and concatenate then')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--folder", dest="folder",help="Enter the name of the design folder (your current working dir) which will be copied to the 48-core cluster to run simulations parallely")
parser.add_option("-c", "--clk", dest='clkfreq', help='Enter the clk frequency in Hz, for eg., if 900MHz, enter 900e6')
parser.add_option("-t", "--tech",dest='tech',  help='Enter the technology node that you want to simulate, for eg.,180 for 180nm')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')

(options, args) = parser.parse_args()


module=options.module
folder=options.folder
clkfreq=options.clkfreq
techn=options.tech
num=options.num



##Example usage: perl GlitchLibGen.pl -i osu018_stdcells_correct_original.sp- this file will be provided by us for the 180nm technology
#Create a glitched std cell library file for 180nm techn
os.system('perl GlitchLibGen.pl -i osu018_stdcells_correct_original.sp')
print "***Created glitch library..\n"

##Generate a template simulatable spice netlist from the dspf file generated after pnr. This would include all .ic, Voltage sources, meas, tran, control, param etc
#NetlistFormat.pl
#perl NetlstFrmt.pl -v decoder_behav_pnr_modelsim.v -s pnr/op_data/decoder_behav_pnr_final.dspf -l glitch_osu018_stdcells_correct_allcells.sp -c 1e9 -t 180 -m decoder_behav_pnr
os.system('perl NetlstFrmt.pl -v %s_modelsim.v  -s pnr/op_data/%s_final.dspf -l glitch_osu018_stdcells_correct_original.sp -c %s -t %s -m %s' %(module,module,clkfreq,techn, module))
print "***Done modifying the spice file to make it simulatable. File available in current directory reference_spice.sp\n"

#Copy the entire Current directory to the machine where the simulations will be run in parallel. Currently we are running it on the 48-core cluster under the username: user1, password: user123 and copying to the folder /home/user1/simulations

#Copy the entire Current directory to the machine where the simulations will be run in parallel. Currently we are running it on the 48-core cluster under the username: user1, password: user123 and copying to the folder /home/user1/simulations. Files will HAVE to be run from the remote machine,since the slave machines are connected only to the master and not to the outside world. So, these slave machines can ONLY be accessed by the master node.
print "\nCopying current working directory to remote cluster to run simulations parallely\n"
os.system('scp -r ../%s user1@10.107.105.201:/home/user1/simulations' %folder)
print "Done copying files\n"
print "Now connecting to the remote machine. Once connected with your password, scripts at that location will be executed..\n"
#os.system('ssh -XY user1@10.107.105.201')
#print "All scripts also copied to remote machine.. Now execute the scripts there to generate multiple decks, running ngspice parallely etc\n"













