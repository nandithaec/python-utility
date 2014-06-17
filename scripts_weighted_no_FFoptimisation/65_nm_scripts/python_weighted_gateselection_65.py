
#!/usr/bin/env python

#Example usage: python python_weighted_gateselection.py 

#This script picks the random gate based on the gate area. The gate with the largest area has a higher probability of getting picked.
#Nanditha Rao

#Modifications:
#Gate array modified according to the decoder and c432 example of 65nm. Need to add more gates as and when larger examples are run and their areas are known: 25/4/2014

def weight_selection(path):
	
	import random,re

	gates=["HS65_GSS_XOR2X6","HS65_GS_AND2X4","HS65_GS_AOI22X6","HS65_GS_BFX284","HS65_GS_DFPQX4", "HS65_GS_IVX9","HS65_GS_NAND2X7","HS65_GS_NOR2X6","HS65_GS_NOR3X4","HS65_GS_AO212X4", "HS65_GS_AO311X9  ", "HS65_GS_AOI12X2", "HS65_GS_AOI212X4", "HS65_GS_AOI311X4", "HS65_GS_AOI32X5", "HS65_GS_AOI33X5", "HS65_GS_NAND2AX7", "HS65_GS_NAND3AX6", "HS65_GS_NAND3X5", "HS65_GS_NAND4ABX3", "HS65_GS_NOR3AX2", "HS65_GS_NOR4ABX2", "HS65_GS_NOR4ABX4", "HS65_GS_OA12X9", "HS65_GS_OAI212X5", "HS65_GS_OAI21X3", "HS65_GS_OAI33X3", "HS65_GS_OR2X9","HS65_GS_AO22X9","HS65_GSS_XOR3X2"]

	gate_areas=[4,3,4,30,8,2,2,2,3,5,5,3,4,4,4,5,3,4,3,4,3,4,4,4,4,3,5,3,4,8]
	areas=gate_areas[:]; #copy list
	#sorted_index= [i[0] for i in sorted(enumerate(gate_areas), key=lambda x:x[1])]


	#sorted array:
	gate_areas.sort() #Ascending sort
	one=gate_areas[0] #The minimum sized gate is the first in the list
	relative_weight=gate_areas[:] #initialise the output list

	#Get the weights of each gate relative to the smallest gate
	for i in range(0,len(areas)):
		relative_weight[i]=areas[i]/one

	subckts=[]
	instance=[]
	gate_weights=[]
	gateindex=[]
	final_gate_index=[]
	dff=0;

	fg = open('/%s/reference_spice.sp' %path, 'r')
	data = [line.strip() for line in fg] #Get the lines in the spice file
	length=len(data) #number of lines in the reference spice file
	j=0
	stop=0;
	for i in range(0,length):
		line=data[i]
		if stop == 0:	
		#If you come across ENDS, do not count any more X subckts because the top level subckt instance will also have X
			if line == ".ENDS": 
				stop=1;
	#If the line is not empty and if the first letter in the line begins with a 'X', it is the subckt statement we are looking for
	#Also, if the next line contains a '+', it is part of the same subckt too..
			if line and line[0]=='X':  
				nextline= data[i+1]
				if nextline[0]=='+':
					a=line
					next=nextline.split(' ',1)[1] #Split till the first instance of 'space'. Remove the '+'.
					subckts.append(a+next) #Append the next line containing '+'
				else:
					subckts.append(line)
	fg.close()
	fw=open('/%s/subcktfile.sp' %path, 'w')
	fa=open('/%s/subcktinstances.sp' %path, 'w') #gates
	for line in subckts:
		fw.write("%s\n" %line) #Write out subckt instances

	print "Number of subckts is:", len(subckts)

	#Grab the last word i.e., the gate..
	#GATE NAMES OF EACH SUBCKT
	for i in range(0,len(subckts)): 
		instance.append(subckts[i].split()[-1]) #For each line, get the gate and append it to the 'instance' list
		fa.write("%s\n" %subckts[i].split()[-1])
		cur_gate=subckts[i].split()[-1];
		if re.search("DF",cur_gate): #Look for FF anywhere in the string
			dff=dff+1; #Count the number of DFFPOS


	len_instance=len(instance) #the standard cells
	print "\nNumber of gate + DFF instances is:", len(instance)
	print "\nNumber of DFF instances is: %s" %dff
	print "\nPercentage of DFF instances is: %f" %(float(dff)/float(len(instance))*100.0)

	
	fw.close()
	fa.close()
	fa=open('/%s/subcktinstances.sp' %path, 'a+')
	#Compare each of the instances in the subckt with that of the standard gates and assign the weigths
	for i in range(0,len(instance)):
		for j in range(0,len(gates)):
			if instance[i]==gates[j]:
				gate_weights.append(relative_weight[j]) #Store the weights of the gates
			
	fa.write("Gate weigths is %s\n" %gate_weights)

	fa.write("\n\n\n")

	print " gate weights array:", gate_weights

	for j in range(0,len(gates)):
		gateindex.append(j)

	#Main gate index is:
	print "Gate index:%s" %gateindex

	fa.write( "Gate index:%s\n" %gateindex)
	fa.write("\n\n\n")	
	
###################################################################################################
##This is the final gate index which is having the duplicated instances of each gate for the number of times as indicated by the weights
	for i in range(0,len(gate_weights)):
		for j in range(0,gate_weights[i]): #Repeat the gates as many times as is the gate index
		#If the gate weight is 2, gate index has to be repeated 2 times, if the weight is 5, repeat gate index 5 times etc.,
			final_gate_index.append(i)
		
	
	fa.write ("Final gate index:\n")	
	fa.write("%s\n" %final_gate_index)	
	#print("Final gate index%s\n" %final_gate_index)
	
	print "Length of the final gate array=%d" %len(final_gate_index)
	lengthgates=len(final_gate_index)
	#Finally, we will pick a random number between 1 and the final length of this array. Say, it picked 5, The deckgen script will then go and pick the 5th subckt in the spice file	
	
	rand_gateindex= int(random.randrange(lengthgates)) 
	print "Random gate index=%d" %rand_gateindex
	subckt_index=final_gate_index[rand_gateindex]
	print "Random gate original index=%d" %subckt_index
	original_gate=instance[subckt_index];
	print "Random gate=%s" %original_gate

	fa.write ("\nNumber of gate instances is:%d" %len(instance))
	fa.write ( "\nNumber of DFF instances is: %s" %dff)
	fa.write ("\nPercentage of DFF instances is: %f" %(float(dff)/float(len(instance))*100.0))

	return subckt_index;

"""
path="/home/nanditha/Documents/iitb/utility/c432_priority_opFF";
num=weight_selection(path);
print "Random subckt line=%d" %num


fa=open('/%s/subcktinstances.sp' %path, 'r')
fb=open('/%s/subcktinstances1.sp' %path, 'w')
read=fa.readlines()
filelen=len(read)
fb.writelines(read[filelen-3])
fb.writelines(read[filelen-2])
fb.writelines(read[filelen-1])
fa.close()
fb.close()
"""









