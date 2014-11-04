#!/usr/bin/env python

from math import *
import sys
from ndim import *

# Spacing between centers of cherrymx switches.
spc = 19.0

# Ergonomic angle of rotation for thumb cluster.
thumb_rotate = radians(-25)

# Ergonomic angle of rotation for whole hand.
hand_rotate = radians(-13)

# Separation of hand circles.
hand_sep = 20.0

# Number of fixing holes per hand.
n_fix = 6


# Ergonomic column offsets for finger cluster.
c0_Y = 0.0 # 1.5x outer.
c1_Y = 0.0 # Pinky finger.
c2_Y = 3.0 # Ring finger.
c3_Y = 4.5 # Middle finger.
c4_Y = 3.0 # Index finger.
c5_Y = 1.5 # Other index finger.
c6_Y = 1.5 # 1.5x inner.

# Non-ergonomic positions from origin
c0_X = 0.0              # 1.5x outer.
c1_X = c0_X + 1.25*spc  # Pinky finger.
c2_X = c1_X + spc       # Ring finger.
c3_X = c2_X + spc       # Middle finger.
c4_X = c3_X + spc       # Index finger.
c5_X = c4_X + spc       # Other index finger.
c6_X = c5_X + spc       # 1.5x inner.

c0 = [
      (c0_X,             4*spc+c0_Y, 0),
      (c0_X,             3*spc+c0_Y, 0),
      (c0_X,             2*spc+c0_Y, 0),
      (c0_X,             1*spc+c0_Y, 0),
      (c0_X + 0.25*spc,  0*spc+c0_Y, 0),
     ]
top_left = c0[0]

c1 = [
      (c1_X,  4*spc+c1_Y, 0),
      (c1_X,  3*spc+c1_Y, 0),
      (c1_X,  2*spc+c1_Y, 0),
      (c1_X,  1*spc+c1_Y, 0),
      (c1_X,  0*spc+c1_Y, 0),
     ]

c2 = [
      (c2_X,  4*spc+c2_Y, 0),
      (c2_X,  3*spc+c2_Y, 0),
      (c2_X,  2*spc+c2_Y, 0),
      (c2_X,  1*spc+c2_Y, 0),
      (c2_X,  0*spc+c2_Y, 0),
     ]

c3 = [
      (c3_X,  4*spc+c3_Y, 0),
      (c3_X,  3*spc+c3_Y, 0),
      (c3_X,  2*spc+c3_Y, 0),
      (c3_X,  1*spc+c3_Y, 0),
      (c3_X,  0*spc+c3_Y, 0),
     ]

c4 = [
      (c4_X,  4*spc+c4_Y, 0),
      (c4_X,  3*spc+c4_Y, 0),
      (c4_X,  2*spc+c4_Y, 0),
      (c4_X,  1*spc+c4_Y, 0),
      (c4_X,  0*spc+c4_Y, 0),
     ]

c5 = [
      (c5_X,  4*spc+c5_Y, 0),
      (c5_X,  3*spc+c5_Y, 0),
      (c5_X,  2*spc+c5_Y, 0),
      (c5_X,  1*spc+c5_Y, 0),
     ]

c6 = [
      (c6_X,  4*spc+c6_Y,    0),
      (c6_X,  2.75*spc+c6_Y, 1),
      (c6_X,  1.25*spc+c6_Y, 1),
     ]

finger_sw_holes = c6 + c5 + c4 + c3 + c2 + c1 + c0
finger_sw_holes = [(p[0], p[1], p[2]*pi/2) for p in finger_sw_holes]


# Lower left of thumb cluster is taken as the origin.
thumb_pos = [c5_X +0.5*spc + 1.5, -0.5*spc - 3]

# Centers of switch holes in thumb cluster.
thumb_sw_holes = [
                  (0*spc, 0*spc),
                  (1*spc, 0*spc),
                  (2*spc, -0.5*spc),
                  (2*spc, +0.5*spc),
                  (2*spc, +1.5*spc),
                  (1*spc, +1.5*spc),
                 ]
