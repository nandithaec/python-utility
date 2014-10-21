
.subckt AND2X1 A B 0 Y vdd
*corrected
**Vvdd vdd 0 1.8

M0 a_2_6# A vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_2_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_9_6# A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 0 B a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_6# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends AND2X1

.subckt AND2X2  A B 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0

M0 a_2_6# A vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_2_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_9_6# A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 0 B a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends AND2X2

.subckt AOI21X1 A B C 0 Y vdd
M0 vdd A a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_2_54# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y C a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_12_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 Y B a_12_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 C Y 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends AOI21X1

.subckt AOI22X1 A B C D 0 Y vdd
*corrected

M0 vdd A a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_2_54# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y D a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_2_54# C Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_11_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y B a_11_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_28_6# D Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 0 C a_28_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends AOI22X1

.subckt BUFX2 A 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd A a_2_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y a_2_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 0 A a_2_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 Y a_2_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends BUFX2

.subckt BUFX4 A 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd A a_2_6# vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y a_2_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 vdd a_2_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 0 A a_2_6# 0 nfet w=1.5u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 Y a_2_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 a_2_6# Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends BUFX4

.subckt CLKBUF1 A 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_6# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd A a_9_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_25_6# a_9_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd a_9_6# a_25_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_41_6# a_25_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 vdd a_25_6# a_41_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Y a_41_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 vdd a_41_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_9_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 0 A a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 a_25_6# a_9_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 0 a_9_6# a_25_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_41_6# a_25_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 0 a_25_6# a_41_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 Y a_41_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 0 a_41_6# Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends CLKBUF1

.subckt CLKBUF2 vdd 0 A Y
M0 a_9_6# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd A a_9_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_25_6# a_9_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd a_9_6# a_25_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_41_6# a_25_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 vdd a_25_6# a_41_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_57_6# a_41_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 vdd a_41_6# a_57_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_73_6# a_57_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 vdd a_57_6# a_73_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 Y a_73_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 vdd a_73_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_9_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 0 A a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 a_25_6# a_9_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 0 a_9_6# a_25_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_41_6# a_25_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 0 a_25_6# a_41_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 a_57_6# a_41_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 0 a_41_6# a_57_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 a_73_6# a_57_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 0 a_57_6# a_73_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M22 Y a_73_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M23 0 a_73_6# Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends CLKBUF2

.subckt CLKBUF3 0 vdd A Y
M0 a_9_6# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd A a_9_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_25_6# a_9_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd a_9_6# a_25_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_41_6# a_25_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 vdd a_25_6# a_41_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_57_6# a_41_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 vdd a_41_6# a_57_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_73_6# a_57_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 vdd a_57_6# a_73_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 a_89_6# a_73_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 vdd a_73_6# a_89_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_105_6# a_89_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 vdd a_89_6# a_105_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 Y a_105_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 vdd a_105_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_9_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 0 A a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 a_25_6# a_9_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 0 a_9_6# a_25_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 a_41_6# a_25_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 0 a_25_6# a_41_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M22 a_57_6# a_41_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M23 0 a_41_6# a_57_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M24 a_73_6# a_57_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M25 0 a_57_6# a_73_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M26 a_89_6# a_73_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M27 0 a_73_6# a_89_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M28 a_105_6# a_89_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M29 0 a_89_6# a_105_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M30 Y a_105_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M31 0 a_105_6# Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends CLKBUF3

.subckt DFFNEGX1 CLK vdd D 0 Q
M0 vdd CLK a_2_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_17_74# D vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_23_6# a_2_6# a_17_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_31_74# CLK a_23_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd a_34_4# a_31_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_34_4# a_23_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_61_74# a_34_4# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_66_6# CLK a_61_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_76_84# a_2_6# a_66_6# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 vdd Q a_76_84# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 0 CLK a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 Q a_66_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_17_6# D 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 a_23_6# CLK a_17_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 a_31_6# a_2_6# a_23_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 0 a_34_4# a_31_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_34_4# a_23_6# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 a_61_6# a_34_4# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 a_66_6# a_2_6# a_61_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 a_76_6# CLK a_66_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 0 Q a_76_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 Q a_66_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends DFFNEGX1

