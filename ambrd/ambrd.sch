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
LIBS:dmcewan
LIBS:ambrd-cache
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
P 4200 5250
F 0 "U?" H 3250 6950 40  0000 C CNN
F 1 "ATMEGA32U4-M" H 4900 3750 40  0000 C CNN
F 2 "dmcewan:atmega32u4_qfn44" H 4200 5250 35  0001 C CIN
F 3 "" H 5300 6350 60  0000 C CNN
	1    4200 5250
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X05 P?
U 1 1 54DB9E4E
P 2150 5150
F 0 "P?" H 2150 5450 50  0000 C CNN
F 1 "USB" V 2250 5150 50  0000 C CNN
F 2 "Connect:USB_Micro-B" H 2150 5150 60  0001 C CNN
F 3 "" H 2150 5150 60  0000 C CNN
	1    2150 5150
	-1   0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DB9F2D
P 1850 4650
F 0 "C?" H 1850 4750 40  0000 L CNN
F 1 "10pF" H 1856 4565 40  0000 L CNN
F 2 "dmcewan:0603" H 1888 4500 30  0001 C CNN
F 3 "" H 1850 4650 60  0000 C CNN
	1    1850 4650
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DB9F7E
P 1250 4650
F 0 "C?" H 1250 4750 40  0000 L CNN
F 1 "10pF" H 1256 4565 40  0000 L CNN
F 2 "dmcewan:0603" H 1288 4500 30  0001 C CNN
F 3 "" H 1250 4650 60  0000 C CNN
	1    1250 4650
	1    0    0    -1  
$EndComp
$Comp
L CRYSTAL X?
U 1 1 54DB9FB5
P 1550 4350
F 0 "X?" H 1550 4500 60  0000 C CNN
F 1 "16MHz" H 1550 4200 60  0000 C CNN
F 2 "dmcewan:tcxo_4smd_320x250" H 1550 4350 60  0001 C CNN
F 3 "" H 1550 4350 60  0000 C CNN
	1    1550 4350
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 54DBA17A
P 1450 6200
F 0 "#PWR?" H 1450 6200 30  0001 C CNN
F 1 "GND" H 1450 6130 30  0001 C CNN
F 2 "" H 1450 6200 60  0000 C CNN
F 3 "" H 1450 6200 60  0000 C CNN
	1    1450 6200
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DBA18E
P 2700 5150
F 0 "R?" V 2700 5050 40  0000 C CNN
F 1 "22r" V 2700 5200 40  0000 C CNN
F 2 "dmcewan:0603" V 2630 5150 30  0001 C CNN
F 3 "" H 2700 5150 30  0000 C CNN
	1    2700 5150
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 54DBA1DD
P 2700 5050
F 0 "R?" V 2700 4950 40  0000 C CNN
F 1 "22r" V 2700 5100 40  0000 C CNN
F 2 "dmcewan:0603" V 2630 5050 30  0001 C CNN
F 3 "" H 2700 5050 30  0000 C CNN
	1    2700 5050
	0    1    1    0   
$EndComp
$Comp
L +5V #PWR?
U 1 1 54DBA753
P 1450 5350
F 0 "#PWR?" H 1450 5440 20  0001 C CNN
F 1 "+5V" H 1450 5440 30  0000 C CNN
F 2 "" H 1450 5350 60  0000 C CNN
F 3 "" H 1450 5350 60  0000 C CNN
	1    1450 5350
	1    0    0    -1  
$EndComp
NoConn ~ 2350 5250
Text GLabel 3650 3400 0    50   Input ~ 0
VCC
Text GLabel 2350 4800 0    50   Input ~ 0
VCC
Text GLabel 1400 5450 0    50   Input ~ 0
VCC
Text GLabel 1400 6050 0    50   Input ~ 0
GND
Text GLabel 2350 5550 0    50   Input ~ 0
GND
Text GLabel 2450 3700 0    50   Input ~ 0
RST
Text GLabel 5450 6100 2    50   Input ~ 0
col0
Text GLabel 5450 6200 2    50   Input ~ 0
col1
Text GLabel 5450 6300 2    50   Input ~ 0
col2
Text GLabel 5450 6400 2    50   Input ~ 0
col3
Text GLabel 5450 6500 2    50   Input ~ 0
col4
Text GLabel 5450 6600 2    50   Input ~ 0
col5
Text GLabel 1550 4900 3    50   Input ~ 0
GND
Text GLabel 3700 6900 0    50   Input ~ 0
GND
$Comp
L SW_PUSH SW?
U 1 1 54DBC824
P 2400 3900
F 0 "SW?" H 2550 4010 50  0000 C CNN
F 1 "REPROG" H 2400 3820 50  0000 C CNN
F 2 "dmcewan:smd_pushsw_6x6" H 2400 3900 60  0001 C CNN
F 3 "" H 2400 3900 60  0000 C CNN
	1    2400 3900
	1    0    0    -1  
