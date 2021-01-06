
use <isogrid.scad>
use <keycapShell.scad>
use <keycapStem.scad>
use <keycap.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.

moldXY = 50;

module moldUpper (z=15, shellNum=1, uMul=1.0, doBump=0) {
  difference() {
    translate([0, 0, z/2])
    cube([moldXY, moldXY, z], center=true);

    if (2 == shellNum) outerDCS(u=uMul, doBump=doBump);
    else               outerDSA(u=uMul, doBump=doBump);
  }
}

module moldLower (z=10, shellNum=1, uMul=1.0) {
  union() {
    difference() {
      translate([0, 0, -z/2])
      cube([moldXY, moldXY, z], center=true);

      if (2 == shellNum) outerDCS(u=uMul);
      else               outerDSA(u=uMul);
    }

    difference() {
      if (2 == shellNum) innerDCS(u=uMul);
      else               innerDSA(u=uMul);

      if (2 == stemNum) stemMatiasALPS();
      else              stemCherryMX();
    }
  }
}

translate([0, 0, -20]) moldUpper(shellNum=shellNum, uMul=uMul, doBump=doBump);
translate([0, 0,  20]) moldLower(shellNum=shellNum, uMul=uMul);
