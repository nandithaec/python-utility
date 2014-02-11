#!/usr/bin/env python

#Compare results of spice and RTL, creates difference files and validation files for each run

#Example usage: python python_taxonomy_gate_FF.py  -p /home/external/iitb/nanditha/simulations/decoder_ip_opFF_rise -m decoder_op_ip

import optparse
import re,os
import csv, re
import time


#import python_compare_remote

from optparse import OptionParser
print "\nExecuting taxonomy.."
from python_gate_strike_taxonomy import taxonomy_gates
from python_FF_strike_taxonomy import taxonomy_FFs
print "\nExecuting taxonomy..1"
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

parser = OptionParser('This script reads in the <path>/<design_case>/results/weighted/gates_FF/low_slack/spice_results/spice_rtl_difference_summary.csv and count_flips_summary.csv in the same path, to classify the observed flips. Two files are written out:\n1. <path>/spice_results/strike_on_gates.csv and\n2.<path>/spice_results/strike_on_FF.csv.\n The classification data is written out to another pdf called  <path>/taxonomy_report.pdf \nAuthor:Nanditha Rao(nanditha@ee.iitb.ac.in)\n')

parser.add_option("-p", "--path", dest="path",help="Enter the ENTIRE path to the folder which contains /spice_results  ")
parser.add_option("-m", "--mod", dest="module",help="Enter the name of the design module ")

(options, args) = parser.parse_args()

path=options.path
design=options.module


#Run the taxonomy for gates. Call the function.
print "\n\nRunning taxonomy for gates\n"
time.sleep(2)
taxonomy_gates(path,design)

#Run the taxonomy for FFs.  Call the function.
print "\n\nRunning taxonomy for FFs\n"
time.sleep(2)
taxonomy_FFs(path,design)



