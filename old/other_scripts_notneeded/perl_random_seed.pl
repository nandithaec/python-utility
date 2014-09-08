#!/usr/bin/perl
#Example: perl deckgen.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -n 1 -m decoder_behav_pnr 
use Getopt::Long;

GetOptions( "s|seed=s"=>\$seed,
            "h|help"=>\$help,
               );
      
if ($help) {
  printManPage();
  exit(0);
}

if ($#ARGV >= 0 || $seed eq "") {
  print STDERR "-E- Found missing/excess arguments\n";
  printErrMessage();
  exit(1);
}

srand($seed);
