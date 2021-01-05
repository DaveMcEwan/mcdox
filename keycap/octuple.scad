$fn = 64; // Increase to render more faces per curve.

use <keycap.scad>

minDim = 0.001;

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.

baseUnit = 18.0;
minSpace = 2.0;

function halfVolRadius(r) = sqrt(pow(r, 2) / 2.0);

/* Top-down view of part layout.
Probably not the best way to make a mold, but a nice experiment.

X0X      X1X
XXX      XXX
   \_  _/         runner2
   / \/ \         runner1
X2X  |   X3X
XXX  |   XXX
     |            runner0
     +---------o  sprue input
     |            runner0
X4X  |   X5X
XXX  |   XXX
   \_/\_/         runner1
   /    \         runner2
X6X      X7X
XXX      XXX

*/

sprueEscape = 10.0; // Length arbitrary, >plateWidth
sprue0_r = 2.0; // Full input cross-section area
sprue0_l = sprue0_r + minSpace*2 + uMul*baseUnit + sprueEscape;

runner0_r = halfVolRadius(sprue0_r); // 1/2 cross-section area
runner1_r = halfVolRadius(runner0_r); // 1/4 cross-section area
runner2_r = halfVolRadius(runner1_r); // 1/8 cross-section area

runner0_l = 2 * (sprue0_r + runner1_r + minSpace*2 + baseUnit);
runner1_l = 2 * (runner0_r + minSpace + uMul*baseUnit/2);
runner2_l = 2 * (runner1_r + minSpace);

runner1_y = runner0_l/2;
runner2_y = runner1_y;
runner2_x = runner1_l/2;


/** Keycap grid resting on XY plane.
*/
module keycapGrid () {

  x = runner1_l/2; // Gate is at midpoint of keycap.
  yInner = runner0_l/2 - (runner1_r + minSpace + baseUnit/2);
  yOuter = runner0_l/2 + (runner1_r + minSpace + baseUnit/2);

  translate([-x,  yOuter, 0]) keycap(stemNum, shellNum, uMul, doBump);
  /*
  */
  translate([ x,  yOuter, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([-x,  yInner, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([ x,  yInner, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([-x, -yInner, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([ x, -yInner, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([-x, -yOuter, 0]) keycap(stemNum, shellNum, uMul, doBump);
  translate([ x, -yOuter, 0]) keycap(stemNum, shellNum, uMul, doBump);
}


/** Runner network for octuple mold.
*/
module runners () {

  module runner(r, l, x=0, y=0, alongYnotX=0) {
    translate([x, y, 0])
    rotate([90*alongYnotX, 90-90*alongYnotX, 0])
    cylinder(h=l, r=r, center=true);
  }

  module reducingChamfer(r1, r2, x=0, y=0, alongYnotX=0) {
    chamfer_l = r1 * 4/3;

    translate([x, y, 0])
    rotate([90*alongYnotX, 90-90*alongYnotX, 0])
    union() {
      // Cones stacked on Z-axis.

      cylinder(h=r1*2, r=r1, center=true);

      translate([0, 0,  r1])
      cylinder(h=chamfer_l, r1=r1, r2=r2, center=false);

      rotate([180, 0, 0])
      translate([0, 0, r1])
      cylinder(h=chamfer_l, r1=r1, r2=r2, center=false);
    }
  }

  union() {
    // Input sprue
    runner(sprue0_r, sprue0_l, sprue0_l/2, 0, 0);

    // Longest runner along length of grid.
    reducingChamfer(sprue0_r, runner0_r, 0, 0, 1);
    runner(runner0_r, runner0_l, 0, 0, 1);

    // Mid-length runners at each end.
    reducingChamfer(runner0_r, runner1_r, 0, -runner1_y, 0);
    reducingChamfer(runner0_r, runner1_r, 0,  runner1_y, 0);
    runner(runner1_r, runner1_l, 0,  runner1_y, 0);
    runner(runner1_r, runner1_l, 0, -runner1_y, 0);

    // Shortest runners going to gates.
    reducingChamfer(runner1_r, runner2_r,  runner2_x,  runner2_y, 1);
    reducingChamfer(runner1_r, runner2_r,  runner2_x, -runner2_y, 1);
    reducingChamfer(runner1_r, runner2_r, -runner2_x,  runner2_y, 1);
    reducingChamfer(runner1_r, runner2_r, -runner2_x, -runner2_y, 1);
    runner(runner2_r, runner2_l,  runner2_x,  runner2_y, 1);
    runner(runner2_r, runner2_l,  runner2_x, -runner2_y, 1);
    runner(runner2_r, runner2_l, -runner2_x,  runner2_y, 1);
    runner(runner2_r, runner2_l, -runner2_x, -runner2_y, 1);
  }
}

keycapGrid();
color("blue") runners();