thumb_sw_holes = pts_rotate(thumb_sw_holes, [thumb_rotate])
thumb_sw_holes = pts_shift(thumb_sw_holes, thumb_pos)
thumb_sw_holes = [list(p) + [thumb_rotate] for p in thumb_sw_holes]
thumb_sw_holes[0][2] += pi/2
thumb_sw_holes[1][2] += pi/2
thumb_sw_holes = [tuple(p) for p in thumb_sw_holes]
bottom_right = thumb_sw_holes[2]


Lsw_holes = thumb_sw_holes + finger_sw_holes
c = pt_between_pts(top_left[:2], bottom_right[:2])
radius = distance_between_pts(top_left[:2], c) + 1.0*spc
diameter = 2 * radius
center = (diameter + hand_sep/2, radius)
Lcenter = (radius, radius)
Rcenter = pt_reflect(Lcenter, [center[0], None])


# Center and rotate.
Lsw_rotates = [h[2] + hand_rotate for h in Lsw_holes]
Lsw_points = [(h[0], h[1]) for h in Lsw_holes]
Lsw_points = pts_shift(Lsw_points, [-c[0] + radius, -c[1] + radius - 3.0])
Lsw_points = pts_rotate(Lsw_points, angle=[hand_rotate], center=(radius, radius))
Lsw_holes = [(Lsw_points[i][0], Lsw_points[i][1], Lsw_rotates[i]) for i in range(len(Lsw_holes))]

Rsw_points = pts_reflect(Lsw_points, [center[0], None])
Rsw_rotates = [-h[2] for h in Lsw_holes]
Rsw_holes = [(Rsw_points[i][0], Rsw_points[i][1], Rsw_rotates[i]) for i in range(len(Lsw_holes))]
sw_holes = Lsw_holes + Rsw_holes
# sw_holes is now a list of tuples containing the coordinates and rotations of all switches on LHS.


# The base is composed of 2 circles with a thinner section in the middle, made
#   from the arcs of other circles.
# Centers of circles are:
# A - left hand
# B - bottom arc
# C - right hand
# D - top arc
# Start stop points of the arcs are:
# E - Between A and D
# F - Between A and B
# G - Between C and D
# H - Between C and B
# The size of the arcs is controlled by 3 parameters:
# hand_sep - separation between hand plates
# r_top - radius of top arc
# r_bot - radius of bottom arc
r_hand = radius

# Arcs spanning the gap between hand circles.
r_top = sqrt(2)*r_hand
r_bot = r_hand/sqrt(2)

sep = hand_sep + 2*r_hand
baseA = (r_hand, r_hand)
baseB = (baseA[0] + sep/2, baseA[1] - sqrt((r_hand + r_bot)**2 - (sep/2)**2))
baseC = (baseA[0] + sep, baseA[1])
baseD = (baseB[0], baseA[1] + sqrt((r_hand + r_top)**2 - (sep/2)**2))
baseE = pt_between_pts(baseA, baseD, r_hand/(r_hand+r_top))
baseF = pt_between_pts(baseA, baseB, r_hand/(r_hand+r_bot))
baseG = pt_between_pts(baseC, baseD, r_hand/(r_hand+r_top))
baseH = pt_between_pts(baseC, baseB, r_hand/(r_hand+r_bot))

# PCB mount
top_edge = baseD[1] - r_top - 2.0 # Lowest point of top arc, minus recess.
spacer = 7.0 # Diameter of 2mm thick spacer between pcb and mount plate.
pcb_width = 50.0
fix_hole_diameter = 3.2
pcb_hole_offset = (spacer/2) + fix_hole_diameter
pcb_holes_top = top_edge - pcb_hole_offset
pcb_holes_left = center[0] - (pcb_width/2) + pcb_hole_offset
pcb_holes_right = center[0] + (pcb_width/2) - pcb_hole_offset
pcb_holes_bot = top_edge - pcb_width + pcb_hole_offset
pcb_holes = [
    (pcb_holes_left, pcb_holes_bot),
    (pcb_holes_right, pcb_holes_bot),
    (pcb_holes_left, pcb_holes_top),
    (pcb_holes_right, pcb_holes_top),
]