$EndComp
Text GLabel 2000 3900 0    50   Input ~ 0
GND
$Comp
L CP2 C?
U 1 1 54DBC933
P 2950 6300
F 0 "C?" H 2950 6400 40  0000 L CNN
F 1 "0.1uF" H 2956 6215 40  0000 L CNN
F 2 "dmcewan:0603" H 2988 6150 30  0001 C CNN
F 3 "" H 2950 6300 60  0000 C CNN
	1    2950 6300
	1    0    0    -1  
$EndComp
Text GLabel 2950 6600 0    50   Input ~ 0
GND
$Comp
L CP2 C?
U 1 1 54DBCA8A
P 1450 5750
F 0 "C?" H 1450 5850 40  0000 L CNN
F 1 "0.1uF" H 1456 5665 40  0000 L CNN
F 2 "dmcewan:0603" H 1488 5600 30  0001 C CNN
F 3 "" H 1450 5750 60  0000 C CNN
	1    1450 5750
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBCABB
P 1700 5750
F 0 "C?" H 1700 5850 40  0000 L CNN
F 1 "0.1uF" H 1706 5665 40  0000 L CNN
F 2 "dmcewan:0603" H 1738 5600 30  0001 C CNN
F 3 "" H 1700 5750 60  0000 C CNN
	1    1700 5750
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBCAD4
P 1950 5750
F 0 "C?" H 1950 5850 40  0000 L CNN
F 1 "0.1uF" H 1956 5665 40  0000 L CNN
F 2 "dmcewan:0603" H 1988 5600 30  0001 C CNN
F 3 "" H 1950 5750 60  0000 C CNN
	1    1950 5750
	1    0    0    -1  
$EndComp
$Comp
L CP2 C?
U 1 1 54DBD987
P 2950 5550
F 0 "C?" H 2950 5650 40  0000 L CNN
F 1 "1uF" H 2956 5465 40  0000 L CNN
F 2 "dmcewan:0603" H 2988 5400 30  0001 C CNN
F 3 "" H 2950 5550 60  0000 C CNN
	1    2950 5550
	1    0    0    -1  
$EndComp
Text GLabel 2950 5850 0    50   Input ~ 0
GND
$Comp
L LED D?
U 1 1 54DBDEC9
P 6200 5900
F 0 "D?" H 6100 5800 50  0000 C CNN
F 1 "LED" H 6250 5800 50  0000 C CNN
F 2 "dmcewan:0603" H 6200 5900 60  0001 C CNN
F 3 "" H 6200 5900 60  0000 C CNN
	1    6200 5900
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DBE1CC
P 5650 5900
F 0 "R?" V 5650 5800 40  0000 C CNN
F 1 "1k" V 5650 5950 40  0000 C CNN
F 2 "dmcewan:0603" V 5580 5900 30  0001 C CNN
F 3 "" H 5650 5900 30  0000 C CNN
	1    5650 5900
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 54DBE34E
P 5650 5800
F 0 "R?" V 5650 5700 40  0000 C CNN
F 1 "1k" V 5650 5850 40  0000 C CNN
F 2 "dmcewan:0603" V 5580 5800 30  0001 C CNN
F 3 "" H 5650 5800 30  0000 C CNN
	1    5650 5800
	0    1    1    0   
$EndComp
Text GLabel 6500 5850 2    50   Input ~ 0
GND
Text GLabel 5400 4900 2    50   Input ~ 0
I2C_SCL
Text GLabel 5400 5000 2    50   Input ~ 0
I2C_SDA
Text GLabel 5450 3700 2    50   Input ~ 0
row0
Text GLabel 5450 3800 2    50   Input ~ 0
row1
Text GLabel 5450 3900 2    50   Input ~ 0
row2
Text GLabel 5450 4000 2    50   Input ~ 0
row3
Text GLabel 5450 4100 2    50   Input ~ 0
row11
Text GLabel 5450 5100 2    50   Input ~ 0
row5
Text GLabel 5450 5200 2    50   Input ~ 0
row6
Text GLabel 5450 4400 2    50   Input ~ 0
row4
Text GLabel 5450 5400 2    50   Input ~ 0
row7
Text GLabel 5450 5300 2    50   Input ~ 0
row8
Text GLabel 5450 5500 2    50   Input ~ 0
row9
Text GLabel 5450 5600 2    50   Input ~ 0
row10
Text GLabel 5450 4200 2    50   Input ~ 0
row12
Text GLabel 5450 4300 2    50   Input ~ 0
row13
Wire Wire Line
	1850 4300 1850 4450
