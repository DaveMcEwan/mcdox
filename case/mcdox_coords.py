#!/usr/bin/env python

from math import *
import sys
from ndim import *

# Spacing between centers of switches.
spc = 19.0

# Ergonomic angle of rotation for thumb cluster.
thumb_rotate = radians(-25)

# Ergonomic angle of rotation for whole hand.
hand_rotate = radians(-13)

# Separation of hand circles.
hand_sep = 29.0

# Number of fixing holes per hand.
n_fix = 6

# Outline border width.
border = 5.0


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
thumb_pos = [c5_X +0.5*spc + 1.5, -0.5*spc - 1]

# Centers of switch holes in thumb cluster.
thumb_sw_holes = [
                  (0*spc, 0*spc),
                  (1*spc, 0*spc),
                  (2*spc, -0.5*spc),
                  (2*spc, +0.5*spc),
                  (2*spc, +1.5*spc),
                  (1*spc, +1.25*spc),
                 ]
thumb_sw_holes = pts_rotate(thumb_sw_holes, [thumb_rotate])
thumb_sw_holes = pts_shift(thumb_sw_holes, thumb_pos)
thumb_sw_holes = [list(p) + [thumb_rotate] for p in thumb_sw_holes]
thumb_sw_holes[0][2] += pi/2
thumb_sw_holes[1][2] += pi/2
thumb_sw_holes = [tuple(p) for p in thumb_sw_holes]
bottom_right = thumb_sw_holes[2]


Lsw_holes = thumb_sw_holes + finger_sw_holes
Lsw_rotates = [h[2] + hand_rotate for h in Lsw_holes]
pcb_sw = Lsw_holes
c = pt_between_pts(top_left[:2], bottom_right[:2])
d = distance_between_pts(top_left[:2], bottom_right[:2])
wrest_r = 93.0
radius = wrest_r
diameter = 2 * radius
center = (diameter + hand_sep/2, radius)


# Center and rotate.
Lsw_points = [(h[0], h[1]) for h in Lsw_holes]
Lsw_points = pts_shift(Lsw_points, [-c[0] + radius, radius])
Lsw_points = pts_rotate(Lsw_points, angle=[hand_rotate], center=(radius, radius))
Lsw_holes = [(Lsw_points[i][0], Lsw_points[i][1], Lsw_rotates[i]) for i in range(len(Lsw_holes))]

Rsw_points = pts_reflect(Lsw_points, [center[0], None])
Rsw_rotates = [-h[2] for h in Lsw_holes]
Rsw_holes = [(Rsw_points[i][0], Rsw_points[i][1], Rsw_rotates[i]) for i in range(len(Lsw_holes))]
sw_holes = Lsw_holes + Rsw_holes
# sw_holes is now a list of tuples containing the coordinates and rotations of all switches on LHS.


# {{{ Outline paths
toparc_center_ptL = pt_relative(sw_holes[33][:2], [-0.75*spc, +0.5*spc], [sw_holes[33][2]])
toparc_center_ptR = pt_reflect(toparc_center_ptL, [center[0], None])
toparc_pathL = {
    'type':         'arc',
    'center':       toparc_center_ptL,
    'radius':       border,
    'startangle':   90,
    'endangle':     180 + degrees(hand_rotate)
}
toparc_pathR = {
    'type':         'arc',
    'center':       toparc_center_ptR,
    'radius':       border,
    'startangle':   -degrees(hand_rotate),
    'endangle':     90
}
top_edge = toparc_center_ptL[1] + border
topedge_upper_ptL = (toparc_center_ptL[0], top_edge)
topedge_upper_ptR = (toparc_center_ptR[0], top_edge)
topedge_lower_ptL = pt_relative(toparc_center_ptL, [+border, 0.0], [radians(180) + hand_rotate])
topedge_lower_ptR = pt_relative(toparc_center_ptR, [+border, 0.0], [-hand_rotate])

leftmost_pt = pt_relative(sw_holes[36][:2], [-0.75*spc-border, -0.5*spc-border], [sw_holes[36][2]])
rightmost_pt = pt_reflect(leftmost_pt, [center[0], None])
leftmost_a = hand_rotate
leftmost_m = tan(leftmost_a)
leftmost_c = leftmost_pt[1] - leftmost_m*leftmost_pt[0] # c = y - mx

thumbarc_pt = pt_relative(sw_holes[2][:2], [+0.5*spc+border, 0.0], [sw_holes[2][2]])

wrest_center_x = leftmost_pt[0] + cos(hand_rotate)*wrest_r
wrest_center_y = leftmost_pt[1] + sin(hand_rotate)*wrest_r
wrest_center_ptL = (wrest_center_x, wrest_center_y)
wrest_center_ptR = pt_reflect(wrest_center_ptL, [center[0], None])
wrest_angle_eR = -hand_rotate
wrest_angle_sL = radians(180) + hand_rotate
wrest_angle_eL = dir_between_pts(wrest_center_ptL, thumbarc_pt)[0]
wrest_angle_sR = radians(180) - wrest_angle_eL
wrest_pathL = {
    'type':         'arc',
    'center':       wrest_center_ptL,
    'radius':       wrest_r,
    'startangle':   degrees(wrest_angle_sL),
    'endangle':     degrees(wrest_angle_eL),
}
wrest_pathR = {
    'type':         'arc',
    'center':       wrest_center_ptR,
    'radius':       wrest_r,
    'startangle':   degrees(wrest_angle_sR),
    'endangle':     degrees(wrest_angle_eR),
}

