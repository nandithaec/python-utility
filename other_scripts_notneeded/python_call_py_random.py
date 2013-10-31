#!/usr/bin/env python
import optparse,os,random

from optparse import OptionParser

parser = OptionParser('Try random num gen')
parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()

seed=int(options.seed)


random.seed(seed)


#os.system('perl perl_random_seed.pl -s %s' %seed)  #Call srand only once

#for loop_var in range(1,11): 
#	os.system('perl perl_random.pl')

for loop in range(1,5): 

	seed_new= int(random.randrange(100000)*random.random())
	print "random number in loop1 is ", seed_new
	os.system('python python_random_loop2.py -s %s' %seed_new)  #Call srand only once

