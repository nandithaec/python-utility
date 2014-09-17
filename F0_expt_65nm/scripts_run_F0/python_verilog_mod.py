#This script will create a new zero delay file from original file

import re, time

f=open("../../CORE65GPSVT.v","r")
lines=f.readlines()
f.close()

fnew=open("../../CORE65GPSVT_nodelay.v","w")

for i in range(len(lines)):
	#print lines[i]
	if re.match("`define",lines[i]): 
		#print "'define found: ",lines[i]
		words=lines[i].split()
		#print "words is:",words
		words[len(words)-1]="0" #replace last word with 0
		line=" ".join(words)
		new_line=line+"\n"
		#print "replaced line",new_line
		fnew.writelines(new_line)
		#print "\n\n"
		
	elif "#1" in lines[i]:
		line = lines[i].replace("#1","")
		#print "#1 found", lines[i]
		#print "modified line",line
		fnew.writelines(line)
	else:
		fnew.writelines(lines[i])
	
	
					
fnew.close()

