#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: python python_repeat_deckgen.py -n 20 -m decoder_behav_pnr

import optparse
import re,os
import fileinput
import subprocess
import python_compare

from optparse import OptionParser

parser = OptionParser('Repeat execution of deckgen.pl')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')

(options, args) = parser.parse_args()

module=options.module
num=options.num


#Removing the existing reference RTL File in module_reference_out/RTL.csv if it already exists.
#This canalready contain values if we have run deckgen- during testing.

if os.path.isfile("%s_reference_out/RTL.csv" %module):
	print "****Removing the existing RTL.csv file in folder %s_reference_out ****\n" %(module)
	os.remove("%s_reference_out/RTL.csv" %module)




#Now, we need the header in RTL.csv, so we create an RTL.csv and copy the headers from the RTL_backup.csv that we had saved from Netlstfrmt.pl
fout = open('%s_reference_out/RTL.csv' %module, 'w')
fin = open('%s_reference_out/RTL_backup.csv' %module, 'r')

in_data=fin.read()
fout.write(in_data)

fout.close()
fin.close()

#perl deckgen.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -n 1 -m decoder_behav_pnr
for loop_var in range(1,(int(num)+1)):
	os.system('perl deckgen.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r %s_reference_out/tool_reference_out.txt -n %d -m %s' %(module,loop_var,module))






















