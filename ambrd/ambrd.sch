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
L ATMEGA32U4-M U?
U 1 1 54DB9D8B
P 5750 3800
F 0 "U?" H 4800 5500 40  0000 C CNN
F 1 "ATMEGA32U4-M" H 6450 2300 40  0000 C CNN
F 2 "SMD_Packages:QFN-44-1EP" H 5750 3800 35  0001 C CIN
F 3 "" H 6850 4900 60  0000 C CNN
	1    5750 3800
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X05 P?
U 1 1 54DB9E4E
P 3700 3700
F 0 "P?" H 3700 4000 50  0000 C CNN
F 1 "USB" V 3800 3700 50  0000 C CNN
F 2 "Connect:USB_Micro-B" H 3700 3700 60  0001 C CNN
F 3 "" H 3700 3700 60  0000 C CNN
	1    3700 3700
	-1   0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DB9F2D
P 3400 3200
F 0 "C?" H 3400 3300 40  0000 L CNN
F 1 "10pF" H 3406 3115 40  0000 L CNN
F 2 "" H 3438 3050 30  0000 C CNN
F 3 "" H 3400 3200 60  0000 C CNN
	1    3400 3200
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DB9F7E
P 2800 3200
F 0 "C?" H 2800 3300 40  0000 L CNN
F 1 "10pF" H 2806 3115 40  0000 L CNN
F 2 "" H 2838 3050 30  0000 C CNN
F 3 "" H 2800 3200 60  0000 C CNN
	1    2800 3200
	1    0    0    -1  
$EndComp
$Comp
L CRYSTAL X?
U 1 1 54DB9FB5
P 3100 2900
F 0 "X?" H 3100 3050 60  0000 C CNN
F 1 "16MHz" H 3100 2750 60  0000 C CNN
F 2 "Crystals_Oscillators_SMD:crystal_FA238-TSX3225" H 3100 2900 60  0001 C CNN
F 3 "" H 3100 2900 60  0000 C CNN
	1    3100 2900
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 54DBA17A
P 3000 4750
F 0 "#PWR?" H 3000 4750 30  0001 C CNN
F 1 "GND" H 3000 4680 30  0001 C CNN
F 2 "" H 3000 4750 60  0000 C CNN
F 3 "" H 3000 4750 60  0000 C CNN
	1    3000 4750
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DBA18E
P 4250 3700
F 0 "R?" V 4250 3600 40  0000 C CNN
F 1 "22r" V 4250 3750 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 4180 3700 30  0001 C CNN
F 3 "" H 4250 3700 30  0000 C CNN
	1    4250 3700
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 54DBA1DD
P 4250 3600
F 0 "R?" V 4250 3500 40  0000 C CNN
F 1 "22r" V 4250 3650 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 4180 3600 30  0001 C CNN
F 3 "" H 4250 3600 30  0000 C CNN
	1    4250 3600
	0    1    1    0   
$EndComp
$Comp
L +5V #PWR?
U 1 1 54DBA753
P 3000 3900
F 0 "#PWR?" H 3000 3990 20  0001 C CNN
F 1 "+5V" H 3000 3990 30  0000 C CNN
F 2 "" H 3000 3900 60  0000 C CNN
F 3 "" H 3000 3900 60  0000 C CNN
	1    3000 3900
	1    0    0    -1  
$EndComp
NoConn ~ 3900 3800
Text GLabel 5200 1950 0    50   Input ~ 0
VCC
Text GLabel 3900 3350 0    50   Input ~ 0
VCC
Text GLabel 2950 4000 0    50   Input ~ 0
VCC
Text GLabel 2950 4600 0    50   Input ~ 0
GND
Text GLabel 3900 4100 0    50   Input ~ 0
GND
Text GLabel 4000 2250 0    50   Input ~ 0
RST
Text GLabel 7000 4650 2    50   Input ~ 0
col0
Text GLabel 7000 4750 2    50   Input ~ 0
col1
Text GLabel 7000 4850 2    50   Input ~ 0
col2
Text GLabel 7000 4950 2    50   Input ~ 0
col3
Text GLabel 7000 5050 2    50   Input ~ 0
col4
Text GLabel 7000 5150 2    50   Input ~ 0
col5
Text GLabel 3100 3450 3    50   Input ~ 0
GND
Text GLabel 5250 5450 0    50   Input ~ 0
GND
$Comp
L SW_PUSH SW?
U 1 1 54DBC824
P 3950 2450
F 0 "SW?" H 4100 2560 50  0000 C CNN
F 1 "REPROG" H 3950 2370 50  0000 C CNN
F 2 "" H 3950 2450 60  0000 C CNN
F 3 "" H 3950 2450 60  0000 C CNN
	1    3950 2450
	1    0    0    -1  
