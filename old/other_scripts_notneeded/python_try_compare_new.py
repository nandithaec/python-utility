#!/usr/bin/env python

#Compare results of spice and RTL

"""
import pandas as pd
df = pd.read_csv("./spice_sim/results/spice.csv", sep=",")
	
print "df \n",df
print "\noutput_dec_7_:\n",df["output_dec_7_"]
"""

import csv, re
f = open('./test_compare/spice.csv', 'rb')
frtl = open('./decoder_behav_pnr_reference_out/RTL.csv', 'rb')
fout = open('./test_compare/spice_try_out.csv', 'wb')

reader = csv.reader(f)
reader_rtl = csv.reader(frtl)
writer = csv.writer(fout)

headers = reader.next()
headers_rtl = reader_rtl.next()
print "\nSpice Headers:%s", headers
print "\nHeader len:\n", range(len(headers))
print "\nHeader len:\n", (len(headers))

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
#k= range(2000) ##List in python

km=[]
#Match headers
for s in range(len(headers)):
	for r in range(len(headers_rtl)):
		if (re.match(headers[s], headers_rtl[r]) != None): ##That is, if the headings match
			k= [] ##Empty the temporary List before starting to append a new column
			print "\n\nMatch!! \nHeader: %s \nspice column: %s \nRTL column: %s:\n" %(headers[s],column[headers[s]],column_rtl[headers_rtl[r]])
			k.append(headers[s]) #Append header
			i= column[headers[s]] #Get the entire column in the spice file
			#Each item in the column is referenced as j[0], j[1] etc
			#print "\ni is:\n",i[0]

			j= column_rtl[headers_rtl[r]] #Get the entire column in the RTL file
			#Each item in the column is referenced as j[0], j[1] etc as many are the number of rows
			#print "\nj is:\n",j[0]
			
			for num_rows in range(0,9): # 10 rows
				#k[s]= abs((float(i[num_rows])- float(j[num_rows])))
				#print "Difference k[%d] is %s" %(s,k[s])
				ab=abs((float(i[num_rows])- float(j[num_rows])))
				if ab < 0.5:
					k.append('0')
				else:
					if ab > 1.5: 
						k.append('1')
				#k.append(abs((float(i[num_rows])- float(j[num_rows]))))

			print "\nk is\n", k  #All the data in the column is collected in k
			km.append(k) #And appended to an empty list
			print "km is\n",km

print "transpose:\n",zip(*km)
writer.writerows(zip(*km))