botarc_m = tan(wrest_angle_eL)
botarc_c = wrest_center_ptL[1] - botarc_m*wrest_center_ptL[0] # c = y - mx
botarc_center_x = center[0]
botarc_center_y = botarc_m*botarc_center_x + botarc_c
botarc_center_pt = (botarc_center_x, botarc_center_y)
botarc_r = distance_between_pts(wrest_center_ptL, botarc_center_pt) - wrest_r
botarc_path = {
    'type':         'arc',
    'center':       botarc_center_pt,
    'radius':       botarc_r,
    'startangle':   degrees(wrest_angle_sR) - 180,
    'endangle':     degrees(wrest_angle_eL) - 180,
}
# }}}

# {{{ Hand PCB mount in base layers
handbrdL_cutout = [
  pt_relative(sw_holes[4][:2], [+(0.5*spc+0.5), +(0.5*spc+0.5)], [sw_holes[4][2]]),
  pt_relative(sw_holes[2][:2], [+(0.5*spc+0.5), -(0.5*spc+0.5)], [sw_holes[2][2]]),
  pt_relative(sw_holes[0][:2], [-(1.0*spc+0.5), +(0.5*spc+0.5)], [sw_holes[0][2]]),
  #
  #pt_relative(sw_holes[17][:2], [+(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[17][2]]),
  #pt_relative(sw_holes[17][:2], [-(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[17][2]]),
  #pt_relative(sw_holes[22][:2], [+(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[22][2]]),
  #pt_relative(sw_holes[22][:2], [-(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[22][2]]),
  #pt_relative(sw_holes[27][:2], [+(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[27][2]]),
  #pt_relative(sw_holes[27][:2], [-(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[27][2]]),
  #pt_relative(sw_holes[32][:2], [+(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[32][2]]),
  pt_relative(sw_holes[37][:2], [-(0.5*spc+0.5),  -(0.5*spc+0.5)], [sw_holes[37][2]]),
  #pt_relative(sw_holes[37][:2], [-(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[37][2]]),
  pt_relative(sw_holes[36][:2], [-(0.5*spc+0.5), -(0.5*spc+0.5)], [sw_holes[36][2]]),
  pt_relative(sw_holes[33][:2], [-(0.5*spc+0.5), +(0.5*spc+0.5)], [sw_holes[33][2]]),
  #
  pt_relative(sw_holes[28][:2], [+(0.5*spc-0.5),  +(0.5*spc+0.5)], [sw_holes[28][2]]),
  pt_relative(sw_holes[23][:2], [-(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[23][2]]),
  pt_relative(sw_holes[23][:2], [+(0.5*spc-0.5),  +(0.5*spc+0.5)], [sw_holes[23][2]]),
  pt_relative(sw_holes[18][:2], [-(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[18][2]]),
  pt_relative(sw_holes[18][:2], [+(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[18][2]]),
  pt_relative(sw_holes[13][:2], [-(0.5*spc-0.5),  +(0.5*spc+0.5)], [sw_holes[13][2]]),
  pt_relative(sw_holes[13][:2], [+(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[13][2]]),
  pt_relative(sw_holes[9][:2],  [-(0.5*spc-0.5),  +(0.5*spc+0.5)], [sw_holes[9][2]]),
  pt_relative(sw_holes[6][:2],  [+(0.5*spc+0.5),  +(0.5*spc+0.5)], [sw_holes[6][2]]),
]
handbrdR_cutout = pts_reflect(handbrdL_cutout, [center[0], None])
handbrdR_cutout.reverse()
# }}}

# {{{ Controller PCB (lollybrd) mount
lollybrd_width = 50.0
lollybrd_height = 50.0
lollybrd_spacer = 7.0 # Diameter of 2mm spacer between pcb and mount plate.
lollybrd_hole_offset = (lollybrd_spacer/2)

lollybrd_cutout_spc = 1.0 # Space between lollybrd and inner base layers.
lollybrd_cutout_width = lollybrd_width + lollybrd_cutout_spc*2
lollybrd_cutout_height = lollybrd_height + lollybrd_cutout_spc*2
lollybrd_cutout_left = center[0] - (lollybrd_cutout_width/2)
lollybrd_cutout_right = center[0] + (lollybrd_cutout_width/2)
#lollybrd_cutout_bot = top_edge - lollybrd_cutout_height
lollybrd_cutout_bot = handbrdL_cutout[-1][1] # Doesn't go all the way to the bottom.
lollybrd_cutout_top = top_edge - border

lollybrd_holes_top = lollybrd_cutout_top - lollybrd_cutout_spc - lollybrd_hole_offset
lollybrd_holes_left = center[0] - (lollybrd_width/2) + lollybrd_hole_offset
lollybrd_holes_right = center[0] + (lollybrd_width/2) - lollybrd_hole_offset
lollybrd_holes_bot = lollybrd_cutout_top - lollybrd_height - lollybrd_cutout_spc + lollybrd_hole_offset
lollybrd_holes = [
    (lollybrd_holes_left, lollybrd_holes_bot),
    (lollybrd_holes_right, lollybrd_holes_bot),
    (lollybrd_holes_left, lollybrd_holes_top),
    (lollybrd_holes_right, lollybrd_holes_top),
]

teensy_cutout_width = 24.0 # Just enough to expose the teensy.
teensy_cutout_height = 50.0
teensy_cutout_left = center[0] - (teensy_cutout_width/2)
teensy_cutout_right = center[0] + (teensy_cutout_width/2)
teensy_cutout_bot = top_edge - teensy_cutout_height - border
teensy_cutout_top = top_edge
teensy_cutout = [
    (teensy_cutout_left,  teensy_cutout_top),
    (teensy_cutout_left,  teensy_cutout_bot),
    (teensy_cutout_right, teensy_cutout_bot),
    (teensy_cutout_right,  teensy_cutout_top),
]

ctrlmnt_top = lollybrd_cutout_top - lollybrd_cutout_spc
ctrlmnt_left = center[0] - (lollybrd_width/2)
ctrlmnt_right = center[0] + (lollybrd_width/2)
ctrlmnt_bot = ctrlmnt_top - lollybrd_height
ctrlmnt_arc_r = lollybrd_spacer/2

ctrlmnt_arcTL = {
    'type':         'arc',
    'center':       (lollybrd_holes_left, lollybrd_holes_top),
    'radius':       ctrlmnt_arc_r,
    'startangle':   -90,
    'endangle':     0
}
ctrlmnt_arcTR = {
    'type':         'arc',
    'center':       (lollybrd_holes_right, lollybrd_holes_top),
    'radius':       ctrlmnt_arc_r,
    'startangle':   180,
    'endangle':     -90
}
ctrlmnt_arcBL = {
    'type':         'arc',
    'center':       (lollybrd_holes_left, lollybrd_holes_bot),
    'radius':       ctrlmnt_arc_r,
    'startangle':   -90,
    'endangle':     90
}
ctrlmnt_arcBR = {
    'type':         'arc',
    'center':       (lollybrd_holes_right, lollybrd_holes_bot),
    'radius':       ctrlmnt_arc_r,
    'startangle':   90,
    'endangle':     270
}

midmnt_cutoutL = [
  (ctrlmnt_left-lollybrd_cutout_spc,lollybrd_holes_bot-ctrlmnt_arc_r),
  pt_relative(sw_holes[7][:2], [+0.5*spc, -0.5*spc], [sw_holes[7][2]]),
  pt_relative(sw_holes[8][:2], [+0.5*spc, -0.5*spc], [sw_holes[8][2]]),
  pt_relative(sw_holes[5][:2], [-0.5*spc, +0.5*spc], [sw_holes[5][2]]),
  pt_relative(sw_holes[5][:2], [+0.5*spc, +0.5*spc], [sw_holes[5][2]]),
  pt_relative(sw_holes[4][:2], [-0.5*spc, +0.5*spc], [sw_holes[4][2]]),
  pt_relative(sw_holes[4][:2], [+0.5*spc, +0.5*spc], [sw_holes[4][2]]),
]
midmnt_cutoutR = pts_reflect(midmnt_cutoutL, [center[0], None])
midmnt_cutoutR.reverse()
midmnt_cutout = midmnt_cutoutL + midmnt_cutoutR

ctrlmnt_path = [
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_left+ctrlmnt_arc_r,lollybrd_holes_bot+ctrlmnt_arc_r),
                                 (ctrlmnt_left-lollybrd_cutout_spc,lollybrd_holes_bot+ctrlmnt_arc_r),
                                 (ctrlmnt_left-lollybrd_cutout_spc,lollybrd_holes_top-ctrlmnt_arc_r),
                                 (ctrlmnt_left+ctrlmnt_arc_r,lollybrd_holes_top-ctrlmnt_arc_r),
                                ]},
    ctrlmnt_arcTL,
    {'type': 'polyline', 'pts': [
                                 (lollybrd_holes_left+ctrlmnt_arc_r,ctrlmnt_top-ctrlmnt_arc_r),
                                 (lollybrd_holes_left+ctrlmnt_arc_r,ctrlmnt_top+lollybrd_cutout_spc),
                                 (lollybrd_holes_right-ctrlmnt_arc_r,ctrlmnt_top+lollybrd_cutout_spc),
                                 (lollybrd_holes_right-ctrlmnt_arc_r,ctrlmnt_top-ctrlmnt_arc_r),
                                ]},
    ctrlmnt_arcTR,
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_right-ctrlmnt_arc_r,lollybrd_holes_top-ctrlmnt_arc_r),
                                 (ctrlmnt_right+lollybrd_cutout_spc,lollybrd_holes_top-ctrlmnt_arc_r),
                                 (ctrlmnt_right+lollybrd_cutout_spc,lollybrd_holes_bot+ctrlmnt_arc_r),
                                 (ctrlmnt_right-ctrlmnt_arc_r,lollybrd_holes_bot+ctrlmnt_arc_r),
                                ]},
    ctrlmnt_arcBR,
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_right+lollybrd_cutout_spc,lollybrd_holes_bot-ctrlmnt_arc_r),
                                 (ctrlmnt_right-ctrlmnt_arc_r,lollybrd_holes_bot-ctrlmnt_arc_r),
                                ]},
    {'type': 'polyline', 'pts': midmnt_cutout},
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_left+ctrlmnt_arc_r,lollybrd_holes_bot-ctrlmnt_arc_r),
                                 (ctrlmnt_left-lollybrd_cutout_spc,lollybrd_holes_bot-ctrlmnt_arc_r),
                                ]},
    ctrlmnt_arcBL,
]
# }}}

