#This script will short all resistors in the subckt. #Nanditha Rao, 10th Sep 2014
#input file is on the 1st line. Output is subckts_noR.sp

#Example: python python_xors_DFF_output.py -p <path to design> -m <module>
import re,time,os

import optparse
import string
from optparse import OptionParser

parser = OptionParser('This script adds XOR gates to all DFF outputs.\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')


parser.add_option("-p", "--path", help="Enter the ENTIRE path to your design folder (your working dir)- /home/user1/simulations/<design_folder_name>",dest="path")
parser.add_option("-m", "--module", help="Enter the main verilog/vhdl module name",dest="module")

#This is the most important line which will parse the cmd line arguments
(options, args) = parser.parse_args()

path=options.path
module=options.module



f=open("%s/pnr/op_data/%s_final.v" %(path,module),"r")
lines=f.readlines()
f.close()

fs=open("%s/pnr/op_data/%s_final_xors.v" %(path,module),"w")
dff_output=[]
ff_name=[]
mod_dff_output=[]
for i in range(len(lines)):
	#print "Lines",lines[i]
	#If Flipflop found, matching for string DFP
	if re.search("DFP",lines[i]):
		words=lines[i].split()
		print "Words",words
		if words[2].startswith("(.Q("): #3rd word is the Q node- capture the output node name
			dff_out=words[2][4:]
			#print "dff output",dff_out
		if dff_out.endswith("),"):
			dff_out=dff_out[:-2]
			dff_output.append(dff_out)
		ff_name.append(words[1])
		
		#Insert an XOR gate between the DFF output and the next node
		#So, replace the Q node name with a "mod_". XOR gate input will be "mod_"
		
		print "dff output list",dff_output
		print "***\n\n***"
		modified="mod_"+dff_out
		modified=modified.replace("[","_")
		modified=modified.replace("]","_")
		mod_dff_output.append(modified)
		lines[i]=lines[i].replace(dff_out,modified)
		print "modified DFF output list",mod_dff_output
		print "***\n\n***"		
		#print "modified line is",lines[i]
		print "FF name list is",ff_name
		print "***\n\n***"
		
				
#print lines

xor_lines=[]

#For the number of flip-flops that are present, add XOR gates to their outputs
for j in range(len(dff_output)):
	xor_string="HS65_GSS_XOR2X12" +" " + "xor_" + ff_name[j] + " " + "(.Z(" + dff_output[j] + ")," + ".A("+mod_dff_output[j] + ")," + ".B(1'b0));\n"
	xor_lines.append(xor_string)
	#print "XOR string is",xor_string

#print "XOR List is:", xor_lines

wires=[]
for i in range(len(mod_dff_output)):
	wire_str="wire"+" " + mod_dff_output[i]+";\n"
	wires.append(wire_str)

print "Wire instances are:",wires


done=0

for i in range (len(lines)):
	if not re.search("endmodule",lines[i]): #Dont write endmodule
		print "no endmodule",lines[i]
		print "Done is %d" %done
		if (done==0):
			print "done=0",done
			if re.search("wire",lines[i]): #only match first instance of wire
				fs.writelines(lines[i])
				fs.writelines(wires) #Append wire instances
				done=1		
			else:
				fs.writelines(lines[i]) #If no wire, still print the lines
		
		else: #After the wires are appended, print the rest
			fs.writelines(lines[i]) 



fs.writelines("//One of the inputs to the XOR is always zero\n")
fs.writelines(xor_lines)
fs.writelines("\nendmodule\n")

print "%s/pnr/op_data/%s_final_xors.v written out.." %(path,module)
						
fs.close()

