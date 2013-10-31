#!/usr/bin/perl
#Example: perl deckgen.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -n 1 -m decoder_behav_pnr 

use Getopt::Long;



$j=int(rand(100));
print "the random number1(1-100) is $j \n";


$i=int(rand(10));
print "the random number2(1-10) is $i \n";
