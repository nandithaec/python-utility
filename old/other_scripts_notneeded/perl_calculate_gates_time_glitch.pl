#Example: perl perl_calculate_gates_time_glitch.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_original.sp -r decoder_behav_pnr_reference_out/tool_reference_out.txt -m decoder_behav_pnr -f decoder 

#perl %s/perl_calculate_gates_time_glitch.pl -s %s/reference_spice.sp -l %s/glitch_osu018_stdcells_correct_original.sp -r %s/%s_reference_out/tool_reference_out.txt -m %s -f %s


#!/usr/bin/perl
use Getopt::Long;
#####################################################################
#
# Author        : Shahbaz Sarik
# Date          : 7th February 2013
# Purpose       : To create spice decks from a reference spice file 
#                 
# Copyright	: IIT BOMBAY
####################################################################

#  Routine to print Error message
sub printErrMessage {

 print "NetldtFrmt ERROR: BAD SYNTAX\n";
 print "TRY '$0 -h' or '$0 --help'  for help\n";
}
#  Routine to print man page
sub printManPage {
  print STDERR <<END; 
    
NetldtFrmt(1)                                                                                  

NAME

NetldtFrmt − Utility to create a glitch induced version of a spice library.

SYNOPSIS

NetldtFrmt [input library file]  

DESCRIPTION

NetldtFrmt utility takes a spice library as input and creates a glitched induced library where eache subciruit has different version, each version has glitch induced to one of its distinct drain excluding Vdd and gnd.

OPTIONS

 
Input library file

-|--input = <input library>

This file should be the spice library whose glitched version is to be created.


NOTE:

Provide full path for files
The glitched libray created in the current directory and named as glitch_library_name

USAGE

Typical usage of the utility after installation is explained below.


Examples:

NetldtFrmt -i|--input <library name> 
NetldtFrmt -i /home/user/Desktop/osu_lib.sp 

SEE ALSO

SPICE.

AUTHOR
Shahbaz sarik (shahbaz\@ee.iitb.ac.in)

This utility has been written for the “ Impact of soft error on circuit” experiment carried out under the guidence of Prof. Madhav. P. Desai (madhav\@ee.iitb.ac.in) at IITBombay.

COPYRIGHT
GPL IIT-Bombay
NetldtFrmt January 3rd February 2013  
    
    
END
}

#  Get the command line arguments
#  check for missing/extra arguments and show usage

GetOptions( "s|spice=s"=>\$spc,
	    "l|lib=s"=>\$lib,
	    "r|ref=s"=>\$ref,
	      "m|module=s"=>\$module,
	    "f|folder=s"=>\$folder,
	     "h|help"=>\$help,
            
          );
      
if ($help) {
  printManPage();
  exit(0);
}

if ($#ARGV >= 0 || $ref eq "" || $spc eq ""|| $lib eq "" || $module eq ""|| $folder eq "") {
  print STDERR "-E- Found missing/excess arguments\n";
  printErrMessage();
  exit(1);
}
#Getting job start time
chomp($date=`date`);
print "\t\t**********    Job started   at $date    **********\n";

#Initializing the parameters
$sim="sim_".$spc;
@sub_ckt="";
$i=0;
$j=0;
$flag=0;
$in=0;
@gates="";
$done=0;
$cycle=0;
$current_cycle=0;
$next_cycle=0;
$sim_time=0;
$active=1;
$glitch_location=0;
$prnt=0;
$num_opt;
#opening the required files
open(SPC,"$spc")||die("unable to open file : $!");
while(<SPC>)
 {  
    $count++;
    if($_=~m/\.ENDS/i)
     {
      $active=0;
	$gate_end_point=$count;
     }
        
    if(($_=~m/^x.*/i)&&($active==1))
       {
        #print $_;
	chomp($gates[$i++]=$_);	
	$flag=1;
	$in=1;
      }
    if(($in==1 && $done == 0)&&($active==1))
      {
        $gate_start_point=$count-1;
        $done=1;
      }
    if((($_=~m/^\+.*/i))&&($active==1))
       {
         if($flag==1)
            {
	     chomp($tail=$_);
	     $tail=~s/\+//;
	     $gates[$i-1].=$tail;
	     
	    }
       }
    if($_=~m/tran 10ps (.*)s/i)
       {
        $sim_time=$1; #print "simulation time = $1\n";
       }
    if($_=~m/Vvdd vdd 0 (.*)/i)
       {
        chomp($vdd=$1);
       #s print "Vdd for this technology is $vdd \n";
       }
    if($_=~m/NUMBER OF OUTPUT PINS = (.*)/)
       {
         chomp($num_opt=$1)
       } 

 }
