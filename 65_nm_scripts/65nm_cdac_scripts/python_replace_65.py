import os



"""
fin = open('pnr/scripts/pnr.tcl', 'r') 
fnew = open('pnr/scripts/pnr_new.tcl', 'w') ## This is the new pnr conf script


for line in fin:
	#Comment out the following Filler lines
	if line == '    addFiller -cell FILL -prefix FILL\n':
		fnew.write('    ##addFiller -cell FILL -prefix FILL\n')
	elif line == '    addFiller -cell FILL -prefix FILL -fillBoundary\n':
		fnew.write('    ##addFiller -cell FILL -prefix FILL -fillBoundary\n')
	else:	
		if "metal5" in line:
			fnew.write(line.replace('metal5', 'M5'))
		if "metal6" in line:
			fnew.write(line.replace('metal6', 'M6'))
		else:
			fnew.write(line)

			
fnew.close()
fin.close()

"""	
import fileinput
import sys


for line in fileinput.input('pnr/scripts/pnr.tcl', inplace=1):
	if "metal5" in line:
		line = line.replace("metal5","M5")
	if "metal6" in line:
		line = line.replace("metal6","M6")
	if "    addFiller -cell FILL -prefix FILL\n" in line:
		line = line.replace("    addFiller -cell FILL -prefix FILL\n","    ##addFiller -cell FILL -prefix FILL\n")
	if "    addFiller -cell FILL -prefix FILL -fillBoundary\n" in line:
		line = line.replace("    addFiller -cell FILL -prefix FILL -fillBoundary\n","    ##addFiller -cell FILL -prefix FILL -fillBoundary\n")
		
		sys.stdout.write(line)
	
	else:
		sys.stdout.write(line)       
        


