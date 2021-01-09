
mcdox - Mechanical Computer Keyboard
====================================

Layout is similar to than of the Ergodox project, but in a unibody case.


Subdirectories
--------------

- case - Lasercut design produced by exporting SVGs from KiCAD.
- doc - Documents like datasheets stored for handy reference.
- keycap - STL model generator written in OpenSCAD suitable for FDM printing.
  Generated models are tracked in `keycap/stl` because it takes a while (~10
  minutes) to generate them.
- pcb/ctrl - TODO Breakout PCB for connecting controller to switch grids.
- pcb/hand - Reversible PCB which connects the switches in a grid.
  - 38 buttons distributed over 5 rows, 8 columns.
  - Lengths beside mounting holes (6mm, 15mm, 25mm) are for standoffs to
    achieve a tenting.
  - Connect to control board with 15 core, 1mm pitch FFC-FPC cable.
    <https://www.te.com/usa-en/product-1-84953-5.html>
    <https://www.digikey.com/en/products/detail/te-connectivity-amp-connectors/1-84953-5/2567541>
    <https://uk.farnell.com/amp-te-connectivity/1-84953-5/connector-ffc-fpc-15pos-1rows/dp/3398659>
    <https://uk.farnell.com/multicomp-pro/mp-ffca10150503a/ffc-cord-15p-same-side-50mm-wht/dp/3385337>
    <https://uk.farnell.com/multicomp-pro/mp-ffca10151003a/ffc-cord-15p-same-side-100mm-wht/dp/3385339>
  - Low level lighting with LED on top and/or bottom, depending how the case
    looks.
  - All diodes (1N4148 compatible), LEDs, and resistors are 0603 (imperial).
- release - Stuff that's actually been manufactured.


BOM
---

- Keycaps - The functionally simplest parts which are also the most difficult to
  source.
  18x 1.5u, 56x 1u
- Case - Standard 3mm acrylic from laser cutter.
- PCBs - 1.2mm FR4, 2-layer, 0.15mm width/clearance
  2x mcdoxHand, 1x mcdoxCtrl
- Switches - CherryMX, or compatible like Gateron, Kailh.
  74x
- Diodes - 1 per switch.
  74x
- Microcontroller - Arduino Pro Micro from Sparkfun, or clone.
- FPC connectors
  4x
- FPC cables - Connect hand PCBs to central controller.
- LEDs - 0603 footprint
  2x
- Resistors - For LEDs and switch matrix.
  10x 220R 0603
- Pushbutton - For putting Arduino Pro Micro into programming mode.
  1x
