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
P 5600 3750
F 0 "U1" H 5600 4375 50  0000 C CNN
F 1 "ArduinoProMicro" H 5600 4284 50  0000 C CNN
F 2 "" H 5600 3750 50  0001 C CNN
F 3 "" H 5600 3750 50  0001 C CNN
	1    5600 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5FB1D769
P 4400 3350
F 0 "R2" V 4500 3350 50  0000 L CNN
F 1 "220" V 4400 3250 50  0000 L CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4330 3350 50  0001 C CNN
F 3 "~" H 4400 3350 50  0001 C CNN
	1    4400 3350
	0    1    1    0   
$EndComp
$Comp
L Connector_Generic:Conn_01x15 J1
U 1 1 5FBD26A4
P 7250 4000
F 0 "J1" H 7330 4042 50  0000 L CNN
F 1 "Conn_01x15" H 7330 3951 50  0000 L CNN
F 2 "ctrl:TE_1-84953-5_1x15-1MP_P1.0mm_Horizontal" H 7250 4000 50  0001 C CNN
F 3 "https://www.te.com/usa-en/product-1-84953-5.html" H 7250 4000 50  0001 C CNN
	1    7250 4000
	1    0    0    1   
$EndComp
Text GLabel 7050 3300 0    50   Input ~ 0
row0
Text GLabel 7050 3400 0    50   Input ~ 0
row1
Text GLabel 7050 3600 0    50   Input ~ 0
row3
Text GLabel 7050 3700 0    50   Input ~ 0
row4
Text GLabel 7050 3500 0    50   Input ~ 0
row2
Text GLabel 7050 3800 0    50   Input ~ 0
col0
Text GLabel 7050 3900 0    50   Input ~ 0
col1
Text GLabel 7050 4000 0    50   Input ~ 0
col2
Text GLabel 7050 4100 0    50   Input ~ 0
col3
Text GLabel 7050 4200 0    50   Input ~ 0
col4
Text GLabel 7050 4300 0    50   Input ~ 0
col5
Text GLabel 7050 4400 0    50   Input ~ 0
col6
Text GLabel 7050 4500 0    50   Input ~ 0
col7
$Comp
L Connector_Generic:Conn_01x15 J2
U 1 1 5FB74996
P 8650 4000
F 0 "J2" H 8730 4042 50  0000 L CNN
F 1 "Conn_01x15" H 8730 3951 50  0000 L CNN
F 2 "ctrl:TE_1-84953-5_1x15-1MP_P1.0mm_Horizontal" H 8650 4000 50  0001 C CNN
F 3 "https://www.te.com/usa-en/product-1-84953-5.html" H 8650 4000 50  0001 C CNN
	1    8650 4000
	1    0    0    -1  
$EndComp
Text GLabel 8450 4500 0    50   Input ~ 0
col7
Text GLabel 8450 4400 0    50   Input ~ 0
col6
Text GLabel 8450 4300 0    50   Input ~ 0
col5
Text GLabel 8450 4200 0    50   Input ~ 0
col4
Text GLabel 8450 4100 0    50   Input ~ 0
col3
Text GLabel 8450 4000 0    50   Input ~ 0
col2
Text GLabel 8450 3900 0    50   Input ~ 0
col1
Text GLabel 8450 3800 0    50   Input ~ 0
col0
Text GLabel 8450 3500 0    50   Input ~ 0
row2
Text GLabel 8450 3700 0    50   Input ~ 0
row4
Text GLabel 8450 3600 0    50   Input ~ 0
row3
Text GLabel 8450 3400 0    50   Input ~ 0
row1
Text GLabel 8450 3300 0    50   Input ~ 0
row0
$Comp
L Device:R R4
U 1 1 5FB7DD33
P 4700 3450
F 0 "R4" V 4800 3450 50  0000 L CNN
F 1 "220" V 4700 3350 50  0000 L CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4630 3450 50  0001 C CNN
F 3 "~" H 4700 3450 50  0001 C CNN
	1    4700 3450
	0    1    1    0   
$EndComp
$Comp
L Device:R R1
U 1 1 5FB7ECCB
P 4400 3750
F 0 "R1" V 4500 3750 50  0000 L CNN
F 1 "220" V 4400 3650 50  0000 L CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4330 3750 50  0001 C CNN
F 3 "~" H 4400 3750 50  0001 C CNN
	1    4400 3750
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5FB7ECD1
P 4700 3850
F 0 "R5" V 4800 3850 50  0000 L CNN
F 1 "220" V 4700 3750 50  0000 L CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4630 3850 50  0001 C CNN
F 3 "~" H 4700 3850 50  0001 C CNN
	1    4700 3850
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5FB804F5
P 4400 3950
F 0 "R3" V 4500 3950 50  0000 L CNN
F 1 "220" V 4400 3850 50  0000 L CNN
F 2 "ctrl:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" V 4330 3950 50  0001 C CNN
F 3 "~" H 4400 3950 50  0001 C CNN
	1    4400 3950
	0    1    1    0   
$EndComp
$EndSCHEMATC