# {{{ Top layers cutouts.
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
  pt_relative(sw_holes[0][:2], [-0.75*spc, +0.5*spc], [sw_holes[0][2]]),
  pt_relative(sw_holes[1][:2], [-0.75*spc, -0.5*spc], [sw_holes[1][2]]),
  pt_relative(sw_holes[2][:2], [-0.5*spc, -0.5*spc], [sw_holes[2][2]]),
  pt_relative(sw_holes[2][:2], [+0.5*spc, -0.5*spc], [sw_holes[2][2]]),
  pt_relative(sw_holes[4][:2], [+0.5*spc, +0.5*spc], [sw_holes[4][2]]),
  pt_relative(sw_holes[4][:2], [-0.5*spc, +0.5*spc], [sw_holes[4][2]]),
  pt_relative(sw_holes[5][:2], [+0.5*spc, +0.5*spc], [sw_holes[5][2]]),
  pt_relative(sw_holes[5][:2], [-0.5*spc, +0.5*spc], [sw_holes[5][2]]),
  pt_relative(sw_holes[1][:2], [+0.75*spc, +0.5*spc], [sw_holes[1][2]]),
  pt_relative(sw_holes[0][:2], [+0.75*spc, +0.5*spc], [sw_holes[0][2]]),
]
thumbsL_outline.append(thumbsL_outline[0])
thumbsR_outline = pts_reflect(thumbsL_outline, [center[0], None])

