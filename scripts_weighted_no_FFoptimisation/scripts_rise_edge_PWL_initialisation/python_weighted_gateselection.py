
#!/usr/bin/env python

#Example usage: python python_weighted_gateselection.py 
#This script picks the random gate based on the gate area. The gate with the largest area has a higher probability of getting picked.
#Nanditha Rao

def weight_selection(path):
	
	import random

	gates=["AND2X1","AND2X2","AOI21X1","AOI22X1","DFFPOSX1","INVX1","INVX2","INVX4","INVX8", "NAND2X1","NAND3X1","NOR2X1","NOR3X1","OAI21X1", "OAI22X1", "OR2X1","OR2X2","XNOR2X1", "XOR2X1"]

	gate_areas=[32,32,32,40,96,16,16,24,40,24,32,24,64,27,40,32,32,56,56]
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
	data = [line.strip() for line in fg]
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
	#Also, if the next line contains a '+', it is part of teh same subckt too..
			if line and line[0]=='X':  
				nextline= data[i+1]
				if nextline[0]=='+':
					a=line
					next=nextline.split(' ',1)[1] 
					subckts.append(a+next)
				else:
					subckts.append(line)
	fg.close()
	fw=open('/%s/subcktfile.sp' %path, 'w')
	fa=open('/%s/subcktinstances.sp' %path, 'w')
	for line in subckts:
		fw.write("%s\n" %line)

	print "Number of subckts is:", len(subckts)

	#Grab the last word i.e., the gate..
	#GATE NAMES OF EACH SUBCKT
	for i in range(0,len(subckts)):
		instance.append(subckts[i].split()[-1])
		fa.write("%s\n" %subckts[i].split()[-1])
		cur_gate=subckts[i].split()[-1];
		if cur_gate=="DFFPOSX1":
			dff=dff+1; #Count the number of DFFPOS


	len_instance=len(instance)
	print "\nNumber of gate instances is:", len(instance)
	print "\nNumber of DFF instances is: %s" %dff
	print "\nPercentage of DFF instances is: %f" %(float(dff)/float(len(instance))*100.0)

	
	fw.close()
	fa.close()
	fa=open('/%s/subcktinstances.sp' %path, 'a+')
	#Compare each of the instances in the subckt with that of the standard gates and assign the weigths
	for i in range(0,len(instance)):
		for j in range(0,len(gates)):
			if instance[i]==gates[j]:
				gate_weights.append(relative_weight[j])
			
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
			final_gate_index.append(i)
		
	fa.write ("Final gate index:\n")	
	fa.write("%s\n" %final_gate_index)	
	#print("Final gate index%s\n" %final_gate_index)
	
	print "Length of the final gate array=%d" %len(final_gate_index)
	lengthgates=len(final_gate_index)
	
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









