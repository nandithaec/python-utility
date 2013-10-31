#!/usr/bin/env python
import optparse,os,random

from optparse import OptionParser

parser = OptionParser('Try random num gen')
parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()

seed=int(options.seed)

os.system('perl perl_random_seed.pl -s %s' %seed)  #Call srand only once

for loop_var in range(1,11): 
	#seed_loop=seed+loop_var
	#os.system('perl perl_random.pl -s %s' %seed_loop)
	os.system('perl perl_random.pl')


