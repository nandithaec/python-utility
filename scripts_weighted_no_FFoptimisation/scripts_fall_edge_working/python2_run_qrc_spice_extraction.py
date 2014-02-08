#!/usr/bin/env python

#Read in the def file and extract the pnr spice netlist in dspf format, along with the vdd, gnd etc.,using Cadence QRC, instead of using the SoC Encounter generated dspf file (using rcOut)

##Example usage: python python2_run_qrc_spice_extraction.py -m c499_clk_opFF

##The pnr def.gz file is by default assumed to be in /pnr/op_data folder

import optparse
import re,os
import fileinput
import subprocess
from optparse import OptionParser

parser = OptionParser('The inputs to the script are listed as arguments below, which are all necessary arguments.\nThis scripts reads in the modified pnr verilog netlist which was the output of a previous script, reads in the original testbench(vhdl/verilog) and the entity name for the testbench. It outputs 2 files:\n1. simulate_vsim.do and\n2. run_sim.bash.\nThe bash script will invoke the do file to invoke Modelsim and simulate the pnr verilog netlist to create two files (outputs):\n1. $pnr_module_reference_out/our_reference_out.txt and\n2. $pnr_module_reference_out/tool_reference_out.txt.\nThe first one is more detailed, where as the 2nd file is used for further processing. These files contain reference input and output values at each clock cycle of the verilog simulation.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')


parser.add_option("-m", "--mod",dest='module', help='Enter the top level entity name(vhdl) or module name (verilog) to be simulated. (Not the top level test bench module name)')


#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

module=options.module


fw = open('qrc_dspf.cmd', 'w') ## This is the commands input file for Cadence QRC- RC extraction

#Write the following commands to this file
fw.write('#OPTION COMMAND FILE created for Cadence Extraction QRC Version 8.1.5-p014\n#\n\n')
fw.write('extraction_setup\\\n\t-promote_pin_pad "LOGICAL"\n')
fw.write('filter_coupling_cap \\\n\t -coupling_cap_threshold_absolute 0.1\n')
fw.write('global_nets \\\n\t  -nets \\\n\t\t "VDD" \\\n\t\t "GND" \\\n\t\t "vdd" \\\n\t\t "gnd" \n')

fw.write('input_db -type def \\\n')
fw.write('\t -design_file "./pnr/op_data/%s_final.def.gz" \\\n' %module)
fw.write('\t -libgen_library_name "/cad/digital/rtl2gds/rtl2gds_install/LIB/lib/tsmc018/fireIce/libgen_lef.cl"\n\n')

fw.write('output_db -type dspf \\\n\t -output_incomplete_nets false \\\n \t -output_unrouted_nets true \\\n')
fw.write('\t-spice_compatible_mode true \\\n\t -disable_instances false \\\n\t -subtype "STANDARD" \\\n\t')
fw.write('-include_parasitic_res_model  comment \\\n\t -compressed false\n')

fw.write('output_setup \\\n\t -compressed false \\\n\t -file_name "%s"\n' %module)

fw.write('parasitic_reduction \\\n\t -enable_reduction true\n')
fw.write('process_technology \\\n\t  -technology_library_file "/home/users/nanditha/tmp/_auto_qrc_techlib.defs" \\\n\t')

fw.write('-technology_name "_auto_tech_"\n\n')
fw.write('extract \\\n\t  -selection "all" \\\n\t -type "rc_coupled"\n \t#Uncomment if reqd\n\t#-type "c_only_coupled"\n')
fw.write('\n#Uncomment out the next line if required \n#extract \\\n\t# -selection "net VDD" \\\n\t# -type "none"\n')
fw.write('#extract \\\n\t# -selection "net vdd" \\\n\t# -type "none"\n')
fw.write('#extract \\\n\t# -selection "net GND" \\\n\t# -type "none"\n')
fw.write('#extract \\\n\t# -selection "net gnd" \\\n\t# -type "none"\n')
print "\n***********Generated the QRC command file qrc_dspf.ccl in the current working directory***********\n"
fw.close()


#Run the qrc-dspf.ccl script through the Cadence qrc
print "\n********************INVOKING CADENCE QRC********************\n"

#Run the ccl script
os.system('qrc -cmd qrc_dspf.cmd')	
print "\n****Completed generating the spice (dspf) netlist in the current working directory.****\n"
print "Spice file name: %s.dspf" %module




