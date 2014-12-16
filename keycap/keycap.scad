$fn = 64; // Increase to render more faces per curve.

key_type = 2; // XXX: Keycap shape (DCS = 1, DSA = 2)
key_size = 1; // XXX: Length in units of key. Ergodox has (1, 1.5, 2)

// Connector brim
// Enabling this makes it easier to print and the brim should just snap off
// easily after printing.
has_brim = 1; // XXX: Enable brim for stem
brim_radius = 6;
brim_depth = .3;

// Homing bumps are usually on the two index finger keys (F and J on qwerty)
// Sometimes on DSA just a deeper dish is used so you may want to try that.
has_bump = 0; // XXX: Enable homing bump

stem_type = 2; // XXX: Stem shape (CherryMX = 1, Matias/ALPS = 2)

// DCS family
DCS_top_x_diff = 6;
DCS_top_y_diff = 4;
DCS_z = 8.5;
DCS_top_tilt = -1;
DCS_top_skew = 1.75;
DCS_dish_depth = 1;

// DSA family
DSA_top_x_diff = 5.3;
DSA_top_y_diff = 5.3;
DSA_z = 7.4;
DSA_top_skew = 0;
DSA_dish_depth = 1.6;


/** Homing bump
 */
bump_z = 0.9;
bump_r1 = 1.9;
bump_r2 = 0.7;
module homingBump ()
{
    if (key_type == 2)
    {
        translate([0, 0, DSA_z-DSA_dish_depth])
          cylinder(h=bump_z, r1=bump_r1, r2=bump_r2, center=false);
    }
    else
    {
        translate([0, 0, DCS_z-DCS_dish_depth])
          cylinder(h=bump_z, r1=bump_r1, r2=bump_r2, center=false);
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


DCS_dish_radius = 20;
DSA_dish_radius = 30;
/** Dish
 * DCS uses a cylindrical cutout from the top face.
 * DSA uses a spherical cutout from the top face.
 */
module dish (key_type)
{
    if (key_type == 2)
    {
        translate([0, DSA_top_skew, DSA_z])
          rotate([90, 0, 0])
            translate([0, DSA_dish_radius - DSA_dish_depth, 0])
              scale([key_size, 1, 1])
                sphere(r=DSA_dish_radius, $fn=256);
    }
    else
    {
        translate([0, DCS_top_skew, DCS_z])
          rotate([90-DCS_top_tilt, 0, 0])
            translate([0, DCS_dish_radius*key_size - DCS_dish_depth, 0])
              cylinder(h=100, r=DCS_dish_radius*key_size, $fn=256, center=true);
    }
}


// The keybase dimensions are fairly standard between most keycap manufacturers.
base_width = 18;
base_corner_radius = 1.8;
/** Key block
 * Both DCS and DSA are done in the same way, just using different variables.
 */
module key_shape (key_type)
{
    difference()
    {
        if (key_type == 2)
        {
            hull()
            {
                rounded_rect([base_width*key_size, base_width, 2], base_corner_radius);

                translate([0, DSA_top_skew, DSA_z])
                  rounded_rect([base_width*key_size - DSA_top_x_diff,
                               base_width - DSA_top_y_diff,
                               .001], base_corner_radius);
            }
        }
        else
        {
            hull()
            {
                rounded_rect([base_width*key_size, base_width, 2], base_corner_radius);

                translate([0, DCS_top_skew, DCS_z])
                  rotate([-DCS_top_tilt, 0, 0])
                    rounded_rect([base_width*key_size - DCS_top_x_diff,
                                 base_width - DCS_top_y_diff,
                                 .001], base_corner_radius);
            }
        }

        dish(key_type);
    }
}


// Scale of inner to outer key shape
wall_thickness_x = 0.9;
wall_thickness_y = 0.9;
wall_thickness_z = 0.65;

// Inner cross of the stem.
cross_width_x = 1.3;
cross_width_y = 1.4;
cross_arm_length = 4.4;
cross_depth = 3.8; // cross depth, stem height is 3.4mm
// Outer stem should be as big and aturdy as possible but still fit in switch.
cherrymx_stem_x = 2.11;
cherrymx_stem_y = 1.1;

/** CherryMX stem
 */
module stem_cherrymx (key_type)
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
                        50]);

                if (has_brim == 1) cylinder(r=brim_radius, h=brim_depth);
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
        difference()
        {
            translate([0, 0, 50])
              cube([100, 100, 100], center=true);

            translate([0, 0, -0.1])
              scale([wall_thickness_x, wall_thickness_y, wall_thickness_z])
                key_shape(key_type);
        }
    }
}

/** ALPS/Matias stem
 */
alps_stem_x = 4;
alps_stem_y = 2;
module stem_alps (key_type)
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
                    50]);

            if (has_brim == 1) cylinder(r=brim_radius, h=brim_depth);
        }

        // Large cube with inner_key_shape cutout to subtract over-deep stem.
        difference()
        {
            translate([0, 0, 50])
              cube([100, 100, 100], center=true);

            translate([0, 0, -0.1])
              scale([wall_thickness_x, wall_thickness_y, wall_thickness_z])
                key_shape(key_type);
        }
    }
}

/** Full keycap
 */
module keycap (key_type)
{
    union()
    {
        difference()
        {
            key_shape(key_type);

            translate([0, 0, -0.1])
              scale([wall_thickness_x, wall_thickness_y, wall_thickness_z])
                key_shape(key_type);
        }

        if (has_bump == 1) homingBump();

        if (stem_type == 1) stem_cherrymx(key_type);
        else if (stem_type == 2) stem_alps(key_type);
    }
}


keycap(key_type);
