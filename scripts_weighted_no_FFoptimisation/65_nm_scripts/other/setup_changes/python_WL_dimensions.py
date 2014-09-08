
import re

f=open("CORE65GPSVT_subckts.spi","r")
f1=open("CORE65GPSVT_subckts_new.sp","w")
lines=f.readlines() #List of all lines

for i in range(0,len(lines)):
	words=lines[i].split() #Every word is captured in a list
	#print "Words",lines[i]
	#print "\n"
	words_new=[]
	for j in range(0,len(words)):
		"""
		b=list(words[j])  #Convert to list
		print "split words",b
		if b[0]=='W' and b[1]=='=':
			a="".join(b)
			a=a+"u"
			print "Word joined back:W:",a
			words_new.append(a)
		"""	
	#	print "Word chosen:",words[j]
		#If the word begins with W=
		if (re.match("W=",words[j])):
			words[j]=words[j]+"u" #Append micron (u)
	#		print "Word joined back:W:",words[j]
			words_new.append(words[j])
		elif (re.match("L=",words[j])):
			words[j]=words[j]+"u" #Append micron (u)
	#		print "Word joined back:L:",words[j]
			words_new.append(words[j])
			
		elif (re.match("PD=",words[j],re.I)):
			words[j]=words[j]+"u" #Append micron (u)
	#		print "Word joined back:PD:",words[j]
			words_new.append(words[j])		
			
		elif (re.match("PS=",words[j],re.I)):
			words[j]=words[j]+"u" #Append micron (u)
	#		print "Word joined back:PS:",words[j]
			words_new.append(words[j])
			
		elif (re.match("AS=",words[j],re.I)):
			words[j]=words[j]+"p" #Append micron*micron (p)
	#		print "Word joined back:AS:",words[j]
			words_new.append(words[j])
			
		elif (re.match("AD=",words[j],re.I)):
			words[j]=words[j]+"p" #Append micron*micron (p)
	#		print "Word joined back:AD:",words[j]
			words_new.append(words[j])
				
			
		else:	
			words_new.append(words[j])
	#		print "Word list",words_new
		
	sentence=" ".join(words_new)+"\n"  #Join with space
#	print "Sentence:",sentence
			
	f1.writelines(sentence) #write modified string
	
