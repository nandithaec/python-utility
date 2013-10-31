#!/usr/bin/env python
import optparse,os,random

from optparse import OptionParser

parser = OptionParser('Try random num gen')
parser.add_option("-s", "--seed",dest='seed', help='Enter the random seed')

(options, args) = parser.parse_args()

seed=int(options.seed)


random.seed(seed)

for loop in range(1,2): 

	seed_new= int(random.randrange(100000)*random.random())
	print "Inside loop2, random number is ", seed_new