# Fixing holes
Lfix_holes = gen_polygon_pts(n_fix, [radius-0.5*spc])
Lfix_holes = pts_rotate(Lfix_holes, [hand_rotate])
Lfix_holes = pts_shift(Lfix_holes, [radius, radius])
Rfix_holes = pts_reflect(Lfix_holes, [center[0], None])
fix_holes = Lfix_holes + Rfix_holes

# Top layers cutouts.
fingersL_outline = [
  pt_relative(sw_holes[33][:2], [-0.75*spc, +0.5*spc], [sw_holes[33][2]]),
  pt_relative(sw_holes[36][:2], [-0.75*spc, -0.5*spc], [sw_holes[36][2]]),
  pt_relative(sw_holes[37][:2], [-0.5*spc,  +0.5*spc], [sw_holes[37][2]]),
  pt_relative(sw_holes[37][:2], [-0.5*spc,  -0.5*spc], [sw_holes[37][2]]),
  pt_relative(sw_holes[32][:2], [+0.5*spc,  -0.5*spc], [sw_holes[32][2]]),
  pt_relative(sw_holes[27][:2], [-0.5*spc,  -0.5*spc], [sw_holes[27][2]]),
  pt_relative(sw_holes[27][:2], [+0.5*spc,  -0.5*spc], [sw_holes[27][2]]),
  pt_relative(sw_holes[22][:2], [-0.5*spc,  -0.5*spc], [sw_holes[22][2]]),
  pt_relative(sw_holes[22][:2], [+0.5*spc,  -0.5*spc], [sw_holes[22][2]]),
  pt_relative(sw_holes[17][:2], [-0.5*spc,  -0.5*spc], [sw_holes[17][2]]),
  pt_relative(sw_holes[17][:2], [+0.5*spc,  -0.5*spc], [sw_holes[17][2]]),
  pt_relative(sw_holes[12][:2], [-0.5*spc,  -0.5*spc], [sw_holes[12][2]]),
  pt_relative(sw_holes[12][:2], [+0.5*spc,  -0.5*spc], [sw_holes[12][2]]),
  pt_relative(sw_holes[8][:2],  [-0.75*spc, -0.5*spc], [sw_holes[8][2]]),
  pt_relative(sw_holes[8][:2],  [+0.75*spc, -0.5*spc], [sw_holes[8][2]]),
  pt_relative(sw_holes[6][:2],  [+0.5*spc,  +0.5*spc], [sw_holes[6][2]]),
  pt_relative(sw_holes[9][:2],  [-0.5*spc,  +0.5*spc], [sw_holes[9][2]]),
  pt_relative(sw_holes[13][:2], [+0.5*spc,  +0.5*spc], [sw_holes[13][2]]),
  pt_relative(sw_holes[13][:2], [-0.5*spc,  +0.5*spc], [sw_holes[13][2]]),
  pt_relative(sw_holes[18][:2], [+0.5*spc,  +0.5*spc], [sw_holes[18][2]]),
  pt_relative(sw_holes[18][:2], [-0.5*spc,  +0.5*spc], [sw_holes[18][2]]),
  pt_relative(sw_holes[23][:2], [+0.5*spc,  +0.5*spc], [sw_holes[23][2]]),
  pt_relative(sw_holes[23][:2], [-0.5*spc,  +0.5*spc], [sw_holes[23][2]]),
  pt_relative(sw_holes[28][:2], [+0.5*spc,  +0.5*spc], [sw_holes[28][2]]),
]
fingersL_outline.append(fingersL_outline[0])
fingersR_outline = pts_reflect(fingersL_outline, [center[0], None])

