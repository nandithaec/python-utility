#!/usr/bin/perl
#Example usage: perl modperl2_outwrtr_new.pl -v pnr/op_data/c499_clk_opFF_final.v -m c499_clk_opFF

#Modifications:
#Code modified backto write out.. not all inputs of DFFs to modelsim file, but only all the outputs - Oct 21
#Code modified to write out fwrite statements to the modelsim verilog file for all inputs of all FFs(pos edge) and write out headers of all inputs to the tool_reference_out.txt  - Oct 11 2013
#RTL and spice headers were being written in Netlstfrmt.pl. Now, they are being written in this script (much better) - Oct 8 2013

use Getopt::Long;
#####################################################################
#
# Author        : Shahbaz Sarik
# Date          : 7th February 2013
# Purpose       : To modify the post PNR verilog file so as to make 
#                 it capable of writing Flip-flop output to external
#                 file
# Copyright	: IIT BOMBAY
####################################################################

#  Routine to print Error message
sub printErrMessage {

 print "outwrtr ERROR: BAD SYNTAX\n";
 print "TRY '$0 -h' or '$0 --help'  for help\n";
}
#  Routine to print man page
sub printManPage {
  print STDERR <<END; 
    
outwrtr(1)                                                                                  

NAME
modperl2_outwrtr - To modify the post PNR verilog file so as to make it capable of writing Flip-flop output to external file

SYNOPSIS

modperl2_outwrtr [post pnr .v file]  [top module name]

DESCRIPTION

outwrtr utility takes a post PNR verilog file from pnr/op_data/<module>_final.v and the top module name of the design as input and creates a verilog file with name as <module_name_modelsim.v> and a reference output directory<post_pnr_.v_file_refrence_out>. The module_name_modelsim.v is a modified version of the post pnr .v file which contains File I/O statements to write out the inputs of all Flip flops at teh positive edge of the clk cycles, and the output of the flip flops at teh negative edge of teh clk cycle. These outputs are written out to the tool_reference_out.txt file and our_reference_out.txt files in the post_pnr_.v_file_reference_out directory. The tool_reference_out.txt file contains a header (inputs and outputs), and rows containing 0's and 1's for each clk cycle. This will be used later while comparing spice outputs. The our_reference_out.txt file contains the same information in a more readable format, so that this file can be used to validate against the actual modelsim simulation.

OPTIONS
 
Input library file

-v|--verilog = <file name> :This file should be the post pnr .v file of the design.

-m|--module = <name> : This should be the top module name of the design.


Examples:

perl modperl2_outwrtr.pl -v pnr/op_data/decoder_behav_pnr_final.v -m decoder_behav_pnr

SEE ALSO
SPICE.

AUTHOR
Shahbaz sarik (shahbaz\@ee.iitb.ac.in)

This utility has been written for the “ Impact of soft error on circuit” experiment carried out under the guidence of Prof. Madhav. P. Desai (madhav\@ee.iitb.ac.in) at IITBombay.

COPYRIGHT
GPL IIT-Bombay
outwrtr 3rd February 2013  
    
    
END
}

#  Get the command line arguments
#  check for missing/extra arguments and show usage

GetOptions( "v|verilog=s"=>\$vlog,
	    "m|module=s"=>\$module,
            "h|help"=>\$help
          );
      
if ($help) {
  printManPage();
  exit(0);
}

if ($#ARGV >= 0 || $vlog eq "" || $module eq "" ) {
  print STDERR "-E- Found missing/excess arguments\n";
  printErrMessage();
  exit(1);
}

#Getting job start time
chomp($date=`date`);
print "\t\t**********    Job started on $date    **********\n";

#Initializing the parameters
$flag=0;
$op=$module."_modelsim.v";
$in_main_module=0;
$ref=$module."_reference_out";
`mkdir $ref`;
#opening the required files
open(VLOG,"$vlog")||die("unable to open file : $!");
open(OPT,">$op")||die("unable to open file : $!");
#This file REF (our_reference.txt is just created. Nothing is written to through this script.
#The modelsim.v file will write to this file when simulated
open(REF,">./$ref/our_reference_out.txt")||die("unable to open file : $!");
open(OUT_FF,">./$ref/ff_oppins.txt")||die("unable to open file : $!");
open(TOOLREF,">./$ref/tool_reference_out.txt")||die("unable to open file : $!");
use File::Path qw(mkpath);
mkpath("spice_results");