Wire Wire Line
	1250 4100 1250 4450
Wire Wire Line
	3150 4100 1250 4100
Connection ~ 1250 4350
Wire Wire Line
	3150 4300 1850 4300
Connection ~ 1850 4350
Wire Wire Line
	2350 5050 2450 5050
Wire Wire Line
	2350 5150 2450 5150
Wire Wire Line
	2950 5050 3050 5050
Wire Wire Line
	2950 5150 3050 5150
Wire Wire Line
	2350 4800 2350 4950
Wire Wire Line
	2350 5350 2350 5550
Wire Wire Line
	3050 4900 2500 4900
Wire Wire Line
	2500 4900 2500 4950
Wire Wire Line
	2500 4950 2350 4950
Wire Wire Line
	3750 3400 3750 3450
Wire Wire Line
	4000 3400 4000 3450
Wire Wire Line
	4100 3400 4100 3450
Wire Wire Line
	4350 3400 4350 3450
Wire Wire Line
	4450 3400 4450 3450
Wire Wire Line
	3650 3400 4450 3400
Connection ~ 4350 3400
Connection ~ 4100 3400
Connection ~ 4000 3400
Connection ~ 3750 3400
Wire Wire Line
	1400 5450 1450 5450
Wire Wire Line
	1450 5350 1450 5550
Wire Wire Line
	1400 6050 1450 6050
Wire Wire Line
	1450 5950 1450 6200
Wire Wire Line
	3800 6850 3800 6900
Wire Wire Line
	3700 6900 4350 6900
Wire Wire Line
	4350 6900 4350 6850
Wire Wire Line
	4250 6850 4250 6900
Connection ~ 4250 6900
Wire Wire Line
	4150 6850 4150 6900
Connection ~ 4150 6900
Wire Wire Line
	4050 6850 4050 6900
Connection ~ 4050 6900
Wire Wire Line
	2450 3700 3050 3700
Wire Wire Line
	5450 6100 5300 6100
Wire Wire Line
	5450 6200 5300 6200
Wire Wire Line
	5450 6300 5300 6300
Wire Wire Line
	5450 6400 5300 6400
Wire Wire Line
	5450 6500 5300 6500
Wire Wire Line
	5450 6600 5300 6600
Wire Wire Line
	1250 4850 1850 4850
Wire Wire Line
	1550 4900 1550 4850
Connection ~ 1550 4850
Connection ~ 3800 6900
Wire Wire Line
	2700 3900 2700 3700
Connection ~ 2700 3700
Wire Wire Line
	2000 3900 2100 3900
Wire Wire Line
	2950 6100 3050 6100
Wire Wire Line
	2950 6500 2950 6600
Connection ~ 1450 5450
Wire Wire Line
	1450 5550 1950 5550
Connection ~ 1700 5550
Wire Wire Line
	1450 5950 1950 5950
Connection ~ 1700 5950
Connection ~ 1450 6050
Wire Wire Line
	3050 5300 2950 5300
Wire Wire Line
	2950 5300 2950 5350
Wire Wire Line
	2950 5850 2950 5750
Wire Wire Line
	5300 5800 5400 5800
Wire Wire Line
	5300 5900 5400 5900
Wire Wire Line
	5900 5900 6000 5900
Wire Wire Line
	5900 5800 6400 5800
Wire Wire Line
	6400 5800 6400 5900
Wire Wire Line
	6400 5850 6500 5850
Connection ~ 6400 5850
Wire Wire Line
	5300 4900 5400 4900
Wire Wire Line
	5300 5000 5400 5000
Wire Wire Line
	5450 3700 5300 3700
Wire Wire Line
	5450 3800 5300 3800
Wire Wire Line
	5450 3900 5300 3900
Wire Wire Line
	5450 4000 5300 4000
Wire Wire Line
	5300 4100 5450 4100
Wire Wire Line
	5300 4200 5450 4200
Wire Wire Line
	5300 4300 5450 4300
