
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

module runner(r, l, x=0, y=0, alongYnotX=0) {
  color("blue")
  translate([x, y, 0])
  rotate([90*alongYnotX, 90-90*alongYnotX, 0])
  cylinder(h=l, r=r, center=true);
  echo("runner r=", r," l=", l);
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

/*
l is child offset from origin, i.e. runner length
r2 is parent runner radius
r1 is self runner radius
r0 is child runner radius
*/
module partPair(r1=1, r2=2) {
  v = r2 + minSpace + baseUnit/2;
  l = r2 + minSpace; // Length of runner. TODO modify for gate.

  union() {
    translate([0,  v, 0]) keycap(stemNum, shellNum, uMul, doBump);
    runner(r1, l*2, 0, 0, 1);
    translate([0, -v, 0]) keycap(stemNum, shellNum, uMul, doBump);
  }
}

module part4(r1=1, r2=2) {
  l = r2 + minSpace + baseUnit/2;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0]) partPair(r1=r0, r2=r1);
    translate([-l, 0, 0]) partPair(r1=r0, r2=r1);
    runner(r1, l*2, 0, 0, 0);
    reducingChamfer(r1, r0,  l, 0, 1);
    reducingChamfer(r1, r0, -l, 0, 1);
  }
}

module part8(r1=1, r2=2) {
  l = r2 + r1 + 2*minSpace + baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([0,  l, 0]) part4(r1=r0, r2=r1);
    translate([0, -l, 0]) part4(r1=r0, r2=r1);
    runner(r1, l*2, 0, 0, 1);
    reducingChamfer(r1, r0, 0,  l, 0);
    reducingChamfer(r1, r0, 0, -l, 0);
  }
}

module part16(r1=1, r2=2) {
  l = r2 + r1 + 2*minSpace + baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0]) part8(r1=r0, r2=r1);
    translate([-l, 0, 0]) part8(r1=r0, r2=r1);
    runner(r1, l*2, 0, 0, 0);
    reducingChamfer(r1, r0,  l, 0, 1);
    reducingChamfer(r1, r0, -l, 0, 1);
  }
}

module part32(r1=1, r2=2) {
  l = r2 + 2*r1 + 4*minSpace + 2*baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([0,  l, 0]) part16(r1=r0, r2=r1);
    translate([0, -l, 0]) part16(r1=r0, r2=r1);
    runner(r1, l*2, 0, 0, 1);
    reducingChamfer(r1, r0, 0,  l, 0);
    reducingChamfer(r1, r0, 0, -l, 0);
  }
}

module part64(r1=1, r2=2) {
  l = r2 + 2*r1 + 4*minSpace + 2*baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0]) part32(r1=r0, r2=r1);
    translate([-l, 0, 0]) part32(r1=r0, r2=r1);
    runner(r1, l*2, 0, 0, 0);
    reducingChamfer(r1, r0,  l, 0, 1);
    reducingChamfer(r1, r0, -l, 0, 1);
  }
}

module isogrid16(r2=2, margin=6) {
  r1 = halfVolRadius(r2); // 1/2 cross-section area
  l = 2 * (r2 + r1 + 2*minSpace + baseUnit) + margin;

  r3 = r2 * sqrt(2); // Input hole radius.

  union() {
    part16(r1=r1, r2=r2);
    runner(r2, l, 0, l/2, 1);
    reducingChamfer(r2, r1, 0,  0, 0);

    // Input hole
    translate([0, l-minDim, 0])
    rotate([-90, 0, 0])
    cylinder(h=r3, r1=r2, r2=r3, center=false);
  }
}

module isogrid64(r2=2, margin=10) {
  r1 = halfVolRadius(r2); // 1/2 cross-section area
  l = 2 * (r2 + r1 + 4*minSpace + 2*baseUnit) + margin;

  r3 = r2 * sqrt(2); // Input hole radius.

  union() {
    part64(r1=r1, r2=r2);
    runner(r2, l, 0, l/2, 1);
    reducingChamfer(r2, r1, 0,  0, 0);

    // Input hole
    translate([0, l-minDim, 0])
    rotate([-90, 0, 0])
    cylinder(h=r3, r1=r2, r2=r3, center=false);
  }
}

// TODO: Sprue radius r2 from viscosity, pressure, injection time,and volume.
// TODO: Mold halves.
// TODO: Gate/tabs.
// TODO: Vents?
isogrid16(r2=2);
//isogrid64(r2=5);
