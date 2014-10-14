-- Testbench of decoder--Nanditha Rao


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.ALL;
use ieee.std_logic_misc.all;
use ieee.numeric_std.all;

entity test_decoder_op_ip is
end test_decoder_op_ip;

architecture tb_decoder_pnr of test_decoder_op_ip is
           
--component- same as the entity in the main vhd file
component decoder_op_ip is
port(input_dec : in  bit_vector(2 downto 0);
	clk: in bit;
	output_dec : out  bit_vector(7 downto 0)
	);
end component;


    --  Specifies which entity is bound with the component.
    for dec_0: decoder_op_ip use entity work.decoder_op_ip;

  signal clk: bit:='0';
  signal input_dec:bit_vector(2 downto 0):="000";
  signal output_dec:bit_vector(7 downto 0):= "00000000";
constant period: time :=4 ns;
  
    begin

    dec_0: decoder_op_ip 
  port map (input_dec,clk,output_dec);
  
 process
    begin
  
    
   clk <= '0';			
--  wait for 2 ns;
wait for period/2;
  clk <= '1';
  wait for period/2;

 
   end process;

process
begin


input_dec(0)<= '0';	
--wait for 4 ns;
wait for period;

input_dec(0)<= '1';	
wait for period;

input_dec(0)<= '0';	
wait for period;

input_dec(0)<= '1';	
wait for period;

input_dec(0)<= '0';	
wait for period;

input_dec(0)<= '1';	
wait for period;

input_dec(0)<= '0';	
wait for period;

input_dec(0)<= '1';	
wait for period;

--input_dec(0) <= not (input_dec(0)) after 10 ns;
end process;


process 
begin


input_dec(1)<= '0';	
wait for period*2;
input_dec(1)<= '1';	
wait for period*2;
input_dec(1)<= '0';	
wait for period*2;
input_dec(1)<= '1';	
wait for period*2;
input_dec(1)<= '0';	
wait for period*2;
input_dec(1)<= '1';	
wait for period*2;
input_dec(1)<= '0';	
wait for period*2;
input_dec(1)<= '1';	
wait for period*2;

end process;

process
begin

input_dec(2)<= '0';	
wait for period*4;
input_dec(2)<= '1';	
wait for period*4;
input_dec(2)<= '0';	
wait for period*4;
input_dec(2)<= '1';	
wait for period*4;
input_dec(2)<= '0';	
wait for period*4;
input_dec(2)<= '1';	
wait for period*4;
input_dec(2)<= '0';	
wait for period*4;
input_dec(2)<= '1';	
wait for period*4;


end process;

end tb_decoder_pnr;

