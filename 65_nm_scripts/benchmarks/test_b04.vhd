-- Testbench--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b04 is
end test_b04;

architecture tb_b04_arch of test_b04 is
           
--component- same as the entity in the main vhd file
component b04 is
 port( RESTART  : in bit;
        AVERAGE  : in bit;
        ENABLE   : in bit;
        DATA_IN  : in integer range 127 downto -128;
        DATA_OUT : out integer range 127 downto -128;
        RESET    : in bit;
        clk    : in bit
        );
end component;

    --  Specifies which entity is bound with the component.
for des_b04: b04 use entity work.b04;

signal clk,AVERAGE,ENABLE : bit:='0';
signal RESTART,RESET: bit:='1';
signal DATA_IN: integer:= -128;
signal DATA_OUT: integer:= -128;
constant period: time :=4 ns;
  
begin

des_b04: b04
port map (RESTART,AVERAGE, ENABLE,DATA_IN, DATA_OUT,RESET,clk) ;
  
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
  
RESET <= '1';			
--  wait for 2 ns;
wait for period*2;
RESET <= '0';
wait for period*10000;
 
end process;


process
begin
  
RESTART <= '1';			
--  wait for 2 ns;
wait for period*4;
RESTART <= '0';
wait for period*5000;
 
end process;



process
begin
  
ENABLE <= '0';			
--  wait for 2 ns;
wait for period*4;
ENABLE <= '1';
wait for period*15000;
 
end process;

----------------------------------------------------------
--Each process content will be executed at the same time instant. i.e., concurrently
--Within each process, the statements are executed sequentially.

process
begin

AVERAGE<= '0';	
--wait for 4 ns;
wait for period;

AVERAGE<= '1';	
wait for period*3;


end process;


process
begin

DATA_IN<= 23;	
--wait for 4 ns;
wait for period;

DATA_IN<= -29;	
wait for period*3;

DATA_IN<= 126;	
wait for period;

DATA_IN<= 0;	
wait for period*4;


DATA_IN<= 123;	
--wait for 4 ns;
wait for period;

DATA_IN<= -19;	
wait for period*2;

DATA_IN<= 16;	
wait for period*7;

DATA_IN<= 60;	
wait for period*5;


end process;


end tb_b04_arch;