$EndComp
Text GLabel 3550 2450 0    50   Input ~ 0
GND
$Comp
L CP2 C?
U 1 1 54DBC933
P 4500 4850
F 0 "C?" H 4500 4950 40  0000 L CNN
F 1 "0.1uF" H 4506 4765 40  0000 L CNN
F 2 "" H 4538 4700 30  0000 C CNN
F 3 "" H 4500 4850 60  0000 C CNN
	1    4500 4850
	1    0    0    -1  
$EndComp
Text GLabel 4500 5150 0    50   Input ~ 0
GND
$Comp
L CP2 C?
U 1 1 54DBCA8A
P 3000 4300
F 0 "C?" H 3000 4400 40  0000 L CNN
F 1 "0.1uF" H 3006 4215 40  0000 L CNN
F 2 "" H 3038 4150 30  0000 C CNN
F 3 "" H 3000 4300 60  0000 C CNN
	1    3000 4300
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBCABB
P 3250 4300
F 0 "C?" H 3250 4400 40  0000 L CNN
F 1 "0.1uF" H 3256 4215 40  0000 L CNN
F 2 "" H 3288 4150 30  0000 C CNN
F 3 "" H 3250 4300 60  0000 C CNN
	1    3250 4300
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBCAD4
P 3500 4300
F 0 "C?" H 3500 4400 40  0000 L CNN
F 1 "0.1uF" H 3506 4215 40  0000 L CNN
F 2 "" H 3538 4150 30  0000 C CNN
F 3 "" H 3500 4300 60  0000 C CNN
	1    3500 4300
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBD987
P 4500 4100
F 0 "C?" H 4500 4200 40  0000 L CNN
F 1 "1uF" H 4506 4015 40  0000 L CNN
F 2 "" H 4538 3950 30  0000 C CNN
F 3 "" H 4500 4100 60  0000 C CNN
	1    4500 4100
	1    0    0    -1  
$EndComp
Text GLabel 4500 4400 0    50   Input ~ 0
GND
$Comp
L LED D?
U 1 1 54DBDEC9
P 7750 4450
F 0 "D?" H 7650 4350 50  0000 C CNN
F 1 "LED" H 7800 4350 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" H 7750 4450 60  0001 C CNN
F 3 "" H 7750 4450 60  0000 C CNN
	1    7750 4450
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DBE1CC
P 7200 4450
F 0 "R?" V 7200 4350 40  0000 C CNN
F 1 "1k" V 7200 4500 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 7130 4450 30  0001 C CNN
F 3 "" H 7200 4450 30  0000 C CNN
	1    7200 4450
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 54DBE34E
P 7200 4350
F 0 "R?" V 7200 4250 40  0000 C CNN
F 1 "1k" V 7200 4400 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 7130 4350 30  0001 C CNN
F 3 "" H 7200 4350 30  0000 C CNN
	1    7200 4350
	0    1    1    0   
$EndComp
Text GLabel 8050 4400 2    50   Input ~ 0
GND
Text GLabel 6950 3450 2    50   Input ~ 0
I2C_SCL
Text GLabel 6950 3550 2    50   Input ~ 0
I2C_SDA
Text GLabel 7000 2250 2    50   Input ~ 0
row0
Text GLabel 7000 2350 2    50   Input ~ 0
row1
Text GLabel 7000 2450 2    50   Input ~ 0
row2
Text GLabel 7000 2550 2    50   Input ~ 0
row3
Text GLabel 7000 2650 2    50   Input ~ 0
row11
Text GLabel 7000 3650 2    50   Input ~ 0
row5
Text GLabel 7000 3750 2    50   Input ~ 0
row6
Text GLabel 7000 2950 2    50   Input ~ 0
row4
Text GLabel 7000 3950 2    50   Input ~ 0
row7
Text GLabel 7000 3850 2    50   Input ~ 0
row8
Text GLabel 7000 4050 2    50   Input ~ 0
row9
Text GLabel 7000 4150 2    50   Input ~ 0
row10
Text GLabel 7000 2750 2    50   Input ~ 0
row12
Text GLabel 7000 2850 2    50   Input ~ 0
row13
Text GLabel 6950 3150 2    50   Input ~ 0
aux0
Text GLabel 6950 3250 2    50   Input ~ 0
aux1
Wire Wire Line
	3400 2850 3400 3000
