import string


mystring="decoder.vhd"

if ".vhd" in mystring.lower():
	print "vhdl file"
else:
	print "verilog file"
