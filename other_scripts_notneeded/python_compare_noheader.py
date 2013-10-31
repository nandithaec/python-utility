#!/usr/bin/env python

#Compare results of spice and RTL
import csv 


f= open('./test_compare/spice.csv','r')
f2= open('./decoder_behav_pnr_reference_out/RTL.csv','r')
deck_clk= open('./test_compare/deck_clk_glitch.csv','r')
fo= open('./test_compare/spice_RTL_combined.csv','w')
fout= open('./test_compare/spice_RTL_diff_noheadermethod.csv','w')

spice_file = csv.reader(f)
rtl_file = csv.reader(f2)
writer = csv.writer(fo)
diffwriter = csv.writer(fout)
dcg_file= csv.reader(deck_clk)

all = []  #Empty array into which we will write out the data
spice_row = spice_file.next() #Goes to next line.. starts off with first

diff1 = []
dcg_row = dcg_file.next() #Goes to next line.. starts off with first

#diff1_row = spice_row
rtl_row = rtl_file.next()
print "\nRTL first row is ", rtl_row
print "\nSpice first row is ", spice_row  


for i in range(len(rtl_row)):
	spice_row.append('RTL_'+ rtl_row[i])  #Append to the combined file, modify the header while writing
	dcg_row.append('diff_'+ rtl_row[i])  #Append to the diff file

#for i in range(len(rtl_row)):
#	spice_row.append('diff_'+ rtl_row[i])  #Append to the combined file again, since we will also write out the diff results


all.append(spice_row) #write out the combined header first
diff1.append(dcg_row)  #Write header from dcg file

print "\nDiff is:", diff1
#diffwriter.writerows(diff1) #Write header

print "\n"
print "\nAll is:", all

##Now repeat this over all the other rows

for spice_row in spice_file: ##This will omit the header. I guess- Similar to #	spice_row = spice_file.next()

	rtl_row = rtl_file.next() #Read the next row from the RTL file 
	for i in range(len(rtl_row)):
	##Append each item in the rtl_row array one by one- else it will print in the form of an array with [" " ] etc 
	##Alternate: spice_row.append(rtl_row) will print as array [ " " ]
		spice_row.append(rtl_row[i]) #Combine the RTL line into spice file
		#spice_row.append(float(spice_row[i])- float(rtl_row[i]))
		

	all.append(spice_row)
	

writer.writerows(all)


f2.close()

f2= open('./decoder_behav_pnr_reference_out/RTL.csv','r')
rtl_file = csv.reader(f2)
rtl_row = rtl_file.next()

print "\n rtl_row is",rtl_row

for dcg_row in dcg_file: ##This will omit the header. I guess- Similar to #	spice_row = spice_file.next()
	rtl_row = rtl_file.next() #Read the next row from the RTL file 
	for i in range(len(rtl_row)):
		ab = abs((float(spice_row[i])- float(rtl_row[i])))
		if ab < 0.5:
			dcg_row.append('0')
		else:
			if ab > 1.5: 
				dcg_row.append('1')

	diff1.append(dcg_row)

print "diff1 list is\n",diff1

diffwriter.writerows(diff1)

	
f.close()
f2.close()
fo.close()
fout.close()
deck_clk.close()







