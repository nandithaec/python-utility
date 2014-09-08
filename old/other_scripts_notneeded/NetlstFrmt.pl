#Example: perl NetlstFrmt.pl -v decoder_behav_pnr_modelsim.v -s pnr/op_data/decoder_behav_pnr_final.dspf -l glitch_osu018_stdcells_correct_original.sp -c 1000 -t 180 -m decoder_behav_pnr
#clk frequency in MHz

use Getopt::Long;
#####################################################################
#
# Author        : Shahbaz Sarik
# Date          : 7th March 2013
# Purpose       : To create a simulatable netlist from the rtl2gds output .dspf file
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

GetOptions( "v|verilog=s"=>\$vlog,
            "s|spice=s"=>\$spc,
	    "l|lib=s"=>\$lib,
	    "c|clk=s"=>\$clk,
	    "t|tech=s"=>\$tech,
	    "m|module=s"=>\$module,
            "h|help"=>\$help
          );
      
if ($help) {
  printManPage();
  exit(0);
}

if ($#ARGV >= 0 || $vlog eq "" || $spc eq ""|| $lib eq ""|| $clk eq "" || $module eq "") {
  print STDERR "-E- Found missing/excess arguments\n";
  printErrMessage();
  exit(1);
}

#Getting job start time
chomp($date=`date`);
print "\t*******    Job started   at $date    **********\n";

#Initializing the parameters
$sim="reference_spice.sp";
@sub_ckt="";
$dnum=1;
$vdd=1.8;
$idd=2.2;
$flag=0;


use File::Path qw(mkpath);
mkpath("spice_results");


#opening the required files
open(SPC,"$spc")||die("unable to open file : $!");
open(VLOG,"$vlog")||die("unable to open file : $!");
open(SIM,">$sim");

#This is required when we combine the spice simulation outputs and write out to a single file with this header
open(RES,">./spice_results/headers.csv")||die("unable to open file : $!"); 

#
#Definig the technology dependent parameters
$vdd=1.8;
$idd=2.2;
if($tech==180)
  {
    $vdd=1.8;
    $idd=2.2;
  }
elsif($tech==130)
  {
    $vdd=1.5;
    $idd=1.8;
  }
elsif($tech==90)
  {
    $vdd=1.2;
    $idd=1.5;
  }
elsif($tech==65)
  {
    $vdd=1.1;
    $idd=1.2;
  }
elsif($tech==45)
  {
    $vdd=1.0;
    $idd=1.0;
  }
elsif($tech==32)
  {
    $vdd=0.9;
    $idd=0.8;
  }
elsif($tech==22)
  {
    $vdd=0.8;
    $idd=0.6;
  }

#including the library files
print SIM "****Template spice file***"."\n\n";
print SIM ".include ../".$lib."\n";
print SIM '**.include /cad/digital/rtl2gds/rtl2gds_install/LIB/lib/tsmc018/lib/tsmc018.m'."\n";
print SIM '.include ../tsmc018.m'."\n\n";
print "\t******Giltched version of the library file and technology file included in the spice file\n";


print SIM "**********Subckt begins*********"."\n\n";

