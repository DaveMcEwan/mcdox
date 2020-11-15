
mcdox - Mechanical Computer Keyboard
====================================

Layout is similar to than of the Ergodox project, but in a unibody case.


Subdirectories
--------------

- keycap - STL model generator written in OpenSCAD suitable for FDM printing.
  Generated models are tracked in `keycap/stl` because it takes a while (~10
  minutes) to generate them.
- release - Stuff that's actually been manufactured.
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
- pcb/ctrl - TODO Breakout PCB for connecting controller to switch grids.
