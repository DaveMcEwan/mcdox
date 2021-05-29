
use <moldIsogrid.scad>
use <keycap.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.

singleImpression = 0; // Faster to render, useful for debug.

/* moldPart 0 -> Both upper and lower halves.
            1 -> Lower only.
            2 -> Upper only.
*/
moldPart = 0;

moldXY = 60;
regpin_l = 8;
regpin_a = 2; // Similar to draft angle
regpin_r1 = 2.5;
regpin_r2 = regpin_r1 - regpin_l * tan(regpin_a);
regvent_r = 1; // Vent to let air escape from registration holes.

baseUnit = 18.0;
minDim = 0.001;

module moldUpper (z=15, shellNum=1, uMul=1.0, doBump=0) {
  x = moldXY + 2*(uMul-1)*baseUnit;
  y = moldXY;

  regpin_x = x/2-2*regpin_r1;
  regpin_y = y/2-2*regpin_r1;

  difference() {
    translate([0, 0, z/2])
    cube([x, y, z], center=true);

    if (0 == singleImpression) {
      moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=3);
    } else {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=3);
    }

    // Registration holes.
    translate([regpin_x, regpin_y, -2*minDim]) {
      cylinder(h=regpin_l, r1=regpin_r1, r2=regpin_r2, center=false, $fn=32);
      cylinder(h=regpin_l*2, r=regvent_r, center=false, $fn=32);
    }
    translate([-regpin_x, -regpin_y, -2*minDim]) {
      cylinder(h=regpin_l, r1=regpin_r1, r2=regpin_r2, center=false, $fn=32);
      cylinder(h=regpin_l*2, r=regvent_r, center=false, $fn=32);
    }
  }
}

module moldLower (z=10, shellNum=1, uMul=1.0) {
  x = moldXY + 2*(uMul-1)*baseUnit;
  y = moldXY;

  regpin_x = x/2-2*regpin_r1;
  regpin_y = y/2-2*regpin_r1;

  union() {
    difference() {
      translate([0, 0, -z/2])
      cube([x, y, z], center=true);

      // Flow registration trough.
      if (0 == singleImpression) {
        moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=2);
      } else {
        keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=2);
      }
    }

    if (0 == singleImpression) {
      moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=1);
    } else {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=1);
    }

    // Registration pins.
    // 5% shorter than holes together with angle for easier mating.
    translate([regpin_x, regpin_y, -minDim-0.05*regpin_l])
    cylinder(h=regpin_l, r1=regpin_r1, r2=regpin_r2, center=false, $fn=32);
    translate([-regpin_x, -regpin_y, -minDim-0.05*regpin_l])
    cylinder(h=regpin_l, r1=regpin_r1, r2=regpin_r2, center=false, $fn=32);
  }
}

if (2 == moldPart) {
  moldUpper(shellNum=shellNum, uMul=uMul, doBump=doBump);
} else if (1 == moldPart) {
  moldLower(shellNum=shellNum, uMul=uMul);
}
else {
  translate([0, 0,  20]) moldLower(shellNum=shellNum, uMul=uMul);
  translate([0, 0, -20]) moldUpper(shellNum=shellNum, uMul=uMul, doBump=doBump);
}
