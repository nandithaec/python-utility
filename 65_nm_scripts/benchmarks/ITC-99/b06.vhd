entity b06 is
 port (Qout_cc_mux : out bit_vector(2 downto 1);
	   eql: in bit;
	   Qout_uscite: out bit_vector(2 downto 1);
	   clk: in bit;
	   Qout_enable_count: out bit;
	   Qout_ackout: out bit;
	   reset: in bit; 
	   cont_eql: in bit);

end b06;

architecture BEHAV of b06 is

constant s_init:integer:=0;
constant s_wait:integer:=1;
constant s_enin:integer:=2;
constant s_enin_w:integer:=3;
constant s_intr:integer:=4;
constant s_intr_1:integer:=5;
constant s_intr_w:integer:=6;

 begin
   process(reset, clk)
	variable state: integer range 6 downto 0;
	
	constant cc_nop: bit_vector(2 downto 1) := "01";
	constant cc_enin: bit_vector(2 downto 1) :="01";
	constant cc_intr: bit_vector(2 downto 1) :="10";
	constant cc_ackin: bit_vector(2 downto 1) :="11";
	constant out_norm: bit_vector(2 downto 1) :="01"; 

 begin
 if clk'event and clk='1' then	
   if reset = '1' then
	state := s_init;
	Qout_cc_mux <= "00";
	Qout_enable_count <= '0';
	Qout_ackout <= '0';
	Qout_uscite <= "00";
   else
	if cont_eql = '1' then
	 Qout_ackout <= '0';
	 Qout_enable_count <= '0';
	else
	 Qout_ackout <= '1';
	 Qout_enable_count <= '1';
	end if;
	
	case state is
   
	 when s_init =>
		Qout_cc_mux <= cc_enin;
		Qout_uscite <= out_norm;
		state := s_wait;
	 
	 when s_wait =>
	 if eql = '1' then
		Qout_uscite <= "00";
		Qout_cc_mux <= cc_ackin;
		state := s_enin;
	 else
		Qout_uscite <= out_norm;
		Qout_cc_mux <= cc_intr;
		state := s_intr_1;
	 end if;

	 when s_intr_1 =>
	 if eql = '1'then
		Qout_uscite <="00";
		Qout_cc_mux <= cc_ackin;
		state := s_intr;
	 else
		Qout_uscite <= out_norm;
		Qout_cc_mux <= cc_enin;
		state := s_wait;
	 end if;

	 when s_enin =>
	 if eql = '1' then
		Qout_uscite <= "00";
		Qout_cc_mux <= cc_ackin;
		state := s_enin;
	 else
		Qout_uscite <= "01";
		Qout_ackout <= '1';
		Qout_enable_count <= '1';
		Qout_cc_mux <= cc_enin;
		state := s_enin_w;
	 end if;

	 when s_enin_w =>
	 if eql = '1' then
		Qout_uscite <= "01";
		Qout_cc_mux <= cc_enin;
		state := s_enin_w;
	 else
		Qout_uscite <= out_norm;
		Qout_cc_mux <= cc_enin;
		state := s_wait;
	 end if;

	 when s_intr =>
	 if eql = '1' then
		Qout_uscite <= "00";
		Qout_cc_mux <= cc_ackin;
		state := s_intr;
	 else
		Qout_uscite <= "11";
		Qout_cc_mux <= cc_intr;
		state := s_intr_w;
	 end if;

	 when s_intr_w =>
	 if eql = '1' then
		Qout_uscite <= "11";
		Qout_cc_mux <= cc_intr;
		state := s_intr_w;
	 else
		Qout_uscite <= out_norm;
		Qout_cc_mux <= cc_enin;
		state := s_wait;
	 end if;

	end case;
   end if;
   end if;
 end process;
end BEHAV;
