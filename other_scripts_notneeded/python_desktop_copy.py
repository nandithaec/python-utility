#!/usr/bin/env python

#IMPORTANT: It is assumed that we are running parallel ngspice simulations on a remote 48-core cluster at 10.107.105.201. If this is not the case, you will need to modify this script to run it on this machine, by commenting out the scp and ssh commands.

#Example usage: Without seed: python python_desktop_copy.py -p ~/simulations/decoder -d decoder -l 1


import optparse
import re,os
import csv, re
import random,shutil,time

#import python_compare_remote

from optparse import OptionParser


#def main(): #Defining a main function
parser = OptionParser('Compare RTL and spice files')
parser.add_option("-d", "--design", dest="design_folder",help="Enter the name of your design folder")
parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-l", "--outloop",dest='outloop', help='This is the number of times this script is executed in a loop- It is NOT a user input, but is taken from a script which is running this script in a loop')

(options, args) = parser.parse_args()


design_folder=options.design_folder
path=options.path
outloop= (options.outloop)

print "\n****deleting existing design folder on desktop****\n"
os.system('rm -rf /home/nanditha/simulations/%s/spice_decks_*' %design_folder)
#time.sleep(2)

#if not os.path.exists(backup_dir):
#	os.mkdir('/home/nanditha/simulations/decoder/spice_decks_%d' %outloop)	

print "\n****Copying design folder to desktop****\n"
os.system('scp -r user1@10.107.105.201:%s/spice_decks_%s nanditha@10.107.90.52:/home/nanditha/simulations/%s/spice_decks_%s' %(path,outloop,design_folder,outloop))

print "\n****Done Copying design folder to desktop****\n"
#time.sleep(2)








