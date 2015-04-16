-- Testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b09 is
end test_b09;

architecture tb_b09_arch of test_b09 is
           
--component- same as the entity in the main vhd file
component b09 is
port (reset,clk: in bit;
	INN_x: in bit;
	Qout_y: out bit
);
   
end component;

    --  Specifies which entity is bound with the component.
for dec_0: b09 use entity work.b09;

signal clk,INN_x,Qout_y : bit:='0';
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

dec_0: b09
port map (reset,clk,INN_x,Qout_y);
  
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

process
begin

INN_x<= '0';	
--wait for 4 ns;
wait for period;

INN_x<= '1';	
wait for period*3;

end process;




end tb_b09_arch;

