
$nextline= ".Q(din_1[5])";
  if(($nextline=~m/Q\((.+)\)/))
 {
    print "Match1\n" ;
    print "$1 \n $'\n"
}

 if(($nextline=~m/Q\(\)/))
 {
    print "Match2\n" ;
    print "$'\n"
}



$text = " quick brown fox jumps over the lazy dog.";
$text =~ m/ (q.+?) /;
print "$1\n";

