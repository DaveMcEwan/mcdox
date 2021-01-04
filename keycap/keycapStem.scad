
minDim = 0.001;

innerCorners_r = 0.02;
outerCorners_r = 0.02;
draft_deg = 0.6; // Slight taper for easier mold removal, Set for ABS.
stemRecess = 1.2;

/** Rounded rectangle
*/
module roundedRect (width, height, radius) {
  x = width/2-radius;
  y = height/2-radius;
  hull() {
    translate([-x, -y, 0]) circle(r=radius);
    translate([-x,  y, 0]) circle(r=radius);
    translate([ x, -y, 0]) circle(r=radius);
    translate([ x,  y, 0]) circle(r=radius);
  }
}

/** Inner cross which press-fits onto CherryMX-compatible switch.
*/
module crossVoid () {
  $fn = 64;

  // Enlarge XY dimensions to allow easy but reliable pressfit onto stem.
  pressfitXY = 0.05; // Includes 0.5% shrinkage tolerance.

  // Void above stem for air, mold detritus, dirt, etc.
  pressfitZ = 0.6;

  /** crossVoid cross-section
  Measured on Gateron Brown.

            o----o                       ^
            |    |                       |
            |    |                       |
            |    |                       |
            |    |                       |
   o--------+    +--------o   ^          |
   |                      |   |          |
   |                      |   |          |
   |                      |   |          |
   o--------+    +--------o   v          |
            |    |            crossHd    |
            |    |                       |
            |    |                       |
            |    |                       |
            o----o                       v
                                         crossVl
            <----> crossVd

   <----------------------> crossHl

  */
  crossVd = 1.15 + pressfitXY;
  crossHd = 1.30 + pressfitXY;
  crossVl = 4.00 + pressfitXY;
  crossHl = 4.05 + pressfitXY;
  crossZ = 3.50 + pressfitZ + minDim; // minDim for later difference().

  /** Top-Rounded Cuboid
  Where draft angle is non-zero this is technically a trapezoid.
  Base is centered on origin with original dimensions with 2D rounded corners.
  Top is centered on +Z with drafted dimensions (slightly smaller) and 3D rounded
  corners.
  */
  module toproundedCube (width, height, depth, radius, topDelta) {
    xTop = width/2 - radius - topDelta;
    yTop = height/2 - radius - topDelta;
    zTop = depth - radius;

    hull() {
      linear_extrude(minDim) roundedRect(width, height, radius);

      translate([-xTop, -yTop, zTop]) sphere(r=radius);
      translate([-xTop,  yTop, zTop]) sphere(r=radius);
      translate([ xTop, -yTop, zTop]) sphere(r=radius);
      translate([ xTop,  yTop, zTop]) sphere(r=radius);
    }
  }

  /** Four Inner Corners with draft and inner and outer radius.
  Rotational extrusions take more code but render much faster than minkowski.
  */
  module innerCorners (offsetX, offsetY, inner_r, outer_r, topDelta, depth) {

    module innerCorner (outer_r, inner_r, topDelta, depth) {

      rotate_extrude(angle=90)
      hull() {
        translate([outer_r + topDelta + inner_r, depth - outer_r, 0])
        union() {
          circle(r=outer_r);

          translate([outer_r, 0])
          square([outer_r*2, outer_r*2], center=true);
        }

        translate([inner_r, 0, 0])
        square([outer_r*2, minDim], center=false);
      }
    }

    x = offsetX/2 + inner_r;
    y = offsetY/2 + inner_r;

    translate([-x, -y, 0])
    innerCorner(outer_r, inner_r, topDelta, depth);

    translate([x, -y, 0])
    rotate([0, 0, 90])
    innerCorner(outer_r, inner_r, topDelta, depth);

    translate([x, y, 0])
    rotate([0, 0, 180])
    innerCorner(outer_r, inner_r, topDelta, depth);

    translate([-x, y, 0])
    rotate([0, 0, 270])
    innerCorner(outer_r, inner_r, topDelta, depth);
  }

  d = crossZ * tan(draft_deg); // Reduction length for draft angle.

  translate([0, 0, -minDim/2]) // minDim for later difference().
  union() {
    toproundedCube(crossVd, crossVl, crossZ, outerCorners_r, d);
    toproundedCube(crossHl, crossHd, crossZ, outerCorners_r, d);
    innerCorners(crossVd, crossHd, outerCorners_r, innerCorners_r, d, crossZ);
  }
}

/** Round pillar with support collar at top.
*/
module solidPillar () {
  diameter = 5.6;

  // Measurements from existing piece.
  height = 5.0 - stemRecess;

  radius = diameter / 2;
  d = height * tan(draft_deg); // Expansion at top for draft angle.

  union() {
    hull() {
      translate([0, 0, height-minDim/2])
      cylinder(h=minDim, r=radius+d, center=true, $fn=256);

      translate([0, 0, outerCorners_r])
      rotate_extrude($fn=256)
      translate([radius - outerCorners_r, outerCorners_r/2, 0])
      circle(r=outerCorners_r, $fn=32);
    }

    // Support structure to reduce stress on joining corners.
    // 45deg collar intended to be mostly removed in final keycap.
    collarZ = 1.0;
    translate([0, 0, height-minDim])
    cylinder(h=collarZ, r1=radius+d, r2=radius+collarZ, center=false, $fn=256);
  }
}

/** Circular Stem for CherryMX, Pre-positioned with Z-recess.
*/
module stemCherryMX () {
  translate([0, 0, stemRecess])
  difference() {
    solidPillar();
    crossVoid();
  }
}
stemCherryMX();

translate([20, 0, 0])
color("red")
crossVoid();

translate([10, 0, 0])
color("blue")
solidPillar();

/** fdmStemBrim Assist FDM printing with brim which should snap off easily.
TODO
*/
module fdmStemBrim () {
  cylinder(r=5.0, h=0.3);
}

