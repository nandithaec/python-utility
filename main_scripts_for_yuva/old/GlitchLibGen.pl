#Example: perl GlitchLibGen.pl -i osu018_stdcells_correct_original.sp

#!/usr/bin/perl
use Getopt::Long;
#####################################################################
#
# Author        : Shahbaz Sarik
# Date          : 7th February 2013
# Purpose       : To create a glitch introduced library of a given
#                 spice library 
#                 
# Copyright	: IIT BOMBAY
####################################################################

#  Routine to print Error message
sub printErrMessage {

 print "GlitchLibGen ERROR: BAD SYNTAX\n";
 print "TRY '$0 -h' or '$0 --help'  for help\n";
}
#  Routine to print man page
sub printManPage {
  print STDERR <<END; 
    
GlitchLibGen(1)                                                                                  

NAME

GlitchLibGen − Utility to create a glitch induced version of a spice library.

SYNOPSIS

GlitchLibGen [input library file]  

DESCRIPTION

GlitchLibGen utility takes a spice library (sp file containing standard cells), say, <std_cell>.sp as input and creates a glitched induced library where each subciruit has different version, each version has glitch induced to one of its distinct drain excluding Vdd and gnd. The output of this file is glitch_<std_cell>.sp in the current working directory.

OPTIONS

 
Input library file

-i |--input = <input library>.sp- which contains std cells (subckts) in spice format

This file should be the spice library whose glitched version is to be created.


Examples:

perl GlitchLibGen.pl -i osu018_stdcells_correct_original.sp

SEE ALSO

SPICE.

AUTHOR
Shahbaz sarik (shahbaz\@ee.iitb.ac.in)

This utility has been written for the “ Impact of soft error on circuit” experiment carried out under the guidence of Prof. Madhav. P. Desai (madhav\@ee.iitb.ac.in) at IITBombay.

COPYRIGHT
GPL IIT-Bombay
GlitchLibGen January 3rd February 2013  
    
    
END
}

#  Get the command line arguments
#  check for missing/extra arguments and show usage

GetOptions( #"o|output=s"=>\$glib,
            "i|input=s"=>\$library,
            "h|help"=>\$help
          );
      
if ($help) {
  printManPage();
  exit(0);
}
$glib="glitch_".$library;
if ($#ARGV >= 0 || $glib eq "" || $library eq "" ) {
  print STDERR "-E- Found missing/excess arguments\n";
  printErrMessage();
  exit(1);
}
#Getting job start time
chomp($date=`date`);
#$log=$0."_run_".$date.".log";
print "\t\t**********    Job started   at $date    **********\n";

#opening the required files
open(NET,"$library")||die("unable to open file : $!");
open(out,">$glib");
#open(logf,">$log");
print  out "*"x10;
print  out " Glitched induced version of LIBRARY : $library ";
print  out "*"x10;
print  out "\n\n\n";

#intializing the variables
@sub_ckt="";
$drain_num=0; 
$drain="";
$sub_ckt_num=0;
$index=0;
$sub_ckt_name="";
$info="\n\n**** SUBCIRCUIT\t\t|VERSION COUNT\n-----------------------------------------\n";

#capturing the subcircuits from the library
while(<NET>)
 {  
   if(/.subckt/ .. /.ends/)
     {
       $sub_ckt[$index++]=$_;
       if($_=~m/.subckt/)
         {
	   ($temp,$sub_ckt_name)=split(" ",$_);  
	 }
     }
#creating the glitched version of a subcircuit and writing it to output file
   else
     {
       if($index!=0)
	 {
	   $index=0;
	   $sub_ckt_num++;
	   print out "\n******************************* ORIGINAL SUBCIRCUIT : $sub_ckt_name ******************************* \n\n";
	   print out join("",@sub_ckt);
	   $head=shift (@sub_ckt);
           $tail=pop (@sub_ckt);  
	   #print "Working on subcircuit : $sub_ckt_num :$sub_ckt_name \n";
#obtaining the distinct drain of the subcircuit
           foreach $i (0 .. $#sub_ckt)
	     {
	       
	       $glitch_sub_ckt=join("",@sub_ckt);
	       if($sub_ckt[$i]=~m/^M\d* /)
	         {
		    ($temp,$drain)=split(' ',$sub_ckt[$i]);
	             
		     if(!(($dlist=~m/$drain/)||($drain=~m/gnd/)||($drain=~m/vdd/i)||($drain=~m/0/)))
		       {			                   
			$dlist.=" $drain";
		        $drain_num++;
			if($head=~s/$sub_ckt_name\_\d+/$sub_ckt_name\_$drain_num/)
                         {
                         }
			else
                         {
			  $head=~s/$sub_ckt_name/$sub_ckt_name\_$drain_num/;                         
                         }			
			$tail=~s/$sub_ckt_name.*/$sub_ckt_name\_$drain_num/;
			chomp($drain);
#introducing glitch into the selected drain
                        $i="Icharge 0 $drain EXP (0 current_magnitude rise_delay rise_time_constant fall_delay fall_time_constant)\n";
			$glitch_sub_ckt=$head.$i.$glitch_sub_ckt.$tail;
#writing the glitch introduced subcircuit to output file
			print out "\n****** $sub_ckt_name : Glitched version $drain_num : glitch at $drain ******\n";                      
			print out "\n$glitch_sub_ckt";
			$count++;
                       }  
		      $drain="";			               
		 }
	     }
#collecting the information about the subcircuits
	   $info=$info."**** $sub_ckt_name\t\t|\t$drain_num\n";
	   $head="";
           $tail="";
	   @sub_ckt="";
	   $sub_ckt_name="";
	   $drain_num=0;
           $dlist="";
	   $sub_ckt_name="";
	   print out "\n";			
	 }
      }
 } 
#writing the information to output and displaying the completion message
chomp($date=`date`);  
print "\t\t**********    Job completed at $date    **********\n";
print "\t\t\t*************** !! RUN SUCESSFULL !! ****************\n";
chomp($path = `pwd`);
print "*********Glitch intoduced library '$glib' created at $path/$glib\n";
print out "\t\t**************************************** LIBRARAY INFORMATION ****************************************\n";
print out " **** This Library contains $sub_ckt_num glitch free Subcircuits \n";
print out " **** This Library contains $count glitch affected Subcircuits \n";
print out " **** Following are the details of these Subcircuits\n";
print out $info;
print out "*"x60;
print out " END ";
print out "*"x60; 
close(NET);
close(out);

