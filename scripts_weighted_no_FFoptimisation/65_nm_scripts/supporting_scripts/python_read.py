#Read line by line and delete \n at the end of the line

f=open("test.sp","r")
f1=open("test1.sp","w")

data=f.readlines()
new_data=[]

for i in range(0,len(data)):
	print "Line:", data[i]
	line=data[i]
	if line[-1]=='\n':
		line=line[:-1]
		print "Modified line",line
	new_data.append(line)
	
f1.writelines(new_data)

f.close()
f1.close()
