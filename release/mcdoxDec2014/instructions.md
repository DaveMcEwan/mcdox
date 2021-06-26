
Instructions for mcdox v1.0
===========================

These are the basic steps to complete in order.
Use the photographs for clarification.

1. Send SVG files to acrylic laser cutters.
2. Send Gerber files to PCB manufacturer (lollybrd + mcdoxhand).
3. Solder/assemble lollybrd PCB.
4. Solder diodes onto mcdoxhand PCBs.
5. Insert switches into mnt layer of case.
6. Lay mcdoxhand PCBs over switches and solder in place.
7. Mount lollybrd PCB onto mnt layer or case with socket-head M3 bolts.
8. Arrange other case layers in order, lining up fixing holes.
9. Insert button-head M3 bolts in fixing holes and finger tighten dome nuts.
10. Put keycaps onto switches.
11. Compile TMK firmware (or use `mcdox_pjrc.hex`). flash using Teensy Loader.

Et voila!
Just in case that isn't enough there are some more details below.

I feel happy releasing this as v1.0 because I have tested it daily for over a
year and am satisfied that the ergonomics work well and it feels like a solid
build.
The build and assembly process was very easy and I'm confident most people with
very basic C and soldering skills could replicate my work.

Designed, built, tested by Dave McEwan 2014-2016.


Parts List
----------

  - Bolts M3-32mm button-head               x12
  - Bolts M3-10mm socket-head               x4
  - Dome Nuts M3                            x12
  - Flat Nuts M3                            x4
  - Washers M3                              x32
  - Diodes 1N4148                           x76
  - PJRC Teensy-2.0                         x1
  - PCB (mcdoxhand)                         x2
  - PCB (lollybrd)                          x1
  - 13-core, 1.27mm pitch IDC Ribbon Cable  x2
  - Switches CherryMX OR Matias ALPS        x76
  - Keycap 1.0u                             x60
  - Keycap 1.5u                             x12
  - Keycap 2.0u                             x4
  - Case (laser cut)                        x1


Laser Cut Acrylic Case With SVG Files
-------------------------------------

  - `mcdox_5mm.svg` - Clear
  - `mcdox_cherrymx_3mm.svg` OR `mcdox_alps_3mm.svg` - Black

Different laser cutting shops prefer different file formats though EPS seems to
be the best supported.
You can tailor the SVG files in Inkscape to whatever specifications your chosen
shop requires.
Typically you want to merge all the files for the same thickness material into
one SVG, convert everything to paths, and "Save As' in Encapsulated PostScript
format.

For each case expect to pay around 20 GPB in materials if using just 3mm and
5mm acrylic.
For each CherryMX case expect to pay for around 20 minutes in cutting time.
For each ALPS case expect to pay for around 30 minutes in cutting time.

Case thickness is sum(3, 5, 5, 3, 5, 3) = 24mm.
M3 acorn nuts which act as feet lift it another 5mm to the bottom.
Keycaps protrude about 5mm from the top.
Total height off the desk is about 34mm.


PCB Manufacture With Gerber Archives
------------------------------------

  - `lollybrd_gerber.zip` - The controller PCB.
  - `mcdoxhand_gerber.zip` - The hand PCB, reversible.

Size of the controller board (lollybrd) is 50x50mm which is very cheap from
SeeedStudio and other low cost, low volume PCB manufacturers.
You need one copy of the lollybrd PCB and 2 copies of the mcdoxhand PCB.
For 2.5 keyboards worth (5 * mcdoxhand + 10 * lollybrd), expect to pay around
60 GBP, this was the minimum order when I tried.

The recommended PCB specs required are basic.

  - 2 layer - Both designs only use 2.
  - 1.6mm FR4 - Usually the cheapest option, doesn't really matter.
  - 15 mil (or less) routes/clearance

Instead of finding 13-core ribbon cable I just sliced a standard 26-core IDE
cable in half.


Firmware With HEX file
----------------------

TMK from my branch with the PJRC loader.
Make any edits to your favourite keymap (I like dvorak) in
`tmk_keyboard/keyboard/mcdox/keymap_dvorak.h` then compile.

    cd tmk_keyboard/keyboard/mcdox
    make dvorak -f Makefile.pjrc

Then drag/drop `mcdox_pjrc.hex` into the Teensy Loader and click program.


Notes And Future Improvements
-----------------------------

I used black M3 washers at both ends of the fixing bolts to allow the dome nuts
to be better positioned on the end of the bolt.
This is really unnecessary and after about 7 months the colour on the top of the
washers started to rub off looking a bit crap.
Forget the washers. If the bolt is too long just file/grind it down.

The 4 thumb keys (2.0u) are sometimes a bit wobbly.
I've seen others using stabilisers but these seem hard to come by.
I could just use 1.5u instead which would mean less wobbly switches and less
different parts.
This would alter the layout slightly but might make it easier to reach opposite
corners with one hand.

The col/row arrangement should be swapped around to save a GPIO pin.
The arrangement of 6 (horizontal) columns and 2x 7 (vertical) rows requires 20
GPIO where columns are driven and rows are read.
This is the same as the ErgoDox where this detail did not matter since there
was no shared columns between sides.
By arranging as 7 (vertical) columns and 2x 6 (horizontal) rows only requires 19
GPIO, and looks more intuitive.
Columns are still driven, rows are still read.

Splaying and soldering the ribbon cable is not production friendly and feels
like the ugliest part of the design.
Using low profile FPC ZIF connectors and cable would be much neater.
The Raspberry Pi camera module uses a 15-pin FPC so these are readily available
to potential keyboard hackers, as well as production facilities.

PimpMyKeyboard who supply keycaps are based in USA and charge very high
shipping, plus HMRC charge 20% VAT, plus Post Office charge 8GBP handling fee.
That all ends up at about 50GBP per board, even in 10+ quantities.
Devlin Electronics in UK are much cheaper, coming in at about 15GBP per board
before shipping of 12GBP.

Wireless would be nice, especially with my TV.
BlueTooth4 Low Energy (BLE) features USB pass through.
Wired and charging while plugged in, bluetooth when unplugged.
Should have a toggle switch on top.

Acrylic case becomes smudged quite easily and is rather heavy.
Replace 5mm layers with 4mm acrylic, and 3mm layers with 2mm aluminium to reduce
thickness by a third.
This also opens up the possibility of having a tented profile.

