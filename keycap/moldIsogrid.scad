
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

module gatePair(r, l, overshoot=0.3) {
  /*
  echo("moldIsogrid.scad gatePair()");
  echo("\t r=", r);
  echo("\t l=", l);
  echo("\t overshoot=", overshoot);
  */

  a = atan(r/l);

  color("green")
  union() {
    rotate([90, 0, 0])
    cylinder(h=2*r+4*minDim, r=r, center=true);

    translate([0, r+l+minDim, 0])
    rotate([0, 90, -90])
    difference() {
      translate([0, 0, -overshoot])
      cylinder(h=l+overshoot, r=r, center=false);

      rotate([0, a, 0])
      translate([0, -r, -r])
      cube([r*2, r*2, 2*l+minDim], center=false);
    }

    translate([0, -(r+l+minDim), 0])
    rotate([0, 90, 90])
    difference() {
      translate([0, 0, -overshoot])
      cylinder(h=l+overshoot, r=r, center=false);

      rotate([0, a, 0])
      translate([0, -r, -r])
      cube([r*2, r*2, 2*l+minDim], center=false);
    }
  }
}

module runner(r, l, alongYnotX=0) {
  /*
  echo("moldIsogrid.scad runner()");
  echo("\t r=", r);
  echo("\t l=", l);
  echo("\t alongYnotX=", alongYnotX);
  */

  color("blue")
  rotate([90*alongYnotX, 90-90*alongYnotX, 0])
  cylinder(h=l, r=r, center=true);
}

module reducingChamfer(r1, r2, x=0, y=0, alongYnotX=0) {
  chamfer_l = r1 * 4/3;

  translate([x, y, 0])
  rotate([90*alongYnotX, 90-90*alongYnotX, 0])
  union() {
    // Cones stacked on Z-axis.

    cylinder(h=r1*2+minDim, r=r1, center=true);

    translate([0, 0,  r1])
    cylinder(h=chamfer_l, r1=r1, r2=r2, center=false);

    rotate([180, 0, 0])
    translate([0, 0, r1])
    cylinder(h=chamfer_l, r1=r1, r2=r2, center=false);
  }
}

module vents() {
  vent_w = 1.0;
  pri_d = 0.02; // ABS
  pri_l = 0.5;
  sec_d = 0.5;
  sec_l = 20; // oversize

  x = baseUnit/3; // Place 1/3 along edge from center.
  pri_y = baseUnit/2 - minDim;
  sec_y = baseUnit/2 + pri_l;

  union () {
    translate([ x, pri_y+pri_l/2, pri_d/2-minDim]) cube([vent_w, pri_l+2*minDim, pri_d], center=true);
    translate([-x, pri_y+pri_l/2, pri_d/2-minDim]) cube([vent_w, pri_l+2*minDim, pri_d], center=true);
    translate([ x, sec_y+sec_l/2, pri_d/2-minDim]) cube([vent_w, sec_l, sec_d], center=true);
    translate([-x, sec_y+sec_l/2, sec_d/2-minDim]) cube([vent_w, sec_l, sec_d], center=true);
  }
}

/*
l is child offset from origin, i.e. runner length
r2 is parent runner radius
r1 is self runner radius
r0 is child runner radius
*/

module partPair(r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0,
                mold=0) {
  /*
  echo("moldIsogrid.scad partPair()");
  echo("\t r2=", r2);
  echo("\t stemNum=", stemNum);
  echo("\t shellNum=", shellNum);
  echo("\t uMul=", uMul);
  echo("\t doBump=", doBump);
  echo("\t solidInner=", solidInner);
  echo("\t innerOnly=", innerOnly);
  echo("\t outerOnly=", outerOnly);
  */

  v = r2 + minSpace + baseUnit/2;
  l = r2 + minSpace; // Length of runner.

  union() {
    translate([0,  v, 0]) {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump,
             mold=mold);

      if (3 == mold) vents();
    }

    translate([0, -v, 0])
    rotate([0, 0, 180]) {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump,
             mold=mold);

      if (3 == mold) vents();
    }

    if (1 != mold) gatePair(r2, minSpace);

  }
}

module part4(r1=1, r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0,
             mold=0) {
  /*
  echo("moldIsogrid.scad part4()");
  echo("\t r1=", r1);
  echo("\t r2=", r2);
  echo("\t stemNum=", stemNum);
  echo("\t shellNum=", shellNum);
  echo("\t uMul=", uMul);
  echo("\t doBump=", doBump);
  echo("\t mold=", mold);
  */

  l = r2 + minSpace + uMul*baseUnit/2;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0])
    partPair(r2=r1,
             stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump,
             mold=mold);

    translate([-l, 0, 0])
    partPair(r2=r1,
             stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump,
             mold=mold);

    if (1 != mold) runner(r1, l*2, 0);
  }
}

