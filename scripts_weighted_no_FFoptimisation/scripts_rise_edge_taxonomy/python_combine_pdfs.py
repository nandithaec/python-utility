
#Combine the 2 reports
doc = SimpleDocTemplate("%s/taxonomy_report_all_%s.pdf" %(path,design), pagesize=letter)

#####################Merge the gate and FF pdfs into one final pdf##################
from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()



if (os.path.isdir('%s/spice_results' %path)):
	#print "Inside if"		
	input1 = PdfFileReader(file("%s/spice_results/taxonomy_report_gates_%s.pdf" %(path,design), "rb"))
	# print how many pages input1 has:
	print "%s/spice_results/taxonomy_report_gates_%s.pdf has %s pages." % (path,design,input1.getNumPages())
	# add page 1 from input1 to output document, unchanged. Each pdf has only one page
	output.addPage(input1.getPage(0))

	input2 = PdfFileReader(file("%s/spice_results/taxonomy_report_FFs_%s.pdf" %(path,design), "rb"))
	# print how many pages input1 has:
	print "%s/spice_results/taxonomy_report_FFs_%s.pdf has %s pages." % (path,design,input1.getNumPages())
	# add page 1 from input1 to output document, unchanged. Each pdf has only one page
	output.addPage(input2.getPage(0))

# finally, write "output" to document-output.pdf
outputStream = file("%s/taxonomy_report_all_%s.pdf" %(path,design), "wb")
output.write(outputStream)
outputStream.close()

print "\nWritten final results file with taxonomy of all designs combined\n"
print "Location of the file: %s/spie_results/taxonomy_report_all_%s.pdf" %(path,design)

