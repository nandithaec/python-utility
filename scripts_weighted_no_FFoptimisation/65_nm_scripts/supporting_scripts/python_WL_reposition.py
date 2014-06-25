
#!/usr/bin/env python

#Example usage: python python_WL_reposition.py

import re

f=open("../CORE65GPSVT_all.sp","r")
fnew=open("../CORE65GPSVT_all_WL.sp","w")

#f=open("test.sp","r")
#fnew=open("test_1.sp","w")


lines=f.readlines()


for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	#print "*****************\n"
	#print "i is",i
	#print "Current line:",current_line


#There will be '+' in subckt definition as well. Print them out as it is
	if re.match("M",current_line):
		#print "M line\n"
		#Write as it is till NSVTGP or PSVTGP, i.e., first 6 words as it is
		words=current_line.split()
		for a in range(0,6):
			fnew.writelines(words[a]+" ")
		
		#scan for W 
		for j in range(0,len(words)):
			if words[j][0]=="W":
				#print "W found",words[j]
				fnew.writelines(words[j]+" ")	
				
		
		#scan for L after W
		for j in range(0,len(words)):
			if words[j][0]=="L":
				#print "L found",words[j]
				fnew.writelines(words[j]+" ")	
						
		fnew.writelines("\n")	

	
	else: #Print out the current line
		fnew.writelines(current_line)
	

