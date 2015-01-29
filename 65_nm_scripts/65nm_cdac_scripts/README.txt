Usage:

You need to have the spice library file “CORE65GPSVT_all_vdd_gnd_WL_ad_noR.txt” one level up from your scripts folder, to generate the glitch library. 

Copy the hspice_65nm_models directory from this directory to your design directory

Have your design (vhd) file and test bench in a design folder

Copy all the scripts in the “65nm_cdac_scripts” to a directory.

cd to the scripts directory and run the script “utility_python_top_level_yuva_65.py” on the vlsi lab machine- to generate the spice reference file. Three example usages are given inside the script itself (at the beginning)

Now, copy your design folder to Pune CDAC cluster. I suggest that you do not copy the directory named ‘work’ created by modelsim (its size is huge and takes a long time to copy)

Modify the parameters in the jobscript.txt. Before launching thousands of jobs, do a test-run with just few jobs- say 4 to 5. This text file will run the script “python_utility2_ngspice_yuva_65.py” on the cluster


Changes done to scripts:

perl_spice_netlist_format_noR_65.pl script updated- .ic statements: Oct 24 2014 

utility_python_top_level_yuva_65.py: #Created a parameter scripts_path - Oct 20 2014
python_utility2_ngspice_yuva_65.py: #Created a parameter scripts_path - Oct 20 2014

perl_glitchLibGen_65.pl: #The condition of distinct drains is removed: (($dlist=~m/$drain/) is deleted : Oct 20 2014

perl_spice_netlist_format_noR_65.pl script is updated: #updated all .ic statements with new initialisation node names. DFPQX4 and DFPQX9 have different .ic node names- Oct 20 2014

python_create_jobscript_65.py: #Updated with scripts_path: Oct 20 2014


python_FF_strike_taxonomy_65.py and python_gate_strike_taxonomy_65.py : #Added few if conditions to solve zero division error: Oct 18 2014

python_combine_pdfs_yuva_65.py created: Oct 18 2014
