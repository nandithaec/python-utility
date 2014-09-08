
$subckt="sfd ad=09p \n";
print "$subckt";
($drain_area)=$subckt =~ m/ ad=(.*)p /;
print "$drain_area\n";


$n = "Price 15.40";
print "$n\n";
$n =~s/[^\d.]//g; 
print "$n\n";

#$text ="adsfsdf AD=0.06p enj kj\n";
$text = "MMM96 Z:F21 B:F22 gnd gnd NSVTGP ad=0.044p as=0.09375p L=0.06u NRD=0.25 NRS=24.8331 PD=0.2u PS=1.11667u W=0.44u lpe=3 ngcon=1 po2act=0.404753 sca=9.58143 scb=0.0105142 scc=0.000771748\n";
print "$text";
#($temp,$content) = $text =~ m/ (ad=|AD=)(.*) (AS|as)/;
($temp,$content) = $text =~ / (ad=|AD=)(.*?) /;
print "$2 \n$content \n";