top_cutout_paths = [
    {'type': 'polyline', 'pts': fingersL_outline},
    {'type': 'polyline', 'pts': fingersR_outline},
    {'type': 'polyline', 'pts': thumbsL_outline},
    {'type': 'polyline', 'pts': thumbsR_outline},
]
# }}}

# {{{ Fixing holes
fix_hole_diameter = 3.3
fix_hole_top = top_edge - border - 2.0
fix_holesL = [
    #pt_relative(sw_holes[4][:2], [+1.0*spc, -7.0], [sw_holes[4][2]]),
    (sw_holes[6][0], fix_hole_top),
    (sw_holes[28][0], fix_hole_top),
    pt_relative(leftmost_pt, [border + 2.0, -border], [hand_rotate]),
    pt_relative(wrest_center_ptL, [5.0, -wrest_r + border + 1.0], [-hand_rotate]),
    pt_relative(wrest_center_ptL, [9.0, -wrest_r + border + 2.0], [5*hand_rotate]),
]
fix_holesR = pts_reflect(fix_holesL, [center[0], None])
fix_holesR.reverse()
fix_holes = fix_holesL + fix_holesR
# }}}

# {{{ Layer outline paths
mnt_outline_path = [
    {'type': 'polyline', 'pts': [leftmost_pt, topedge_lower_ptL]},
    toparc_pathL,
    {'type': 'polyline', 'pts': [topedge_upper_ptL, topedge_upper_ptR]},
    toparc_pathR,
    {'type': 'polyline', 'pts': [topedge_lower_ptR, rightmost_pt]},
    wrest_pathR,
    botarc_path,
    wrest_pathL,
]

base0_outline_path = [
    {'type': 'polyline', 'pts': [leftmost_pt, topedge_lower_ptL]},
    toparc_pathL,
    {'type': 'polyline', 'pts': [topedge_upper_ptL] + teensy_cutout + [topedge_upper_ptR]},
    toparc_pathR,
    {'type': 'polyline', 'pts': [topedge_lower_ptR, rightmost_pt]},
    wrest_pathR,
    botarc_path,
    wrest_pathL,
]


lollybrd_toparc_r = lollybrd_spacer/2 + lollybrd_cutout_spc
lollybrd_toparc_pathL = {
    'type':         'arc',
    'center':       lollybrd_holes[2],
    'radius':       lollybrd_toparc_r,
    'startangle':   90,
    'endangle':     180
}
lollybrd_toparc_pathR = {
    'type':         'arc',
    'center':       lollybrd_holes[3],
    'radius':       lollybrd_toparc_r,
    'startangle':   0,
    'endangle':     90
}
base1_top_cutoutL = [
    (teensy_cutout_left, top_edge),
    (teensy_cutout_left, lollybrd_cutout_top),
    (lollybrd_cutout_left + lollybrd_toparc_r, lollybrd_cutout_top),
]
base1_top_cutoutR = pts_reflect(base1_top_cutoutL, [center[0], None])
base1_top_cutoutR.reverse()

base1_main_cutoutL = [
    (lollybrd_cutout_left, lollybrd_cutout_top - lollybrd_toparc_r),
    (lollybrd_cutout_left, lollybrd_cutout_bot),
] + handbrdL_cutout[::-1]
base1_main_cutoutR = pts_reflect(base1_main_cutoutL, [center[0], None])
base1_main_cutoutR.reverse()
base1_main_cutout = base1_main_cutoutL + base1_main_cutoutR

base1_outline_path = [
    {'type': 'polyline', 'pts': [leftmost_pt, topedge_lower_ptL]},
    toparc_pathL,
    {'type': 'polyline', 'pts': [topedge_upper_ptL] + base1_top_cutoutL},
    lollybrd_toparc_pathL,
    {'type': 'polyline', 'pts': base1_main_cutout},
    lollybrd_toparc_pathR,
    {'type': 'polyline', 'pts': base1_top_cutoutR + [topedge_upper_ptR]},
    toparc_pathR,
    {'type': 'polyline', 'pts': [topedge_lower_ptR, rightmost_pt]},
    wrest_pathR,
    botarc_path,
    wrest_pathL,
]


