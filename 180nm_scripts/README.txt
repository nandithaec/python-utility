Code changes from Oct 21 2014

spice library osu018_stdcells_correct_vdd_gnd.sp assumed to be in your scripts folder
execute the script "utility_python_top_level.py" in your lab mc.
Copy scripts and design folder to CDAC cluster
Execute the jobscript.txt- this runs "python_utility_step2_yuva.py" on the cluster

Changes:
perl_spice_netlist_format.pl:
#Automated the flip-flop type selection in meas statements and module instantiation of .ic statement (q_reg) for ISCAS and non-ISCAS benchmarks: Oct 21 2014 


perl_glitchLibGen.pl - #Removed #($dlist=~m/$drain/)|| option - Oct 21 2014

python_run_qrc_spice_extraction.py - #Added the path to the output file -file_name - Oct 21 2014