#Parsing the post pnr verilog file
while(<VLOG>)
 {  
   
   if(($_=~m/module $module \(/ .. /endmodule/)) #parsing the main module only
     {
	 $in_main_module=1;
	 if(($_=~m/DFF/)||($_=~m/LATCH/)||($flag==1)) #searching for flip flop and latches
	    {
		if($flag == 0)
		   {
                     ($fftype,$ffname,$pin)=split(" ",$_);#capturing the output pin of the flip flop
		     $pin=~m/\(.*\((.*)\)/;
		     $ffopin[$i++]=$1;#this array has all output pins of all FFs
		     $flag=1;
		   }
                else
		   {
                     $_=~m/.*\((.*)\)/; #capturing the input pin of the flip flop
		    # $ffipin[$j++]=$1; #captures input pins of all FFs. If you comment this out, uncomment push @ffipin,@ipin; this will capture inputs of only input FFs
		     $flag=0;
		   }
	    }
	#capturing the input ports of the main module
       if($_=~m/ *input /)
	    {
		
		if($_=~m/ *input \[(.*):(.*)\] (\d*)/)#capturing vector input such as name[0:3] etc to break up the input names
		  {				
			$m=$1+$2;		     
			($t1,$t2,$t3)=split(" ",$_);
			chop($t3);
			while($m>=0)
			 {
			   $pn=$t3."[$m]";
			   push @ipin,$pn;
			   $m--;
			 }
             	  }
		else
		  {
			($t1,$t2)=split(" ",$_);#capturing non vector input
			chop($t2);
			if($t2 ne "clk")
			  {
			     push @ipin,$t2;
			  }
		  }
		
	    }
	    
   # Capturing the outputs of the main module
	    if($_=~m/ *output /)
	    {
		
		if($_=~m/ *output \[(.*):(.*)\] (\d*)/)#capturing vector input
		  {				
			$m=$1+$2;		     
			($t1,$t2,$t3)=split(" ",$_);
			chop($t3);
			while($m>=0)
			 {
			   $pn=$t3."[$m]";
			   push @opin,$pn;
			   $m--;
			 }
             	  }
		else
		  {
			($t1,$t2)=split(" ",$_);#capturing non vector input
			chop($t2);
			if($t2 ne "clk")
			  {
			     push @opin,$t2;
			  }
		  }
		
     }
 } #ending if module

#copying the file into the new .v file
   if(($in_main_module==0)||(!($_=~m/endmodule/)))
      {
        print OPT $_;
      }
#Adding reference output generating statements
    else
      {
        print OPT "//************************* CODE APPENDED TO ORIGINAL .v FILE STARTS FROM HERE *************************\n";
        print OPT 'integer fileout;'."\n";
	print OPT 'integer clk_count = 0;'."\n";
	print OPT 'integer fileout1;'."\n";
	print OPT 'integer clk_count1 = 0;'."\n";
	print OPT 'initial'."\n";
	print OPT 'begin'."\n"; 
	print OPT 'fileout= $fopen("./'.$ref.'/our_reference_out.txt","a+");'."\n";
	print OPT 'fileout1= $fopen("./'.$ref.'/tool_reference_out.txt","a+");'."\n";
	print OPT 'end'."\n";
#Writing output of flip flop at negative edge
	print OPT 'always @(negedge clk)'."\n";
	print OPT 'begin'."\n";
	
#Merging the output pins which are not the output pin of any flip flop
    #$c_pins = join(" ",@ffopin);
    $limit = $#ffopin;	
    foreach $j(0 .. $#opin)
      {  
		  $match=0;
		  foreach $l(0 .. $limit)
		     {
				 if($opin[$j] eq $ffopin[$l])
	               {
		               $match=1;
		            }
		      }
		   if($match==0)
		      {
				  #print "\n$opin[$j]\n";
				  push(@ffopin,$opin[$j]);
			  }
      }		        
     	
	foreach $i(0 .. $#ffopin)
		{
		  print OPT '$fwrite(fileout,"'.$ffopin[$i].' = %b\n", '.$ffopin[$i].");\n";
		  print OPT '$fwrite(fileout1,"%b ", '.$ffopin[$i].");\n";
		}
	print OPT '$fwrite(fileout,"\n");'."\n";
	print OPT '$fwrite(fileout1,"\n");'."\n";
	print OPT '$fwrite(fileout,"%d CLOCK CYCLE ENDS   :SIGNAL VALUES AT THIS POINT \n\n",clk_count);'."\n";
	print OPT '$fwrite(fileout,"***********************************************************************************************************\n\n");'."\n";			
	print OPT 'end'."\n";
	print OPT 'always @(posedge clk)'."\n";
	print OPT 'begin'."\n";
        print OPT 'clk_count=clk_count+1;'."\n";
	print OPT '$fwrite(fileout,"%d CLOCK CYCLE STARTS :SIGNAL VALUES AT THIS POINT \n\n",clk_count);'."\n";
	push @ffipin,@ipin;
	foreach $i(0 .. $#ffipin)
		{
		  print OPT '$fwrite(fileout,"'.$ffipin[$i].' = %b\n", '.$ffipin[$i].");\n";
		  print OPT '$fwrite(fileout1,"%b ", '.$ffipin[$i].");\n";
		}
	print OPT 'end'."\n"; 
	print OPT $_;
   }

 }
push @pin, @ffipin;
push @pin, @ffopin;
foreach $i (0 .. $#pin)
	{
	   $pin[$i]=~s/\[/_/;
	   $pin[$i]=~s/\]/_/;
	   $pin[$i]=~s/\//_/;
	   $pin[$i]=~s/\//_/;
	}
#Printing the header (pin names) in the tool reference output header
print TOOLREF join(" ",@pin);
print TOOLREF "\n";
#printing exit message
print "\t\t\t\t\t************************\n";
print "\t\t\t\t\t*                      *\n";
print "\t\t\t\t\t*  !!RUN SUCCESSFUL!!  *\n";
print "\t\t\t\t\t*                      *\n";
print "\t\t\t\t\t************************\n";
print "***MODELSIM simulatable file \" $op \" created in the current directory\n";
print "***Reference output file ./$ref/tool_reference_out.txt and /$ref/our_reference_out.txt created sucessfully\n";

#both the for loops do the same thing
#foreach $pp(@ffopin)
# {
#  print OUT_FF "$pp,\n";
# }

#Just a temp file that contains all FF output names
foreach $i(0 .. $#ffopin)
{
  $new1=$ffopin[$i];
  print OUT_FF "$new1".",";

}


#creating the toplevel csv file - which contains the RTL headers
#ffopin contains outputs of all DFFs
open(IM,">./$module\_reference_out/RTL.csv");
print IM 'deck_num,clk,glitch,gate,subcktlinenum,';
foreach $i(0 .. $#ffopin)

 {
   $new1=$ffopin[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
      if ($i == $#ffopin) 
	{
	print IM "$new1";
	} 
	else 
	{
	print IM "$new1".",";
	}

	
   }
}

## Not sure if this is needed
print IM "\n";
close(IM);

#Backup header file required later
open(IM2,">./$module\_reference_out/RTL_backup.csv");
print IM2 'deck_num,clk,glitch,gate,subcktlinenum,';
foreach $i(0 .. $#ffopin)
 {
   $new1=$ffopin[$i];
   $new1=~s/\[/_/g;
   $new1=~s/\]/_/g;
   $new1=~s/\//_/g;
   if($new1 ne "clk")
   {
       if ($i == $#ffopin) 
	{
	print IM2 "$new1";
	} 
	else 
	{
	print IM2 "$new1".",";
	}

   }
}

## Not sure if this is needed
print IM2 "\n";

close(IM2);
print "RTL headers RTL.csv and RTL_backup.csv created inside the $module_reference_out directory\n";


##Printing spice headers to the csv file in spice_results/
#This is required when we combine the spice simulation outputs and write out to a single file with this header
open(RES,">./spice_results/headers.csv")||die("unable to open file : $!"); 

#foreach $i(0 .. $#to_ff)
# {
#   $new="ff_op_".$i;
 #  $new1=~s/\[/_/g;
 #  $new1=~s/\]/_/g;
 #  $new1=~s/\//_/g;
#   if($new ne "clk")
#   {
#      print RES "$new".",";
#   }
#}


foreach $i(0 .. $#ffopin)
{
  $new1=$ffopin[$i];
  print RES "$new1".",";

}


print RES "\n";

close(RES);
print "Spice header file spice_results/headers.csv created\n";


close(VLOG);
close(OPT);
close(REF);
close(TOOLREF);


