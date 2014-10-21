
`timescale 1ns/100ps

module test_c1355;
  //(clk, reset, go,in_addr, mem_in, io_in, mem_out, io_out,s1s0, adr_15to8, ad7_0, io_mbar, in_rd_wrbar, rd_bar, wr_bar,rdy, ALE, current_tstate);

//inputs as reg and o/ps as wires, inout as reg

reg clk,PGG1,PGG2,PGG3,PGG4,PGG5,PGG6,PGG7,PGG8,PGG9,PGG10,PGG11,PGG12,PGG13,PGG14,PGG15,PGG16,PGG17,PGG18,PGG19,PGG20,
  PGG21,PGG22,PGG23,PGG24,PGG25,PGG26,PGG27,PGG28,PGG29,PGG30,PGG31,PGG32,PGG33,PGG34,PGG35,PGG36,PGG37,PGG38,PGG39,
  PGG40,PGG41;


c1355_clk_ipFF  u1 (clk,PGG1,PGG10,PGG11,PGG12,PGG13,
	Q_PGG1324,Q_PGG1325,Q_PGG1326,Q_PGG1327,Q_PGG1328,Q_PGG1329,Q_PGG1330,
  Q_PGG1331,Q_PGG1332,Q_PGG1333,Q_PGG1334,Q_PGG1335,Q_PGG1336,Q_PGG1337,Q_PGG1338,Q_PGG1339,Q_PGG1340,Q_PGG1341,Q_PGG1342,
  Q_PGG1343,Q_PGG1344,Q_PGG1345,Q_PGG1346,Q_PGG1347,Q_PGG1348,Q_PGG1349,Q_PGG1350,Q_PGG1351,Q_PGG1352,Q_PGG1353,Q_PGG1354,
  Q_PGG1355,
	PGG14,PGG15,PGG16,PGG17,PGG18,PGG19,PGG2,PGG20,PGG21,PGG22,PGG23,PGG24,PGG25,PGG26,PGG27,PGG28,PGG29,PGG3,
  PGG30,PGG31,PGG32,PGG33,PGG34,PGG35,PGG36,PGG37,PGG38,PGG39,PGG4,PGG40,PGG41,PGG5,PGG6,PGG7,PGG8,PGG9);
 
parameter period = 20; //20ns = clk period


//initialise all inputs to zero
initial
begin

clk= 0; 
PGG1= 0; 
PGG2= 0; 
PGG3= 0; 
PGG4= 0; 
PGG5= 0; 
PGG6= 0; 
PGG7= 0; 
PGG8= 0; 
PGG9= 0; 
PGG10= 0; 
PGG11= 0; 
PGG12= 0; 
PGG13= 0; 
PGG14= 0; 
PGG15= 0; 
PGG16= 0; 
PGG17= 0; 
PGG18= 0; 
PGG19= 0; 
PGG20= 0; 
PGG21= 0; 
PGG22= 0; 
PGG23= 0; 
PGG24= 0; 
PGG25= 0; 
PGG26= 0; 
PGG27= 0; 
PGG28= 0; 
PGG29= 0; 
PGG30= 0; 
PGG31= 0; 
PGG32= 0; 
PGG33= 0; 
PGG34= 0; 
PGG35= 0; 
PGG36= 0; 
PGG37= 0; 
PGG38= 0; 
PGG39= 0; 
PGG40= 0; 
PGG41=0;

end
  


  always begin

 #(period/2) clk= ~clk; //1ns(timescale) * 100 = 100ns= half period
 
  end

always begin

//invert after duration=period
//this delay will be wrt the previous time and not wrt time 0

#(period *2) PGG3= ~PGG3; 
#(period ) PGG4= ~PGG4; 
#(period ) PGG1= ~PGG1; 
#(period *4) PGG5= ~PGG5; 
#(period *2) PGG6= ~PGG6; 
#(period) PGG2= ~PGG2; 

#(period *3) PGG7= ~PGG7; 

end


always begin

#(period *2) PGG9= ~PGG9; 
#(period *4) PGG11= ~PGG11; 
#(period *2) PGG12= ~PGG12; 
#(period *3) PGG10= ~PGG10; 
#(period) PGG8= ~PGG8; 
#(period) PGG13= ~PGG13; 

end


always begin

#(period) PGG18= ~PGG18;  
#(period) PGG14= ~PGG14; 
#(period *4) PGG17= ~PGG17; 
#(period *2) PGG15= ~PGG15; 
#(period *2) PGG16= ~PGG16; 


end


always begin


#(period *2) PGG20= ~PGG20; 
#(period *4) PGG24= ~PGG24; 
#(period *2) PGG25= ~PGG25; 
#(period ) PGG21= ~PGG21; 
#(period) PGG22= ~PGG22; 
#(period) PGG19= ~PGG19; 

#(period *5) PGG23= ~PGG23; 

 
end


always begin

#(period) PGG28= ~PGG28; 
#(period *2) PGG29= ~PGG29; 
#(period) PGG26= ~PGG26; 

#(period *2) PGG34= ~PGG34;
#(period *3) PGG31= ~PGG31; 
#(period *2) PGG32= ~PGG32; 
#(period) PGG27= ~PGG27; 

#(period *5) PGG30= ~PGG30; 

#(period) PGG33= ~PGG33; 




end

always begin

#(period) PGG38= ~PGG38; 
#(period) PGG39= ~PGG39; 
#(period *2) PGG36= ~PGG36; 
#(period) PGG40= ~PGG40; 
#(period *2) PGG35= ~PGG35; 
#(period *4) PGG41= ~PGG41;
#(period *3) PGG37= ~PGG37; 


end



endmodule
