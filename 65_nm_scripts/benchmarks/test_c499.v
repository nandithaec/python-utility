
`timescale 1ns/100ps

module test_c499;
  //(clk, reset, go,in_addr, mem_in, io_in, mem_out, io_out,s1s0, adr_15to8, ad7_0, io_mbar, in_rd_wrbar, rd_bar, wr_bar,rdy, ALE, current_tstate);

//inputs as reg and o/ps as wires, inout as reg

reg clk,PNN1,PNN5,PNN9,PNN13,PNN17,PNN21,PNN25,PNN29,PNN33,PNN37,
      PNN41,PNN45,PNN49,PNN53,PNN57,PNN61,PNN65,PNN69,PNN73,PNN77,
      PNN81,PNN85,PNN89,PNN93,PNN97,PNN101,PNN105,PNN109,PNN113,PNN117,
      PNN121,PNN125,PNN129,PNN130,PNN131,PNN132,PNN133,PNN134,PNN135,PNN136,
      PNN137;


c499_clk_ipFF  u1 (clk,PNN1,PNN5,PNN9,PNN13,PNN17,PNN21,PNN25,PNN29,PNN33,PNN37,
             PNN41,PNN45,PNN49,PNN53,PNN57,PNN61,PNN65,PNN69,PNN73,PNN77,
             PNN81,PNN85,PNN89,PNN93,PNN97,PNN101,PNN105,PNN109,PNN113,PNN117,
             PNN121,PNN125,PNN129,PNN130,PNN131,PNN132,PNN133,PNN134,PNN135,PNN136,
             PNN137,
	     Q_PNN724,Q_PNN725,Q_PNN726,Q_PNN727,Q_PNN728,Q_PNN729,Q_PNN730,Q_PNN731,Q_PNN732,
             Q_PNN733,Q_PNN734,Q_PNN735,Q_PNN736,Q_PNN737,Q_PNN738,Q_PNN739,Q_PNN740,Q_PNN741,Q_PNN742,
             Q_PNN743,Q_PNN744,Q_PNN745,Q_PNN746,Q_PNN747,Q_PNN748,Q_PNN749,Q_PNN750,Q_PNN751,Q_PNN752,
             Q_PNN753,Q_PNN754,Q_PNN755);
 
parameter period = 20; //20ns = clk period


//initialise all inputs to zero
initial
begin

clk = 0;
PNN1  = 0;
PNN5  = 0;
PNN9  = 0;
PNN13 = 0;
PNN17 = 0;
PNN21 = 0;
PNN25 = 0;
PNN29 = 0;
PNN33 = 0;
PNN37 = 0;
PNN41 = 0;
PNN45 = 0;
PNN49 = 0;
PNN53 = 0;
PNN57 = 0;
PNN61 = 0;
PNN65 = 0;
PNN69 = 0;
PNN73 = 0;
PNN77 = 0;
PNN81 = 0;
PNN85 = 0;
PNN89 = 0;
PNN93 = 0;
PNN97 = 0;
PNN101 = 0;
PNN105 = 0;
PNN109 = 0;
PNN113 = 0;
PNN117 = 0;
PNN121 = 0;
PNN125 = 0;
PNN129 = 0;
PNN130 = 0;
PNN131 = 0;
PNN132 = 0;
PNN133 = 0;
PNN134 = 0;
PNN135 = 0;
PNN136 = 0;
PNN137 = 0;

end
  


  always begin

 #(period/2) clk= ~clk; //1ns(timescale) * 100 = 100ns= half period
 
  end

always begin

 #(period*4)  PNN1 = ~PNN1; //invert after duration=period
 #period PNN5 = ~PNN5; //this delay will be wrt the previous time and not wrt time 0

 #(period*2) PNN21 = ~PNN21;
 #period PNN9 = ~PNN9;
 #(period*2) PNN17 = ~PNN17;
 #(period*2) PNN13 = ~PNN13;
  #period PNN25 = ~PNN25;
end


always begin

 #period PNN33 = ~PNN33;
 #period PNN29 = ~PNN29;
 #(period*2) PNN37 = ~PNN37;
end


always begin

  #(period*2) PNN45 = ~PNN45;
  #(period*2) PNN49 = ~PNN49;
#(period*2) PNN41 = ~PNN41;

 #(period*5) PNN53 = ~PNN53;
#period PNN57 = ~PNN57;
 #period PNN61 = ~PNN61;


end


always begin

 #(period*2)  PNN77 = ~PNN77; 
 #period PNN65 = ~PNN65;
#period PNN69 = ~PNN69;
 #(period*2)  PNN73 = ~PNN73;
 
end


always begin
  #period PNN89 = ~PNN89;
 #period PNN81 = ~PNN81;
 #(period*2)  PNN85 = ~PNN85;



end

always begin

  #(period*2)  PNN105 = ~PNN105;
  #period PNN101 = ~PNN101;
 #period PNN109 = ~PNN109;
#(period*3)  PNN93 = ~PNN93;
#period PNN97 = ~PNN97;


end

always begin

  #period PNN121 = ~PNN121;
 #period PNN125 = ~PNN125;
#(period*4)  PNN113 = ~PNN113;
 #period PNN117 = ~PNN117;
 #period PNN131 = ~PNN131;
 #(period*2)  PNN129 = ~PNN129;
 #period PNN130 = ~PNN130;
end

always begin

#period PNN136 = ~PNN136;
 #(period*2)  PNN137 = ~PNN137;
  #period PNN135 = ~PNN135;
 #period PNN132 = ~PNN132;
 #(period*2)  PNN133 = ~PNN133;
#period PNN134 = ~PNN134;


end

endmodule
