
// Overrideable parameters.
stemNum     = 1;    // Stem shape (CherryMX:1, Matias/ALPS:2)
profileNum  = 2;    // Profile (DCS:1, DSA:2)
lengthMul   = 1.0;  // Length multiple. Ergodox has (1, 1.5, 2)
doBump      = 0;    // Enable homing bump.
doBrim      = 0;    // Enable FDM brim for stem.

// Common parameters.
//                                DSA   : DCS
keycap_z    = (profileNum == 2) ? 7.8   : 8.5;
top_tilt    = (profileNum == 2) ? 0     : -1;
top_skew    = (profileNum == 2) ? 0     : 1.75;
dish_depth  = (profileNum == 2) ? 1.2   : 1;

// Standard for mechanical computer keyboards.
baseUnit = 18;

