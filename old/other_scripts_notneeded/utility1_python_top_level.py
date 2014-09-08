#!/usr/bin/env python

#Example usage: python utility1_python_top_level.py -v /home/users/nanditha/Documents/utility/decoder/decoder.vhd -m decoder_behav_pnr -t /home/users/nanditha/Documents/utility/decoder/test_decoder_pnr.vhd -b t_decoder_pnr -c 900 -r 1us

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


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

rtl=options.rtl
module=options.module
clkfreq=options.clkfreq

test_path=options.test_path
test_module=options.test_module
runtime=options.runtime


#Example usage: python python1_read_RTL_syn_pnr.py -f decoder.vhd -m decoder_behav_pnr -clk 900
os.system('python python1_read_RTL_syn_pnr.py -f %s -m %s -c %s' %(rtl,module,clkfreq))

#Example usage: perl perl2_outwrtr.pl -v pnr/op_data/decoder_behav_pnr_final.v -m decoder_behav_pnr
os.system('perl modperl2_outwrtr.pl -v pnr/op_data/%s_final.v -m %s' %(module,module))

##Example usage: python python3_create_simdo_vsim.py -rtl decoder_behav_pnr_modelsim.v -tb test_decoder_pnr.vhd -tb_mod t_decoder_pnr -time 1us
os.system('python python3_create_simdo_vsim.py -v %s_modelsim.v -t %s -b %s -r %s' %(module,test_path,test_module,runtime))





