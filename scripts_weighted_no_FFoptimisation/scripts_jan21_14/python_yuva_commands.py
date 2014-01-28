#!/usr/bin/env python

import os
import time
##Example usage:  python /home/external/iitb/nanditha/simulations/c2670_alu/python_yuva_commands.py


os.system('cat $PBS_NODEFILE > /home/external/iitb/nanditha/simulations/c2670_alu/nodes.txt')
print "PBS NODEFILE contents....written to nodes.txt\n"
time.sleep(3)

os.system('python /home/external/iitb/nanditha/simulations/c2670_alu/python_ssh_addr_yuva.py -p /home/external/iitb/nanditha/simulations/c2670_alu')
os.system('cat /home/external/iitb/nanditha/simulations/c2670_alu/sshmachines.txt')
print "Check contents of sshmachines.txt file....\n"
time.sleep(3)


os.system("seq 1 10| /opt/parallel-20130422/bin/parallel --progress -j +0 --sshloginfile /home/external/iitb/nanditha/simulations/c2670_alu/sshmachines.txt 'cd /home/external/iitb/nanditha/simulations/c2670_alu/spice_decks_1; pwd; /home/external/iitb/nanditha/ngspice-25/bin/ngspice /home/external/iitb/nanditha/simulations/c2670_alu/spice_decks_1/deck_{}.sp;pwd;'")
