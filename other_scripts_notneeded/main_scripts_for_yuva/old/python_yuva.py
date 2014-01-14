import os

os.system("seq 1 10| /opt/parallel-20130422/bin/parallel --progress -j +0 --sshloginfile /home/external/iitb/nanditha/c499_ecat_yuva/sshmachines.txt 'cd /home/external/iitb/nanditha/c499_ecat_yuva/spice_decks_1; pwd; /home/external/iitb/nanditha/ngspice-25/bin/ngspice /home/external/iitb/nanditha/c499_ecat_yuva/spice_decks_1/deck_{}.sp;pwd;'")
