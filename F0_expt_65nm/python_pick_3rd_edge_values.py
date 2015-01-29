#!/usr/bin/env python

#Pick the relevant row (using the clk cycle) from F0_tool_reference_out.txt and write it into F0_obtained.csv in csv format
#Example usage: python python_pick_3rd_edge_values.py -m c432_clk_ipFF -f //home/users/nanditha/Documents/utility/65nm/c432 -c 1443

import optparse
import re,os
import csv, re,time
import random,shutil

#import python_compare_remote

from optparse import OptionParser


parser = OptionParser("This is run after every simulation is complete,Picks the relevant row (using the clk cycle) from F0_tool_reference_out.txt and writes it into F0_obtained.csv in csv format\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n")

parser.add_option("-m", "--mod",dest='module', help='Enter the entity name(vhdl) or module name (verilog)')
parser.add_option("-f", "--folder", dest="path",help="Enter the ENTIRE path to your design folder(your working dir)- either on this machine or remote machine ")
parser.add_option("-c", "--clkcycle",dest='clkcycle', help='This is the clk cycle that was simulated in this cycle.')


(options, args) = parser.parse_args()


module=options.module
path=options.path

clkcycle= int(options.clkcycle)


#Pick the relevant row (using the clk cycle) from F0_tool_reference_out.txt and write it into F0_obtained.csv in csv format
f = open('%s/%s_reference_out/F0_tool_reference_out.txt' %(path,module), 'rb')
fwr = open('%s/%s_reference_out/F0_obtained.csv' %(path,module), 'a')

F0_data=f.readlines()
print "F0 clk cycle from file:%d" %clkcycle
row_to_pick=clkcycle+3 #2 cycles as per simulation + 1 accounting the header
#since index starts fom 0: Subtract 1
row_to_pick=row_to_pick-1
print "F0 row index to pick:%d" %row_to_pick
data=F0_data[row_to_pick]
print "Row data:\n",data
#print "Row data 1445:\n",F0_data[1445]

print "Data obtained - 3rd rising edge from this clk cycle:",data

words=data.split()
print "Words",words
data=",".join(words)
print "Data csv",data #Making it csv

fwr.writelines(data)
fwr.writelines("\n")

f.close()
fwr.close()

##########################################################################################
#Pick the relevant row (using the clk cycle) from tool_reference_out.txt and write it into RTL_obtained.csv in csv format
f = open('%s/%s_reference_out/tool_reference_out.txt' %(path,module), 'rb')
fwr = open('%s/%s_reference_out/RTL_expected.csv' %(path,module), 'a')

RTL_data=f.readlines()
print "RTL clk cycle from file:%d" %clkcycle
row_to_pick=clkcycle+3 #2 cycles as per simulation + 1 accounting the header
#since index starts fom 0: Subtract 1
row_to_pick=row_to_pick-1
print "RTL row index to pick:%d" %row_to_pick
data=RTL_data[row_to_pick]

print "RTL expected- 3rd rising edge from this clk cycle:",data

words=data.split()
print "Words",words
data=",".join(words)
print "RTL csv",data #Making it csv

fwr.writelines(data)
fwr.writelines("\n")

f.close()
fwr.close()

