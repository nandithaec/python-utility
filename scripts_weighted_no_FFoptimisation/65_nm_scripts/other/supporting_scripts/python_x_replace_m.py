

#Replace subckts of transistors with the transistor models
#Replace 'X' with 'M' in subckts

f=open("CORE65GPSVT.spi","r")
f1=open("CORE65GPSVT_subckts.spi","w")
data=f.readlines()

for i in range(0,len(data)):
	line=data[i]
	b=list(line)  #Convert to list
	if b[0]=='X' and b[1] !='l':
		b[0]='M'
		a="".join(b) #convert back to string
		f1.writelines(a) #write modified string
	else:
		f1.writelines(line) #write as it is
	
	
