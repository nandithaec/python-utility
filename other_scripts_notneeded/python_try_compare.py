#!/usr/bin/env python

#Compare results of spice and RTL

"""
import pandas as pd
df = pd.read_csv("./spice_sim/results/spice.csv", sep=",")
	
print "df \n",df
print "\noutput_dec_7_:\n",df["output_dec_7_"]
"""

import csv, re
f = open('./spice_sim/results/spice.csv', 'rb')
frtl = open('./decoder_behav_pnr_reference_out/RTL_chosen.csv', 'rb')
fout = open('./spice_sim/results/spice_try_out.csv', 'wb')

reader = csv.reader(f)
reader_rtl = csv.reader(frtl)
writer = csv.writer(fout)

headers = reader.next()
headers_rtl = reader_rtl.next()
print "\nSpice Headers:\n", headers
print "\nSpice Headers[0]:\n", headers[0]

print "\nRTL Headers:\n", headers_rtl
print "\nRTL Headers[0]:\n", headers_rtl[0]

column = {}
for h in headers:
   column[h] = []

print "\nColumn:\n", column
print "\nColumn 1:\n",column['output_dec_7_']

for row in reader:
  for h, v in zip(headers, row):
    column[h].append(v)

print "\nColumn output_dec_7_:\n", column[headers[1]]


####################################################################################

column_rtl = {}
for h2 in headers_rtl:
   column_rtl[h2] = []

print "\nColumn:\n", column_rtl
print "\nColumn 1:\n",column_rtl['output_dec_7_']

for row2 in reader_rtl:
  for h2, v2 in zip(headers_rtl, row2):
    column_rtl[h2].append(v2)

print "\nColumn :\n", column_rtl[headers_rtl[0]]

####################################################################################

#Match headers

if (re.match(headers[0], headers_rtl[0]) != None):
	print "Match"
	print "Match!! \nHeader: %s \nspice data: %s \nRTL data: %s:\n" %(headers[0],column[headers[0]],column_rtl[headers_rtl[0]])

i= column[headers[0]]
print "\ni is:\n",i[0]

j= column_rtl[headers_rtl[0]]
print "\nj is:\n",j[0]

##List in python
k= []
k.append(float(i[0])- float(j[0]))
print "k is", k[0]







