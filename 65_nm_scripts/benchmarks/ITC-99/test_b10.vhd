-- Testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b10 is
end test_b10;

architecture tb_b10_arch of test_b10 is
           
--component- same as the entity in the main vhd file
component b10 is
	port ( r_button : in  bit ;
		g_button : in  bit ;
		key      : in  bit ;
		start    : in  bit ;
		reset    : in  bit ;
		test     : in  bit ;
		Qout_cts      : out bit ;
		Qout_ctr      : out bit ;
		rts      : in  bit ;
		rtr      : in  bit ;
		clk    : in  bit ;
		v_in     : in  bit_vector(3 downto 0) ;
		Qout_vout    : out bit_vector(3 downto 0)
		) ;
   
end component;

    --  Specifies which entity is bound with the component.
for dec_0: b10 use entity work.b10;

signal r_button,g_button,key,start,test,Qout_cts,Qout_ctr, rts,rtr,clk : bit:='0';
signal v_in,Qout_vout: bit_vector (3 downto 0):="0000";
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

dec_0: b10
port map (r_button,g_button,key,start,reset,test,Qout_cts,Qout_ctr, rts,rtr,clk,v_in,Qout_vout);
  
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
wait for period*100;


end process;


process
begin

r_button<= '0';	
--wait for 4 ns;
wait for period*4;

r_button<= '1';	
wait for period*6;

g_button<= '0';	
--wait for 4 ns;
wait for period*2;

g_button<= '1';	
wait for period;

key<= '0';	
--wait for 4 ns;
wait for period*3;

key<= '1';	
wait for period*5;


end process;


process
begin

test<= '0';	
--wait for 4 ns;
wait for period;

test<= '1';	
wait for period*3;

rts<= '0';	
wait for period*3;

rts<= '1';	
wait for period;

rtr<= '0';	
wait for period*4;

rtr<= '1';	
wait for period*5;

end process;

process
begin

v_in<= x"E";	
wait for period*7;

v_in<= x"1";	
wait for period*4;

v_in<= x"A";	
wait for period*3;

v_in<= x"8";	
wait for period*2;

v_in<= x"9";	
wait for period*5;

v_in<= x"4";	
wait for period*3;


end process;



end tb_b10_arch;

