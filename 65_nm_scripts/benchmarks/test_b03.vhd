-- Testbench--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b03 is
end test_b03;

architecture tb_b03_arch of test_b03 is
           
--component- same as the entity in the main vhd file
component b03 is
port (  clk     : in bit;
        reset     : in bit;
        request1  : in bit;
        request2  : in bit;
        request3  : in bit;
        request4  : in bit;
        Qout_grant_o   : out bit_vector(3 downto 0)
      );
   
end component;

    --  Specifies which entity is bound with the component.
for des_b03: b03 use entity work.b03;

signal clk,request1,request2,request3,request4 : bit:='0';
signal reset:bit:='1';
signal Qout_grant_o:bit_vector(3 downto 0):="0000";
constant period: time :=4 ns;
  
begin

des_b03: b03
port map (clk,reset,request1,request2,request3,request4,Qout_grant_o);
  
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

request1<= '0';	
--wait for 4 ns;
wait for period;

request1<= '1';	
wait for period*3;

request2<= '1';	
wait for period*2;

request2<= '0';	
wait for period;


end process;


process
begin

request3<= '0';	
--wait for 4 ns;
wait for period;

request3<= '1';	
wait for period*3;

request4<= '1';	
wait for period;

request4<= '0';	
wait for period*4;


end process;

end tb_b03_arch;