base2_top_cutout = [
    (lollybrd_cutout_right - lollybrd_toparc_r, lollybrd_cutout_top),
    (lollybrd_cutout_left + lollybrd_toparc_r, lollybrd_cutout_top),
]
base2_main_cutoutL = [
    (lollybrd_cutout_left, lollybrd_cutout_top - lollybrd_toparc_r),
    (lollybrd_cutout_left, lollybrd_cutout_bot),
] + handbrdL_cutout[::-1]
base2_main_cutoutR = pts_reflect(base2_main_cutoutL, [center[0], None])
base2_main_cutoutR.reverse()
base2_main_cutout = base2_main_cutoutL + base2_main_cutoutR
base2_cutout_path = [
    {'type': 'polyline', 'pts': base2_top_cutout},
    lollybrd_toparc_pathL,
    {'type': 'polyline', 'pts': base2_main_cutout},
    lollybrd_toparc_pathR,
]
# }}}

pcb_cut_bot = pt_relative(pcb_sw[4][:2], [+0.5*spc, +0.5*spc], [pcb_sw[4][2]])
pcb_cut_top = pt_relative(pcb_sw[6][:2], [+0.5*spc,  +0.5*spc], [pcb_sw[6][2]])
pcb_outline = [
  pcb_cut_bot,
  pt_relative(pcb_sw[2][:2], [+0.5*spc, -0.5*spc], [pcb_sw[2][2]]),
  pt_relative(pcb_sw[0][:2], [-1.0*spc, +0.5*spc], [pcb_sw[0][2]]),
  #
#  pt_relative(pcb_sw[17][:2], [+0.5*spc,  -0.5*spc], [pcb_sw[17][2]]),
#  pt_relative(pcb_sw[17][:2], [-0.5*spc,  -0.5*spc], [pcb_sw[17][2]]),
#  pt_relative(pcb_sw[22][:2], [+0.5*spc,  -0.5*spc], [pcb_sw[22][2]]),
#  pt_relative(pcb_sw[22][:2], [-0.5*spc,  -0.5*spc], [pcb_sw[22][2]]),
#  pt_relative(pcb_sw[27][:2], [+0.5*spc,  -0.5*spc], [pcb_sw[27][2]]),
#  pt_relative(pcb_sw[27][:2], [-0.5*spc,  -0.5*spc], [pcb_sw[27][2]]),
#  pt_relative(pcb_sw[32][:2], [+0.5*spc,  -0.5*spc], [pcb_sw[32][2]]),
  pt_relative(pcb_sw[37][:2], [-0.5*spc,  -0.5*spc], [pcb_sw[37][2]]),
#  pt_relative(pcb_sw[37][:2], [-0.5*spc,  +0.5*spc], [pcb_sw[37][2]]),
  pt_relative(pcb_sw[36][:2], [-0.5*spc, -0.5*spc], [pcb_sw[36][2]]),
  pt_relative(pcb_sw[33][:2], [-0.5*spc, +0.5*spc], [pcb_sw[33][2]]),
  #
  pt_relative(pcb_sw[28][:2], [+0.5*spc,  +0.5*spc], [pcb_sw[28][2]]),
  pt_relative(pcb_sw[23][:2], [-0.5*spc,  +0.5*spc], [pcb_sw[23][2]]),
  pt_relative(pcb_sw[23][:2], [+0.5*spc,  +0.5*spc], [pcb_sw[23][2]]),
  pt_relative(pcb_sw[18][:2], [-0.5*spc,  +0.5*spc], [pcb_sw[18][2]]),
  pt_relative(pcb_sw[18][:2], [+0.5*spc,  +0.5*spc], [pcb_sw[18][2]]),
  pt_relative(pcb_sw[13][:2], [-0.5*spc,  +0.5*spc], [pcb_sw[13][2]]),
  pt_relative(pcb_sw[13][:2], [+0.5*spc,  +0.5*spc], [pcb_sw[13][2]]),
  pt_relative(pcb_sw[9][:2],  [-0.5*spc,  +0.5*spc], [pcb_sw[9][2]]),
  pcb_cut_top,
]
pcb_outline.append(pcb_outline[0])

sw_pos = [ # {{{ (column, row) map of switch positions in the matrix.
(5, 3),
(5, 2),
(5, 1),
(5, 4),
(5, 6),
(5, 5),
#
(0, 6),
(1, 6),
(3, 6),
#
(0, 5),
(1, 5),
(2, 5),
(3, 5),
#
(0, 4),
(1, 4),
(2, 4),
(3, 4),
(4, 4),
#
(0, 3),
(1, 3),
(2, 3),
(3, 3),
(4, 3),
#
(0, 2),
(1, 2),
(2, 2),
(3, 2),
(4, 2),
#
(0, 1),
(1, 1),
(2, 1),
(3, 1),
(4, 1),
#
(0, 0),
(1, 0),
(2, 0),
(3, 0),
(4, 0),
]
assert len(sw_pos) == 38
assert len(sw_pos) == len(pcb_sw)
# }}} End of sw_pos
pcb_header_pt = pt_between_pts(pcb_cut_bot, pcb_cut_top, 0.5)
pcb_header_dir = dir_between_pts(pcb_cut_top, pcb_cut_bot)[0]
pcb_header_pt = pt_relative(pcb_header_pt, [-(3*0.8+3.0), 0.0], [pcb_header_dir + pi/2])

