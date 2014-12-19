$fn = 64; // Increase to render more faces per curve.

profile_type = 2; // XXX: Keycap shape (DCS = 1, DSA = 2)
key_size = 1.0; // XXX: Length in units of key. Ergodox has (1, 1.5, 2)

// Connector brim
// Enabling this makes it easier to print and the brim should just snap off
// easily after printing.
brim = 0; // XXX: Enable brim for stem
brim_radius = 5;
brim_depth = .3;

// Homing bumps are usually on the two index finger keys (F and J on qwerty)
// Sometimes on DSA just a deeper dish is used so you may want to try that.
bump = 0; // XXX: Enable homing bump

stem_type = 2; // XXX: Stem shape (CherryMX = 1, Matias/ALPS = 2)

// DCS family
DCS_top_x_diff = 6;
DCS_top_y_diff = 4;
DCS_z = 8.5;
DCS_top_tilt = -1;
DCS_top_skew = 1.75;
DCS_dish_depth = 1;
DCS_dish_radius = 20;

// DSA family
DSA_top_x_diff = 5.3;
DSA_top_y_diff = 5.3;
DSA_z = 7.8;
DSA_dish_depth = 1.2;
DSA_dish_radius = 30;

straight_wall_side = 3.0;

// ALPS stems must be 5mm long which is slightly bigger than that required
// for CherryMX stems.
stem_z = stem_type == 2 ? 5.0 : 4.0;

top_x_diff = profile_type == 2 ? DSA_top_x_diff : DCS_top_x_diff;
top_y_diff = profile_type == 2 ? DSA_top_y_diff : DCS_top_y_diff;
keycap_z = profile_type == 2 ? DSA_z : DCS_z;
top_tilt = profile_type == 2 ? 0 : DCS_top_tilt;
top_skew = profile_type == 2 ? 0 : DCS_top_skew;
dish_depth = profile_type == 2 ? DSA_dish_depth : DCS_dish_depth;
dish_radius = profile_type == 2 ? DSA_dish_radius : DCS_dish_radius;


/** Homing bump
 */
bump_z = 0.9;
bump_r1 = 1.9;
bump_r2 = 0.7;
module homing_bump ()
{
    translate([0, 0, keycap_z - dish_depth])
      cylinder(h=bump_z, r1=bump_r1, r2=bump_r2, center=false);
}

/** Dish
 * DCS uses a cylindrical cutout from the top face.
 * DSA uses a spherical cutout from the top face.
 */
dish_bottom = keycap_z - dish_depth;
module dish (profile_type)
{
    translate([0, top_skew, keycap_z])
      rotate([90-top_tilt, 0, 0])
        translate([0, dish_radius - dish_depth, 0])
    if (profile_type == 2)
    {
          scale([key_size, 1, 1])
            sphere(r=DSA_dish_radius, $fn=256);
    }
    else
    {
          cylinder(h=base_width, r=DCS_dish_radius*key_size, $fn=256, center=true);
    }
}

/** Rounded rectangle
 */
module rounded_rect (size, radius)
{
    x = size[0];
    y = size[1];
    z = size[2];

    translate([-x/2, -y/2, 0])
      linear_extrude(height=z)
        hull()
        {
            translate([radius, radius, 0]) circle(r=radius);

            translate([x - radius, radius, 0]) circle(r=radius);

            translate([x - radius, y - radius, 0]) circle(r=radius);

            translate([radius, y - radius, 0]) circle(r=radius);
        }
}

// The keybase dimensions are fairly standard between most keycap manufacturers.
base_width = 18;
base_corner_radius = 1.8;
/** Key block
 * Both DCS and DSA are done in the same way, just using different variables.
 */
module key_shape (profile_type)
{
    difference()
    {
        hull()
        {
            rounded_rect([base_width*key_size,
                          base_width,
                          straight_wall_side], base_corner_radius);

            translate([0, top_skew, keycap_z])
              rotate([-top_tilt, 0, 0])
                rounded_rect([base_width*key_size - top_x_diff,
                              base_width - top_y_diff,
                              .001], base_corner_radius);
        }

        dish(profile_type);
    }
}

