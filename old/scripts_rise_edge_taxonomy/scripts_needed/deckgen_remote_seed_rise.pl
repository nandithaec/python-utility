#Example: perl deckgen_remote_seed_rise.pl -s reference_spice.sp -l glitch_osu018_stdcells_correct_vdd_gnd.sp -r decoder_op_ip_reference_out/tool_reference_out.txt -n 1 -m decoder_op_ip -f /home/external/iitb/nanditha/simulations/decoder_ip_opFF_rise -g 4 -d 2 -c 23584 -i 4.91e-09 -o 1 

#Modifications:
#THe previous change was incorrect. Reverting it back to "$start=$#temp-$num_opt+1;". A comman is needed after printing the "$random_drain," info to the RTL.csv files. Hence the drain info that it was writing was incorrect earlier. : Feb 12 2014

#Since I added 'drain' info also, I had to modify "$start=$#temp-$num_opt+1;" to :$start=$#temp-$num_opt;" inorder to print out all the RTL reference output values to the RTL.csv and RTL_2ndedge.csv : Feb 11 2014
#Appended the $random_drain to the RTL*.csv. This is needed to generate decks by just looking at the taxonomy.csv: Feb 11 2014
#Introduced 'next_2_cycle', which will capture the value of the rising edge of the next to next clk cycle. This is in sync with the change in modperl2_outwrtr_new.pl which was modified to write out all outputs at the rising edge instead of -ve edge: Feb 6 2014
#Code changed to include .ic ref values to all outputs of all FFs- Oct 20 2013
#Code changed to include .ic ref values for all inputs of all FFs in the spice file- didnt help - Oct 11 2013


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

 print "deckgen_remote_seed ERROR: BAD SYNTAX\n";
 print "TRY '$0 -h' or '$0 --help'  for help\n";
}
#  Routine to print man page
sub printManPage {
  print STDERR <<END; 
    
deckgen_remote_seed(1)                                                                                  

NAME

deckgen_remote_seed − Utility to create a simulatable spice deck from the template reference_spice.sp


SYNOPSIS

deckgen_remote_seed [input library file]  

DESCRIPTION

deckgen_remote_seed utility takes a spice library as input and creates a glitched induced library where eache subciruit has different version, each version has glitch induced to one of its distinct drain excluding Vdd and gnd.
deckgen.pl will modify the template spice file to introduce the glitched version of the gate in the spice file. The deckgen will get the 4 random numbers as input: random clk, random glitch instant, random gate and the random drain. It will go to the corresponding clk cycle in the decoder_op_ip_reference_out/tool_reference_out.txt and grab the input values at that clk edge and will insert these values into the reference_spice.sp file, to create, say, deck_1.sp. Again, for the next set of random numbers, the same is repeated, till the max number of decks specified, is reached. For each of the random clk cycles picked, this script will also write out the corresponding output values (which were written on the -ve edge) of the next clock cycle, into the decoder_op_ip_reference_out/RTL.csv file, which will be used as a reference value, during comparison of spice vs verilog simulation.

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

deckgen_remote_seed -i|--input <library name> 
deckgen_remote_seed -i /home/user/Desktop/osu_lib.sp 

SEE ALSO

SPICE.

AUTHOR
Shahbaz sarik (shahbaz\@ee.iitb.ac.in)

This utility has been written for the “ Impact of soft error on circuit” experiment carried out under the guidence of Prof. Madhav. P. Desai (madhav\@ee.iitb.ac.in) at IITBombay.

COPYRIGHT
GPL IIT-Bombay
deckgen_remote_seed January 3rd February 2013  
    
    
END
}

#  Get the command line arguments
#  check for missing/extra arguments and show usage

GetOptions( "s|spice=s"=>\$spc,
	    "l|lib=s"=>\$lib,
	    "r|ref=s"=>\$ref,
	    "n|num=s"=>\$deck_num,
	    "m|module=s"=>\$module,
	    "f|folder=s"=>\$folder,
	     "o|outloop=s"=>\$outloop,
	     "g|gate=s"=>\$rand_gate,
	     "d|drain=s"=>\$rand_drain,
	     "c|rclk=s"=>\$rand_clk,
	     "i|glitch=s"=>\$rand_glitch,
            "h|help"=>\$help,
            
          );
      
if ($help) {
  printManPage();
  exit(0);
}