.subckt DFFPOSX1 Q CLK D 0 vdd


*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd CLK a_2_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_17_74# D vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_22_6# CLK a_17_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_31_74# a_2_6# a_22_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd a_34_4# a_31_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_34_4# a_22_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_61_74# a_34_4# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_66_6# a_2_6# a_61_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_76_84# CLK a_66_6# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 vdd Q a_76_84# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 0 CLK a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 Q a_66_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_17_6# D 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 a_22_6# a_2_6# a_17_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 a_31_6# CLK a_22_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 0 a_34_4# a_31_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_34_4# a_22_6# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 a_61_6# a_34_4# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 a_66_6# CLK a_61_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 a_76_6# a_2_6# a_66_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 0 Q a_76_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 Q a_66_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends DFFPOSX1

.subckt DFFSR Q CLK R S D 0 vdd

M0 a_2_6# R vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd a_10_61# a_2_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_10_61# a_23_27# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd S a_10_61# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_23_27# a_47_71# a_2_6# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_57_6# a_47_4# a_23_27# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 vdd D a_57_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 vdd a_47_71# a_47_4# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_47_71# CLK vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_105_6# a_47_71# a_10_61# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 a_113_6# a_47_4# a_105_6# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_122_6# a_105_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 vdd R a_122_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 a_113_6# a_122_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 vdd S a_113_6# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 vdd a_122_6# Q vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_10_6# R a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 0 a_10_61# a_10_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 a_26_6# a_23_27# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 a_10_61# S a_26_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 a_23_27# a_47_4# a_2_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 a_57_6# a_47_71# a_23_27# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M22 0 D a_57_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M23 0 a_47_71# a_47_4# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M24 a_47_71# CLK 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M25 a_105_6# a_47_4# a_10_61# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M26 a_113_6# a_47_71# a_105_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M27 a_130_6# a_105_6# a_122_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M28 0 R a_130_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M29 a_146_6# a_122_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M30 a_113_6# S a_146_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M31 0 a_122_6# Q 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends DFFSR

.subckt FAX1 YC YS A B C 0 vdd

M0 vdd A a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_2_54# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_25_6# C a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_33_54# B a_25_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd A a_33_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_46_54# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 vdd B a_46_54# vdd pfet w=3.6u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_46_54# C vdd vdd pfet w=3.6u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_70_6# a_25_6# a_46_54# vdd pfet w=3.6u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_79_46# C a_70_6# vdd pfet w=4.8u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 a_84_46# B a_79_46# vdd pfet w=4.8u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 vdd A a_84_46# vdd pfet w=4.8u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 YS a_70_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 YC a_25_6# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M14 0 A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M15 a_2_6# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M16 a_25_6# C a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M17 a_33_6# B a_25_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M18 0 A a_33_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M19 a_46_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M20 0 B a_46_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M21 a_46_6# C 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M22 a_70_6# a_25_6# a_46_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M23 a_79_6# C a_70_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M24 a_84_6# B a_79_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M25 0 A a_84_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M26 YS a_70_6# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M27 YC a_25_6# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends FAX1

.subckt HAX1 YC YS A B 0 vdd

M0 vdd A a_2_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_2_74# B vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 vdd a_2_74# YC vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_41_74# a_2_74# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_49_54# B a_41_74# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 vdd A a_49_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 YS a_41_74# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_9_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_2_74# B a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 0 a_2_74# YC 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 a_38_6# a_2_74# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_41_74# B a_38_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M12 a_38_6# A a_41_74# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M13 YS a_41_74# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends HAX1

.subckt INVX1 A 0 Y vdd


*Vvdd vdd 0 1.8
*V0 0 0 0


M0 Y A vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y A 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends INVX1

.subckt INVX2 A 0 Y vdd
*corrected

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 Y A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends INVX2

.subckt INVX4 A gnd Y vdd
*corrected

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 Y A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd A Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 0 A Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends INVX4

.subckt INVX8  A 0 Y vdd
*corrected

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 Y A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd A Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd A Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 Y A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 A Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Y A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 0 A Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends INVX8

