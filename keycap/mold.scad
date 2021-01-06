
use <moldIsogrid.scad>
use <keycap.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.

moldXY = 60;

singleImpression = 0; // Faster to render, useful for debug.

module moldUpper (z=15, shellNum=1, uMul=1.0, doBump=0) {
  difference() {
    translate([0, 0, z/2])
    cube([moldXY, moldXY, z], center=true);

    if (0 == singleImpression) {
      moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=3);
    } else {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=3);
    }

    // TODO: registration hole
  }
}

module moldLower (z=10, shellNum=1, uMul=1.0) {
  union() {
    difference() {
      translate([0, 0, -z/2])
      cube([moldXY, moldXY, z], center=true);

      // Flow registration trough.
      if (0 == singleImpression) {
        moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=2);
      } else {
        keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=2);
      }

      // TODO: Vents?
      // TODO: Ejector pin holes?
    }

    if (0 == singleImpression) {
      moldIsogrid4(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=1);
    } else {
      keycap(stemNum=stemNum, shellNum=shellNum, uMul=uMul, doBump=doBump, mold=1);
    }

    // TODO: registration pin
  }
}

translate([0, 0, -20]) moldUpper(shellNum=shellNum, uMul=uMul, doBump=doBump);
translate([0, 0,  20]) moldLower(shellNum=shellNum, uMul=uMul);
