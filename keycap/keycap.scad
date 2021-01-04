
use <keycapStem.scad>
use <keycapShell.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
profileNum  = 1;    // Profile (DSA:1, DCS:2)
lengthMul   = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.
doBrim      = 0;    // Enable FDM brim for stem.



/** ALPS/Matias stem
TODO: Move to keycapStem and do properly with rounding, drafting, etc.
 */
module stem_alps () {
  stem_x = 4;
  stem_y = 2;
  stem_z = 5.0;
  baseUnit = 18.0;

  union() {
    // Massively over-deep stem which is cut down later.
    translate([-(stem_x)/2, -(stem_y)/2, 0])
    cube([stem_x, stem_y, baseUnit]);

    // Support structure to reduce stress on joining corners.
    // Only seen when keycap_z is very high.
    translate([0, 0, stem_z])
    cylinder(h=(baseUnit - stem_y)/2,
             r1=stem_y/2,
             r2=baseUnit/2,
             center=false);
  }
}

/** Full keycap
 */
module keycap () {
  union() {
    #color("lightgreen")
    if (2 == profileNum)
      shellDCS(lengthMul, doBump);
    else
      shellDSA(lengthMul, doBump);

    color("lightblue")
    if (2 == stemNum)
      stem_alps();
    else
      stemCherryMX();
  }
}

keycap();

