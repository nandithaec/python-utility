Usage:

You need to have the spice library file “CORE65GPSVT_all_vdd_gnd_WL_ad.txt” one level up from your scripts folder, to generate the glitch library. 

Have your design (vhd) file and test bench in a design folder

Copy all the scripts in the “65_nm_scripts” to a directory.

cd to the scripts directory and run the script “utility_python_top_level_65.py” on the vlsi lab machine- to generate the spice reference file. Three example usages are given inside the script itself (at the beginning)

Now, copy your design folder to Pune CDAC cluster. I suggest that you do not copy the directory named ‘work’ created by modelsim (its size is huge and takes a long time to copy)

Modify the parameters in the jobscript.txt. Before launching thousands of jobs, do a test-run with just few jobs- say 4 to 5. This text file will run the script “python_utility2_hspice_2cycles_time0_65.py" on the lab machine to run hspice


Changes done to scripts:

perl_spice_netlist_format_65.pl script updated- .ic statements: Oct 24 2014 

