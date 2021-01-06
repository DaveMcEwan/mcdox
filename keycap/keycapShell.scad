
minDim = 0.001;

baseUnit = 18.0;
draft_deg = 20; // Large taper for easier mold removal, Set for anything.
registration_z = 0.3;

/** Rounded rectangle
*/
module roundedRect (width, height, radius) {
  x = width/2-radius;
  y = height/2-radius;
  hull() {
    translate([-x, -y, 0]) circle(r=radius, $fn=64);
    translate([-x,  y, 0]) circle(r=radius, $fn=64);
    translate([ x, -y, 0]) circle(r=radius, $fn=64);
    translate([ x,  y, 0]) circle(r=radius, $fn=64);
  }
}


module outerDSA (u=1.0, doBump=0) {
  // Top is smaller than base.
  xDiff = 5.3;
  yDiff = 5.3;

  topZ = 7.8;
  dishDepth = 1.2; // Bottom of dish is topZ-dishDepth above origin.
  corner_r = 1.8;

  /** dishVoidDSA Spherical cutout from the top face.
  */
  module dishVoidDSA (u=1.0) {
    r = 38;

    rotate([90, 0, 0])
    translate([0, r, 0])
    scale([u, 1, 1])
    sphere(r=r, $fn=100);
  }

  // Walls are almost straight, but edge at keycap midheight is slightly smaller
  // to make walls slant inwards (draft) for easier mold release.
  wallZ = 5.0;
  d = wallZ * tan(draft_deg); // Reduction length for draft angle.

  union() {
    difference() {
      hull() {
        linear_extrude(minDim)
        roundedRect(baseUnit*u, baseUnit, corner_r);

        translate([0, 0, wallZ])
        linear_extrude(minDim)
        roundedRect(baseUnit*u-d, baseUnit-d, corner_r);

        translate([0, 0, topZ])
        linear_extrude(minDim)
        roundedRect(baseUnit*u-xDiff, baseUnit-yDiff, corner_r);

        // Registration cutout in bottom mold half.
        translate([0, 0, -registration_z])
        linear_extrude(registration_z+minDim)
        roundedRect(baseUnit*u, baseUnit, corner_r);
      }

      translate([0, 0, topZ - dishDepth])
      dishVoidDSA(u);
    }

    // Homing bump
    // Usually on the two index finger keys (F,J on qwerty, U,H on dvorak).
    // Sometimes on DSA just a deeper dish is used.
    if (0 != doBump)
      translate([0, 0, topZ - 1.5*dishDepth])
      cylinder(h=0.9, r1=1.9, r2=0.7, center=false, $fn=32);
  }
}

module innerDSA (u=1.0) {
  wallT = 1.0; // Wall thickness
  roofT = 1.1;

  // Top is smaller than base.
  xDiff = 5.3;
  yDiff = 5.3;
  topZ = 6.6 - roofT; // outerDSA.topZ - dishDepth - roofT = 5.5

  corner_r = 1.5;

  // Walls are almost straight, but edge at keycap midheight is slightly smaller
  // to make walls slant inwards (draft) for easier mold release.
  wallZ = 5.0;
  d = wallZ * tan(draft_deg); // Reduction length for draft angle.

  hull() {
    translate([0, 0, -minDim])
    linear_extrude(minDim)
    roundedRect(baseUnit*u - 2*wallT, baseUnit - 2*wallT, corner_r);

    translate([0, 0, wallZ])
    linear_extrude(minDim)
    roundedRect(baseUnit*u-d - 2*wallT, baseUnit-d - 2*wallT, corner_r);

    translate([0, 0, topZ])
    linear_extrude(minDim)
    roundedRect(baseUnit*u-xDiff - 2*wallT, baseUnit-yDiff - 2*wallT, corner_r);

    // Registration cutout in bottom mold half.
    translate([0, 0, -minDim-registration_z])
    linear_extrude(registration_z+minDim)
    roundedRect(baseUnit*u - 2*wallT, baseUnit - 2*wallT, corner_r);
  }
}

module shellDSA (u=1.0, doBump=0, solidInner=0) {
  difference() {
    outerDSA(u, doBump);

    if (0 == solidInner) innerDSA(u);
  }
}