Wire Wire Line
	2800 2650 2800 3000
Wire Wire Line
	4700 2650 2800 2650
Connection ~ 2800 2900
Wire Wire Line
	4700 2850 3400 2850
Connection ~ 3400 2900
Wire Wire Line
	3900 3600 4000 3600
Wire Wire Line
	3900 3700 4000 3700
Wire Wire Line
	4500 3600 4600 3600
Wire Wire Line
	4500 3700 4600 3700
Wire Wire Line
	3900 3350 3900 3500
Wire Wire Line
	3900 3900 3900 4100
Wire Wire Line
	4600 3450 4050 3450
Wire Wire Line
	4050 3450 4050 3500
Wire Wire Line
	4050 3500 3900 3500
Wire Wire Line
	5300 1950 5300 2000
Wire Wire Line
	5550 1950 5550 2000
Wire Wire Line
	5650 1950 5650 2000
Wire Wire Line
	5900 1950 5900 2000
Wire Wire Line
	6000 1950 6000 2000
Wire Wire Line
	5200 1950 6000 1950
Connection ~ 5900 1950
Connection ~ 5650 1950
Connection ~ 5550 1950
Connection ~ 5300 1950
Wire Wire Line
	2950 4000 3000 4000
Wire Wire Line
	3000 3900 3000 4100
Wire Wire Line
	2950 4600 3000 4600
Wire Wire Line
	3000 4500 3000 4750
Wire Wire Line
	5350 5400 5350 5450
Wire Wire Line
	5250 5450 5900 5450
Wire Wire Line
	5900 5450 5900 5400
Wire Wire Line
	5800 5400 5800 5450
Connection ~ 5800 5450
Wire Wire Line
	5700 5400 5700 5450
Connection ~ 5700 5450
Wire Wire Line
	5600 5400 5600 5450
Connection ~ 5600 5450
Wire Wire Line
	4000 2250 4600 2250
Wire Wire Line
	7000 4650 6850 4650
Wire Wire Line
	7000 4750 6850 4750
Wire Wire Line
	7000 4850 6850 4850
Wire Wire Line
	7000 4950 6850 4950
Wire Wire Line
	7000 5050 6850 5050
Wire Wire Line
	7000 5150 6850 5150
Wire Wire Line
	2800 3400 3400 3400
Wire Wire Line
	3100 3450 3100 3400
Connection ~ 3100 3400
Connection ~ 5350 5450
Wire Wire Line
	4250 2450 4250 2250
Connection ~ 4250 2250
Wire Wire Line
	3550 2450 3650 2450
Wire Wire Line
	4500 4650 4600 4650
Wire Wire Line
	4500 5050 4500 5150
Connection ~ 3000 4000
Wire Wire Line
	3000 4100 3500 4100
Connection ~ 3250 4100
Wire Wire Line
	3000 4500 3500 4500
Connection ~ 3250 4500
Connection ~ 3000 4600
Wire Wire Line
	4600 3850 4500 3850
Wire Wire Line
	4500 3850 4500 3900
Wire Wire Line
	4500 4400 4500 4300
Wire Wire Line
	6850 4350 6950 4350
Wire Wire Line
	6850 4450 6950 4450
Wire Wire Line
	7450 4450 7550 4450
Wire Wire Line
	7450 4350 7950 4350
Wire Wire Line
	7950 4350 7950 4450
Wire Wire Line
	7950 4400 8050 4400
Connection ~ 7950 4400
Wire Wire Line
	6850 3450 6950 3450
Wire Wire Line
	6850 3550 6950 3550
Wire Wire Line
	7000 2250 6850 2250