Wire Wire Line
	5300 4400 5450 4400
Wire Wire Line
	5300 5100 5450 5100
Wire Wire Line
	5300 5200 5450 5200
Wire Wire Line
	5300 5300 5450 5300
Wire Wire Line
	5300 5400 5450 5400
Wire Wire Line
	5300 5500 5450 5500
Wire Wire Line
	5300 5600 5450 5600
$Comp
L CONN_02X13 P?
U 1 1 54DC1BBC
P 4050 1900
F 0 "P?" H 4050 2600 50  0000 C CNN
F 1 "LEFT_HAND" V 4050 1900 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x13" H 4050 750 60  0001 C CNN
F 3 "" H 4050 750 60  0000 C CNN
	1    4050 1900
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X13 P?
U 1 1 54DC1C76
P 5050 1900
F 0 "P?" H 5050 2600 50  0000 C CNN
F 1 "RIGHT_HAND" V 5050 1900 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x13" H 5050 750 60  0001 C CNN
F 3 "" H 5050 750 60  0000 C CNN
	1    5050 1900
	1    0    0    -1  
$EndComp
$Comp
L CONN_02X03 P?
U 1 1 54DC1D75
P 2200 3300
F 0 "P?" H 2200 3500 50  0000 C CNN
F 1 "PROG" H 2200 3100 50  0000 C CNN
F 2 "dmcewan:avr_isp6_header" H 2200 2100 60  0001 C CNN
F 3 "" H 2200 2100 60  0000 C CNN
	1    2200 3300
	1    0    0    -1  
$EndComp
Text GLabel 1400 6450 0    50   Input ~ 0
VCC
Text GLabel 1500 7050 0    50   Input ~ 0
I2C_SCL
Text GLabel 1950 7050 0    50   Input ~ 0
I2C_SDA
$Comp
L R R?
U 1 1 54DC2499
P 1950 6700
F 0 "R?" V 1950 6600 40  0000 C CNN
F 1 "10k" V 1950 6750 40  0000 C CNN
F 2 "dmcewan:0603" V 1880 6700 30  0001 C CNN
F 3 "" H 1950 6700 30  0000 C CNN
	1    1950 6700
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 54DC2560
P 1500 6700
F 0 "R?" V 1500 6600 40  0000 C CNN
F 1 "10k" V 1500 6750 40  0000 C CNN
F 2 "dmcewan:0603" V 1430 6700 30  0001 C CNN
F 3 "" H 1500 6700 30  0000 C CNN
	1    1500 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 6450 1950 6450
Connection ~ 1500 6450
Wire Wire Line
	1500 7050 1500 6950
Wire Wire Line
	1950 7050 1950 6950
Text GLabel 1850 3200 0    50   Input ~ 0
MISO
Text GLabel 1850 3300 0    50   Input ~ 0
SCK
Text GLabel 1850 3400 0    50   Input ~ 0
RST
Text GLabel 2550 3200 2    50   Input ~ 0
VCC
Text GLabel 2550 3300 2    50   Input ~ 0
MOSI
Text GLabel 2550 3400 2    50   Input ~ 0
GND
Wire Wire Line
	2550 3400 2450 3400
Wire Wire Line
	2550 3300 2450 3300
Wire Wire Line
	2450 3200 2550 3200
Wire Wire Line
	1950 3200 1850 3200
Wire Wire Line
	1950 3300 1850 3300
Wire Wire Line
	1950 3400 1850 3400
Text GLabel 2250 2750 2    50   Input ~ 0
SCK
Text GLabel 2250 2850 2    50   Input ~ 0
MOSI
Text GLabel 2250 2950 2    50   Input ~ 0
MISO
Text GLabel 2150 2750 0    50   Input ~ 0
row1
Text GLabel 2150 2850 0    50   Input ~ 0
row2
Text GLabel 2150 2950 0    50   Input ~ 0
row3
Wire Wire Line
	2150 2750 2250 2750
Wire Wire Line
	2150 2850 2250 2850
Wire Wire Line
	2150 2950 2250 2950
$Comp
L MAX7313 IC?
U 1 1 54FE12F6
P 8450 4700
F 0 "IC?" H 7950 5550 50  0000 L CNN
F 1 "MAX7313" H 8650 3850 50  0000 L CNN
F 2 "24-TQFN-EP" H 8450 4700 50  0000 C CIN
F 3 "" H 8450 4700 60  0000 C CNN
	1    8450 4700
	1    0    0    -1  
