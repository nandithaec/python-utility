-- testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b12 is
end test_b12;

architecture tb_b12_arch of test_b12 is
           
--component- same as the entity in the main vhd file
component b12 is
port(clk     : in  bit;
       reset     : in  bit;
       start     : in  bit;
       in_k         : in  bit_vector ( 3 downto 0);
       Qout_nloss     : out bit;
       Qout_nl_vec        : out bit_vector ( 3 downto 0);
       Qout_speaker   : out bit);
   
end component;

    --  Specifies which entity is bound with the component.
for des: b12 use entity work.b12;

signal start,clk,Qout_nloss,Qout_speaker: bit:='0';
signal in_k,Qout_nl_vec: bit_vector ( 3 downto 0):= x"0";
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

des: b12
port map (clk,reset,start,in_k,Qout_nloss,Qout_nl_vec,Qout_speaker);
  
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
wait for period*1000;
 
end process;


----------------------------------------------------------

process
begin

start<= '0';	
--wait for 4 ns;
wait for period*4;

start<= '1';	
wait for period*20;


end process;


process
begin

in_k<= x"E";	
--wait for 4 ns;
wait for period;

in_k<= x"3";	
wait for period*3;

in_k<= x"A";	
wait for period*3;

in_k<= x"8";	
wait for period;

in_k<= x"5";	
wait for period*4;

in_k<= x"F";	
wait for period;

in_k<= x"9";	
wait for period*2;

end process;

end tb_b12_arch;