// Wall thickness in mm.
wall_thickness_x = 0.8;
wall_thickness_y = 0.8;
wall_thickness_z = 1.0;
wall_scale_x = 1 - 2*(wall_thickness_x / base_width);
wall_scale_y = 1 - 2*(wall_thickness_y / base_width);
wall_scale_z = 1 - 2*(wall_thickness_z / keycap_z);
module inner_key_shape (profile_type)
{
    translate([0, 0, -.001])
      scale([wall_scale_x, wall_scale_y, wall_scale_z])
        difference ()
        {
            key_shape(profile_type);

            translate([0, 0, base_width/2 + dish_bottom])
              cube([base_width, base_width, base_width], center=true);
        }
}

module key_shell (profile_type)
{
    difference()
    {
        key_shape(profile_type);

        inner_key_shape(profile_type);
    }
}

/** Large cube with inner_key_shape cutout.
 */
module subtractor_cube (profile_type)
{
    difference()
    {
        translate([0, 0, base_width/2])
          cube([base_width+.001, base_width+.001, base_width+.001], center=true);

        inner_key_shape(profile_type);
    }
}

// Inner cross of the stem.
cross_width_x = 1.3;
cross_width_y = 1.4;
cross_arm_length = 4.4;
cross_depth = 3.8; // Cross depth, stem height is 3.4mm.
// Outer stem should be as big and aturdy as possible but still fit in switch.
cherrymx_stem_x = 2.11;
cherrymx_stem_y = 1.1;

/** CherryMX stem
 */
module stem_cherrymx (profile_type)
{
    difference(){
        difference()
        {
            union()
            {
                // Massively over-deep stem which is cut down later.
                translate([-(cross_arm_length + cherrymx_stem_x)/2,
                           -(cross_arm_length + cherrymx_stem_y)/2,
                           0])
                  cube([cross_arm_length + cherrymx_stem_x,
                        cross_arm_length + cherrymx_stem_y,
                        base_width]);

                // Support structure to reduce stress on joining corners.
                translate([0, 0, stem_z])
                  cylinder(h=keycap_z, r1=(cross_arm_length + cherrymx_stem_y)/2, r2=base_width/2, center=false);

                if (brim == 1) cylinder(r=brim_radius, h=brim_depth);
            }

            // Inner cross
            translate([0, 0, cross_depth/2])
              union()
              {
                  cube([cross_width_x, cross_arm_length, cross_depth + .001], center=true);
                  cube([cross_arm_length, cross_width_y, cross_depth + .001], center=true);
              }
        }

        // Large cube with inner_key_shape cutout to subtract over-deep stem.
        subtractor_cube(profile_type);
    }
}

/** ALPS/Matias stem
 */
alps_stem_x = 4;
alps_stem_y = 2;
module stem_alps (profile_type)
{
    difference(){
        union()
        {
            // Massively over-deep stem which is cut down later.
            translate([-(alps_stem_x)/2,
                       -(alps_stem_y)/2,
                       0])
              cube([alps_stem_x,
                    alps_stem_y,
                    base_width]);

            // Support structure to reduce stress on joining corners.
            // Only seen when keycap_z is very high.
            translate([0, 0, stem_z])
              cylinder(h=(base_width - alps_stem_y)/2, r1=alps_stem_y/2, r2=base_width/2, center=false);

            if (brim == 1) cylinder(r=brim_radius, h=brim_depth);
        }

        // Large cube with inner_key_shape cutout to subtract over-deep stem.
        subtractor_cube(profile_type);
    }
}

/** Full keycap
 */
module keycap (profile_type)
{
    union()
    {
        key_shell(profile_type);

        if (bump == 1) homing_bump();

        if (stem_type == 1) stem_cherrymx(profile_type);
        else if (stem_type == 2) stem_alps(profile_type);
    }
}

keycap(profile_type);

