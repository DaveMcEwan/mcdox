
use <keycapStem.scad>
use <keycapShell.scad>

// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
shellNum    = 1;    // Profile (DSA:1, DCS:2)
uMul        = 1.5;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.


/** Full keycap

mold 0 -> no mold
     1 -> lower negative
     2 -> lower positive, Only for registration trough.
     3 -> upper positive
 */
module keycap (stemNum=1, shellNum=1, uMul=1.0, doBump=0, mold=0) {
  /*
  echo("keycap.scad keycap()");
  echo("\t stemNum=", stemNum);
  echo("\t shellNum=", shellNum);
  echo("\t uMul=", uMul);
  echo("\t doBump=", doBump);
  echo("\t mold=", mold);
  */

  if (1 == mold) {

    difference() {
      color("crimson")
      if (2 == shellNum) innerDCS(u=uMul);
      else               innerDSA(u=uMul);

      color("lightblue")
      if (2 == stemNum) stemMatiasALPS();
      else              stemCherryMX();
    }

  } else if (2 == mold) {

      color("lightgreen")
      if (2 == shellNum) shellDCS(u=uMul, doBump=0);
      else               shellDSA(u=uMul, doBump=0);

  } else if (3 == mold) {

      color("lightgreen")
      if (2 == shellNum) outerDCS(uMul, doBump);
      else               outerDSA(uMul, doBump);

  } else {

    union() {
      color("lightgreen")
      if (2 == shellNum) shellDCS(uMul, doBump);
      else               shellDSA(uMul, doBump);

      color("lightblue")
      if (2 == stemNum) stemMatiasALPS();
      else              stemCherryMX();
    }

  }

}

keycap(stemNum, shellNum, uMul, doBump);