def sw_outline_pts(sw_type='', args={}): # {{{
    '''Define a switch hole.
    '''
    sw_type = sw_type.lower()

    if sw_type in ['alps', 'matias']:
        width = 15.3 if 'width' not in args else args['width']
        height = 12.7 if 'height' not in args else args['height']
        ret = [
            (-width/2, -height/2),
            (+width/2, -height/2),
            (+width/2, +height/2),
            (-width/2, +height/2),
        ]
    elif sw_type in ['cherrymx']:
        width = 13.7 if 'width' not in args else args['width']
        notch_depth = 1.0 if 'notch_depth' not in args else args['notch_depth']
        notch_height = 3.7 if 'notch_height' not in args else args['notch_height']

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

def cap_size(n): # {{{
    '''Return string with capsize for a particular switch number.
    '''
    n = n % 38
    if n in [
               0,
               1,
               7,
               8,
               36,
               35,
               34,
               33,
              ]:
        return 'cap_15'
    else:
        return 'cap_10'
# }}} End of cap_size()

# {{{ Labels
labelsL_dvorak = [
 (-90, [('Shift',   -7.0, +8.0)                                                     ]),
 (-90, [('Ctrl',    -7.0, +8.0)                                                     ]),
 (0,   [('Flip',    -7.0, +4.0)                                                     ]),
 (0,   [('Del',     -7.0, +4.0),                            ('Ins',    +1.0, -8.0)  ]),
 (0,   [('Alt',     -7.0, +4.0)                                                     ]),
 (0,   [('`',       -6.0, +1.0),    ('~',  -6.5, +5.5)                              ]),
 (0,   [('F4',      -7.0, +1.0),                            ('F6',     +2.0, -8.0)  ]),
 (-90, [('Home',    -7.0, +6.0),                            ('Vol+',   -2.0, -11.0) ]),
 (-90, [('End',     -7.0, +6.0),                            ('Vol-',   -2.0, -11.0) ]),
 (0,   [('5',       -7.0, +1.0),    ('%',  -7.0, +5.0),     ('F5',     +2.0, -8.0)  ]),
 (0,   [('Y',       -7.0, +2.0)                                                     ]),
 (0,   [('I',       -7.0, +2.0)                                                     ]),
 (0,   [('X',       -7.0, +2.0)                                                     ]),
 (0,   [('4',       -7.0, +1.0),    ('$',  -7.0, +5.0),     ('F4',     +2.0, -8.0)  ]),
 (0,   [('P',       -7.0, +2.0)                                                     ]),
 (0,   [('U',       -7.0, +2.0)                                                     ]),
 (0,   [('K',       -7.0, +2.0)                                                     ]),
 (0,   [                                                                            ]),
 (0,   [('3',       -7.0, +1.0),    ('#',  -7.0, +5.0),     ('F3',     +2.0, -8.0)  ]),
 (0,   [('.',       -7.0, +2.0),    ('>',  -7.0, +5.0)                              ]),
 (0,   [('E',       -7.0, +2.0)                                                     ]),
 (0,   [('J',       -7.0, +2.0)                                                     ]),
 (0,   [                                                                            ]),
 (0,   [('2',       -7.0, +1.0),    ('@',  -7.0, +5.0),     ('F2',     +2.0, -8.0)  ]),
 (0,   [(',',       -7.0, +2.0),    ('<',  -7.0, +5.0)                              ]),
 (0,   [('O',       -7.0, +2.0)                                                     ]),
 (0,   [('Q',       -7.0, +2.0)                                                     ]),
 (0,   [('App',     -7.0, +4.0)                                                     ]),
 (0,   [('1',       -7.0, +1.0),    ('!',  -6.0, +5.0),     ('F1',     +2.0, -8.0)  ]),
 (0,   [('\'',      -5.5, +1.0),    ('"',  -5.5, +4.0)                              ]),
 (0,   [('A',       -7.0, +2.0)                                                     ]),
 (0,   [(';',       -6.0, +1.9),    (':',  -6.0, +5.0)                              ]),
 (0,   [('PgDn',    -7.0, +4.0)                                                     ]),
 (0,   [('Esc',     -11.0,+4.0)                                                     ]),
 (0,   [('Tab',     -11.0,+4.0)                                                     ]),
 (0,   [('Fn',      -11.0,+4.0)                                                     ]),
 (0,   [('Bkspc',   -11.0,+4.0)                                                     ]),
 (0,   [('PgUp',    -7.0, +4.0)                                                     ]),
]