#parsing the verilog file
while(<VLOG>)
 {  
   
   if(($_=~m/^ *input/)||($_=~m/^ *output/)) #Extracting the input and output from the verilog code
     {
        chomp($_);
	chop($_);
	@temp=split(" ",$_);
	$type=shift(@temp);
	foreach $i(0..$#temp)
	   {
		if(!($temp[$i]=~m/.*[.*:.*].*/))
		  {
                     if(($type eq "input") || ($type eq "inout"))
			{
			  $inputs[$j++]=$temp[$i];
			}
		     elsif($type eq "output")
			{
			  $outputs[$k++]=$temp[$i];
			}
		  }
	   }
	
     }
}

  
print "\n\t********** Input output of the RTL file extracted\n";

#Parsing the spice file
while(<SPC>)
 {  
   
   if(!($_=~m/ FILL$/)&&!($_=~m/^\*/))# removing the fills and comments
     {
	$new=$_;
	$new=~s/\[/_/g;
	$new=~s/\]/_/g;
	$new=~s/\//_/g;
	$new=~s/\//_/g;
	print SIM $new;
     }
        
    if(($_=~m/^x.*/i)&&(!($_=~m/ FILL$/)))
       {
        #print $_;
	chomp($gates[$i++]=$_);	
	$flag=1;
	$in=1;
      }
    if(($_=~m/^\+.*/i))
       {
         if($flag==1)
            {
	     chomp($tail=$_);
	     $tail=~s/\+//;
	     $gates[$i-1].=$tail;
	     
	    }
       }
    
  #print join("\n",@gates);
   if(/.SUBCKT/../Net Section/) #extracting the subcircuit
     {
        if(!(($_=~m/.SUBCKT/)||($_=~m/Net Section/))&&($_=~m/\+/))
         {
           $new=$_;
	   $new=~s/\[/_/g;
	   $new=~s/\]/_/g;
	   $new=~s/\//_/g;
	   $new=~s/\//_/g;
	   $sub_ckt[$i++]=$new;
	   $pin=$_;
           $pin=~s/\+ //;
	   @temp=split (" ",$pin);
           push @pins ,@temp;
         }
     
      }
   if($_=~m/.SUBCKT/) # Capturing the name of the subcircuit
     {
	$new=$_;
	$new=~s/\[/_/g;
	$new=~s/\]/_/g;
	$new=~s/\//_/g;
	$new=~s/\//_/g;	
	($temp,$s_name)=split(" ",$new);
     }
}

#instantiating the sub circuit

print SIM "\n\n******Simulation parameters*****"."\n\n";


#including the user defined clock information

$clk_period = (1/$clk)*(0.000001);
$sim_time=2.5*$clk_period;#defining simulation time
$fall_from=(2*$clk_period); #defining fall time window
$fall_to= 2.2*$clk_period;

#$half_clk_period=$clk_period/2;
#$double_clk_period=2*$clk_period;
#$change_time=$half_clk_period/3;
#$end_PWL= $half_clk_period+$change_time;


#Declaring the param statements in sice file

print SIM "****Param definitions***"."\n";

print SIM ".param clk_period= '(1/$clk)*(0.000001)' \n"; 
print SIM "+half_clk_period= '(clk_period/2)'\n";
print SIM "+double_clk_period= '(clk_period*2)'\n\n";


print SIM ".param fall_from_value=$fall_from\n"; 
print SIM "+ fall_to_value=$fall_to\n\n";

print SIM ".param init_delay = half_clk_period\n";
print SIM "+ rise_time= 50p\n";
print SIM "+ fall_time= 50p\n\n";


print SIM ".param change_time='(half_clk_period/3)'\n";
print SIM ".param end_PWL= '(half_clk_period + change_time)'\n";
print SIM "+end_PWL_rise = \'(end_PWL + 100ps)\'\n\n";

print SIM ".param current_magnitude = $idd";
print SIM "mA\n";
#Adding the glitch information
#Dont leave a space after the glitch_location_time and ns
print SIM "+rise_delay= ##glitch_location##s\n";
print SIM "+fall_delay= \'rise_delay+5p\'\n";
print SIM "+rise_time_constant = 1ps\n";
print SIM "+fall_time_constant=130ps\n\n";


#defining global pins
print SIM '.GLOBAL vdd VDD'."\n\n";
print SIM "Vvdd vdd 0 $vdd\n";

#clock period
##print "Clock period".$clk_period."\n";
print SIM "VCk  clk   0  PULSE(0 $vdd init_delay rise_time fall_time half_clk_period clk_period)\n\n";

print SIM "\n\n******Instantiating the subckt*****"."\n\n";

chomp($sub_ckt[$#sub_ckt]);
$sub_ckt[$#sub_ckt].=" $sname";
print SIM "X$s_name\n";
print SIM join("",@sub_ckt);
print SIM $s_name;

print SIM "\n\n******Done instantiating the subckt*****"."\n";

print "\t*************Fills removed from the spice file\n";
print "\t*************Sub circuit instantiated in the spice file\n";

#classifying the pins as input and output pins

foreach $i (0..$#pins)
 {
   $flag=0;
   foreach $j (0..$#outputs)
     {
	$pin=$pins[$i];
	$pin=~s/\[.*\]//;
	if($pin eq $outputs[$j])
	   {
		$flag=1;
		push @opins ,$pins[$i];       
		last;
           } 
     }   
        if($flag==0)
	   {
		push @ipins ,$pins[$i];
	   }
    
 } 

#print "\nthe following are the input pins\n";
#print join("\n",@ipins);
#print "\nthe following are the output pins\n";
#print join("\n",@opins);
$measure_at_rising_edge="";
foreach $g(0 .. $#gates)
  {
   if(($gates[$g]=~m/DFF/)||($gates[$g]=~m/LATCH/))
   {
     $gates[$g]=~m/:Q (.*:D) /;
	push @dffipin, $1;
  
   }
  }
 
#Initializing the inputs 

foreach $i(0 .. $#ipins)
 {
   $new=$ipins[$i];
   $new=~s/\[/_/g;
   $new=~s/\]/_/g;
   $new=~s/\//_/g;
   #print $new;

   if($new ne "clk")
   {
     print SIM "\n\nV$i $new 0 PWL( 0 ##$new\_reference_1## end_PWL ##$new\_reference_1## end_PWL_rise ##$new\_reference_2## $sim_time ##$new\_reference_2##)\n";
   }
}

 print SIM "\n**Initialising input of FFs- not used currently\n";
foreach $i(0 .. $#dffipin)
 {
   $new=$dffipin[$i];
   $new=~s/\[/_/g;
   $new=~s/\]/_/g;
   $new=~s/\//_/g;
   if($new ne "clk")
   {
      print SIM "**.ic v($new)= ##$new\_reference_1##\n";
   }
}

##Initialise primary outputs
 print SIM "\n**Initialising primary outputs\n\n";
foreach $i(0 .. $#opins)
 {
   $new1=$opins[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
      #print SIM ".ic v($new1)= ##$new1\_reference_1##\n";
	print SIM ".ic v($new1)= 0\n";
   }
}




$measure_at_falling_edge="";
foreach $i(0 .. $#opins)
 {
   $measure_at_falling_edge.="meas tran $opins[$i]_voltage MAX v($opins[$i]) from=$fall_from"."s"." to=$fall_to"."s\n";
 }

#Adding the control part
print SIM "\n\n.control\n";
print SIM "tran 10ps ".$sim_time."s\n\n";
print SIM "**Uncomment the following and run this spice file, if you need a waveform\n";
print SIM "**write waveform_file.raw v(clk) v(input_dec_2_) v(input_dec_1_) v(input_dec_0_)  v(output_dec_3_) v(output_dec_1_) \n*+v.xdecoder_behav_pnr.xu11.vcharge#branch \n\n";

print SIM "**************************** Measuring Flip Flop output at falling edge *************************************************\n";
$measure_at_falling_edge=~s/\[/_/g;
$measure_at_falling_edge=~s/\]/_/g;
$measure_at_falling_edge=~s/\//_/g;
print SIM $measure_at_falling_edge;
print SIM "\n\n***************** saving the outputs ****************\n";
#print SIM "echo deck_##deck_num## , ";
print SIM "echo ";
##Still printing the echo statement
foreach $i(0 .. $#opins)
 {
   $new=$opins[$i];
   $new=~s/\[/_/g;
   $new=~s/\]/_/g;
   $new=~s/\//_/g; 
  print SIM '"$&'.$new."_voltage\" , ";
 } 
print SIM '> glitch_report_outputs_'."##deck_num##.csv".'  $$New file'."\n";
print SIM "\nquit\n\n";
print SIM ".endc\n\n\n";
print SIM ".end\n";


##Printing headers to the csv file in spice_decks/results
#print RES "deck_##deck_num## , ";
##Still printing to the RES file
foreach $i(0 .. $#opins)
 {
   $new1=$opins[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
      print RES "$new1".",";
   }
}
print RES "\n";



$num=@opins;
print SIM "\n** NUMBER OF OUTPUT PINS = $num";


print "\t********control statement written in the spice file\n";
#closing the files
close(SPC);
close(out);
chomp($sim1=`pwd`);
$sim1=$sim1."/$sim\n";
print "\n SPICE FILE written named ".$sim."\n";
#creating the toplevel csv file
open(IM,">./$module\_reference_out/RTL.csv");
print IM 'deck_num,clk,glitch,';
foreach $i(0 .. $#opins)

 {
   $new1=$opins[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
      if ($i == $#opins) 
	{
	print IM "$new1";
	} 
	else 
	{
	print IM "$new1".",";
	}

	
   }
}

close(IM);

open(IM2,">./$module\_reference_out/RTL_backup.csv");
print IM2 'deck_num,clk,glitch,';
foreach $i(0 .. $#opins)
 {
   $new1=$opins[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
       if ($i == $#opins) 
	{
	print IM2 "$new1";
	} 
	else 
	{
	print IM2 "$new1".",";
	}

   }
}

close(IM2);