translate([20, 0, 0])
shellDSA(1.0, 1);

translate([20, 30, 0])
shellDSA(1.5, 1);

translate([50, 0, 0])
color("lightblue")
outerDSA(1.0);

translate([50, 30, 0])
color("lightblue")
outerDSA(1.5);

translate([80, 0, 0])
color("red")
innerDSA(1.0);

translate([80, 30, 0])
color("red")
innerDSA(1.5);


module outerDCS (u=1.0, doBump=0) {
  // Top is smaller than base.
  xDiff = 6;
  yDiff = 4;

  topZ = 8.2;
  dishDepth = 1.0; // Bottom of dish is topZ-dishDepth above origin.
  corner_r = 1.8;

  /** dishVoidDCS Cylindrical cutout from the top face.
  */
  module dishVoidDCS (u=1.0) {
    r = 20;
    tilt_deg = 2.0;

    // Tilt direction is unclear for non-square, so lie cutout flat.
    if (1.0 == u)
      rotate([90-tilt_deg, 0, 90])
      translate([0, r - dishDepth, 0])
      cylinder(h=baseUnit*u+minDim, r=r, center=true, $fn=60);
    else
      rotate([90, 0, 90])
      translate([0, r - dishDepth, 0])
      cylinder(h=baseUnit*u+minDim, r=r, center=true, $fn=60);
  }

  // Walls are almost straight, but edge at keycap midheight is slightly smaller
  // to make walls slant inwards (draft) for easier mold release.
  wallZ = 5.0;
  d = wallZ * tan(draft_deg); // Reduction length for draft angle.

  union() {
    difference() {
      hull() {
        linear_extrude(minDim)
        roundedRect(baseUnit*u, baseUnit, corner_r);

        translate([0, 0, wallZ])
        linear_extrude(minDim)
        roundedRect(baseUnit*u-d, baseUnit-d, corner_r);

        translate([0, 0, topZ])
        linear_extrude(minDim)
        roundedRect(baseUnit*u-xDiff, baseUnit-yDiff, corner_r);
      }

      translate([0, 0, topZ - dishDepth])
      dishVoidDCS(u);
    }

    // Homing bump
    // Usually on the two index finger keys (F,J on qwerty, U,H on dvorak).
    // Sometimes on DSA just a deeper dish is used.
    if (0 != doBump)
      translate([0, 0, topZ - 2.1*dishDepth])
      cylinder(h=0.8, r1=1.9, r2=0.8, center=false, $fn=32);
  }
}

module innerDCS (u=1.0) {
  wallT = 0.8; // Wall thickness
  roofT = 1.3;

  // Top is smaller than base.
  xDiff = 5.3;
  yDiff = 5.3;
  topZ = 7.2 - roofT; // outerDCS.topZ - dishDepth - roofT = 6.4

  corner_r = 1.5;

  // Walls are almost straight, but edge at keycap midheight is slightly smaller
  // to make walls slant inwards (draft) for easier mold release.
  wallZ = 5.0;
  d = wallZ * tan(draft_deg); // Reduction length for draft angle.

  hull() {
    translate([0, 0, -minDim])
    linear_extrude(minDim)
    roundedRect(baseUnit*u - 2*wallT, baseUnit - 2*wallT, corner_r);

    translate([0, 0, wallZ])
    linear_extrude(minDim)
    roundedRect(baseUnit*u-d - 2*wallT, baseUnit-d - 2*wallT, corner_r);

    translate([0, 0, topZ])
    linear_extrude(minDim)
    roundedRect(baseUnit*u-xDiff - 2*wallT, baseUnit-yDiff - 2*wallT, corner_r);
  }
}

module shellDCS (u=1.0, doBump=0) {
  difference() {
    outerDCS(u, doBump);
    innerDCS(u);
  }
}


translate([-20, 0, 0])
shellDCS(1.0, 1);

translate([-20, 30, 0])
shellDCS(1.5, 1);

translate([-50, 0, 0])
color("lightblue")
outerDCS(1.0);

translate([-50, 30, 0])
color("lightblue")
outerDCS(1.5);

translate([-80, 0, 0])
color("red")
innerDCS(1.0);

translate([-80, 30, 0])
color("red")
innerDCS(1.5);
