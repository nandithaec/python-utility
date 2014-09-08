
#!/usr/bin/env python

#Example usage: python python_WL_reposition.py

import re

#f=open("../CORE65GPSVT_all.sp","r")
fs=open("../CORE65GPSVT_all_WL.sp","w")

f=open("test.sp","r")
fnew=open("test_1.sp","w")


lines=f.readlines()
spice=fs.readlines()


for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	#print "*****************\n"
	#print "i is",i
	#print "Current line:",current_line


	if re.match("X",current_line):  #if it is a subckt instance
		print "match X %s\n", current_line
		words=current_line.split()
		last_word=words[-1] #Save the last word: gate instance
		print "last word:",last_word	
		
				
	

