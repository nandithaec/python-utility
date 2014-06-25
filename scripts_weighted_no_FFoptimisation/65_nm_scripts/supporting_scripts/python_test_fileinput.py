import fileinput


cap1="CPN:F36"
cap2="net22:F81"
cap_new=cap1+cap2
cap3=" "+cap1+" "
cap4=" "+cap2+" "
print "cap1 =%s, cap2=%s,cap_new=%s, cap3=%s,cap4=%s" %(cap1,cap2,cap_new,cap3,cap4)
#Do this action everytime you find "C"
print "replacing..into for"
x=fileinput.input("../test_final1.txt",inplace=1) #make inplace editing on a duplicate copy of the same file
for line in x:
	line=line.replace(cap3," "+cap_new+" ")
	line=line.replace(cap4," "+cap_new+" ")
	print line,  #The comma is required to prevent the newline after replacements

x.close()
