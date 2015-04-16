-- Testbench--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b01 is
end test_b01;

architecture tb_b01_arch of test_b01 is
           
--component- same as the entity in the main vhd file
component b01 is
port(
   line1: in bit; 
   line2: in bit;
   reset: in bit;
   outp  : out bit;
   Qout_overflw : out bit;
   clk : in bit );
   
end component;

    --  Specifies which entity is bound with the component.
for des_b01: b01 use entity work.b01;

signal clk,line1,line2,outp,Qout_overflw: bit:='0';
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

des_b01: b01
port map (line1,line2,reset,outp,Qout_overflw,clk);
  
process
begin
  
clk <= '0';			
--  wait for 2 ns;
wait for period/2;
clk <= '1';
wait for period/2;
 
end process;

----------------------------------------------------------


process
begin
  
reset <= '1';			
--  wait for 2 ns;
wait for period*2;
reset <= '0';
wait for period*10000;
 
end process;


----------------------------------------------------------
--Each process content will be executed at the same time instant. i.e., concurrently
--Within each process, the statements are executed sequentially.

process
begin

line1<= '0';	
--wait for 4 ns;
wait for period;

line1<= '1';	
wait for period*3;

line2<= '0';	
wait for period*2;

line2<= '1';	
wait for period;


end process;



end tb_b01_arch;

