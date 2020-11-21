EESchema Schematic File Version 4
EELAYER 30 0
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
L ctrl:ArduinoProMicro U1
U 1 1 5FB71D0A
P 8900 2550
F 0 "U1" H 8900 3175 50  0000 C CNN
F 1 "ArduinoProMicro" H 8900 3084 50  0000 C CNN
F 2 "ctrl:ArduinoProMicro" H 8900 2550 50  0001 C CNN
F 3 "" H 8900 2550 50  0001 C CNN
	1    8900 2550
	1    0    0    -1  
$EndComp
$Comp
L Device:R R0
U 1 1 5FBACF2E
P 10250 3050
F 0 "R0" V 10350 3100 50  0001 C CNN
F 1 "220" V 10250 3050 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3050 50  0001 C CNN
F 3 "~" H 10250 3050 50  0001 C CNN
	1    10250 3050
	0    1    1    0   
$EndComp
$Comp
L Device:R R1
U 1 1 5FBB7BCC
P 10250 3150
F 0 "R1" V 10350 3200 50  0001 C CNN
F 1 "220" V 10250 3150 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3150 50  0001 C CNN
F 3 "~" H 10250 3150 50  0001 C CNN
	1    10250 3150
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5FBB93BF
P 10250 3250
F 0 "R2" V 10350 3300 50  0001 C CNN
F 1 "220" V 10250 3250 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3250 50  0001 C CNN
F 3 "~" H 10250 3250 50  0001 C CNN
	1    10250 3250
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5FBB93C5
P 10250 3350
F 0 "R3" V 10350 3400 50  0001 C CNN
F 1 "220" V 10250 3350 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3350 50  0001 C CNN
F 3 "~" H 10250 3350 50  0001 C CNN
	1    10250 3350
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5FBBA532
P 10250 3450
F 0 "R4" V 10350 3500 50  0001 C CNN
F 1 "220" V 10250 3450 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3450 50  0001 C CNN
F 3 "~" H 10250 3450 50  0001 C CNN
	1    10250 3450
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5FBBA538
P 10250 3550
F 0 "R5" V 10350 3600 50  0001 C CNN
F 1 "220" V 10250 3550 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3550 50  0001 C CNN
F 3 "~" H 10250 3550 50  0001 C CNN
	1    10250 3550
	0    1    1    0   
$EndComp
$Comp
L Device:R R6
U 1 1 5FBBA53E
P 10250 3650
F 0 "R6" V 10350 3700 50  0001 C CNN
F 1 "220" V 10250 3650 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3650 50  0001 C CNN
F 3 "~" H 10250 3650 50  0001 C CNN
	1    10250 3650
	0    1    1    0   
$EndComp
$Comp
L Device:R R7
U 1 1 5FBBA544
P 10250 3750
F 0 "R7" V 10350 3800 50  0001 C CNN
F 1 "220" V 10250 3750 50  0000 C CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 10180 3750 50  0001 C CNN
F 3 "~" H 10250 3750 50  0001 C CNN
	1    10250 3750
	0    1    1    0   
$EndComp
Text GLabel 10400 3750 2    50   Input ~ 0
col7
Text GLabel 10400 3650 2    50   Input ~ 0
col6
Text GLabel 10400 3550 2    50   Input ~ 0
col5
Text GLabel 10400 3450 2    50   Input ~ 0
col4
Text GLabel 10400 3350 2    50   Input ~ 0
col3
Text GLabel 10400 3250 2    50   Input ~ 0
col2
Text GLabel 10400 3150 2    50   Input ~ 0
col1
Text GLabel 10400 3050 2    50   Input ~ 0
col0
Text GLabel 8250 2150 0    50   Input ~ 0
row0
Text GLabel 8250 2250 0    50   Input ~ 0
row1
Text GLabel 8250 2550 0    50   Input ~ 0
row2
Text GLabel 8250 2650 0    50   Input ~ 0
row3
Text GLabel 8250 2750 0    50   Input ~ 0
row4
$Comp
L power:GND #PWR0105
U 1 1 5FBF5B4F
P 9550 2250
F 0 "#PWR0105" H 9550 2000 50  0001 C CNN
F 1 "GND" V 9555 2122 50  0000 R CNN
F 2 "" H 9550 2250 50  0001 C CNN
F 3 "" H 9550 2250 50  0001 C CNN
	1    9550 2250
	0    -1   -1   0   
$EndComp
NoConn ~ 9550 2150
NoConn ~ 9550 2350
Text GLabel 9550 2550 2    50   Input ~ 0
row9
Text GLabel 9550 2650 2    50   Input ~ 0
row8
Text GLabel 9550 2750 2    50   Input ~ 0
row7
Text GLabel 9550 2850 2    50   Input ~ 0
row6
Text GLabel 9550 2950 2    50   Input ~ 0
row5
Text Notes 8350 6650 2    50   ~ 0
Drive rows, read common columns.
NoConn ~ 8250 2350
NoConn ~ 8250 2450
$Comp
L power:+3.3V #PWR0106
U 1 1 5FC00541
P 9550 2450
F 0 "#PWR0106" H 9550 2300 50  0001 C CNN
F 1 "+3.3V" V 9565 2578 50  0000 L CNN
F 2 "" H 9550 2450 50  0001 C CNN
F 3 "" H 9550 2450 50  0001 C CNN
	1    9550 2450
	0    1    1    0   
$EndComp
Wire Wire Line
	9550 3050 10100 3050
Wire Wire Line
	9550 3150 10100 3150
Wire Wire Line
	9550 3250 10100 3250
Wire Wire Line
	10100 3350 8250 3350
