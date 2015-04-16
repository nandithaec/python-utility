
`timescale 1ns/100ps

module test_c880;
  //(clk, reset, go,in_addr, mem_in, io_in, mem_out, io_out,s1s0, adr_15to8, ad7_0, io_mbar, in_rd_wrbar, rd_bar, wr_bar,rdy, ALE, current_tstate);

//inputs as reg and o/ps as wires, inout as reg

reg clk,PCN1,PCN8,PCN13,PCN17,PCN26,PCN29,PCN36,PCN42,PCN51,PCN55,
      PCN59,PCN68,PCN72,PCN73,PCN74,PCN75,PCN80,PCN85,PCN86,PCN87,
      PCN88,PCN89,PCN90,PCN91,PCN96,PCN101,PCN106,PCN111,PCN116,PCN121,
      PCN126,PCN130,PCN135,PCN138,PCN143,PCN146,PCN149,PCN152,PCN153,PCN156,
      PCN159,PCN165,PCN171,PCN177,PCN183,PCN189,PCN195,PCN201,PCN207,PCN210,
      PCN219,PCN228,PCN237,PCN246,PCN255,PCN259,PCN260,PCN261,PCN267,PCN268;


c880_clk_ipFF  u1 (clk,PCN1,PCN8,PCN13,PCN17,PCN26,PCN29,PCN36,PCN42,PCN51,PCN55,
             PCN59,PCN68,PCN72,PCN73,PCN74,PCN75,PCN80,PCN85,PCN86,PCN87,
             PCN88,PCN89,PCN90,PCN91,PCN96,PCN101,PCN106,PCN111,PCN116,PCN121,
             PCN126,PCN130,PCN135,PCN138,PCN143,PCN146,PCN149,PCN152,PCN153,PCN156,
             PCN159,PCN165,PCN171,PCN177,PCN183,PCN189,PCN195,PCN201,PCN207,PCN210,
             PCN219,PCN228,PCN237,PCN246,PCN255,PCN259,PCN260,PCN261,PCN267,PCN268,
             Q_PCN388,Q_PCN389,Q_PCN390,Q_PCN391,Q_PCN418,Q_PCN419,Q_PCN420,Q_PCN421,Q_PCN422,Q_PCN423,
             Q_PCN446,Q_PCN447,Q_PCN448,Q_PCN449,Q_PCN450,Q_PCN767,Q_PCN768,Q_PCN850,Q_PCN863,Q_PCN864,
             Q_PCN865,Q_PCN866,Q_PCN874,Q_PCN878,Q_PCN879,Q_PCN880);
 
parameter period = 20; //20ns = clk period


//initialise all inputs to zero
initial
begin

clk= 0; 
PCN1= 0; 
PCN8= 0; 
PCN13= 0; 
PCN17= 0; 
PCN26= 0; 
PCN29= 0; 
PCN36= 0; 
PCN42= 0; 
PCN51= 0; 
PCN55= 0; 
PCN59= 0; 
PCN68= 0; 
PCN72= 0; 
PCN73= 0; 
PCN74= 0; 
PCN75= 0; 
PCN80= 0; 
PCN85= 0; 
PCN86= 0; 
PCN87= 0; 
PCN88= 0; 
PCN89= 0; 
PCN90= 0; 
PCN91= 0; 
PCN96= 0; 
PCN101= 0; 
PCN106= 0; 
PCN111= 0; 
PCN116= 0; 
PCN121= 0; 
PCN126= 0; 
PCN130= 0; 
PCN135= 0; 
PCN138= 0; 
PCN143= 0; 
PCN146= 0; 
PCN149= 0; 
PCN152= 0; 
PCN153= 0; 
PCN156= 0; 
PCN159= 0; 
PCN165= 0; 
PCN171= 0; 
PCN177= 0; 
PCN183= 0; 
PCN189= 0; 
PCN195= 0; 
PCN201= 0; 
PCN207= 0; 
PCN210= 0; 
PCN219= 0; 
PCN228= 0; 
PCN237= 0; 
PCN246= 0; 
PCN255= 0; 
PCN259= 0; 
PCN260= 0; 
PCN261= 0; 
PCN267= 0; 
PCN268 = 0;

end
  


  always begin

 #(period/2) clk= ~clk; //1ns(timescale) * 100 = 100ns= half period
 
  end

always begin

//invert after duration=period
//this delay will be wrt the previous time and not wrt time 0

#(period) PCN8 =   ~PCN8 ; 
#(period*2) PCN13=   ~PCN13; 
#(period*2) PCN1 =   ~PCN1 ; 
#(period) PCN26=   ~PCN26; 
#(period*2) PCN29=   ~PCN29;
#(period*4) PCN17=   ~PCN17; 
 
#(period*2) PCN36=   ~PCN36; 

end


always begin

#(period) PCN51=   ~PCN51; 
#(period*2) PCN55=   ~PCN55; 
#(period*2) PCN42=   ~PCN42; 

#(period) PCN59=   ~PCN59; 
#(period*2) PCN68=   ~PCN68; 
end


always begin

#(period*2) PCN73=   ~PCN73; 
#(period*2) PCN74=   ~PCN74; 
#(period) PCN72=   ~PCN72; 

#(period*2) PCN75=   ~PCN75; 
#(period*3) PCN80=   ~PCN80; 

end


always begin

#(period*2) PCN87=   ~PCN87; 
#(period*3) PCN88=   ~PCN88; 
#(period*2) PCN85=   ~PCN85; 
#(period) PCN86=   ~PCN86; 
#(period*2) PCN90=   ~PCN90; 
#(period) PCN91=   ~PCN91; 
#(period*4) PCN89=   ~PCN89; 

#(period*2) PCN96=   ~PCN96; 
 
end


always begin

#(period*2) PCN111=  ~PCN111; 
#(period*4) PCN116=  ~PCN116;
#(period*2) PCN101=  ~PCN101; 
#(period) PCN106=  ~PCN106; 
 
#(period) PCN121=  ~PCN121; 
#(period) PCN126=  ~PCN126; 



end

always begin


#(period) PCN135=  ~PCN135; 
#(period*2) PCN138=  ~PCN138; 
#(period) PCN130=  ~PCN130; 

#(period*2) PCN143=  ~PCN143; 
#(period) PCN146=  ~PCN146; 


end

always begin

#(period) PCN153=  ~PCN153; 
#(period*2) PCN156=  ~PCN156; 
#(period) PCN149=  ~PCN149; 
#(period*2) PCN152=  ~PCN152; 

 #(period*2) PCN159= ~PCN159;  
#(period) PCN171=  ~PCN171; 
#(period*2) PCN177=  ~PCN177; 
#(period) PCN165=  ~PCN165; 

#(period*4) PCN183=  ~PCN183;
end

always begin

#(period*4) PCN201=  ~PCN201; 
#(period*2) PCN207=  ~PCN207; 
#(period) PCN189=  ~PCN189; 
#(period) PCN195=  ~PCN195; 
#(period*2) PCN219=  ~PCN219; 
#(period) PCN228=  ~PCN228; 
#(period) PCN210=  ~PCN210; 


end



endmodule