labelsR_dvorak = [
 (90,  [('Space',   -7.0, +8.0)                                                     ]),
 (90,  [('Enter',   -7.0, +8.0)                                                     ]),
 (0,   [('Flip',    -7.0, +4.0)                                                     ]),
 (0,   [('Shift',   -7.0, +4.0),                                                    ]),
 (0,   [('Mute',    -7.0, +4.0)                                                     ]),
 (0,   [('Super',   -7.0, +4.0),                                                    ]),
 (0,   [('F5',      -7.0, +2.0),                            ('F7',     +2.0, -8.0)  ]),
 (90,  [('[',       -7.0, +1.0),    ('{',  -7.5, +5.0),                             ]),
 (90,  [(']',       -7.0, +1.0),    ('{',  -7.5, +5.0),                             ]),
 (0,   [('6',       -7.0, +1.0),    ('^',  -7.0, +5.0),     ('F8',     +2.0, -8.0)  ]),
 (0,   [('F',       -7.0, +2.0)                                                     ]),
 (0,   [('D',       -7.0, +2.0)                                                     ]),
 (0,   [('B',       -7.0, +2.0)                                                     ]),
 (0,   [('7',       -7.0, +1.0),    ('&',  -7.0, +5.0),     ('F9',     +2.0, -8.0)  ]),
 (0,   [('G',       -7.0, +2.0)                                                     ]),
 (0,   [('H',       -7.0, +2.0),                            ('clkL',   -1.0, -8.0)  ]),
 (0,   [('M',       -7.0, +2.0),                            ('scrL',   -1.0, -8.0)  ]),
 (0,   [('Lft',     -7.0, +4.0),                            ('msL',    -1.0, -8.0)  ]),
 (0,   [('8',       -7.0, +1.0),    ('*',  -7.0, +5.0),     ('F10',    +1.0, -8.0)  ]),
 (0,   [('C',       -7.0, +2.0),                                                    ]),
 (0,   [('T',       -7.0, +2.0),                            ('clkM',   -1.0, -8.0)  ]),
 (0,   [('W',       -7.0, +2.0),                            ('srcU',   -1.0, -8.0)  ]),
 (0,   [('Up',      -7.0, +4.0),                            ('msU',    -1.0, -8.0)  ]),
 (0,   [('9',       -7.0, +1.0),    ('(',  -7.0, +5.0),     ('F11',    +1.0, -8.0)  ]),
 (0,   [('R',       -7.0, +2.0),                                                    ]),
 (0,   [('N',       -7.0, +2.0),                            ('clkR',   -1.0, -8.0)  ]),
 (0,   [('V',       -7.0, +2.0),                            ('scrD',   -1.0, -8.0)  ]),
 (0,   [('Dn',      -7.0, +4.0),                            ('msD',    -1.0, -8.0)  ]),
 (0,   [('0',       -7.0, +1.0),    (')',  -7.0, +5.0),     ('F12',    +1.0, -8.0)  ]),
 (0,   [('L',       -7.0, +2.0),                                                    ]),
 (0,   [('S',       -7.0, +2.0)                                                     ]),
 (0,   [('Z',       -7.0, +2.0),                            ('scrR',   -1.0, -8.0)  ]),
 (0,   [('Rgt',     -7.0, +4.0),                            ('msR',    -1.0, -8.0)  ]),
 (0,   [('/',      -11.0, +1.0),    ('?', -11.0, +5.0)                              ]),
 (0,   [('=',      -11.0, +1.0),    ('+', -11.0, +5.0)                              ]),
 (0,   [('-',      -11.0, +1.0),    ('_', -11.0, +5.0)                              ]),
 (0,   [('Ctrl',   -11.0, +4.0)                                                     ]),
 (0,   [('\\',      -7.0, +1.0),    ('|',  -7.0, +5.0)                              ]),
]

labelsL_qwerty = [
 (-90, [('Shift',   -7.0, +12.0)                                                    ]),
 (-90, [('Ctrl',    -7.0, +12.0)                                                    ]),
 (0,   [('Flip',    -7.0, +4.0)                                                     ]),
 (0,   [('Del',     -7.0, +4.0),                            ('Ins',    +1.0, -8.0)  ]),
 (0,   [('Alt',     -7.0, +4.0)                                                     ]),
 (0,   [('`',       -6.0, +1.0),    ('~',  -6.5, +5.5)                              ]),
 (0,   [('F4',      -7.0, +1.0),                            ('F6',     +2.0, -8.0)  ]),
 (-90, [('Home',    -7.0, +6.0),                            ('Vol+',   -2.0, -11.0) ]),
 (-90, [('End',     -7.0, +6.0),                            ('Vol-',   -2.0, -11.0) ]),
 (0,   [('5',       -7.0, +1.0),    ('%',  -7.0, +5.0),     ('F5',     +2.0, -8.0)  ]),
 (0,   [('T',       -7.0, +2.0)                                                     ]),
 (0,   [('G',       -7.0, +2.0)                                                     ]),
 (0,   [('B',       -7.0, +2.0)                                                     ]),
 (0,   [('4',       -7.0, +1.0),    ('$',  -7.0, +5.0),     ('F4',     +2.0, -8.0)  ]),
 (0,   [('R',       -7.0, +2.0),                                                    ]),
 (0,   [('F',       -7.0, +2.0)                                                     ]),
 (0,   [('V',       -7.0, +2.0)                                                     ]),
 (0,   [                                                                            ]),
 (0,   [('3',       -7.0, +1.0),    ('#',  -7.0, +5.0),     ('F3',     +2.0, -8.0)  ]),
 (0,   [('E',       -7.0, +2.0)                                                     ]),
 (0,   [('D',       -7.0, +2.0)                                                     ]),
 (0,   [('C',       -7.0, +2.0)                                                     ]),
 (0,   [                                                                            ]),
 (0,   [('2',       -7.0, +1.0),    ('@',  -7.0, +5.0),     ('F2',     +2.0, -8.0)  ]),
 (0,   [('W',       -7.0, +2.0)                                                     ]),
 (0,   [('S',       -7.0, +2.0)                                                     ]),
 (0,   [('X',       -7.0, +2.0)                                                     ]),
 (0,   [('App',     -7.0, +4.0)                                                     ]),
 (0,   [('1',       -7.0, +1.0),    ('!',  -6.0, +5.0),     ('F1',     +2.0, -8.0)  ]),
 (0,   [('Q',       -7.0, +2.0)                                                     ]),
 (0,   [('A',       -7.0, +2.0)                                                     ]),
 (0,   [('Z',       -7.0, +2.0),                                                    ]),
 (0,   [('PgDn',    -7.0, +4.0)                                                     ]),
 (0,   [('Esc',     -11.0,+4.0)                                                     ]),
 (0,   [('Tab',     -11.0,+4.0)                                                     ]),
 (0,   [('Fn',      -11.0,+4.0)                                                     ]),
 (0,   [('Bkspc',   -11.0,+4.0)                                                     ]),
 (0,   [('PgUp',    -7.0, +4.0),                            ('Teensy', -5.0, -8.0)  ]),
]

