-- x_inbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b11 is
end test_b11;

architecture tb_b11_arch of test_b11 is
           
--component- same as the entity in the main vhd file
component b11 is
	port(
		signal x_in:    in integer range 63 downto 0;
		signal stbi:    in bit;
		signal clk:   in bit;
		signal reset:   in bit;
		signal x_out:   out integer range 63 downto 0
	);
   
end component;

    --  Specifies which entity is bound with the component.
for dec_0: b11 use entity work.b11;

signal stbi,clk: bit:='0';
signal x_in,x_out: integer:= 0;
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

dec_0: b11
port map (x_in,stbi,clk,reset,x_out);
  
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

stbi<= '0';	
--wait for 4 ns;
wait for period*4;

stbi<= '1';	
wait for period*20;


end process;


process
begin

x_in<= 45;	
--wait for 4 ns;
wait for period;

x_in<= 12;	
wait for period*3;

x_in<= 9;	
wait for period*3;

x_in<= 62;	
wait for period;

x_in<= 18;	
wait for period*4;

x_in<= 02;	
wait for period;

x_in<= 28;	
wait for period*2;

end process;

end tb_b11_arch;