Wire Wire Line
	8250 3350 8250 3250
Wire Wire Line
	10100 3450 8150 3450
Wire Wire Line
	8150 3450 8150 3150
Wire Wire Line
	8150 3150 8250 3150
Wire Wire Line
	10100 3550 8050 3550
Wire Wire Line
	8050 3550 8050 3050
Wire Wire Line
	8050 3050 8250 3050
Wire Wire Line
	10100 3650 7950 3650
Wire Wire Line
	7950 3650 7950 2950
Wire Wire Line
	7950 2950 8250 2950
Wire Wire Line
	10100 3750 7850 3750
Wire Wire Line
	7850 3750 7850 2850
Wire Wire Line
	7850 2850 8250 2850
Text Notes 8000 6300 0    50   ~ 0
Jright1 connects right hand from left-side of ctrl.\n\nLeft/right are swapped since ctrl is upside down relative to keyboard.
$Comp
L Connector_Generic:Conn_01x15 Jright1
U 1 1 5FBD26A4
P 8300 5100
F 0 "Jright1" H 8380 5142 50  0000 L CNN
F 1 "Conn_01x15" H 8380 5051 50  0000 L CNN
F 2 "ctrl:TE_1-84953-5_1x15-1MP_P1.0mm_Horizontal" H 8300 5100 50  0001 C CNN
F 3 "https://www.te.com/usa-en/product-1-84953-5.html" H 8300 5100 50  0001 C CNN
	1    8300 5100
	1    0    0    -1  
$EndComp
Text GLabel 8100 4400 0    50   Input ~ 0
row0
Text GLabel 8100 4500 0    50   Input ~ 0
row1
Text GLabel 8100 4700 0    50   Input ~ 0
row3
Text GLabel 8100 4800 0    50   Input ~ 0
row4
Text GLabel 8100 4600 0    50   Input ~ 0
row2
Text GLabel 8100 4900 0    50   Input ~ 0
col0
Text GLabel 8100 5000 0    50   Input ~ 0
col1
Text GLabel 8100 5100 0    50   Input ~ 0
col2
Text GLabel 8100 5200 0    50   Input ~ 0
col3
Text GLabel 8100 5300 0    50   Input ~ 0
col4
Text GLabel 8100 5400 0    50   Input ~ 0
col5
Text GLabel 8100 5500 0    50   Input ~ 0
col6
Text GLabel 8100 5600 0    50   Input ~ 0
col7
$Comp
L power:GND #PWR0104
U 1 1 5FB91767
P 7750 5800
F 0 "#PWR0104" H 7750 5550 50  0001 C CNN
F 1 "GND" H 7755 5627 50  0000 C CNN
F 2 "" H 7750 5800 50  0001 C CNN
F 3 "" H 7750 5800 50  0001 C CNN
	1    7750 5800
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0103
U 1 1 5FB92FA7
P 7750 5700
F 0 "#PWR0103" H 7750 5550 50  0001 C CNN
F 1 "+3.3V" H 7765 5873 50  0000 C CNN
F 2 "" H 7750 5700 50  0001 C CNN
F 3 "" H 7750 5700 50  0001 C CNN
	1    7750 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 5700 8100 5700
Wire Wire Line
	7750 5800 8100 5800
Wire Wire Line
	10100 5800 9750 5800
Wire Wire Line
	10100 5700 9750 5700
$Comp
L power:+3.3V #PWR0102
U 1 1 5FB92974
P 10100 5700
F 0 "#PWR0102" H 10100 5550 50  0001 C CNN
F 1 "+3.3V" H 10115 5873 50  0000 C CNN
F 2 "" H 10100 5700 50  0001 C CNN
F 3 "" H 10100 5700 50  0001 C CNN
	1    10100 5700
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5FB92154
P 10100 5800
F 0 "#PWR0101" H 10100 5550 50  0001 C CNN
F 1 "GND" H 10105 5627 50  0000 C CNN
F 2 "" H 10100 5800 50  0001 C CNN
F 3 "" H 10100 5800 50  0001 C CNN
	1    10100 5800
	-1   0    0    -1  
$EndComp
Text GLabel 9750 4400 2    50   Input ~ 0
row9
Text GLabel 9750 4500 2    50   Input ~ 0
row8
Text GLabel 9750 4700 2    50   Input ~ 0
row6
Text GLabel 9750 4800 2    50   Input ~ 0
row5
Text GLabel 9750 4600 2    50   Input ~ 0
row7
Text GLabel 9750 4900 2    50   Input ~ 0
col0
Text GLabel 9750 5000 2    50   Input ~ 0
col1
Text GLabel 9750 5100 2    50   Input ~ 0
col2
Text GLabel 9750 5200 2    50   Input ~ 0
col3
Text GLabel 9750 5300 2    50   Input ~ 0
col4
Text GLabel 9750 5400 2    50   Input ~ 0
col5
Text GLabel 9750 5500 2    50   Input ~ 0
col6
Text GLabel 9750 5600 2    50   Input ~ 0
col7
$Comp
L Connector_Generic:Conn_01x15 Jleft1
U 1 1 5FB74996
P 9550 5100
F 0 "Jleft1" H 9630 5142 50  0000 L CNN
F 1 "Conn_01x15" H 9630 5051 50  0000 L CNN
F 2 "ctrl:TE_1-84953-5_1x15-1MP_P1.0mm_Horizontal" H 9550 5100 50  0001 C CNN
F 3 "https://www.te.com/usa-en/product-1-84953-5.html" H 9550 5100 50  0001 C CNN
	1    9550 5100
	-1   0    0    1   
$EndComp
$EndSCHEMATC