thumbsL_outline = [
  pt_relative(sw_holes[0][:2], [-1.0*spc, +0.5*spc], [sw_holes[0][2]]),
  pt_relative(sw_holes[2][:2], [+0.5*spc, -0.5*spc], [sw_holes[2][2]]),
  pt_relative(sw_holes[4][:2], [+0.5*spc, +0.5*spc], [sw_holes[4][2]]),
  pt_relative(sw_holes[5][:2], [-0.5*spc, +0.5*spc], [sw_holes[5][2]]),
  pt_relative(sw_holes[1][:2], [+1.0*spc, +0.5*spc], [sw_holes[1][2]]),
  pt_relative(sw_holes[0][:2], [+1.0*spc, +0.5*spc], [sw_holes[0][2]]),
]
thumbsL_outline.append(thumbsL_outline[0])
thumbsR_outline = pts_reflect(thumbsL_outline, [center[0], None])

# Cutouts under the PCB and fro wiring.
base0_cutout_width = 18.0 # Just enough to expose the teensy.
base0_cutout_height = 30.0
base0_cutout_left = center[0] - (base0_cutout_width/2)
base0_cutout_right = center[0] + (base0_cutout_width/2)
base0_cutout_bot = top_edge - base0_cutout_height
base0_cutout_top = -(r_top**2 - (base0_cutout_left - baseD[0])**2)**0.5 + baseD[1]
base0I = (base0_cutout_left,  base0_cutout_top)
base0J = (base0_cutout_right,  base0_cutout_top)
base0_cutout = [
    base0I,
    (base0_cutout_left,  base0_cutout_bot),
    (base0_cutout_right, base0_cutout_bot),
    base0J,
]

base2_cutout_width = 52.0 # Expose the PCB.
base2_cutout_height = 52.0
base2_cutout_left = center[0] - (base2_cutout_width/2)
base2_cutout_right = center[0] + (base2_cutout_width/2)
base2_cutout_bot = top_edge - base2_cutout_height
base2_cutout_top = top_edge
base2I = (base2_cutout_left,  base2_cutout_top)
base2J = (base2_cutout_right,  base2_cutout_top)
base2L_outline = [
  pt_relative(sw_holes[4][:2], [+0.5*spc, +0.5*spc], [sw_holes[4][2]]),
  pt_relative(sw_holes[2][:2], [+0.5*spc, -0.5*spc], [sw_holes[2][2]]),
  pt_relative(sw_holes[0][:2], [-1.0*spc, +0.5*spc], [sw_holes[0][2]]),
  #
  pt_relative(sw_holes[17][:2], [+0.5*spc,  -0.5*spc], [sw_holes[17][2]]),
  pt_relative(sw_holes[17][:2], [-0.5*spc,  -0.5*spc], [sw_holes[17][2]]),
  pt_relative(sw_holes[22][:2], [+0.5*spc,  -0.5*spc], [sw_holes[22][2]]),
  pt_relative(sw_holes[22][:2], [-0.5*spc,  -0.5*spc], [sw_holes[22][2]]),
  pt_relative(sw_holes[27][:2], [+0.5*spc,  -0.5*spc], [sw_holes[27][2]]),
  pt_relative(sw_holes[27][:2], [-0.5*spc,  -0.5*spc], [sw_holes[27][2]]),
  pt_relative(sw_holes[32][:2], [+0.5*spc,  -0.5*spc], [sw_holes[32][2]]),
  pt_relative(sw_holes[37][:2], [-0.5*spc,  -0.5*spc], [sw_holes[37][2]]),
  pt_relative(sw_holes[37][:2], [-0.5*spc,  +0.5*spc], [sw_holes[37][2]]),
  pt_relative(sw_holes[36][:2], [-0.75*spc, -0.5*spc], [sw_holes[36][2]]),
  pt_relative(sw_holes[33][:2], [-0.75*spc, +0.5*spc], [sw_holes[33][2]]),
  #
  pt_relative(sw_holes[28][:2], [+0.5*spc,  +0.5*spc], [sw_holes[28][2]]),
  pt_relative(sw_holes[23][:2], [-0.5*spc,  +0.5*spc], [sw_holes[23][2]]),
  pt_relative(sw_holes[23][:2], [+0.5*spc,  +0.5*spc], [sw_holes[23][2]]),
  pt_relative(sw_holes[18][:2], [-0.5*spc,  +0.5*spc], [sw_holes[18][2]]),
  pt_relative(sw_holes[18][:2], [+0.5*spc,  +0.5*spc], [sw_holes[18][2]]),
  pt_relative(sw_holes[13][:2], [-0.5*spc,  +0.5*spc], [sw_holes[13][2]]),
  pt_relative(sw_holes[13][:2], [+0.5*spc,  +0.5*spc], [sw_holes[13][2]]),
  pt_relative(sw_holes[9][:2],  [-0.5*spc,  +0.5*spc], [sw_holes[9][2]]),
  pt_relative(sw_holes[6][:2],  [+0.5*spc,  +0.5*spc], [sw_holes[6][2]]),
]
base2R_outline = pts_reflect(base2L_outline, [center[0], None])
base2R_outline.reverse()
base2_cutout = base2L_outline + [
    (base2_cutout_left,  base2_cutout_bot),
    base2I,
    base2J,
    (base2_cutout_right, base2_cutout_bot),
] + base2R_outline
base2_cutout.append(pt_shift(tuple(base2_cutout[-1]), [0.0, 25.0]))
base2_cutout.append(pt_shift(tuple(base2_cutout[0]), [0.0, 25.0]))
base2_cutout.append(base2_cutout[0])

