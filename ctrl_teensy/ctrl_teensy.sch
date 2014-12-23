EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:ctrl_teensy
LIBS:ctrl_teensy-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_01X13 P3
U 1 1 54984863
P 6600 4100
F 0 "P3" H 6600 4800 50  0000 C CNN
F 1 "CONN_01X13" V 6700 4100 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x13" H 6600 4100 60  0001 C CNN
F 3 "" H 6600 4100 60  0000 C CNN
	1    6600 4100
	-1   0    0    -1  
$EndComp
Text GLabel 6800 3500 2    60   BiDi ~ 0
col5
Text GLabel 6800 3600 2    60   BiDi ~ 0
col4
Text GLabel 6800 3700 2    60   BiDi ~ 0
col3
Text GLabel 6800 3800 2    60   BiDi ~ 0
col2
Text GLabel 6800 3900 2    60   BiDi ~ 0
col1
Text GLabel 6800 4000 2    60   BiDi ~ 0
col0
Text GLabel 6800 4100 2    60   BiDi ~ 0
row0
Text GLabel 6800 4200 2    60   BiDi ~ 0
row1
Text GLabel 6800 4300 2    60   BiDi ~ 0
row2
Text GLabel 6800 4400 2    60   BiDi ~ 0
row3
Text GLabel 6800 4500 2    60   BiDi ~ 0
row4
Text GLabel 6800 4600 2    60   BiDi ~ 0
row5
Text GLabel 6800 4700 2    60   BiDi ~ 0
row6
Text GLabel 5500 4000 0    60   BiDi ~ 0
col0
Text GLabel 5500 3900 0    60   BiDi ~ 0
col1
Text GLabel 5500 3800 0    60   BiDi ~ 0
col2
Text GLabel 5500 3700 0    60   BiDi ~ 0
col3
Text GLabel 5500 3600 0    60   BiDi ~ 0
col4
$Comp
L CONN_01X13 P2
U 1 1 54984707
P 5700 4100
F 0 "P2" H 5700 4800 50  0000 C CNN
F 1 "CONN_01X13" V 5800 4100 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x13" H 5700 4100 60  0001 C CNN
F 3 "" H 5700 4100 60  0000 C CNN
	1    5700 4100
	1    0    0    -1  
$EndComp
Text GLabel 5500 3500 0    60   BiDi ~ 0
col5
Text GLabel 5500 4100 0    60   BiDi ~ 0
rowD
Text GLabel 5500 4200 0    60   BiDi ~ 0
rowC
Text GLabel 5500 4300 0    60   BiDi ~ 0
rowB
Text GLabel 5500 4400 0    60   BiDi ~ 0
rowA
Text GLabel 5500 4500 0    60   BiDi ~ 0
row9
Text GLabel 5500 4600 0    60   BiDi ~ 0
row8
Text GLabel 5500 4700 0    60   BiDi ~ 0
row7
$Comp
L teensy U1
U 1 1 54985B7B
P 6150 2150
F 0 "U1" H 6150 2800 60  0000 C CNN
F 1 "teensy" H 6150 2150 60  0000 C CNN
F 2 "teensy:teensy_2.0" H 6000 2300 60  0001 C CNN
F 3 "" H 6000 2300 60  0000 C CNN
	1    6150 2150
	1    0    0    -1  
$EndComp
Text GLabel 6750 1700 2    60   BiDi ~ 0
row6
Text GLabel 6750 1800 2    60   BiDi ~ 0
row5
Text GLabel 6750 1900 2    60   BiDi ~ 0
row4
Text GLabel 6750 2000 2    60   BiDi ~ 0
row3
Text GLabel 6750 2100 2    60   BiDi ~ 0
row2
Text GLabel 6750 2200 2    60   BiDi ~ 0
row1
Text GLabel 6750 2500 2    60   BiDi ~ 0
row0
NoConn ~ 6750 2700
Text GLabel 6750 1600 2    60   Input ~ 0
VCC
Text GLabel 5550 1600 0    60   Input ~ 0
GND
Text GLabel 5550 1700 0    60   BiDi ~ 0
row7
Text GLabel 5550 1800 0    60   BiDi ~ 0
row8
Text GLabel 5550 1900 0    60   BiDi ~ 0
row9
Text GLabel 5550 2000 0    60   BiDi ~ 0
rowA
Text GLabel 5550 2400 0    60   BiDi ~ 0
col5
Text GLabel 5550 2100 0    60   BiDi ~ 0
rowB
Text GLabel 5550 2200 0    60   BiDi ~ 0
rowC
NoConn ~ 6050 3050
NoConn ~ 6150 3050
NoConn ~ 6250 3050
Text GLabel 5550 2300 0    60   BiDi ~ 0
rowD
Text GLabel 5550 2500 0    60   BiDi ~ 0
col4
Text GLabel 5550 2600 0    60   BiDi ~ 0
col3
Text GLabel 5550 2700 0    60   BiDi ~ 0
col2
Text GLabel 6350 3050 3    60   BiDi ~ 0
col0
$Comp
L R R_left1
U 1 1 54986164
P 7550 2200
F 0 "R_left1" V 7630 2200 40  0000 C CNN
F 1 "220R" V 7557 2201 40  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM15mm" V 7480 2200 30  0001 C CNN
F 3 "" H 7550 2200 30  0000 C CNN
	1    7550 2200
	0    1    1    0   
$EndComp
$Comp
L R R_right1
U 1 1 549861D9
P 7550 2500
F 0 "R_right1" V 7630 2500 40  0000 C CNN
F 1 "220R" V 7557 2501 40  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM15mm" V 7480 2500 30  0001 C CNN
F 3 "" H 7550 2500 30  0000 C CNN
	1    7550 2500
	0    1    1    0   
$EndComp
Wire Wire Line
	6750 2400 7200 2400
Wire Wire Line
	7200 2400 7200 2500
Wire Wire Line
	7200 2500 7300 2500
Wire Wire Line
	6750 2300 7200 2300
Wire Wire Line
	7200 2300 7200 2200
Wire Wire Line
	7200 2200 7300 2200
Text GLabel 7800 2200 2    60   Output ~ 0
ledL
Text GLabel 7800 2500 2    60   Output ~ 0
ledR
$Comp
L CONN_01X02 P4
U 1 1 549862E6
P 7300 3550
F 0 "P4" H 7300 3700 50  0000 C CNN
F 1 "CONN_01X02" V 7400 3550 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 7300 3550 60  0001 C CNN
F 3 "" H 7300 3550 60  0000 C CNN
	1    7300 3550
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X02 P1
U 1 1 549863B3
P 5000 3550
F 0 "P1" H 5000 3700 50  0000 C CNN
F 1 "CONN_01X02" V 5100 3550 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 5000 3550 60  0001 C CNN
F 3 "" H 5000 3550 60  0000 C CNN
	1    5000 3550
	1    0    0    -1  
$EndComp
Text GLabel 7500 3600 2    60   Input ~ 0
GND
Text GLabel 7500 3500 2    60   Output ~ 0
ledL
Text GLabel 4800 3500 0    60   Input ~ 0
GND
Text GLabel 4800 3600 0    60   Output ~ 0
ledR
Text GLabel 5950 3050 3    60   BiDi ~ 0
col1
NoConn ~ 6750 2600
$EndSCHEMATC