$EndComp
$Comp
L MAX7313 IC?
U 1 1 54FE1421
P 8450 2400
F 0 "IC?" H 7950 3250 50  0000 L CNN
F 1 "MAX7313" H 8650 1550 50  0000 L CNN
F 2 "24-TQFN-EP" H 8450 2400 50  0000 C CIN
F 3 "" H 8450 2400 60  0000 C CNN
	1    8450 2400
	1    0    0    -1  
$EndComp
Text GLabel 8450 5700 0    60   Input ~ 0
GND
Text GLabel 8450 3400 0    60   Input ~ 0
GND
Text GLabel 8450 3700 0    60   Input ~ 0
VCC
Text GLabel 8450 1450 0    60   Input ~ 0
VCC
Text GLabel 7600 3050 0    60   Input ~ 0
GND
Text GLabel 7600 5400 0    60   Input ~ 0
GND
Text GLabel 7600 5250 0    60   Input ~ 0
I2C_SCL
Wire Wire Line
	7700 5350 7700 5450
Wire Wire Line
	7600 5400 7700 5400
Connection ~ 7700 5400
Wire Wire Line
	7600 5250 7700 5250
Wire Wire Line
	7700 2950 7700 3150
Connection ~ 7700 3050
Wire Wire Line
	7700 3050 7600 3050
Text GLabel 7700 3950 0    60   Input ~ 0
I2C_SCL
Text GLabel 7700 1650 0    60   Input ~ 0
I2C_SCL
Text GLabel 7700 1750 0    60   Input ~ 0
I2C_SDA
Text GLabel 7700 4050 0    60   Input ~ 0
I2C_SDA
NoConn ~ 9200 5450
NoConn ~ 9200 5350
NoConn ~ 9200 5250
NoConn ~ 9200 3150
NoConn ~ 9200 3050
NoConn ~ 9200 2950
NoConn ~ 7700 4700
NoConn ~ 7700 2400
Text GLabel 9200 3950 2    60   Input ~ 0
ledl_col0
Text GLabel 9200 4050 2    60   Input ~ 0
ledl_col1
Text GLabel 9200 4150 2    60   Input ~ 0
ledl_col2
Text GLabel 9200 4250 2    60   Input ~ 0
ledl_col3
Text GLabel 9200 4350 2    60   Input ~ 0
ledl_col4
Text GLabel 9200 4450 2    60   Input ~ 0
ledl_col5
Text GLabel 9200 4550 2    60   Input ~ 0
ledl_row0
Text GLabel 9200 4650 2    60   Input ~ 0
ledl_row1
Text GLabel 9200 4750 2    60   Input ~ 0
ledl_row2
Text GLabel 9200 4850 2    60   Input ~ 0
ledl_row3
Text GLabel 9200 4950 2    60   Input ~ 0
ledl_row4
Text GLabel 9200 5050 2    60   Input ~ 0
ledl_row5
Text GLabel 9200 5150 2    60   Input ~ 0
ledl_row6
Text GLabel 9200 1650 2    60   Input ~ 0
ledr_col0
Text GLabel 9200 1750 2    60   Input ~ 0
ledr_col1
Text GLabel 9200 1850 2    60   Input ~ 0
ledr_col2
Text GLabel 9200 1950 2    60   Input ~ 0
ledr_col3
Text GLabel 9200 2050 2    60   Input ~ 0
ledr_col4
Text GLabel 9200 2150 2    60   Input ~ 0
ledr_col5
Text GLabel 9200 2250 2    60   Input ~ 0
ledr_row7
Text GLabel 9200 2350 2    60   Input ~ 0
ledr_row8
Text GLabel 9200 2450 2    60   Input ~ 0
ledr_row9
Text GLabel 9200 2550 2    60   Input ~ 0
ledr_row10
Text GLabel 9200 2650 2    60   Input ~ 0
ledr_row11
Text GLabel 9200 2750 2    60   Input ~ 0
ledr_row12
Text GLabel 9200 2850 2    60   Input ~ 0
ledr_row13
$Comp
L CONN_01X02 P?
U 1 1 54FE2CD6
P 5600 4650
F 0 "P?" H 5600 4800 50  0000 C CNN
F 1 "AUX" V 5700 4650 50  0000 C CNN
F 2 "" H 5600 4650 60  0000 C CNN
F 3 "" H 5600 4650 60  0000 C CNN
	1    5600 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 4600 5400 4600
Wire Wire Line
	5300 4700 5400 4700
$EndSCHEMATC
