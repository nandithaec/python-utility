import re,fileinput, time

f=open("../dff_65_noC.txt","r")
fnew=open("../dff_65_new2.txt","w")

"""
#f=open("../test.sp","r")
#fnew=open("../test_final.sp","w")

lines=f.readlines()
print "length of lines",len(lines)

#Remove those caps which are connected to gnd
for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	#print "*****************\n"
	#print "i is",i
	#print "Current line:",current_line


	if re.match("C",current_line): #starts with a 'C'
		
		words=current_line.split()
		if words[2]!= "0":
			fnew.writelines(current_line)
	
	else: #Print out the current line if its not a C
		fnew.writelines(current_line)
	
	
f.close()
fnew.close()


f=open("../dff_65_new.txt","r")
fnew=open("../dff_65_new1.txt","w")

lines=f.readlines()
fnew.writelines(lines) #make a copy of the file
fnew.close()
print "length of lines",len(lines)



#short the caps and rename all those nodes that are connected to cap with the new name
for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	print "*****************\n"
	print "i is",i
	print "Current line:",current_line


	if re.match("C",current_line): #starts with a 'C'

		words=current_line.split()
		cap1=" "+words[1]+" "
		cap2=" "+words[2]+" "
		cap_new=" "+words[0]+" "
		
		print "cap1 =%s, cap2=%s,cap_new=%s" %(cap1,cap2,cap_new)
		
		#Do this action everytime you find "C"
		print "replacing..into for"
		x=fileinput.input("../dff_65_new1.txt",inplace=1) #make inplace editing on a duplicate copy of the same file
		for line in x:
			line=line.replace(cap1,cap_new)
			line=line.replace(cap2,cap_new)
			print line,  #The comma is required to prevent the newline after replacements

		x.close()
		print "outside for C"			
f.close()
fnew.close()
"""

lines=f.readlines()
fnew.writelines(lines) #make a copy of the file
fnew.close()
print "length of lines",len(lines)



#short the resistors and rename all those nodes that are connected to cap with the new name
for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	print "*****************\n"
	print "i is",i
	print "Current line:",current_line


	if re.match("R",current_line): #starts with a 'R'

		words=current_line.split()
		cap1=" "+words[1]+" "
		cap2=" "+words[2]+" "
		cap_new=" "+words[0]+" "
		
		print "cap1 =%s, cap2=%s, cap_new=%s" %(cap1,cap2,cap_new)
		
		#Do this action everytime you find "R"
		print "replacing..into for"
		x=fileinput.input("../dff_65_new2.txt",inplace=1) #make inplace editing on a duplicate copy of the same file
		for line in x:
			
			line=line.replace(cap1,cap_new)
			line=line.replace(cap2,cap_new)
			print line,  #The comma is required to prevent the newline after replacements

		x.close()
		print "outside for R"			
f.close()
fnew.close()
