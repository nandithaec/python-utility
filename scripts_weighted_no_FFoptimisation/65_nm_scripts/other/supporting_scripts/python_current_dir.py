import re

f=open("deck_1.sp","r")
fnew=open("hspice_deck_1.sp","w")

#f=open("test.sp","r")
#fnew=open("test_final.sp","w")

lines=f.readlines()


for i in range(0,len(lines)):
	#Get each line
	current_line=lines[i]
	print "*****************\n"
	print "i is",i
	print "length of lines",len(lines)
	#last current line is the last line, then line+1 wont work.
	if (i < len(lines)-1):
		next_line=lines[i+1]
		print "Next line:",next_line
	print "Current line:",current_line


#There will be '+' in subckt definition as well. Print them out as it is
	if re.match(".SUBCKT",current_line) or re.match(".subckt",current_line):
		print "subckt line\n"
		flag=0
		fnew.writelines(current_line)
		while flag==0:
			i=i+1
			if re.match("\+",lines[i]): #If next line has +
				fnew.writelines(lines[i])
			else:
				flag=1 #When the next line is no longer a '+', the subckt has ended. So break the loop
				
	elif re.match("X",current_line):  #if it is a subckt instance
		#Check if next line is its continuation. Check for '+'
		print "match X\n"
		if re.match("\+",next_line):
			print "match + next line\n"
			if current_line[-1]=='\n':
			#Remove \n from the current line before appending next line
				current_line=current_line[:-1] 
			#Eliminate the first character of next line which is '+' and append the rest
			for j in range(1,len(next_line)):  
				current_line=current_line+next_line[j] #append the 2 lines
		
			
			#Do not write out the next line which starts with '+'
			#Hence increment the index. Doesnt work
			#i=i+2
			#print "i incremented is\n",i
			
			
		else: #If there is no continuation of subckt, print out the current subckt
		
			print "no continuation of subckt:",current_line
	
	#Write gnd gnds vdd vdds before the std cell instance name
		words=current_line.split()
		last_word=words[-1] #Save the last word			
		print "last word:",last_word	
		del words[-1]  #Remove the last word
		sentence=" ".join(words)+" gnd gnds vdd vdds "+last_word+"\n"
		
		fnew.writelines(sentence)
		print "Modified line:",sentence		
			
	
	else: #If not a subckt instance, write as it is the non-subckt line.
		if (re.match("\+",current_line)==None): #If the line does not start with '+'
			fnew.writelines(current_line)
			print "not a subckt instance:",current_line
		else:
			print "starts with +. Hence omitting\n"
	

