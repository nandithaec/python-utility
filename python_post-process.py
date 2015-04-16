#!/usr/bin/env python

#Feb 9 2015

#Example usage: python python_post-process.py  -t /home/users/nanditha/sentaurus/65nm_mos/final/Monte_carlo -f nmos2_ser_layout -n 320

import optparse
import re,os
import csv, re
import random,shutil
import fileinput,sys


from optparse import OptionParser



parser = OptionParser('This script does post processing on the plot files obtained from sdevice simulation, to extract current pulse magnitude, rise and fall times, charge collected\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-t", "--tem",dest='temp_path', help='Enter the path of the results files')
parser.add_option("-f", "--fil",dest='result', help='Enter the name of the results files')
parser.add_option("-n", "--num",dest='num', help='Enter the total number of results files ')


(options, args) = parser.parse_args()


path=options.temp_path
number=int(options.num)
result_file=options.result

fres = open('%s/result_combined.csv' %(path), 'wb')
writer = csv.writer(fres)

#plot_number=106
file_csv=[]

for plot_number in range(1,number+1):
	print "\n\n##########Processing %s_%d.plt######\n\n" %(result_file,plot_number)
	f = open('%s/%s_%d.plt' %(path,result_file,plot_number), 'r')
	fwr = open('%s/plot_data.csv' %path, 'wb')

	copy = False
	fwr.write("Time,Drain1,Drain2,Source1,Source2\n")

	for line in f:
		if line.strip() == "Data {":
			copy = True
		elif line.strip() == "}":
			copy = False
		elif copy:
			fwr.write(line)
	
	fwr.close()
	f.close()

	for line in fileinput.input('%s/plot_data.csv' %(path), inplace=1):
		if ("      ") in line:
			line = line.replace("      ","")
			sys.stdout.write(line)
	
		else:
			sys.stdout.write(line)  #Write line in file as it is


	for line in fileinput.input('%s/plot_data.csv' %(path), inplace=1):
		if ("   ") in line:
			line = line.replace("   ",",")
		
		if ("  ") in line:
			line = line.replace("  ",",")
			sys.stdout.write(line)
		else:
			sys.stdout.write(line)  #Write line in file as it is


	fileinput.close()


	###########################################################################################

	fpar = open('%s/plot_data.csv' %(path), 'rb')
	plot_data_lines=fpar.readlines()
	print "len(plot_data_lines) is", len(plot_data_lines)
	print "Last line, time instant is", plot_data_lines[len(plot_data_lines)-1]
	fpar.close()
	row_csv=[]
	cur_index=[]
	peak_cur_value=[]

	if (len(plot_data_lines) > 90): #If the simulation converged, the number of data lines (in plot) will be more
	
		fpar = open('%s/plot_data.csv' %(path), 'rb')
		reader= csv.reader(fpar)
		#print "\nfile", reader
		headers = reader.next() #parameter headers

		print "\nHeaders", headers


		column = {}
		for h in headers:
			column[h] = []

		#print "\nColumn inside for:\n", column

		for row in reader:
			for h, v in zip(headers, row):
				column[h].append(v)

		#print "\n column[headers[0]]:\n", column[headers[0]]  #This means, column[time], where time is the headers[0]
		#print "\nColumn:\n", column


		time_column= column[headers[0]] 

		#################Finding Peak of the current pulse###################

		
		#There are 4 probe points- Drain1,Drain2,Source1,Source2
		#Peak current
		for c in range(1,5): 
			current_list=[]
			current_column=column[headers[c]]
			for cd in range(0,len(current_column)):
				current_list.append(float(current_column[cd]))

			neg_value=min(current_list)

			if neg_value<0: 
				peak_cur_value.append(min(current_list))
				row_csv.append(min(current_list)) #probing negative current
				cur_index.append(current_list.index(min(current_list)))
			else:
				peak_cur_value.append(max(current_list))
				row_csv.append(max(current_list)) #probing positive current
				cur_index.append(current_list.index(max(current_list)))

		print "Peak current",peak_cur_value
		print "Peak current index ",cur_index


		collect_tau1=[]
		collect_tau2=[]
		Qcoll_list=[]

		#################Finding tau1,tau2 and Qcoll of the current pulse###################

		#tau1 - rise time- (time to reach max current)	
		for c in range(1,5): #Index 0 = time. So, start from index 1 - which have currents
			print "******************************************\n"
			print "Processing column %d" %(c)
			current_column=column[headers[c]]
			current_time0=float(current_column[0])
			print "Current at time 0 is",current_time0

			list_val=[]
			for cd in range(0,len(current_column)):
				list_val.append(float(current_column[cd])) #Convert strings into floats

			#print "list is ", list_val
	
			neg_value=min(list_val)

			tau2_list=[]
			########################################################################################################################
			if neg_value<0: #Negative going pulse

				spike_value=max(list_val) #See if there are any positive spikes
				#print "Spike value is %f, time0 current is %f" %(spike_value,current_time0)


				index=list_val.index(min(list_val)) #Find the negative most current value and its index
				peak_time=time_column[index] #Negative peak time
				peak_index=index

				if ((abs(spike_value-current_time0))>1e-6): #Substantial positive spike before the negative pulse detected
		
					pos_index=list_val.index(spike_value)
					min_time_index=pos_index
					#print "positive spike, min time index is ", min_time_index 
					#print "Pos value is", spike_value

				else:

					for d in range(0,len(list_val)-1):
						diff=abs((list_val[d+1])-(list_val[d]))
						if(diff>1e-7): #Current just begins to rise
							min_time_index=d+1
							print "Negative pulse, min time index is ", min_time_index
							#print "The 2 numbers are %s, %s" %(list_val[d+1],list_val[d])
							break;
				min_time=time_column[min_time_index]
				print "min time instant is", (min_time)
				print "peak time instant is",(peak_time)
				tau1=abs(float(peak_time)-float(min_time))
				print "**Neg pulse, Tau1 (rise) time is**",tau1
				collect_tau1.append(tau1) #Append the rise time (tau1) each time in the loop

				########Tau2########
				for n in range(peak_index,len(list_val)):
					tau2_list.append(list_val[n])

				#print "Tau2 list",tau2_list

				#for dt in range(0,len(tau2_list)-1):
					#diff_tau2=abs((tau2_list[dt+1])-(tau2_list[dt]))
		
				max_value_tau2_list=max(tau2_list)
				tau2_time_index=(tau2_list.index(max_value_tau2_list))+peak_index
				print "Neg pulse, Max value in tau2 is %f, index is %d" %(max_value_tau2_list,tau2_time_index)
		
				"""
				if(diff_tau2 < 10.00e-08): #Current just begins to plateau
					tau2_time_index=dt+1+(peak_index) #To find the actual index of the final list list_val
					print "tau2 < 10e-8 found and index is %d, final index %d" %(dt,tau2_time_index)
					break;
				else:
					tau2_time_index=len(list_val)-1 #The last value
					#print "tau2 < 10e-8 NOT found"
					"""
				tau2_time=time_column[tau2_time_index]
				print "tau2 plateau time instant is",(tau2_time)
				tau2=abs(float(peak_time)-float(tau2_time))
				print "**tau2(fall) time is**",tau2
				collect_tau2.append(tau2)


				###########Collected charge- Qcoll########
				base=float(tau2_time)-float(min_time) #base of the triangle
				height=peak_cur_value[c-1] #Since c is starting to loop from 1.
				area=abs(0.5*base*height)
				Qcoll_list.append(area)
				print "**Qcoll is**",area
			##################################################################################################################################################

			else:

			 #Positive going pulse

				spike_value=min(list_val) #See if there are any negative spikes
				#print "Spike value is " ,spike_value
				#print "Current at time 0 is",current_time0

				index=list_val.index(max(list_val)) #Find the positive most current value and its index
				peak_time=time_column[index] #Positive peak time
				#print "Difference between spike and time0 value",(abs(spike_value-current_time0))
				if ((abs(spike_value-current_time0))>1e-6): #negative spike before the positive pulse detected
		
					pos_index=list_val.index(spike_value)
					min_time_index=pos_index
					#print "spike value",spike_value
					#print "negative spike, min time index is ", min_time_index 
					#print "Pos value is", spike_value

				else:
					#find rise time
					for d in range(0,len(list_val)-1):
						diff=abs((list_val[d+1])-(list_val[d]))
						if(diff>1e-7): #Current just begins to rise
							min_time_index=d+1
							print "Positive pulse, min time index is ", min_time_index
							#print "The 2 numbers are %s, %s" %(list_val[d+1],list_val[d])
							break;
				min_time=time_column[min_time_index]
				print "min time instant is", (min_time)
				print "peak time instant is",(peak_time)
				tau1=abs(float(peak_time)-float(min_time))

				collect_tau1.append(tau1) #Append the rise time (tau1) each time in the loop
				print "**Pos pulse, tau1 (rise) time is**",tau1
			
				########Tau2########
				for n in range(peak_index,len(list_val)):
					tau2_list.append(list_val[n])

				#print "Tau2 list",tau2_list

				#for dt in range(0,len(tau2_list)-1):
				#	diff_tau2=abs((tau2_list[dt+1])-(tau2_list[dt]))
					#print "Difference in tau2 is", diff_tau2
					"""		
					if(diff_tau2 < 1.00e-09): #Current just begins to plateau
						tau2_time_index=dt+1+(peak_index) #To find the actual index of the final list list_val
						print "tau2 < 1e-9 found and index is %d, final index %d" %(dt,tau2_time_index)
						break;
					else:
						tau2_time_index=len(list_val)-1 #The last value
						#print "tau2 < 10e-8 NOT found"
					"""
				min_value_tau2_list=min(tau2_list)
				tau2_time_index=(tau2_list.index(min_value_tau2_list))+peak_index
				print "Pos pulse, Max value in tau2 is %f, index is %d" %(min_value_tau2_list,tau2_time_index)
				tau2_time=time_column[tau2_time_index]
				print "tau2 plateau time instant is",(tau2_time)
				tau2=abs(float(peak_time)-float(tau2_time))
				print "**tau2(Fall) time is**",tau2

				collect_tau2.append(tau2)

				###########Collected charge- Qcoll########
				base=float(tau2_time)-float(min_time) #base of the triangle
				height=peak_cur_value[c-1] #Since c is starting to loop from 1.
				area=abs(0.5*base*height)
				Qcoll_list.append(area)
				print "**Qcoll is**",area
				print "******************************************\n"
		for kk in range(0,len(collect_tau1)):
			row_csv.append(collect_tau1[kk])
		for kk in range(0,len(collect_tau2)):
			row_csv.append(collect_tau2[kk])
		for kk in range(0,len(Qcoll_list)):
			row_csv.append(Qcoll_list[kk])

		##################################################################
		print "All extracted results",row_csv

		file_csv.append(row_csv)
		fpar.close()
	else:
		append_zero=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		for m in range(0,16):
			row_csv.append(append_zero[m])
		file_csv.append(row_csv)
		fpar.close()

#Write header for the result combined file
fres.writelines("Idrain1,Idrain2,Isource1,Isource2,Tau1-drain1,Tau1-drain2,Tau1-source1,Tau1-Source2,Tau2-drain1,Tau2-drain2,Tau2-source1,Tau2-Source2,Qcoll-drain1,Qcoll-drain2,Qcoll-Source1,Qcoll-Source2\n")
writer.writerows(file_csv)
	


fres.close()



