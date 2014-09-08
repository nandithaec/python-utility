#!/usr/bin/env python

#Example usage: python utility_python_top_level.py --rtl=/home/users/nanditha/Documents/utility/decoder/decoder.vhd --mod=decoder_behav_pnr --test=/home/users/nanditha/Documents/utility/decoder/test_decoder_pnr.vhd --tb_mod=t_decoder_pnr --clk=1000 --run=1us --design=decoder --tech=180 --num=1000 --path=/home/user1/simulations/decoder 

#This script does a synthesis, place and route of the vhd/verilog file using rtl2gds. The pnr verilog file is modified to include fwrite statements to write the FF outputs to a reference file. This verilog file simulated using modelsim and the reference FF output values written to a text file.


import optparse
import re,os
import fileinput
import subprocess
from optparse import OptionParser

parser = OptionParser('Read in a RTL file, synthesis, pnr and simulate. Write the reference outputs to a file')

parser.add_option("-v","--rtl", help='Enter the ENTIRE path of the RTL (verilog or vhdl) including the RTL file name',dest='rtl')
parser.add_option("-m","--mod", help='Enter the entity name(vhdl) or module name (verilog)',dest='module')
parser.add_option("-t","--test", help='Enter the path of the testbench (vhd/verilog) file for simulating the post layout RTL file, include the filename along with extension as part of this path',dest='test_path')
parser.add_option("-b","--tb_mod", help='Enter the test bench module name that needs to be simulated',dest='test_module')
parser.add_option("-c","--clk", help='Enter the clk frequency in MHz, for eg., if 900MHz, enter 900',dest='clkfreq')
parser.add_option("-r","--run", help='Enter the duration of the simulation run. e.g., 1us or 1 us',dest='runtime')
#########################################################################
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of the design folder (your current working dir) which will be copied to the 48-core cluster to run simulations parallely")
parser.add_option("--tech",dest='tech',  help='Enter the technology node that you want to simulate, for eg.,180 for 180nm')
parser.add_option("-n", "--num",dest='num',  help='Enter the number of spice decks to be generated and simulated')
parser.add_option("--group",dest='group',  help='Enter the number of spice decks to be simulated at a time. For eg., if -n option is 10000, and say we want to run 100 at a time, then enter 100')
parser.add_option("-p", "--path", dest="folder",help="Enter the ENTIRE path to your design folder (your working dir)- either this machine or remote machine. IF remote machine, enter /home/user1/simulations/<design_folder_name>")
#########################################################################

#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

rtl=options.rtl
module=options.module
clkfreq=options.clkfreq
test_path=options.test_path
test_module=options.test_module
runtime=options.runtime
########################
design_folder=options.design_folder
techn=options.tech
num=options.num
########################
path_folder=options.folder
group=options.group



#Example usage: python python1_read_RTL_syn_pnr.py -f decoder.vhd -m decoder_behav_pnr -clk 900
os.system('python python1_read_RTL_syn_pnr.py -f %s -m %s -c %s' %(rtl,module,clkfreq))

#Example usage: perl perl2_outwrtr.pl -v pnr/op_data/decoder_behav_pnr_final.v -m decoder_behav_pnr
os.system('perl modperl2_outwrtr.pl -v pnr/op_data/%s_final.v -m %s' %(module,module))

##Example usage: python python3_create_simdo_vsim.py -rtl decoder_behav_pnr_modelsim.v -tb test_decoder_pnr.vhd -tb_mod t_decoder_pnr -time 1us
os.system('python python3_create_simdo_vsim.py -v %s_modelsim.v -t %s -b %s -r %s' %(module,test_path,test_module,runtime))

####################################################################################################################################################################


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
os.system('scp -r ../%s user1@10.107.105.201:/home/user1/simulations' %design_folder)
print "Done copying files\n"
print "Now connecting to the remote machine. Once connected with your password, scripts at that location will be executed..\n"
#os.system('ssh -XY user1@10.107.105.201')
#print "All scripts also copied to remote machine.. Now execute the scripts there to generate multiple decks, running ngspice parallely etc\n"

####################################################################################################################################################################

##Generate multiple decks with the random gate and random clk cycle picked, with a glitch introduced at a random time instant in a clk cycle
#deckgen.pl will need to be remotely executed through python_repeat_deckgen.py multiple number of times
# python python_utility3_remote_seed.py -m decoder_behav_pnr -p /home/user1/simulations/decoder -d decoder -t 180 -n 10000 --group 1000 --clk 1000
print "Executing script on remote machine- to clear existing spice files, creating multiple spice decks in spice_decks folder, running ngspice and comparing RTL, spice values\n"
os.system('ssh user1@10.107.105.201 python %s/python_utility3_remote.py -n %s -m %s -p %s -d %s -t %s --group %s --clk %s' %(path_folder,num,module,path_folder,design_folder,techn,group,clkfreq))