close(SPC);
#print "subcircuit starts from line number $gate_start_point and ends at line number $gate_end_point \n";
#print join("\n",@gates);
#print "total number of gates = $#gates \n";
#print "\nThis is deck number $deck_num\n";
#Pick a random gate in the design


open(RAN,">$folder/tmp_random.txt");
#Number of gates
$num_of_gates=$#gates-1;

print RAN "$num_of_gates\n";

$j=int(rand($num_of_gates));
$j+=1;
@temp=split(" ",$gates[$j]);
$random_gate=$temp[$#temp];
#print "Random gate picked = $random_gate \n";
#print "the random gate selected is gate number $j \n";


#selcting arandom glitched gate
open(LIB,"$lib")||die("unable to open file : $!");
while(<LIB>)
 {  
   if($_=~m/^\*\*\*\* $random_gate/)
     {
       $_=~m/(\d+)$/;
	$drain=$1;
	last;
     }
}
#Pick a random drain in the random gate in the design
#Number of drains
$num_of_drains=$drain-1;
print RAN "$num_of_drains\n";
$random_drain=int(rand($num_of_drains));
$random_drain+=1;
#print "$drain ----- $random_drain\n";
#print "$gates[$j]-------------$random_gate\n";
$gates[$j]=~s/$random_gate/$random_gate\_$random_drain/;
#print join("\n",@gates);


#selecting a random clock cycle from the total number of cycles (as in refrence file)
open(REF,"$ref")||die("unable to open file : $!");
$count =0;
while(<REF>)
 {  
   $count++;
 }
close(REF);
$count-=4;

#Number of clk cycles
print "\nNumber of gates is $num_of_gates\n";
print "num of drains for theis $num_of_drains\n";
print "number of simulatable clock cycles is $count \n";

#Pick a random clk cycle to simulate



print RAN "$count\n";



#$cycle=int(rand($count));
#print "selected clock cycle : $cycle\n";
#$count=0;
#storing the input output values from reference file for present clock cycle and next cycle

#print "header : $header \n";
#print " clock cycle : $cycle input/output condition is $current_cycle \n";
#print " next clock cycle input/output condition is $next_cycle \n";
#@cycle1=split(" ",$current_cycle);
#@cycle2=split(" ",$next_cycle);

#selecting a random glitch location (between 1.2 clock_period to 1.5 clock period)
#$clk_period=$sim_time/2.5;

#Pick a random glitch location in the clk cycle
#Number of clk cycles
#$glitch_location=1.2*$clk_period + rand(0.3*$clk_period);
#print "Random glitch point is at time $glitch_location \n"; 


#creating the spice deck
#`mkdir $folder/spice_decks_$outloop`;
#open(OPT,">$folder/spice_decks_$outloop/deck_$deck_num.sp")||die("unable to open file : $!");
#print "\t\t\t\t\t\t\t !! SPICE DECK DIRECTORY CREATED !!\n";
#writing into the new spice file
#$count=0;
#open(SPC,"$spc")||die("unable to open file : $!");

#Appending to the RTL reference output file, which contains outputs of those clk cycles that were picked by this script randomly
#open(IM,">>$folder/$module\_reference_out/RTL.csv");
#print IM "\n";
#print IM "$deck_num,$cycle,$glitch_location,";
#@temp=split (" ",$next_cycle);
#$start=$#temp-$num_opt+1;



