#!/usr/bin/env python

import os
import ssh



from ssh import SSHClient

host="10.107.105.201"
user="user1"
client = SSHClient()
client.load_system_host_keys()
client.connect(host, username=user)
stdin, stdout, stderr = client.exec_command('(cd /home/user1/simulations/decoder_optimised/decoder_node_1; python python_GNUparallel_ngspice.py --num=10 --ssh=/home/user1/simulations/decoder_optimised/decoder_node_1/sshmachines.txt --dir=/home/user1/simulations/decoder_optimised/decoder_node_1/decoder_node_1_line1 --spc=decoder_node_1_line1_sim)')
print "stderr: ", stderr.readlines()
print "pwd: ", stdout.readlines()


