
`timescale 1ns/100ps

module test_c432;
  //(clk, reset, go,in_addr, mem_in, io_in, mem_out, io_out,s1s0, adr_15to8, ad7_0, io_mbar, in_rd_wrbar, rd_bar, wr_bar,rdy, ALE, current_tstate);

//inputs as reg and o/ps as wires, inout as reg

reg clk,PCN1,PCN4,PCN8,PCN11,PCN14,PCN17,PCN21,PCN24,PCN27,PCN30,
      PCN34,PCN37,PCN40,PCN43,PCN47,PCN50,PCN53,PCN56,PCN60,PCN63,
      PCN66,PCN69,PCN73,PCN76,PCN79,PCN82,PCN86,PCN89,PCN92,PCN95,
      PCN99,PCN102,PCN105,PCN108,PCN112,PCN115;


c432_clk_ipFF u1 (clk,PCN1,PCN4,PCN8,PCN11,PCN14,PCN17,PCN21,PCN24,PCN27,PCN30,
             PCN34,PCN37,PCN40,PCN43,PCN47,PCN50,PCN53,PCN56,PCN60,PCN63,
             PCN66,PCN69,PCN73,PCN76,PCN79,PCN82,PCN86,PCN89,PCN92,PCN95,
             PCN99,PCN102,PCN105,PCN108,PCN112,PCN115,Qout_PCN_223,Qout_PCN_329,Qout_PCN_370,Qout_PCN_421,
             Qout_PCN_430,Qout_PCN_431,Qout_PCN_432);
 
parameter period = 20; //20ns = clk period


//initialise all inputs to zero
initial
begin

clk=0;
PCN1= 0'b0;
PCN4= 0'b0;
PCN8= 0'b0;
PCN11 = 0'b0;
PCN14 = 0'b0;
PCN17 = 0'b0;
PCN21 = 0'b0;
PCN24 = 0'b0;
PCN27 = 0'b0;
PCN30 = 0'b0;
PCN34 = 0'b0;
PCN37 = 0'b0;
PCN40 = 0'b0;
PCN43 = 0'b0;
PCN47 = 0'b0;
PCN50 = 0'b0;
PCN53 = 0'b0;
PCN56 = 0'b0;
PCN60 = 0'b0;
PCN63 = 0'b0;
PCN66 = 0'b0;
PCN69 = 0'b0;
PCN73 = 0'b0;
PCN76 = 0'b0;
PCN79 = 0'b0;
PCN82 = 0'b0;
PCN86 = 0'b0;
PCN89 = 0'b0;
PCN92 = 0'b0;
PCN95 = 0'b0;
PCN99 = 0'b0;
PCN102 = 0'b0;
PCN105 = 0'b0;
PCN108 = 0'b0;
PCN112 = 0'b0;
PCN115 = 0'b0;

end
  


  always begin

 #(period/2) clk= ~clk; //1ns(timescale) * 100 = 100ns= half period
 
  end

always begin

 #period PCN1 = ~PCN1; //invert after duration=period
 #period PCN4 = ~PCN4; //this delay will be wrt the previous time and not wrt time 0

 #(period*2) PCN21 = ~PCN21;
 #period PCN11 = ~PCN11;
 #(period*2) PCN17 = ~PCN17;
 #(period*2) PCN14 = ~PCN14;
  #period PCN8 = ~PCN8;
end


always begin

 #period PCN30 = ~PCN30;
 #period PCN34 = ~PCN34;

#(period*4) PCN24 = ~PCN24;
 #period PCN27 = ~PCN27;

 #(period*2) PCN37 = ~PCN37;
end


always begin

 #(period*2) PCN40 = ~PCN40;
  #(period*2) PCN60 = ~PCN60;
 #period PCN63= ~PCN63;
 #period PCN50 = ~PCN50;
 #(period*5) PCN53 = ~PCN53;
#period PCN43 = ~PCN43;
 #period PCN47 = ~PCN47;

 #period PCN56 = ~PCN56;

end


always begin

 #(period*2) PCN66 = ~PCN66;
  #period PCN73 = ~PCN73;
#period PCN69 = ~PCN69;

 #period PCN76 = ~PCN76;
 
end


always begin
  #period PCN89 = ~PCN89;
#(period*2) PCN79= ~PCN79;
 #period PCN82 = ~PCN82;
 #period PCN86 = ~PCN86;



end

always begin

  #period PCN105 = ~PCN105;
  #period PCN95 = ~PCN95;
 #period PCN99 = ~PCN99;
#period PCN108 = ~PCN108;
#period PCN92 = ~PCN92;

 #period PCN102 = ~PCN102;


end

always begin

 #period PCN112 = ~PCN112;
 #period PCN115 = ~PCN115;

end


endmodule
