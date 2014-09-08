import re

f=open("../CORE65GPSVT_RC_1.sp","r")
fnew=open("../CORE65GPSVT_1.sp","w")

#f=open("test.sp","r")
#fnew=open("test_final.sp","w")

lines=f.readlines()


for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	#print "Line\n"
#See if the sentence begins with 'C' or 'R'
	if (re.match("C",current_line)==None):
		#if (re.match("R",current_line)==None):
		fnew.writelines(current_line)
		
				

	

