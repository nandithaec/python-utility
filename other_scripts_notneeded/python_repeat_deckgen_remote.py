#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: python python_repeat_deckgen_remote.py -n 20 -m decoder_behav_pnr -f decoder -s 2323

import optparse
import re,os
import fileinput
import subprocess
import python_compare,random

from optparse import OptionParser

parser = OptionParser('Repeat execution of deckgen.pl')
parser.add_option("-n", "--num",dest='num',  help='number of spice decks simulated at a time')
parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--folder", dest="folder",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-o", "--outloop", dest="outloop",help="Outer loop variable ")
#parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()

module=options.module
path=options.folder
#/home/user1/simulations/decoder
num_at_a_time=int(options.num)
outloop=int(options.outloop)
#seed=int(options.seed)

#path= ("/home/user1/simulations/%s" %folder)

#Removing the existing reference RTL File in module_reference_out/RTL.csv if it already exists.
#This can already contain values if we have run deckgen- during testing.

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

if not os.path.exists('%s/spice_decks_%s' %(path,outloop)):
	os.mkdir('%s/spice_decks_%s' %(path,outloop))

start= ((outloop-1)*num_at_a_time) + 1  # ((1-1)*10) +1 =1  , ((2-1)*10) +1 =11
end = (num_at_a_time)*outloop  #(10*1) = 10, (10*2)=20

print "***Inside repeat_deckgen. Executing deckgen to create decks and RTL.csv reference file\n***"
for loop_var in range(start, end+1): 
	#random.seed(seed+loop_var)
	#seed_mod=random.randrange(10000000)
	os.system('perl %s/deckgen_remote.pl -s %s/reference_spice.sp -l %s/glitch_osu018_stdcells_correct_original.sp -r %s/%s_reference_out/tool_reference_out.txt -n %d -m %s -f %s -o %s' %(path,path,path,path,module,loop_var,module,path,outloop))























