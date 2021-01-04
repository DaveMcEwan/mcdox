$fn = 64; // Increase to render more faces per curve.
include <keycapParameters.scad>

use <keycap.scad>

/*

X0X      X1X
XXX      XXX
   \_  _/     runner2
   / \/ \     runner1
X2X  |   X3X
XXX  |   XXX
     |        runner0
     o        sprue input
     |        runner0
X4X  |   X5X
XXX  |   XXX
   \_/\_/      runner1
   /    \      runner2
X6X      X7X
XXX      XXX

*/

minSpace = 2.0;

// radius
function halfVolRadius(r) = sqrt(pow(r, 2) / 2.0);
sprue0_r = 1.0; // Full input cross-section area
runner0_r = halfVolRadius(sprue0_r); // 1/2 cross-section area
runner1_r = halfVolRadius(runner0_r); // 1/4 cross-section area
runner2_r = halfVolRadius(runner1_r); // 1/8 cross-section area

echo("sprue0_r=", sprue0_r);
echo("runner0_r=", runner0_r);
echo("runner1_r=", runner1_r);
echo("runner2_r=", runner2_r);

grid_xTranslate = runner0_r + minSpace + baseUnit*lengthMul*0.5;
grid_yInnersTranslate = minSpace*0.5 + baseUnit*0.5;
grid_yOutersTranslate = runner1_r + minSpace*2.5 + baseUnit*1.5;

module keycapGrid () {

  translate([-grid_xTranslate, grid_yOutersTranslate, 0]) keycap();
  translate([grid_xTranslate,  grid_yOutersTranslate, 0]) keycap();
  translate([-grid_xTranslate, grid_yInnersTranslate, 0]) keycap();
  translate([grid_xTranslate,  grid_yInnersTranslate, 0]) keycap();
  translate([-grid_xTranslate, -grid_yInnersTranslate, 0]) keycap();
  translate([grid_xTranslate,  -grid_yInnersTranslate, 0]) keycap();
  translate([-grid_xTranslate, -grid_yOutersTranslate, 0]) keycap();
  translate([grid_xTranslate,  -grid_yOutersTranslate, 0]) keycap();
}

// TODO
module runners () {

  sprue0_z = 10.0; // arbitrary, >plateWidth
  cylinder(h=sprue0_z, r=sprue0_r);

  // Champfer from sprue0 to runner0.
  translate([0, sprue0_r, 0])
    rotate([90, 0, 0])
      cylinder(h=sprue0_r*2, r=sprue0_r);
  translate([0, -sprue0_r+0.001, 0])
    rotate([90, 0, 0])
      cylinder(h=sprue0_r*2, r1=sprue0_r, r2=runner0_r);
  translate([0, sprue0_r-0.001, 0])
    rotate([-90, 0, 0])
      cylinder(h=sprue0_r*2, r1=sprue0_r, r2=runner0_r);

  runner0_l = runner1_r + minSpace*2 + baseUnit*2;
  translate([0, runner0_l/2, 0])
  rotate([90, 0, 0])
  cylinder(h=runner0_l, r=runner0_r);

  // Champfer from runner0 to runner1.
  translate([-runner0_r, runner0_l/2, 0])
    rotate([0, 90, 0])
      cylinder(h=runner0_r*2, r=runner0_r);
  translate([runner0_r, runner0_l/2, 0])
    rotate([0, 90, 0])
      cylinder(h=runner0_r*2, r1=runner0_r, r2=runner1_r);
  translate([-runner0_r, runner0_l/2, 0])
    rotate([0, -90, 0])
      cylinder(h=runner0_r*2, r1=runner0_r, r2=runner1_r);

  runner1_l = runner0_r*2 + minSpace*2;
  translate([-runner1_l/2, runner0_l/2, 0])
  rotate([0, 90, 0])
  cylinder(h=runner1_l, r=runner1_r);

  runner2_l = runner1_r + 2*minSpace;
  runner2_x = runner0_r + minSpace;
  runner2_y = grid_yOutersTranslate - baseUnit*0.5;
  translate([runner2_x,  runner2_y, 0]) rotate([90, 0, 0])  cylinder(h=runner2_l, r=runner2_r);
  translate([-runner2_x, runner2_y, 0]) rotate([90, 0, 0])  cylinder(h=runner2_l, r=runner2_r);
  translate([runner2_x,  -runner2_y, 0]) rotate([90, 0, 0]) cylinder(h=runner2_l, r=runner2_r);
  translate([-runner2_x, -runner2_y, 0]) rotate([90, 0, 0]) cylinder(h=runner2_l, r=runner2_r);
}

//keycapGrid();
color("blue") runners();
