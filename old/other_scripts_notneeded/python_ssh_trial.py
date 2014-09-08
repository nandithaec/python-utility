#!/usr/bin/env python

import os, optparse


from optparse import OptionParser

parser = OptionParser('Copy design folder to remote cluster, generate multiple decks and simulate. Obtain results and concatenate them')
parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path of the design folder which will be copied to the 48-core cluster")

(options, args) = parser.parse_args()

path=options.path

#Copy the entire Current directory to the machine where the simulations will be run in parallel. Currently we are running it on the 48-core cluster under the username: user1, password: user123 and copying to the folder /home/user1/simulations
print "\nTo copy current working directory to remote cluster to run simulations parallely\n"
os.system('scp -r %s user1@10.107.105.201:/home/user1/simulations' %path)
print "Done copying files\n"
print "Now doing ssh to remote machine..\n"
os.system('ssh -XY user1@10.107.105.201')
print "All scripts also copied to remote machine.. Now execute the scripts there to generate multiple decks, running ngspice parallely etc\n"