Wire Wire Line
	7000 2350 6850 2350
Wire Wire Line
	7000 2450 6850 2450
Wire Wire Line
	7000 2550 6850 2550
Wire Wire Line
	6850 2650 7000 2650
Wire Wire Line
	6850 2750 7000 2750
Wire Wire Line
	6850 2850 7000 2850
Wire Wire Line
	6850 2950 7000 2950
Wire Wire Line
	6850 3150 6950 3150
Wire Wire Line
	6850 3250 6950 3250
Wire Wire Line
	6850 3650 7000 3650
Wire Wire Line
	6850 3750 7000 3750
Wire Wire Line
	6850 3850 7000 3850
Wire Wire Line
	6850 3950 7000 3950
Wire Wire Line
	6850 4050 7000 4050
Wire Wire Line
	6850 4150 7000 4150
$Comp
L CONN_02X13 P?
U 1 1 54DC1BBC
P 8550 2750
F 0 "P?" H 8550 3450 50  0000 C CNN
F 1 "LEFT_HAND" V 8550 2750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x13" H 8550 1600 60  0001 C CNN
F 3 "" H 8550 1600 60  0000 C CNN
	1    8550 2750
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X13 P?
U 1 1 54DC1C76
P 9800 2750
F 0 "P?" H 9800 3450 50  0000 C CNN
F 1 "RIGHT_HAND" V 9800 2750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x13" H 9800 1600 60  0001 C CNN
F 3 "" H 9800 1600 60  0000 C CNN
	1    9800 2750
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X03 P?
U 1 1 54DC1D75
P 3750 1850
F 0 "P?" H 3750 2050 50  0000 C CNN
F 1 "PROG" H 3750 1650 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x03" H 3750 650 60  0001 C CNN
F 3 "" H 3750 650 60  0000 C CNN
	1    3750 1850
	1    0    0    -1  
$EndComp
Text GLabel 2950 5000 0    50   Input ~ 0
VCC
Text GLabel 3050 5600 0    50   Input ~ 0
I2C_SCL
Text GLabel 3500 5600 0    50   Input ~ 0
I2C_SDA
$Comp
L R R?
U 1 1 54DC2499
P 3500 5250
F 0 "R?" V 3500 5150 40  0000 C CNN
F 1 "10k" V 3500 5300 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 3430 5250 30  0000 C CNN
F 3 "" H 3500 5250 30  0000 C CNN
	1    3500 5250
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DC2560
P 3050 5250
F 0 "R?" V 3050 5150 40  0000 C CNN
F 1 "10k" V 3050 5300 40  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 2980 5250 30  0001 C CNN
F 3 "" H 3050 5250 30  0000 C CNN
	1    3050 5250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 5000 3500 5000
Connection ~ 3050 5000
Wire Wire Line
	3050 5600 3050 5500
Wire Wire Line
	3500 5600 3500 5500
Text GLabel 3400 1750 0    50   Input ~ 0
MISO
Text GLabel 3400 1850 0    50   Input ~ 0
SCK
Text GLabel 3400 1950 0    50   Input ~ 0
RST
Text GLabel 4100 1750 2    50   Input ~ 0
VCC
Text GLabel 4100 1850 2    50   Input ~ 0
MOSI
Text GLabel 4100 1950 2    50   Input ~ 0
GND
Wire Wire Line
	4100 1950 4000 1950
Wire Wire Line
	4100 1850 4000 1850
Wire Wire Line
	4000 1750 4100 1750
Wire Wire Line
	3500 1750 3400 1750
Wire Wire Line
	3500 1850 3400 1850
Wire Wire Line
	3500 1950 3400 1950
Text GLabel 3800 1300 2    50   Input ~ 0
SCK
Text GLabel 3800 1400 2    50   Input ~ 0
MOSI
Text GLabel 3800 1500 2    50   Input ~ 0
MISO
Text GLabel 3700 1300 0    50   Input ~ 0
row1
Text GLabel 3700 1400 0    50   Input ~ 0
row2
Text GLabel 3700 1500 0    50   Input ~ 0
row3
Wire Wire Line
	3700 1300 3800 1300
Wire Wire Line
	3700 1400 3800 1400
Wire Wire Line
	3700 1500 3800 1500
$EndSCHEMATC
