entity b13 is 
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
end b13;

architecture BEHAV of b13 is

	constant GP001 :integer:=0;
	constant GP010 :integer:=1;
	constant GP011 :integer:=2;
	constant GP100 :integer:=3;
	constant GP100w :integer:=4;
	constant GP101 :integer:=5;
	constant GP110 :integer:=6;
	constant GP111 :integer:=7;

	constant GP01 :integer:=0;
	constant GP10 :integer:=1;
	constant GP11 :integer:=2;
	constant GP11w :integer:=3;

	constant START_BIT :integer:=0;
	constant STOP_BIT :integer:=1;
	constant BIT0 :integer:=2;
	constant BIT1 :integer:=3;
	constant BIT2 :integer:=4;
	constant BIT3 :integer:=5;
	constant BIT4 :integer:=6;
	constant BIT5 :integer:=7;
	constant BIT6 :integer:=8;
	constant BIT7 :integer:=9;

	constant G_IDLE :integer:=0;
	constant G_LOAD :integer:=1;
	constant G_SEND :integer:=2;
	constant G_WAIT_END :integer:=3;

	signal S1 : integer range 7 downto 0;
	signal S2 : integer range 3 downto 0;

	signal mpx,
	       rdy, 
               send_data : bit;

	signal confirm : bit;
	signal shot : bit;

	signal	send_en : bit;
	signal	tre : bit;
	signal	out_reg : bit_vector( 7 downto 0 );
	signal	next_bit : integer range 9 downto 0;
	signal	tx_end : bit;
	signal	itfc_state : integer range 3 downto 0;
	signal	send, load : bit;

	signal	tx_conta : integer range 512 downto 0;

begin

process( reset, clk )
	variable	conta_tmp : integer range 8 downto 0;
begin

if clk'event and clk = '1' then
	if reset = '1' then
		S1 <= GP001;
		Qout_soc <= '0';
		Qout_canale <= 0;
		conta_tmp := 0;
		send_data <= '0';
		Qout_load_dato <= '0';
		Qout_mux_en <= '0';
	else
		case S1 is
			when GP001 =>
				Qout_mux_en <= '1';
				S1 <= GP010;
			when GP010 =>
				S1 <= GP011;
			when GP011 =>
				Qout_soc <= '1';	
				S1 <= GP101;
			when GP101 =>
				if eoc = '1' then
					S1 <= GP101;
				else
					Qout_load_dato <= '1';
					S1 <= GP110;
					Qout_mux_en <= '0';
				end if;
			when GP110 =>
				Qout_load_dato <= '0';
				Qout_soc <= '0';			
				conta_tmp := conta_tmp+1;
				if conta_tmp = 8 then
					conta_tmp := 0;
				end if;
				Qout_canale <= conta_tmp;
				S1 <= GP111;
			when GP111 =>
				send_data <= '1';
				S1 <= GP100w;
			when GP100w =>
				S1 <= GP100;
			when GP100 =>
				if rdy = '0' then
					S1 <= GP100;
				else
					S1 <= GP001;
					send_data <= '0';
				end if;
			when others =>
		end case;
	end if;
	end if;
end process;

process (reset, clk )
begin
if clk'event and clk = '1' then
	if  reset = '1'  then
		S2 <= GP01;
		rdy <= '0';
		Qout_add_mpx2 <='0';
		mpx <= '0';
		shot <= '0';
	else
		case S2 is
			when GP01 =>  
				if send_data = '1' then
					rdy <= '1';
					S2 <= GP10;
				else
					S2 <= GP01;
				end if;
			when GP10 => 
				shot <= '1';
				S2 <= GP11;
			when GP11 => 
				if confirm = '0' then
					shot <= '0';
					S2 <= GP11;
				else 
					if mpx = '0' then
						Qout_add_mpx2 <= '1';
						mpx <= '1';
						S2 <= GP10;
					else
						mpx <= '0';
						rdy <= '0';
						S2 <= GP11w;
					end if;
				end if;
			when GP11w =>
				S2 <= GP01;
			when others => 
		end case;
	end if;
	end if;
end process;


process( clk, reset )
begin
if clk'event and clk = '1' then
	if reset = '1' then
		load <= '0'; 
		send <= '0';
		confirm <= '0';
		itfc_state <= G_IDLE;
	else
		case itfc_state is
			when G_IDLE =>
				if shot = '1' then
					load <= '1';
					confirm <= '0';
					itfc_state <= G_LOAD;
				else
					confirm <= '0';
					itfc_state <= G_IDLE;
				end if;
			when G_LOAD =>
				load <= '0';
				send <= '1';
				itfc_state <= G_SEND;
			when G_SEND =>
				send <= '0';
				itfc_state <= G_WAIT_END;
			when G_WAIT_END =>
				if tx_end = '1' then
					confirm <= '1';
					itfc_state <= G_IDLE;
				end if;
			when others =>
		end case;
	end if;
	end if;
end process;
					
process( clk, reset )
begin
	if clk'event and clk = '1' then
	if reset ='1' then
		send_en <= '0';
		out_reg <= "00000000";
		tre <= '0';
		Qout_error_sig <= '0';
	else
		if tx_end = '1' then
			send_en <= '0';
			tre <= '1';
		end if;

		if load = '1' then
			if tre = '0' then
				out_reg <= data_in;
				tre <= '1';
				Qout_error_sig <= '0';
			else
				Qout_error_sig <= '1';
			end if;
		end if;

		if send = '1' then
			if tre = '0' or dsr = '0' then 
				Qout_error_sig <= '1';
			else
				Qout_error_sig <= '0';		
				send_en <= '1';
			end if;
		end if;
	end if;
	end if;
end process;
	
process( clk, reset )
	constant DelayTime : integer := 104;
begin
	if clk'event and clk = '1' then
	if reset = '1' then
		tx_end <= '0';
		Qout_data <= '0';
		next_bit <= START_BIT;

		tx_conta <= 0;
	else
		tx_end <= '0';
		Qout_data <= '1';
		if send_en = '1' then		
			if tx_conta > DelayTime then
				case next_bit is
					when START_BIT =>
						Qout_data <= '0';
						next_bit <= BIT0;
					when BIT0 =>
						Qout_data <= out_reg( 7 );
						next_bit <= BIT1;	
					when BIT1 =>
						Qout_data <= out_reg( 6 );
						next_bit <= BIT2;	
					when BIT2 =>
						Qout_data <= out_reg( 5 );
						next_bit <= BIT3;	
					when BIT3 =>
						Qout_data <= out_reg( 4 );
						next_bit <= BIT4;	
					when BIT4 =>
						Qout_data <= out_reg( 3 );
						next_bit <= BIT5;	
					when BIT5 =>
						Qout_data <= out_reg( 2 );
						next_bit <= BIT6;	
					when BIT6 =>
						Qout_data <= out_reg( 1 );
						next_bit <= BIT7;	
					when BIT7 =>
						Qout_data <= out_reg( 0 );
						next_bit <= STOP_BIT;	
					when STOP_BIT =>
						Qout_data <= '1';
						next_bit <= START_BIT;
						tx_end <= '1';
				end case;
				tx_conta <= 0;
			else
				tx_conta <= tx_conta+1;
			end if;
		end if;
	end if;
	end if;
end process;
end BEHAV;
