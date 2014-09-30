#This script will short all resistors in the subckt. #Nanditha Rao, 10th Sep 2014
#input file is on the 1st line. Output is subckts_noR.sp

#Example: python python_xors_DFF_output.py -p /home/users/nanditha/Documents/utility/65nm/c432 -m c432_clk_ipFF
import re,time,os

import optparse
import string
from optparse import OptionParser

parser = OptionParser('This script adds XOR gates to all DFF outputs. Output: %s/pnr/op_data/%s_final_xors.v\nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')


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
	#if re.search("DFP",lines[i]): #This is for decoder
	if re.search("DFF",lines[i]): #This is for iscas
		words=lines[i].split()
		print "**\n\n\nWords",words
		print "**\nCurrent line is",lines[i]
		#if words[2].startswith("(.Q("): #3rd word is the Q node- capture the output node name- for decoder and ITC 
		if words[2].startswith("(.q("): #3rd word is the Q node- capture the output node name- for iscas
			dff_out=words[2][4:] #eliminate the first 4 letters
			
			
			if dff_out.endswith("),"):
				dff_out=dff_out[:-2]
				dff_output.append(dff_out)
			
			print "\ndff output",dff_out
			
		elif words[2].startswith("(.QN("): #3rd word is the QN node- capture the output node name- for ITC 
		#if words[2].startswith("(.q("): #3rd word is the Q node- capture the output node name- for iscas
			dff_out=words[2][5:]
			
			
			if dff_out.endswith("),"):
				dff_out=dff_out[:-2]
				dff_output.append(dff_out)
			print "\ndff output",dff_out
		#ff_name.append(words[1]) ##Flipflop name
		#print "FF name list is",ff_name
		
		
		#Insert an XOR gate between the DFF output and the next node
		#So, replace the Q node name with a "mod_". XOR gate input will be "mod_"
		
		print "\n**dff output list",dff_output
		modified="mod_"+dff_out
		modified=modified.replace("[","_")
		modified=modified.replace("]","_")
			
		print "DFF out is %s, modified is %s" %(dff_out,modified)
		mod_dff_output.append(modified)
		lines[i]=lines[i].replace(dff_out,modified) #Only replace the DFF lines
		print "\nmodified DFF output list",mod_dff_output

		#print "modified line is",lines[i]
		
		
for i in range(len(lines)):
	#if re.search("DFP",lines[i]): #This is for decoder
	if re.search("DFF",lines[i]): #This is for decoder
		words1=lines[i].split()
		ff_name.append(words1[1]) ##Flipflop name
		#print "Lines",lines[i]
		print "\nFF name list is",ff_name
		#print "***\n\n***"
		
				
#print lines

xor_lines=[]

#For the number of flip-flops that are present, add XOR gates to their outputs
for j in range(len(dff_output)):
	xor_string="HS65_GSS_XOR2X12" +" " + "xor_" + ff_name[j] + " " + "(.Z(" + dff_output[j] + ")," + ".A("+mod_dff_output[j] + ")," + ".B(1'b0));\n"
	xor_lines.append(xor_string)
	#print "XOR string is",xor_string

print "\n\nXOR List is:", xor_lines

wires=[]
for i in range(len(mod_dff_output)):
	wire_str="wire"+" " + mod_dff_output[i]+";\n"
	wires.append(wire_str)

print "\n\n**Wire instances are:",wires


done=0

for i in range (len(lines)-2): #dont write the last endmodule
	#print "Done is %d" %done
	if (done==0):
		#print "done=0",done
		if re.search("wire",lines[i]): #only match first instance of wire
			fs.writelines(lines[i])
			fs.writelines(wires) #Append wire instances
			done=1		
		else:
			fs.writelines(lines[i]) #If no wire, still print the lines
	
	else: #After the wires are appended, print the rest
		fs.writelines(lines[i]) 

#if not re.search("endmodule",lines[i]): #Dont write endmodule
#	print "no endmodule",lines[i]

fs.writelines("//One of the inputs to the XOR is always zero\n")
fs.writelines(xor_lines)
fs.writelines("\nendmodule\n")

print "%s/pnr/op_data/%s_final_xors.v written out.." %(path,module)
						
fs.close()

