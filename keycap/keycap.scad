
use <keycapStem.scad>
use <keycapShell.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.
//doBrim      = 0;    // Enable FDM brim for stem.


/** Full keycap
 */
module keycap () {
  union() {
    color("lightgreen")
    if (2 == shellNum) shellDCS(uMul, doBump);
    else               shellDSA(uMul, doBump);

    color("lightblue")
    if (2 == stemNum) stemMatiasALPS();
    else              stemCherryMX();
  }
}

keycap();