module part8(r1=1, r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  l = r2 + r1 + 2*minSpace + baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([0,  l, 0])
    part4(r1=r0, r2=r1,
          stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump);

    translate([0, -l, 0])
    part4(r1=r0, r2=r1,
          stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump);

    runner(r1, l*2, 1);
    reducingChamfer(r1, r0, 0,  l, 0);
    reducingChamfer(r1, r0, 0, -l, 0);
  }
}

module part16(r1=1, r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  l = r2 + r1 + 2*minSpace + baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0]) part8(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    translate([-l, 0, 0]) part8(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    runner(r1, l*2, 0);
    reducingChamfer(r1, r0,  l, 0, 1);
    reducingChamfer(r1, r0, -l, 0, 1);
  }
}

module part32(r1=1, r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  l = r2 + 2*r1 + 4*minSpace + 2*baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([0,  l, 0]) part16(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    translate([0, -l, 0]) part16(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    runner(r1, l*2, 1);
    reducingChamfer(r1, r0, 0,  l, 0);
    reducingChamfer(r1, r0, 0, -l, 0);
  }
}

module part64(r1=1, r2=2, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  l = r2 + 2*r1 + 4*minSpace + 2*baseUnit;
  r0 = halfVolRadius(r1); // 1/2 cross-section area

  union() {
    translate([ l, 0, 0]) part32(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    translate([-l, 0, 0]) part32(r1=r0, r2=r1, stemNum, shellNum, uMul, doBump);
    runner(r1, l*2, 0);
    reducingChamfer(r1, r0,  l, 0, 1);
    reducingChamfer(r1, r0, -l, 0, 1);
  }
}

module moldIsogrid4(r2=1, margin=5, stemNum=1, shellNum=1, uMul=1.0, doBump=0,
                mold=0) {
  /*
  echo("moldIsogrid.scad moldIsogrid4()");
  echo("\t r2=", r2);
  echo("\t margin=", margin);
  echo("\t stemNum=", stemNum);
  echo("\t shellNum=", shellNum);
  echo("\t uMul=", uMul);
  echo("\t doBump=", doBump);
  echo("\t mold=", mold);
  */

  r1 = halfVolRadius(r2); // 1/2 cross-section area
  l = 2 * (r2 + minSpace + baseUnit/2) + margin;

  r3 = r2 * sqrt(2); // Input hole radius.

  union() {
    part4(r1=r1, r2=r2,
          stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump,
          mold=mold);

    if (1 != mold) {
      translate([0, l/2, 0]) runner(r2, l, 1);
      reducingChamfer(r2, r1, 0,  0, 0);

      // Input hole
      translate([0, l-minDim, 0])
      rotate([-90, 0, 0])
      cylinder(h=r3, r1=r2, r2=r3, center=false);
    }
  }
}

module moldIsogrid16(r2=4, margin=6, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  r1 = halfVolRadius(r2); // 1/2 cross-section area
  l = 2 * (r2 + r1 + 2*minSpace + baseUnit) + margin;

  r3 = r2 * sqrt(2); // Input hole radius.

  union() {
    part16(r1=r1, r2=r2, stemNum, shellNum, uMul, doBump);
    translate([0, l/2, 0]) runner(r2, l, 1);
    reducingChamfer(r2, r1, 0,  0, 0);

    // Input hole
    translate([0, l-minDim, 0])
    rotate([-90, 0, 0])
    cylinder(h=r3, r1=r2, r2=r3, center=false);
  }
}

module moldIsogrid64(r2=5, margin=10, stemNum=1, shellNum=1, uMul=1.0, doBump=0) {
  r1 = halfVolRadius(r2); // 1/2 cross-section area
  l = 2 * (r2 + r1 + 4*minSpace + 2*baseUnit) + margin;

  r3 = r2 * sqrt(2); // Input hole radius.

  union() {
    part64(r1=r1, r2=r2, stemNum, shellNum, uMul, doBump);
    translate([0, l/2, 0]) runner(r2, l, 1);
    reducingChamfer(r2, r1, 0,  0, 0);

    // Input hole
    translate([0, l-minDim, 0])
    rotate([-90, 0, 0])
    cylinder(h=r3, r1=r2, r2=r3, center=false);
  }
}

// TODO: Sprue radius r2 from viscosity, pressure, injection time,and volume.
moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=0);
//moldIsogrid16(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump);
//moldIsogrid64(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump);