if ($#ARGV >= 0 || $ref eq "" || $spc eq ""|| $lib eq "" || $deck_num eq "" || $module eq ""|| $folder eq "" || $outloop eq "" || $rand_gate eq "" || $rand_drain eq "" || $rand_clk eq "" || $rand_glitch eq "") {
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
$current_cycle="";
$next_cycle="";
$next_2_cycle="";
$minus1_cycle="";
$minus2_cycle="";
$minus3_cycle="";
$minus4_cycle="";
$minus5_cycle="";

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
       # print "Vdd for this technology is $vdd \n";
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
print "\nThis is deck number $deck_num\n";
#Pick a random gate in the design
#srand($seed);
#$j=int(rand($#gates-1));

$j=int($rand_gate);
#$j+=1;
@temp=split(" ",$gates[$j]);
$random_gate=$temp[$#temp];
print "Random gate picked = $random_gate \n";
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
#srand($seed);
#$random_drain=int(rand($drain-1));

$random_drain=int($rand_drain);
#$random_drain+=1;
print "Random drain $drain ----- $random_drain\n";
print "$gates[$j]-------------$random_gate\n";
$gates[$j]=~s/$random_gate/$random_gate\_$random_drain/;
#print join("\n",@gates);


#selecting a random clock cycle from the total number of cycles (as in refrence file)

#Not being used here. count calculated in perl_calculate_gates.pl
#open(REF,"$ref")||die("unable to open file : $!");
#count =0;
#while(<REF>)
# {  
#   $count++;
# }
#close(REF);
#This count value denotes the number of actual simulatable cycles for error analysys.

#$count-=10;
#print "\nnumber of simulatable clock cycles is $count \n";

#Pick a random clk cycle to simulate
#srand($seed);
$cycle=int($rand_clk);
#print "selected clock cycle : $cycle\n";
$count=0;
#storing the input output values from reference output file for present clock cycle and next cycle
#This file handle should be actually REF instead of SPC.
open(SPC,"$ref")||die("unable to open file : $!");
while(<SPC>)
 {  
     
    $count++;
    if($count==1)
       {
         chomp($header=$_);
       }
    else
       {
 	 $minus5_cycle =  $minus4_cycle;
 	 $minus4_cycle =  $minus3_cycle;
         $minus3_cycle =  $minus2_cycle;
         $minus2_cycle =  $minus1_cycle;
         $minus1_cycle =  $current_cycle;
         $current_cycle=$next_cycle;
         $next_cycle=$next_2_cycle;
         chomp($next_2_cycle=$_);
       }
       
    if($count==($cycle+3))
       {
          #print "last line = $count\n";print "\nDONE\n";
	  last;
       }
 }
#print "header : $header \n";
#print " clock cycle : $cycle input/output condition is $current_cycle \n";
#print " next clock cycle input/output condition is $next_cycle \n";
@cycle1=split(" ",$current_cycle);
@cycle2=split(" ",$next_cycle);

@cycle_minus1=split(" ",$minus1_cycle);
@cycle_minus2=split(" ",$minus2_cycle);
@cycle_minus3=split(" ",$minus3_cycle);
@cycle_minus4=split(" ",$minus4_cycle);
@cycle_minus5=split(" ",$minus5_cycle);

#selecting a random glitch location (between 1.2 clock_period to 1.5 clock period)
$clk_period=$sim_time/2.5;

#Pick a random glitch location in the clk cycle
#srand($seed);
#$glitch_location=1.2*$clk_period + rand(0.3*$clk_period);
$glitch_location=$rand_glitch;
print "Random glitch point is at time $glitch_location \n"; 

#creating the spice deck
#`mkdir $folder/spice_decks_$outloop`;
open(OPT,">$folder/spice_decks_$outloop/deck_$deck_num.sp")||die("unable to open file : $!");
print "\t\t\ !! SPICE DECK DIRECTORY CREATED !!\n";
#writing into the new spice file
$count=0;
open(SPC,"$spc")||die("unable to open file : $!");
while(<SPC>)
 {
    
  if($_=~m/\.ENDS/i)
     { 
      print OPT "\n$_";
     }  
 if($prnt==0)
     {
      print OPT "**clk_$cycle\_glitch_$glitch_location\_random_gate_$random_gate\_random_drain_$random_drain\_deck_number_$deck_num\n";
      $prnt=1;
     }
    $count++;
    $new=$_;
#Substituting the random glitch location
     if($_=~m/##glitch_location##/)
        {
         $new='+rise_delay= '.$glitch_location."s\n";

        }
#Substituting the deck number
     if($_=~m/##deck_num##/)
        {
          $new=$_;
          $new=~s/##deck_num##/$deck_num/;
        }
#Substituting the reference values
     if(($_=~m/PWL\(/))
#||($_=~m/\.ic/)
        {
	   ($temp1,$pinname)=split(" ",$_);
           #print $pinname."\n";
           @temp=split(" ",$header);
           foreach $index( 0 .. $#temp)
              {
                if($pinname eq $temp[$index])
                   {
                      #print "match found $pinname === $temp[$index]\n";
			#This is for the PWL statements in the spice file
		      $ref1=$cycle1[$index]*$vdd;
		      $ref2=$cycle2[$index]*$vdd;
		      $ref_minus1=$cycle_minus1[$index]*$vdd;
		      $ref_minus2=$cycle_minus2[$index]*$vdd;
		      $ref_minus3=$cycle_minus3[$index]*$vdd;
		      $ref_minus4=$cycle_minus4[$index]*$vdd;

                      $new=$_;
                      $new=~s/##$pinname\_reference_1##/$ref1/g;
		      $new=~s/##$pinname\_reference_2##/$ref2/g;
		      $new=~s/##$pinname\_reference_minus1##/$ref_minus1/g;
		      $new=~s/##$pinname\_reference_minus2##/$ref_minus2/g;
		      $new=~s/##$pinname\_reference_minus3##/$ref_minus3/g;
		      $new=~s/##$pinname\_reference_minus4##/$ref_minus4/g;

                   }
              }
           
        }
     
 

##################### Although this part is used, the corresponding .ic statments in the spice file
####################have been commented out as initialising the inputs did not work

#This part of the code is not being used
if(($_=~m/\.ic/))
        {
	   ($junk1,$temp1,$pinname)=split(" ",$_);
           chomp($pinname);
           $pinname=~s/_reference_minus5.*//;
           $pinname=~s/\#\#//;
          # print $pinname."\n";
          # print $pinname."\n";
           @temp=split(" ",$header);
           foreach $index( 0 .. $#temp)
              {
                if($pinname eq $temp[$index])
                   {
                      $ref_minus5=$cycle_minus5[$index]*$vdd;
      

                      $new=$_;
                      $new=~s/##$pinname\_reference_minus5##/$ref_minus5/g;

		     
                   }
              }
           
        }
######################




     if(($count<=$gate_start_point)||($count>$gate_end_point))
        {
           print OPT $new;
        }
     if($count==$gate_start_point+1)
        {
          print OPT join("\n",@gates);
        }

 }
#Appending to the RTL reference output file, which contains outputs of those clk cycles, that were picked by this script randomly, at the 3rd rising edge of the clk
#This will be used for the spice vs verilog simulation comparison
open(IM,">>$folder/$module\_reference_out/RTL.csv");
print IM "\n";
print "Random drain..RTL.csv $drain ----- $random_drain\n";
#A comma is needed at the end of the last entry
print IM "$deck_num,$cycle,$glitch_location,$random_gate,$rand_gate,$random_drain,";
@temp=split (" ",$next_2_cycle);
$start=$#temp-$num_opt+1;
#$start=$#temp-$num_opt;
foreach $index( $start .. $#temp)
  {
     
       if ($index == $#temp) 
	{
	print IM "$temp[$index]";
	} 
	else 
	{
	print IM "$temp[$index],";
	}

  }



#Appending to the RTL_2nd_edge reference output file, which contains outputs of those clk cycles, that were picked by this script randomly , at the 2nd rising edge of the clk
#This will be used for the spice vs verilog simulation comparison
open(IM,">>$folder/$module\_reference_out/RTL_2nd_edge.csv");
print IM "\n";
print "Random drain..RTL_2nd_edge.csv $drain ----- $random_drain\n";
#A comma is needed at the end of the last entry
print IM "$deck_num,$cycle,$glitch_location,$random_gate,$rand_gate,$random_drain,";
@temp=split (" ",$next_cycle);
$start=$#temp-$num_opt+1;
#$start=$#temp-$num_opt;
foreach $index( $start .. $#temp)
  {
     
       if ($index == $#temp) 
	{
	print IM "$temp[$index]";
	} 
	else 
	{
	print IM "$temp[$index],";
	}

  }








