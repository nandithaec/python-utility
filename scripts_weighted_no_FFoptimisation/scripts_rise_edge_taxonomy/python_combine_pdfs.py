#This script just combines 2 pdfs

#Example usage: python python_combine_pdfs.py -p /home/nanditha/Documents/utility/design_cases_taxonomy/decoder/low_slack/spice_results -m decoder_op_ip

import optparse,os

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from optparse import OptionParser

parser = OptionParser('This script just combines 2 pdfs \nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path to the folder which contains the 2 pdfs to be merged ")
parser.add_option("-m", "--mod", dest="module",help="Enter the module name ")

(options, args) = parser.parse_args()

path=options.path
design=options.module

#Combine the 2 reports
doc = SimpleDocTemplate("%s/taxonomy_report_all_%s.pdf" %(path,design), pagesize=letter)

#####################Merge the gate and FF pdfs into one final pdf##################
from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()

if (os.path.isdir('%s' %path)):
	#print "Inside if"		
	input1 = PdfFileReader(file("%s/taxonomy_report_gates_%s.pdf" %(path,design), "rb"))
	# print how many pages input1 has:
	print "\n%s/taxonomy_report_gates_%s.pdf has %s pages." % (path,design,input1.getNumPages())
	# add page 1 from input1 to output document, unchanged. Each pdf has only one page
	output.addPage(input1.getPage(0))

	input2 = PdfFileReader(file("%s/taxonomy_report_FFs_%s.pdf" %(path,design), "rb"))
	# print how many pages input1 has:
	print "\n%s/taxonomy_report_FFs_%s.pdf has %s pages." % (path,design,input1.getNumPages())
	# add page 1 from input1 to output document, unchanged. Each pdf has only one page
	output.addPage(input2.getPage(0))

# finally, write "output" to document-output.pdf
outputStream = file("%s/taxonomy_report_all_%s.pdf" %(path,design), "wb")
output.write(outputStream)
outputStream.close()

print "\nWritten final results file with taxonomy of all designs combined\n"
print "\nLocation of the file: %s/taxonomy_report_all_%s.pdf\n\n" %(path,design)

