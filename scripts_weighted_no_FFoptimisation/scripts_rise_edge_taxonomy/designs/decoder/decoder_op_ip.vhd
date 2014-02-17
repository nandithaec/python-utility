
library IEEE;
library std;
use IEEE.std_logic_1164.ALL;
use IEEE.std_logic_arith.ALL;
use IEEE.std_logic_unsigned.ALL;
use IEEE.std_logic_misc.ALL;
use IEEE.numeric_std.ALL;
use std.textio.all;
use ieee.std_logic_textio.all;
----------------------------------
-------------------------------------------
entity decoder_op_ip is
port(input_dec : in  bit_vector(2 downto 0);
	clk: in bit;
	output_dec : out  bit_vector(7 downto 0)
	);
end decoder_op_ip;

architecture decoder_op_ip_arch of decoder_op_ip is

signal indecoder:bit_vector(2 downto 0) := "000";
signal outdecoder:bit_vector(7 downto 0) := "00000000";
begin

    process(clk)
		--file      outfile  : text is out "file_out_decoder.csv";  --declare output_dec file
   	--	variable  outline  : line;   --line number declaration
		

    begin

        -- clock rising edge

	---if (clk='1' and clk'event) then
	
		
	---end if;
	
	if (clk='1' and clk'event) then
	
		indecoder<=input_dec;
		case indecoder is
			when "111" => outdecoder<="00000001";
			when "110" => outdecoder<="00000010";
			when "101" => outdecoder<="00000100";
			when "100" => outdecoder<="00001000";
			when "011" => outdecoder<="00010000";
			when "010" => outdecoder<="00100000";
			when "001" => outdecoder<="01000000";
			when "000" => outdecoder<="10000000";
			when others => null;
		end case;

	end if;
	
    end process;	
  
  output_dec<=outdecoder;	

end decoder_op_ip_arch;
-----------------------------------------------------------------------------------------------------


