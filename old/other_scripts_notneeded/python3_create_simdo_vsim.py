#!/usr/bin/env python

#Read in the pnr netlist, testbench and the entity name for the testbench, simulate it to create a file with FF outputs

##Example usage: python python3_create_simdo_vsim.py -v decoder_behav_pnr_test.v -t test_decoder_pnr.vhd -b t_decoder_pnr -r 1us

##The pnr netlist is by default assumed to be in /pnr/op_data folder

import optparse
import re,os
import fileinput
import subprocess
from optparse import OptionParser

parser = OptionParser('Read in the pnr netlist, testbench and the entity name for the testbench, simulate it to create a file with FF outputs')

parser.add_option("-v","--rtl", help='Enter the post layout verilog netlist name along with its path that needs to be simulated',dest='rtl_pnr')
parser.add_option("-t","--test", help='Enter the path of the testbench (vhd/verilog) file for simulating the post layout RTL file, include the filename along with extension as part of this path',dest='test_path')
parser.add_option("-b","--tb_mod", help='Enter the test bench module name that needs to be simulated',dest='test_module')
parser.add_option("-r","--run", help='Enter the duration of the simulation run. e.g., 1us or 1 us',dest='runtime')

#Optional arguments - read in string
#parser.add_option('module_name', help='Enter the entity name(vhdl) or module name (verilog) to be synthesised')

#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

rtl_pnr=options.rtl_pnr
#rtl_module=options.rtl_module
test_path=options.test_path
test_module=options.test_module
runtime=options.runtime
#module=options.module_name


fw = open('simulate_vsim.do', 'w') ## This is the commands input file for modelsim

#Write the following commands to this file
fw.write('set VLIB /cad/digital/rtl2gds/rtl2gds_install/LIB/lib/tsmc018/lib/osu018_stdcells.v \n\n')
fw.write('set RTLLANG vhdl \nglobal toplevel \n')
fw.write('set TB %s \n' %test_path)
fw.write('set LANG vhdl \n')
fw.write('set TB_TOP %s \n' %test_module)
fw.write('\n\nvlib work \n')
fw.write('if { [string match "verilog" $LANG] == 1 } { \n')
fw.write('# TB and library inputs\n')
fw.write('vlog   $VLIB $TB\n')
fw.write('} else {\n')
##Assuming that the pnr rtl verilog netlist is by default in this path, since rtl2gds creates this file
##fw.write('vlog  $VLIB pnr/op_data/decoder_behav_pnr_final.v\n')
fw.write('vlog  $VLIB %s\n' %rtl_pnr)

fw.write('vcom $TB\n')
fw.write('}\n\n')

fw.write('# TB module name and THE simulate command\n')
fw.write('vsim $TB_TOP -t 100ps \n\n')
fw.write('add wave * \n #Uncomment out the next line if required \n #add list * \n')
fw.write('run %s \n' %runtime)
fw.write('#If the add list above was uncommented, then uncomment the following line as well, to store the list file \n')
fw.write('#write list -window .main_pane.mdi.interior.cs.vm.paneset.cli_1.wf.clip.cs list_script.lst \n')
fw.write('\n\nquit -f \n ')


#Create the bash script to run modelsim with the above simulate_vsim.do file as the input
fw1 = open('run_sim.bash', 'w') ## This is the commands input file for modelsim
fw1.write('#!/bin/bash\n\n')
#Remove work directory if it exists
fw1.write('\\rm -rf ./work\n')
#Run simulation, invoke modelsim
fw1.write('vsim -do simulate_vsim.do\n')

fw.close()
fw1.close()
print "\n********************INVOKING MODELSIM********************\n"

#Run the bash script
os.system('bash run_sim.bash')	
print "\n****Completed simulating the post layout verilog netlist.\n Reference FF outputs written****"




