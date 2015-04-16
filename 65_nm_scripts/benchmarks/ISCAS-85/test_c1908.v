
`timescale 1ns/100ps

module test_c1908;
  //(clk, reset, go,in_addr, mem_in, io_in, mem_out, io_out,s1s0, adr_15to8, ad7_0, io_mbar, in_rd_wrbar, rd_bar, wr_bar,rdy, ALE, current_tstate);

//inputs as reg and o/ps as wires, inout as reg

reg clk,PNN1,PNN4,PNN7,PNN10,PNN13,PNN16,PNN19,PNN22,PNN25,PNN28,
      PNN31,PNN34,PNN37,PNN40,PNN43,PNN46,PNN49,PNN53,PNN56,PNN60,
      PNN63,PNN66,PNN69,PNN72,PNN76,PNN79,PNN82,PNN85,PNN88,PNN91,
      PNN94,PNN99,PNN104;

/*wire PNN2753,PNN2754,PNN2755,PNN2756,PNN2762,PNN2767,PNN2768,PNN2779,PNN2780,PNN2781,
       PNN2782,PNN2783,PNN2784,PNN2785,PNN2786,PNN2787,PNN2811,PNN2886,PNN2887,PNN2888,
       PNN2889,PNN2890,PNN2891,PNN2892,PNN2899;
*/

c1908_clk_ipFF  u1	(clk,PNN1,PNN4,PNN7,PNN10,PNN13,PNN16,PNN19,PNN22,PNN25,PNN28,
              PNN31,PNN34,PNN37,PNN40,PNN43,PNN46,PNN49,PNN53,PNN56,PNN60,
              PNN63,PNN66,PNN69,PNN72,PNN76,PNN79,PNN82,PNN85,PNN88,PNN91,
              PNN94,PNN99,PNN104,Q_PNN2753,Q_PNN2754,Q_PNN2755,Q_PNN2756,Q_PNN2762,Q_PNN2767,Q_PNN2768,
              Q_PNN2779,Q_PNN2780,Q_PNN2781,Q_PNN2782,Q_PNN2783,Q_PNN2784,Q_PNN2785,Q_PNN2786,Q_PNN2787,Q_PNN2811,
              Q_PNN2886,Q_PNN2887,Q_PNN2888,Q_PNN2889,Q_PNN2890,Q_PNN2891,Q_PNN2892,Q_PNN2899);
 
parameter period = 20; //200ns = clk period


  initial
  begin
 clk= 0'b0;
 PNN1 = 0'b0;
 PNN4 = 0'b0;
 PNN7 = 0'b0;
 PNN10 = 0'b0;
 PNN13 = 0'b0;
 PNN16 = 0'b0;
 PNN19 = 0'b0;
 PNN22 = 0'b0;
 PNN25 = 0'b0;
 PNN28 = 0'b0;
 PNN31 = 0'b0;
 PNN34 = 0'b0;
 PNN37 = 0'b0;
 PNN40 = 0'b0;
 PNN43 = 0'b0;
 PNN46 = 0'b0;
 PNN49 = 0'b0;
 PNN53 = 0'b0;
 PNN56 = 0'b0;
 PNN60 = 0'b0;
 PNN63=  0'b0;
 PNN66 = 0'b0;
 PNN69 = 0'b0;
 PNN72 = 0'b0;
 PNN76 = 0'b0;
 PNN79=  0'b0;
 PNN82 = 0'b0;
 PNN85 = 0'b0;
 PNN88 = 0'b0;
 PNN91 = 0'b0;
 PNN94 = 0'b0;
 PNN99 = 0'b0;
 PNN104 = 0'b0;
  end
  


  always begin

 #(period/2) clk= ~clk; //1ns(timescale) * 100 = 100ns= half period
 
  end

always begin

 #period PNN1 = ~PNN1; //invert after duration=period
 #period PNN4 = ~PNN4; //this delay will be wrt the previous time and not wrt time 0
 #period PNN7 = ~PNN7;
 #period PNN10 = ~PNN10;
 #(period*2) PNN13 = ~PNN13;
 #(period*2) PNN16 = ~PNN16;
 
end


always begin

#(period*4) PNN19 = ~PNN19;
 #period PNN22 = ~PNN22;
 #period PNN25 = ~PNN25;
 #period PNN28 = ~PNN28;
 #period PNN31 = ~PNN31;
 #period PNN34 = ~PNN34;
 #(period*2) PNN37 = ~PNN37;
end


always begin

 #(period*2) PNN40 = ~PNN40;
 #period PNN43 = ~PNN43;
 #period PNN46 = ~PNN46;
 #period PNN49 = ~PNN49;


end


always begin
 #(period) PNN53 = ~PNN53;
 #period PNN56 = ~PNN56;
 #(period*2) PNN60 = ~PNN60;
 #period PNN63= ~PNN63;
 #(period*2) PNN66 = ~PNN66;
 #period PNN69 = ~PNN69;
 #period PNN72 = ~PNN72;
 #period PNN76 = ~PNN76;
 
end


always begin
 #(period*2) PNN79= ~PNN79;
 #period PNN82 = ~PNN82;
 #period PNN85 = ~PNN85;
 #period PNN88 = ~PNN88;
 #period PNN91 = ~PNN91;
 #period PNN94 = ~PNN94;
 #period PNN99 = ~PNN99;
 #period PNN104 = ~PNN104;

end

endmodule