.subckt LATCH D Q  CLK

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd CLK a_2_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_18_74# D vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_23_6# a_2_6# a_18_74# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_35_84# CLK a_23_6# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd Q a_35_84# vdd pfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 CLK a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Q a_23_6# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# D 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_23_6# CLK a_18_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_35_6# a_2_6# a_23_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 0 Q a_35_6# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 Q a_23_6# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends LATCH

.subckt MUX2X1 A B S 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd S a_2_10# vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_17_50# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y S a_17_50# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_30_54# a_2_10# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd A a_30_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 S a_2_10# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 a_17_10# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 Y a_2_10# a_17_10# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 a_30_10# S Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 0 A a_30_10# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends MUX2X1

.subckt NAND2X1  A B 0 Y vdd
**corrected



M0 Y A vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B Y vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_9_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 Y B a_9_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends NAND2X1

.subckt NAND3X1 A B C 0 Y vdd


*Vvdd vdd 0 1.8
*V0 0 0 0


M0 Y A vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B Y vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y C vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_9_6# A 0 0 nfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_14_6# B a_9_6# 0 nfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y C a_14_6# 0 nfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends NAND3X1

.subckt NOR2X1  A B 0 Y vdd
**corrected

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_54# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y B a_9_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 0 B Y 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends NOR2X1

.subckt NOR3X1 A B C 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd A a_2_64# vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_2_64# A vdd vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_25_64# B a_2_64# vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_2_64# B a_25_64# vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 Y C a_25_64# vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_25_64# C Y vdd pfet w=3u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Y A 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 0 B Y 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 Y C 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends NOR3X1

.subckt OAI21X1  A B C 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_54# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y B a_9_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 vdd C Y vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 0 A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_2_6# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y C a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends OAI21X1

.subckt OAI22X1  A B C D 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_54# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y B a_9_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_28_54# D Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd C a_28_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 0 A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_2_6# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Y D a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_2_6# C Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends OAI22X1

.subckt OR2X1 A B 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_54# A a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_9_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_54# vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_2_54# A 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 0 B a_2_54# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_54# 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends OR2X1

.subckt OR2X2 A B 0 Y vdd

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_54# A a_2_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 vdd B a_9_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_54# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_2_54# A 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 0 B a_2_54# 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 Y a_2_54# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends OR2X2

.subckt TBUFX1 EN A Y

*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_6# EN vdd vdd pfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_26_54# a_9_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 vdd A a_26_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_9_6# EN 0 0 nfet w=1u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_26_6# EN Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 0 A a_26_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends TBUFX1

.subckt TBUFX2 A EN Y


*Vvdd vdd 0 1.8
*V0 0 0 0


M0 a_9_6# EN vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 Y a_9_6# a_18_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 a_18_54# a_9_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 vdd A a_18_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 a_18_54# A vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_9_6# EN 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 Y EN a_18_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# EN Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 0 A a_18_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_18_6# A 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends TBUFX2

.subckt XNOR2X1 A B 0 Y vdd

*Corrected
*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd A a_2_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_18_54# a_12_41# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y a_2_6# a_18_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_35_54# A Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd B a_35_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_12_41# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 0 A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# a_12_41# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 Y A a_18_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_35_6# a_2_6# Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 0 B a_35_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_12_41# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends XNOR2X1

.subckt XOR2X1 A B 0 Y vdd

*Corrected
*Vvdd vdd 0 1.8
*V0 0 0 0


M0 vdd A a_2_6# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M1 a_18_54# a_13_43# vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M2 Y A a_18_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M3 a_35_54# a_2_6# Y vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M4 vdd B a_35_54# vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M5 a_13_43# B vdd vdd pfet w=4u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M6 0 A a_2_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M7 a_18_6# a_13_43# 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M8 Y a_2_6# a_18_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M9 a_35_6# A Y 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M10 0 B a_35_6# 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
M11 a_13_43# B 0 0 nfet w=2u l=0.2u
+ ad=0p pd=0u as=0p ps=0u 
.ends XOR2X1




