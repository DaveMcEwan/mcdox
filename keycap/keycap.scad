$fn = 64; // Increase to render more faces per curve.

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


/** FDM brim
 * Enabling this makes it easier to print and the brim should just snap off
 * easily after printing.
 */
module brim () {
  cylinder(r=5.0, h=0.3);
}

/** Homing bump
 * Usually on the two index finger keys (F,J on qwerty, U,H on dvorak).
 * Sometimes on DSA just a deeper dish is used.
 */
module homing_bump () {
  translate([0, 0, keycap_z - dish_depth])
  cylinder(h=0.9, r1=1.9, r2=0.7, center=false);
}

/** Rounded rectangle
 */
module rounded_rect (size, radius) {
  x = size[0];
  y = size[1];
  z = size[2];

  translate([-x/2, -y/2, 0])
  linear_extrude(height=z)
  hull() {
    translate([radius, radius, 0])
    circle(r=radius);

    translate([x - radius, radius, 0])
    circle(r=radius);

    translate([x - radius, y - radius, 0])
    circle(r=radius);

    translate([radius, y - radius, 0])
    circle(r=radius);
  }
}

/** Dish
 * DCS: cylindrical cutout from the top face.
 * DSA: spherical cutout from the top face.
 */
module dish (profileNum) {
  dish_radius = (profileNum == 2) ? 38 : 20;

  translate([0, top_skew, keycap_z])
  rotate([90-top_tilt, 0, 0])
  translate([0, dish_radius - dish_depth, 0])
  if (profileNum == 2)
    scale([lengthMul, 1, 1])
    sphere(r=dish_radius, $fn=256);
  else
    cylinder(h=baseUnit, r=dish_radius*lengthMul, $fn=256, center=true);
}

/** Key blockish shape
 * Inner is a scaled and translated copy of outer.
 */
module outerShape (profileNum) {
  top_x_diff  = (profileNum == 2) ? 5.3 : 6;
  top_y_diff  = (profileNum == 2) ? 5.3 : 4;
  base_corner_radius = 1.8;
  straight_wall_side = 3.0;

  difference() {
    hull() {
      rounded_rect([baseUnit*lengthMul,
                    baseUnit,
                    straight_wall_side], base_corner_radius);

      translate([0, top_skew, keycap_z])
      rotate([-top_tilt, 0, 0])
      rounded_rect([baseUnit*lengthMul - top_x_diff,
                    baseUnit - top_y_diff,
                    .001], base_corner_radius);
    }

    dish(profileNum);
  }
}

module innerShape (profileNum) {
  wall_thickness_x = 0.8;
  wall_thickness_y = 0.8;
  wall_thickness_z = 1.0;

  wall_scale_x = 1 - 2*(wall_thickness_x / baseUnit);
  wall_scale_y = 1 - 2*(wall_thickness_y / baseUnit);
  wall_scale_z = 1 - 2*(wall_thickness_z / keycap_z);

  translate([0, 0, -.001])
  scale([wall_scale_x, wall_scale_y, wall_scale_z])
  difference () {
    outerShape(profileNum);

    translate([0, 0, baseUnit/2 + keycap_z - dish_depth])
    cube([lengthMul*baseUnit, baseUnit, baseUnit], center=true);
  }
}

/** CherryMX stem
 */
module stem_cherrymx () {
  // Outer stem should be as big,sturdy as possible but still fit on switch.
  stem_x = 2.11;
  stem_y = 1.1;
  stem_z = 4.0;

  // Inner cross of the stem.
  cross_x = 1.3;
  cross_y = 1.4;
  cross_arm = 4.4;
  cross_z = 3.8; // Cutout depth, stem height is 3.4mm.

  difference() {
    union() {
      // Massively over-deep stem which is cut down later.
      translate([-(cross_arm + stem_x)/2,
                 -(cross_arm + stem_y)/2,
                 0])
      cube([cross_arm + stem_x,
            cross_arm + stem_y,
            baseUnit]);

      // Support structure to reduce stress on joining corners.
      translate([0, 0, stem_z])
      cylinder(h=keycap_z,
               r1=(cross_arm + stem_y)/2,
               r2=baseUnit/2,
               center=false);

      if (doBrim == 1)
        brim();
    }

    // Inner cross
    translate([0, 0, cross_z/2])
    union() {
      cube([cross_x, cross_arm, cross_z + .001], center=true);
      cube([cross_arm, cross_y, cross_z + .001], center=true);
    }
  }
}

/** ALPS/Matias stem
 */
module stem_alps () {
  stem_x = 4;
  stem_y = 2;
  stem_z = 5.0;

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

    if (doBrim == 1)
        brim();
  }
}

/** Full keycap
 */
module keycap () {
  union() {
    // Basic shell shape.
    difference() {
      outerShape(profileNum);
      innerShape(profileNum);
    }

    if (doBump == 1)
      homing_bump();

    // Correct-length stem formed by subtracting large cube from overdeep stem.
    difference() {
      if (stemNum == 1)
        stem_cherrymx();
      else if (stemNum == 2)
        stem_alps();

      // Large cube with innerShape cutout to subtract over-deep stem.
      difference() {
        translate([0, 0, baseUnit/2])
        cube([lengthMul*baseUnit+1, baseUnit+1, baseUnit+1], center=true);

        innerShape(profileNum);
      }
    }
  }
}

keycap();

