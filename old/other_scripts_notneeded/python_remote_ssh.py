#!/usr/bin/env python

import os
import optparse

"""import paramiko

from ssh import SSHClient

host="10.107.105.201"
user="user1"
client = SSHClient()
client.load_system_host_keys()
client.connect(host, username=user)
stdin, stdout, stderr = client.exec_command('(cd /home/user1/simulations/decoder_optimised/decoder_node_1; python python_GNUparallel_ngspice.py --num=10 --ssh=/home/user1/simulations/decoder_optimised/decoder_node_1/sshmachines.txt --dir=/home/user1/simulations/decoder_optimised/decoder_node_1/decoder_node_1_line1 --spc=decoder_node_1_line1_sim)')
print "stderr: ", stderr.readlines()
print "pwd: ", stdout.readlines()
"""


from optparse import OptionParser

parser = OptionParser('Run ngspice parallely on the multiple spice decks on the 48-core cluster machine, using an utility called GNU parallel')
parser.add_option("-n", "--num", type="int", dest="num_spice",help="Enter the number of spice decks to be simulated")
parser.add_option("-s", "--ssh", dest="ssh_txt",help="Enter the name of the text file which contains the IP addresses of the machines to which we can ssh to run ngspice using GNU Parallel. Eg is provided in sshmachines.txt. Place it in the current working directory")
parser.add_option("-d", "--dir", dest="directory",help="Enter the path where the spice decks are present on this machine and on those machines where you want to ssh. The path should be the same in all machines. So, pls mention for eg: ~/ for 'home' folder, instead of /home/user/ etc")
parser.add_option("-f", "--spc", dest="spice",help="Enter the spice file names at the above path. Exclude the '_1', '_2' etc")

(options, args) = parser.parse_args()

num_spice=options.num_spice
ssh_txt=options.ssh_txt
directory=options.directory
spice_name=options.spice



#--num=10 --ssh=/home/user1/simulations/decoder_optimised/decoder_node_1/sshmachines.txt --dir=/home/user1/simulations/decoder_optimised/decoder_node_1/decoder_node_1_line1 --spc=decoder_node_1_line1_sim


os.system('ssh user1@10.107.105.201 python /home/user1/simulations/decoder_optimised/decoder_node_1/python_GNUparallel_ngspice.py --num=%s --ssh=%s --dir=%s  --spc=%s' %(num_spice, ssh_txt, directory,spice_name) )


#os.system('python python1_read_RTL_syn_pnr.py -f %s -m %s -clk %s' %(rtl,module,clkfreq))





