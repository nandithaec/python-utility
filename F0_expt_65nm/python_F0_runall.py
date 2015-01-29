
#!/usr/bin/env python
#Run all cases sequentially automatically! - Nov 30 2014

import os

"""
os.system('python python_F0_expt.py -m c880_clk_ipFF -f /home/users/nanditha/Documents/utility/65nm/c880/spice_results/c880_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/c880/spice_results/c880_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/c880 -b u1 --test_path /home/users/nanditha/Documents/utility/65nm/c880/test_c880.v --tb_mod test_c880 --period 20000')

os.system('python python_F0_expt.py -m c1355_clk_ipFF -f /home/users/nanditha/Documents/utility/65nm/c1355/spice_results/c1355_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/c1355/spice_results/c1355_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/c1355 -b u1 --test_path /home/users/nanditha/Documents/utility/65nm/c1355/test_c1355.v --tb_mod test_c1355 --period 20000')

os.system('python python_F0_expt.py -m c1908_clk_ipFF -f /home/users/nanditha/Documents/utility/65nm/c1908/spice_results/c1908_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/c1908/spice_results/c1908_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/c1908 -b u1 --test_path /home/users/nanditha/Documents/utility/65nm/c1908/test_c1908.v --tb_mod test_c1908 --period 20000')

os.system('python python_F0_expt.py -m decoder_op_ip -f /home/users/nanditha/Documents/utility/65nm/decoder/spice_results/decoder_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/decoder/spice_results/decoder_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/decoder -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/decoder/test_decoder_opFF.vhd --tb_mod test_decoder_op_ip --period 4000')

#LFSR commented out.. to be run later
os.system('python python_F0_expt.py -m b01 -f /home/users/nanditha/Documents/utility/65nm/b01/spice_results/b01_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b01/spice_results/b01_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b01 -b des_b01 --test_path /home/users/nanditha/Documents/utility/65nm/b01/test_b01.vhd --tb_mod test_b01 --period 4000')

os.system('python python_F0_expt.py -m b03 -f /home/users/nanditha/Documents/utility/65nm/b03/spice_results/b03_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b03/spice_results/b03_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b03 -b des_b03 --test_path /home/users/nanditha/Documents/utility/65nm/b03/test_b03.vhd --tb_mod test_b03 --period 4000')


os.system('python python_F0_expt.py -m b04 -f /home/users/nanditha/Documents/utility/65nm/b04/spice_results/b04_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b04/spice_results/b04_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b04 -b des_b04 --test_path /home/users/nanditha/Documents/utility/65nm/b04/test_b04.vhd --tb_mod test_b04 --period 4000')

os.system('python python_F0_expt.py -m b06 -f /home/users/nanditha/Documents/utility/65nm/b06/spice_results/b06_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b06/spice_results/b06_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b06 -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/b06/test_b06.vhd --tb_mod test_b06 --period 4000')

"""

os.system('python python_F0_expt.py -m b09 -f /home/users/nanditha/Documents/utility/65nm/b09/spice_results/b09_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b09/spice_results/b09_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b09 -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/b09/test_b09.vhd --tb_mod test_b09 --period 4000')

os.system('python python_F0_expt.py -m b10 -f /home/users/nanditha/Documents/utility/65nm/b10/spice_results/b10_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b10/spice_results/b10_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b10 -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/b10/test_b10.vhd --tb_mod test_b10 --period 4000')

os.system('python python_F0_expt.py -m b11 -f /home/users/nanditha/Documents/utility/65nm/b11/spice_results/b11_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b11/spice_results/b11_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b11 -b dec_0 --test_path /home/users/nanditha/Documents/utility/65nm/b11/test_b11.vhd --tb_mod test_b11 --period 4000')

os.system('python python_F0_expt.py -m b13 -f /home/users/nanditha/Documents/utility/65nm/b13/spice_results/b13_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/b13/spice_results/b13_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/b13 -b des_b13 --test_path /home/users/nanditha/Documents/utility/65nm/b13/test_b13.vhd --tb_mod test_b13 --period 4000')

os.system('python python_F0_expt.py -m lfsr -f /home/users/nanditha/Documents/utility/65nm/LFSR/spice_results/LFSR_F0_2nd_edge.csv -g /home/users/nanditha/Documents/utility/65nm/LFSR/spice_results/LFSR_F0_3rd_edge.csv   -p /home/users/nanditha/Documents/utility/65nm/LFSR -b uut --test_path /home/users/nanditha/Documents/utility/65nm/LFSR/test_lfsr.vhd --tb_mod lfsr_tb --period 1000')