labelsR_qwerty = [
 (90,  [('Space',   -7.0, +12.0)                                                    ]),
 (90,  [('Enter',   -7.0, +12.0)                                                    ]),
 (0,   [('Flip',    -7.0, +4.0)                                                     ]),
 (0,   [('Shift',   -7.0, +4.0),                                                    ]),
 (0,   [('Mute',    -7.0, +4.0)                                                     ]),
 (0,   [('Super',   -7.0, +4.0),                                                    ]),
 (0,   [('F5',      -7.0, +2.0),                            ('F7',     +2.0, -8.0)  ]),
 (90,  [('[',       -7.0, +1.0),    ('{',  -7.5, +5.0),                             ]),
 (90,  [(']',       -7.0, +1.0),    ('{',  -7.5, +5.0),                             ]),
 (0,   [('6',       -7.0, +1.0),    ('^',  -7.0, +5.0),     ('F8',     +2.0, -8.0)  ]),
 (0,   [('Y',       -7.0, +2.0)                                                     ]),
 (0,   [('H',       -7.0, +2.0)                                                     ]),
 (0,   [('N',       -7.0, +2.0),                                                    ]),
 (0,   [('7',       -7.0, +1.0),    ('&',  -7.0, +5.0),     ('F9',     +2.0, -8.0)  ]),
 (0,   [('U',       -7.0, +2.0)                                                     ]),
 (0,   [('J',       -7.0, +2.0),                            ('clkL',   -1.0, -8.0)  ]),
 (0,   [('M',       -7.0, +2.0),                            ('scrL',   -1.0, -8.0)  ]),
 (0,   [('Lft',     -7.0, +4.0),                            ('msL',    -1.0, -8.0)  ]),
 (0,   [('8',       -7.0, +1.0),    ('*',  -7.0, +5.0),     ('F10',    +1.0, -8.0)  ]),
 (0,   [('I',       -7.0, +2.0),                                                    ]),
 (0,   [('K',       -7.0, +2.0),                            ('clkM',   -1.0, -8.0)  ]),
 (0,   [(',',       -7.0, +2.0),    ('<',  -7.0, +5.0),     ('srcU',   -1.0, -8.0)  ]),
 (0,   [('Up',      -7.0, +4.0),                            ('msU',    -1.0, -8.0)  ]),
 (0,   [('9',       -7.0, +1.0),    ('(',  -7.0, +5.0),     ('F11',    +1.0, -8.0)  ]),
 (0,   [('O',       -7.0, +2.0)                                                     ]),
 (0,   [('L',       -7.0, +2.0),                            ('clkR',   -1.0, -8.0)  ]),
 (0,   [('.',       -7.0, +2.0),    ('>',  -7.0, +5.0),     ('scrD',   -1.0, -8.0)  ]),
 (0,   [('Dn',      -7.0, +4.0),                            ('msD',    -1.0, -8.0)  ]),
 (0,   [('0',       -7.0, +1.0),    (')',  -7.0, +5.0),     ('F12',    +1.0, -8.0)  ]),
 (0,   [('P',       -7.0, +2.0)                                                     ]),
 (0,   [(';',       -6.0, +1.9),    (':',  -6.0, +5.0)                              ]),
 (0,   [('/',       -7.0, +1.0),    ('?',  -7.0, +5.0),     ('scrR',   -1.0, -8.0)  ]),
 (0,   [('Rgt',     -7.0, +4.0),                            ('msR',    -1.0, -8.0)  ]),
 (0,   [('-',      -11.0, +1.0),    ('_', -11.0, +5.0)                              ]),
 (0,   [('=',      -11.0, +1.0),    ('+', -11.0, +5.0)                              ]),
 (0,   [('\'',      -9.5, +1.0),    ('"',  -9.5, +4.0)                              ]),
 (0,   [('Ctrl',   -11.0, +4.0)                                                     ]),
 (0,   [('\\',      -7.0, +1.0),    ('|',  -7.0, +5.0)                              ]),
]

labels = labelsL_dvorak + labelsR_dvorak
# }}}

if __name__ == '__main__':
    out = []
    out += ['Switch holes:']
    for h in sw_holes:
        out += ['\t(%0.2f, %0.2f) rotate=%d' % (h[0], h[1], degrees(h[2]))]
    out += ['Fixing holes:']
    for h in fix_holes:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['PCB holes:']
    for h in lollybrd_holes:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['Outer:']
    out += ['\theight=%0.2f' % top_edge]
    out += ['\twidth=%0.2f' % (wrest_center_ptR[0] + wrest_r)]
    print('\n'.join(out))
