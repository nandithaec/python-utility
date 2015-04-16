-- Testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_b13 is
end test_b13;

architecture tb_b13_arch of test_b13 is
           
--component- same as the entity in the main vhd file
component b13 is
port(
	clk : in bit;	
	data_in	: in bit_vector( 7 downto 0 ); 
	dsr : in bit;
	reset : in bit;
	eoc : in bit;  
	Qout_soc : out bit;
	Qout_load_dato,Qout_add_mpx2 : out bit;
	Qout_canale : out integer range 8 downto 0;
	Qout_mux_en : out bit; 	
	Qout_error_sig : out bit;
	Qout_data : out bit
);
   
end component;

    --  Specifies which entity is bound with the component.
for des_b13: b13 use entity work.b13;

signal clk,dsr,eoc,Qout_soc, Qout_load_dato, Qout_add_mpx2, Qout_mux_en, Qout_error_sig, Qout_data  : bit:='0';
signal data_in: bit_vector (7 downto 0):=x"00";
signal Qout_canale: integer := 0;
signal reset:bit:='1';
constant period: time :=4 ns;
  
begin

des_b13: b13
port map (clk,data_in,dsr,reset,eoc,Qout_soc, Qout_load_dato, Qout_add_mpx2,Qout_canale,Qout_mux_en, Qout_error_sig, Qout_data);
  
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

dsr<= '0';	
--wait for 4 ns;
wait for period*4;

dsr<= '1';	
wait for period*6;

eoc<= '0';	
--wait for 4 ns;
wait for period;

eoc<= '1';	
wait for period*25;

end process;



process
begin

data_in<= x"AE";	
wait for period*7;

data_in<= x"1F";	
wait for period*4;

data_in<= x"04";	
wait for period*3;

data_in<= x"84";	
wait for period*2;

data_in<= x"C9";	
wait for period*5;

data_in<= x"40";	
wait for period*3;

data_in<= x"01";	
wait for period;


end process;



end tb_b13_arch;

