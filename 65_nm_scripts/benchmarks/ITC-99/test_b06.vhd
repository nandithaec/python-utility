-- Testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b06 is
end test_b06;

architecture tb_b06_arch of test_b06 is
           
--component- same as the entity in the main vhd file
component b06 is
port (Qout_cc_mux : out bit_vector(2 downto 1);
	   eql: in bit;
	   Qout_uscite: out bit_vector(2 downto 1);
	   clk: in bit;
	   Qout_enable_count: out bit;
	   Qout_ackout: out bit;
	   reset: in bit; 
	   cont_eql: in bit);
   
end component;

    --  Specifies which entity is bound with the component.
for dec_0: b06 use entity work.b06;

signal clk,eql,cont_eql,Qout_ackout,Qout_enable_count : bit:='0';
signal Qout_cc_mux,Qout_uscite : bit_vector(2 downto 1):="00";
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

dec_0: b06
port map (Qout_cc_mux,eql,Qout_uscite,clk,Qout_enable_count,Qout_ackout,reset,cont_eql);
  
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

eql<= '0';	
--wait for 4 ns;
wait for period*4;

eql<= '1';	
wait for period*3;

cont_eql<= '0';	
--wait for 4 ns;
wait for period*3;

cont_eql<= '1';	
wait for period*2;

end process;




end tb_b06_arch;