base1R_outline = [
    base0J,
    (base0_cutout_right, top_edge),
    base2J,
    (base2_cutout_right, base2_cutout_bot),
] + base2R_outline
base1R_outline.append(pt_shift(tuple(base1R_outline[-1]), [0.0, 25.0]))
base1L_outline = pts_reflect(base1R_outline, [center[0], None])
base1L_outline.reverse()
base1_cutout = base1R_outline + base1L_outline

def sw_outline_pts(sw_type='', args={}): # {{{
    '''Define a switch hole.
    '''
    sw_type = sw_type.lower()

    if sw_type in ['alps', 'matias']:
        width = 15.4 if 'width' not in args else args['width']
        height = 12.8 if 'height' not in args else args['height']
        ret = [
            (-width/2, -height/2),
            (+width/2, -height/2),
            (+width/2, +height/2),
            (-width/2, +height/2),
        ]
    elif sw_type in ['cherrymx']:
        width = 13.5 if 'width' not in args else args['width']
        notch_depth = 1.5 if 'notch_depth' not in args else args['notch_depth']
        notch_height = 4.0 if 'notch_height' not in args else args['notch_height']
    
        inner_x = width/2
        outer_x = inner_x + notch_depth
        outer_y = inner_x
        inner_y =  width/2 - notch_height
    
        # Points relative to centre listed in CW direction.
        ret = [
            (-inner_x, +inner_y),
            (-outer_x, +inner_y),
            (-outer_x, +outer_y),
            (+outer_x, +outer_y),
            (+outer_x, +inner_y),
            (+inner_x, +inner_y),
            (+inner_x, -inner_y),
            (+outer_x, -inner_y),
            (+outer_x, -outer_y),
            (-outer_x, -outer_y),
            (-outer_x, -inner_y),
            (-inner_x, -inner_y),
        ]
    else:
        ret = [
            (-spc/2, -spc/2),
            (+spc/2, -spc/2),
            (+spc/2, +spc/2),
            (-spc/2, +spc/2),
        ]

    ret.append(ret[0]) # Join back to start point.

    return ret
# }}} End of sw_outline_pts()

if __name__ == '__main__':
    out = []
    out += ['Switch holes:']
    for h in sw_holes:
        out += ['\t(%0.2f, %0.2f) rotate=%d' % (h[0], h[1], degrees(h[2]))]
    out += ['Fixing holes:']
    for h in fix_holes:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['PCB holes:']
    for h in pcb_holes:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['Outer:']
    out += ['\theight=%0.2f' % diameter]
    out += ['\twidth=%0.2f' % (diameter*2 + hand_sep)]
    print('\n'.join(out))
