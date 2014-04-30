import re,fileinput, time

f=open("../decoder_65nm/glitch_CORE65GPSVT_selected_lib.sp","r")
fnew=open("../decoder_65nm/glitch_CORE65GPSVT_selected_lib_vg.sp","w")

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

	words=current_line.split()
	for j in range(0,len(words)):
		if re.search("vdd",words[j]): #If the word contains vdd,for eg., vdd:F6, then replace it with vdd
			words[j]="vdd"
		elif re.search("gnd",words[j]): 
			words[j]="gnd"
		
	sentence=" ".join(words)+"\n"
	fnew.writelines(sentence)
	
	
f.close()
fnew.close()


