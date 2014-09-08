#!/usr/bin/env python
import python_compare

x= python_compare.main()
print "Multiple flip percentage=",x


if (x < 0.00001 and x > 0.01): #Too low or too high- we can stop the sims
	run_loop=0

else: #If in between, iterate over the simulations again
	run_loop=1



