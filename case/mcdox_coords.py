#!/usr/bin/env python

from math import *
import sys
from ndim import *

# TODO: refactoring
# Regular naming scheme:
#   angle       - _a
#   radius      - _r
#   width       - _w
#   height      - _h
#   depth       - _d
#   gradient    - _m
#   offset      - _c
#   cutout      - _co
#   hole        - _hl
#   point       - _pt
#   extended point - _ept Point with angle and possibly other info attached.
#   left        - _L
#   right       - _R
#   bottom      - _B
#   top         - _T
# Consistent naming scheme:
#   wrest - Wrist rest.
#   base0, base1, base2, mnt, top0, top1, top2 - layer names.
# M3 module

# Unit width of one switch, standardised at 19mm.
u = 19.0

# Ergonomic angle of rotation for whole hand.
hand_a = radians(-13)

# Ergonomic angle of rotation for thumb cluster, in addition to hand_a.
thumb_a = radians(-25)

# Separation of hand circles.
hand_sep = 29.0

# Outline border width.
border = 5.0

# Radius of wrist rests.
wrest_r = 93.0

# Center of entire keyboard.
center = (2*wrest_r + hand_sep/2, wrest_r)


# {{{ Switch grid for left hand (not rotated)

# Ergonomic column offsets for finger cluster.
c0_Y = 0.0 # 1.5x outer.
c1_Y = 0.0 # Pinky finger.
c2_Y = 3.0 # Ring finger.
c3_Y = 4.5 # Middle finger.
c4_Y = 3.0 # Index finger.
c5_Y = 1.5 # Other index finger.
c6_Y = 1.5 # 1.5x inner.

# Non-ergonomic positions from origin
c0_X = 0.0            # 1.5x outer.
c1_X = c0_X + 1.25*u  # Pinky finger.
c2_X = c1_X + u       # Ring finger.
c3_X = c2_X + u       # Middle finger.
c4_X = c3_X + u       # Index finger.
c5_X = c4_X + u       # Other index finger.
c6_X = c5_X + u       # 1.5x inner.

#    X                  Y               angle
c0 = [
    (c0_X,              4*u+c0_Y,       0.0),
    (c0_X,              3*u+c0_Y,       0.0),
    (c0_X,              2*u+c0_Y,       0.0),
    (c0_X,              1*u+c0_Y,       0.0),
    (c0_X + 0.25*u,     0*u+c0_Y,       0.0),
]

c1 = [
    (c1_X,              4*u+c1_Y,       0.0),
    (c1_X,              3*u+c1_Y,       0.0),
    (c1_X,              2*u+c1_Y,       0.0),
    (c1_X,              1*u+c1_Y,       0.0),
    (c1_X,              0*u+c1_Y,       0.0),
]

c2 = [
    (c2_X,              4*u+c2_Y,       0.0),
    (c2_X,              3*u+c2_Y,       0.0),
    (c2_X,              2*u+c2_Y,       0.0),
    (c2_X,              1*u+c2_Y,       0.0),
    (c2_X,              0*u+c2_Y,       0.0),
]

c3 = [
    (c3_X,              4*u+c3_Y,       0.0),
    (c3_X,              3*u+c3_Y,       0.0),
    (c3_X,              2*u+c3_Y,       0.0),
    (c3_X,              1*u+c3_Y,       0.0),
    (c3_X,              0*u+c3_Y,       0.0),
]

c4 = [
    (c4_X,              4*u+c4_Y,       0.0),
    (c4_X,              3*u+c4_Y,       0.0),
    (c4_X,              2*u+c4_Y,       0.0),
    (c4_X,              1*u+c4_Y,       0.0),
    (c4_X,              0*u+c4_Y,       0.0),
]

c5 = [
    (c5_X,              4*u+c5_Y,       0.0),
    (c5_X,              3*u+c5_Y,       0.0),
    (c5_X,              2*u+c5_Y,       0.0),
    (c5_X,              1*u+c5_Y,       0.0),
]

c6 = [
    (c6_X,              4*u+c6_Y,       0.0),
    (c6_X,              2.75*u+c6_Y,    pi/2),
    (c6_X,              1.25*u+c6_Y,    pi/2),
]

pcb_sw_finger_epts = c6 + c5 + c4 + c3 + c2 + c1 + c0


thumb_ptBL = [c5_X + 0.5*u + 1.5, -0.5*u - 1]

pcb_sw_thumb_pts = [
    (0*u, 0*u),
    (1*u, 0*u),
    (2*u, -0.5*u),
    (2*u, +0.5*u),
    (2*u, +1.5*u),
    (1*u, +1.25*u),
]
pcb_sw_thumb_pts = pts_rotate(pcb_sw_thumb_pts, [thumb_a])
pcb_sw_thumb_pts = pts_shift(pcb_sw_thumb_pts, thumb_ptBL)
pcb_sw_thumb_epts = [list(p) + [thumb_a] for p in pcb_sw_thumb_pts]
pcb_sw_thumb_epts[0][2] += pi/2
pcb_sw_thumb_epts[1][2] += pi/2
pcb_sw_thumb_epts = [tuple(p) for p in pcb_sw_thumb_epts]

# Switch points at opposite corners are used to find the center of the hand.
# Opposite corners are top-left to bottom-right.
# hand_pt: Center between opposite corners.
sw_ptTL = c0[0][:2]
sw_ptBR = pcb_sw_thumb_pts[2]
hand_pt = pt_between_pts(sw_ptTL, sw_ptBR)


pcb_sw_epts = pcb_sw_thumb_epts + pcb_sw_finger_epts
pcb_sw_pts = [(h[0], h[1]) for h in pcb_sw_epts]
pcb_sw_a = [h[2] + hand_a for h in pcb_sw_epts]
n_sw = len(pcb_sw_epts)

pcb_sw = pcb_sw_epts


# Real coordinates of switches.
sw_ptsL = pts_shift(pcb_sw_pts, [-hand_pt[0] + wrest_r, wrest_r])
sw_ptsL = pts_rotate(sw_ptsL, angle=[hand_a], center=(wrest_r, wrest_r))
sw_ptsR = pts_reflect(sw_ptsL, [center[0], None])
sw_pts = sw_ptsL + sw_ptsR

sw_aL = pcb_sw_a
sw_aR = [-a for a in pcb_sw_a]
sw_a = sw_aL + sw_aR

sw_eptsL = [(sw_ptsL[i][0], sw_ptsL[i][1], sw_aL[i]) for i in range(n_sw)]
sw_eptsR = [(sw_ptsR[i][0], sw_ptsR[i][1], sw_aR[i]) for i in range(n_sw)]
sw_epts = sw_eptsL + sw_eptsR

# }}} Switch grid for left hand (not rotated)


# {{{ Outline paths
toparc_center_ptL = pt_relative(sw_pts[33], [-0.75*u, +0.5*u], [sw_a[33]])
toparc_center_ptR = pt_reflect(toparc_center_ptL, [center[0], None])
toparc_pathL = {
    'type':         'arc',
    'center':       toparc_center_ptL,
    'radius':       border,
    'startangle':   90,
    'endangle':     180 + degrees(hand_a)
}
toparc_pathR = {
    'type':         'arc',
    'center':       toparc_center_ptR,
    'radius':       border,
    'startangle':   -degrees(hand_a),
    'endangle':     90
}
top_edge = toparc_center_ptL[1] + border
topedge_upper_ptL = (toparc_center_ptL[0], top_edge)
topedge_upper_ptR = (toparc_center_ptR[0], top_edge)
topedge_lower_ptL = pt_relative(toparc_center_ptL, [+border, 0.0], [radians(180) + hand_a])
topedge_lower_ptR = pt_relative(toparc_center_ptR, [+border, 0.0], [-hand_a])

leftmost_pt = pt_relative(sw_pts[36], [-0.75*u-border, -0.5*u-border], [sw_a[36]])
rightmost_pt = pt_reflect(leftmost_pt, [center[0], None])
leftmost_m = tan(hand_a)
leftmost_c = leftmost_pt[1] - leftmost_m*leftmost_pt[0] # c = y - mx

thumbarc_pt = pt_relative(sw_pts[2], [+0.5*u+border, 0.0], [sw_a[2]])

wrest_center_x = leftmost_pt[0] + cos(hand_a)*wrest_r
wrest_center_y = leftmost_pt[1] + sin(hand_a)*wrest_r
wrest_center_ptL = (wrest_center_x, wrest_center_y)
wrest_center_ptR = pt_reflect(wrest_center_ptL, [center[0], None])
wrest_angle_eR = -hand_a
wrest_angle_sL = radians(180) + hand_a
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
  pt_relative(sw_pts[4], [+(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[4]]),
  pt_relative(sw_pts[2], [+(0.5*u+0.5), -(0.5*u+0.5)], [sw_a[2]]),
  pt_relative(sw_pts[0], [-(1.0*u+0.5), +(0.5*u+0.5)], [sw_a[0]]),
  #
  #pt_relative(sw_pts[17], [+(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[17]]),
  #pt_relative(sw_pts[17], [-(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[17]]),
  #pt_relative(sw_pts[22], [+(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[22]]),
  #pt_relative(sw_pts[22], [-(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[22]]),
  #pt_relative(sw_pts[27], [+(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[27]]),
  #pt_relative(sw_pts[27], [-(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[27]]),
  #pt_relative(sw_pts[32], [+(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[32]]),
  pt_relative(sw_pts[37], [-(0.5*u+0.5),  -(0.5*u+0.5)], [sw_a[37]]),
  #pt_relative(sw_pts[37], [-(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[37]]),
  pt_relative(sw_pts[36], [-(0.5*u+0.5), -(0.5*u+0.5)], [sw_a[36]]),
  pt_relative(sw_pts[33], [-(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[33]]),
  #
  pt_relative(sw_pts[28], [+(0.5*u-0.5),  +(0.5*u+0.5)], [sw_a[28]]),
  pt_relative(sw_pts[23], [-(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[23]]),
  pt_relative(sw_pts[23], [+(0.5*u-0.5),  +(0.5*u+0.5)], [sw_a[23]]),
  pt_relative(sw_pts[18], [-(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[18]]),
  pt_relative(sw_pts[18], [+(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[18]]),
  pt_relative(sw_pts[13], [-(0.5*u-0.5),  +(0.5*u+0.5)], [sw_a[13]]),
  pt_relative(sw_pts[13], [+(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[13]]),
  pt_relative(sw_pts[9],  [-(0.5*u-0.5),  +(0.5*u+0.5)], [sw_a[9]]),
  pt_relative(sw_pts[6],  [+(0.5*u+0.5),  +(0.5*u+0.5)], [sw_a[6]]),
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
  pt_relative(sw_pts[7], [+0.55*u, -0.55*u], [sw_a[7]]),
  pt_relative(sw_pts[8], [+0.55*u, -0.55*u], [sw_a[8]]),
  pt_relative(sw_pts[5], [-0.55*u, +0.55*u], [sw_a[5]]),
  pt_relative(sw_pts[5], [+0.45*u, +0.55*u], [sw_a[5]]),
  pt_relative(sw_pts[4], [-0.55*u, +0.55*u], [sw_a[4]]),
  pt_relative(sw_pts[4], [+0.55*u, +0.55*u], [sw_a[4]]),
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
  pt_relative(sw_pts[33], [-0.75*u, +0.5*u], [sw_a[33]]),
  pt_relative(sw_pts[36], [-0.75*u, -0.5*u], [sw_a[36]]),
  pt_relative(sw_pts[37], [-0.5*u,  +0.5*u], [sw_a[37]]),
  pt_relative(sw_pts[37], [-0.5*u,  -0.5*u], [sw_a[37]]),
  pt_relative(sw_pts[32], [+0.5*u,  -0.5*u], [sw_a[32]]),
  pt_relative(sw_pts[27], [-0.5*u,  -0.5*u], [sw_a[27]]),
  pt_relative(sw_pts[27], [+0.5*u,  -0.5*u], [sw_a[27]]),
  pt_relative(sw_pts[22], [-0.5*u,  -0.5*u], [sw_a[22]]),
  pt_relative(sw_pts[22], [+0.5*u,  -0.5*u], [sw_a[22]]),
  pt_relative(sw_pts[17], [-0.5*u,  -0.5*u], [sw_a[17]]),
  pt_relative(sw_pts[17], [+0.5*u,  -0.5*u], [sw_a[17]]),
  pt_relative(sw_pts[12], [-0.5*u,  -0.5*u], [sw_a[12]]),
  pt_relative(sw_pts[12], [+0.5*u,  -0.5*u], [sw_a[12]]),
  pt_relative(sw_pts[8],  [-0.75*u, -0.5*u], [sw_a[8]]),
  pt_relative(sw_pts[8],  [+0.75*u, -0.5*u], [sw_a[8]]),
  pt_relative(sw_pts[6],  [+0.5*u,  +0.5*u], [sw_a[6]]),
  pt_relative(sw_pts[9],  [-0.5*u,  +0.5*u], [sw_a[9]]),
  pt_relative(sw_pts[13], [+0.5*u,  +0.5*u], [sw_a[13]]),
  pt_relative(sw_pts[13], [-0.5*u,  +0.5*u], [sw_a[13]]),
  pt_relative(sw_pts[18], [+0.5*u,  +0.5*u], [sw_a[18]]),
  pt_relative(sw_pts[18], [-0.5*u,  +0.5*u], [sw_a[18]]),
  pt_relative(sw_pts[23], [+0.5*u,  +0.5*u], [sw_a[23]]),
  pt_relative(sw_pts[23], [-0.5*u,  +0.5*u], [sw_a[23]]),
  pt_relative(sw_pts[28], [+0.5*u,  +0.5*u], [sw_a[28]]),
]
fingersL_outline.append(fingersL_outline[0])
fingersR_outline = pts_reflect(fingersL_outline, [center[0], None])

thumbsL_outline = [
  pt_relative(sw_pts[0], [-0.75*u, +0.5*u], [sw_a[0]]),
  pt_relative(sw_pts[1], [-0.75*u, -0.5*u], [sw_a[1]]),
  pt_relative(sw_pts[2], [-0.5*u, -0.5*u], [sw_a[2]]),
  pt_relative(sw_pts[2], [+0.5*u, -0.5*u], [sw_a[2]]),
  pt_relative(sw_pts[4], [+0.5*u, +0.5*u], [sw_a[4]]),
  pt_relative(sw_pts[4], [-0.5*u, +0.5*u], [sw_a[4]]),
  pt_relative(sw_pts[5], [+0.5*u, +0.5*u], [sw_a[5]]),
  pt_relative(sw_pts[5], [-0.5*u, +0.5*u], [sw_a[5]]),
  pt_relative(sw_pts[1], [+0.75*u, +0.5*u], [sw_a[1]]),
  pt_relative(sw_pts[0], [+0.75*u, +0.5*u], [sw_a[0]]),
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

# {{{ Weight saving cutouts
# TODO
wsco_above_ptsL = [
    (ctrlmnt_left - border, pt_relative(sw_pts[6], [+0.5*u,  +0.5*u + border], [0.0])[1]),
    (ctrlmnt_left - border, top_edge - 2*border),
]
wsco_above_ptsR = pts_reflect(wsco_above_ptsL, [center[0], None])
wsco_above_ptsR.reverse()

#wsco_below_ptsL = [
#]
#wsco_below_ptsR = pts_reflect(wsco_below_ptsL, [center[0], None])
#wsco_below_ptsR.reverse()

wsco_paths = [
    {'type': 'polyline', 'pts': wsco_above_ptsL},
    {'type': 'polyline', 'pts': wsco_above_ptsR},
]
# }}}

# {{{ Fixing holes
M3_d = 3.3
M3_r = M3_d/2
fix_hole_top = top_edge - border - 2.0
fix_holesL = [
    #pt_relative(sw_pts[4], [+1.0*u, -7.0], [sw_a[4]]),
    (sw_pts[6][0], fix_hole_top),
    (sw_pts[28][0], fix_hole_top),
    pt_relative(leftmost_pt, [border + 2.0, -border], [hand_a]),
    pt_relative(wrest_center_ptL, [5.0, -wrest_r + border + 1.0], [-hand_a]),
    pt_relative(wrest_center_ptL, [9.0, -wrest_r + border + 2.0], [5*hand_a]),
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

pcb_cut_bot = pt_relative(pcb_sw_pts[4], [+0.5*u, +0.5*u], [pcb_sw_a[4]])
pcb_cut_top = pt_relative(pcb_sw_pts[6], [+0.5*u, +0.5*u], [pcb_sw_a[6]])
pcb_outline = [
  pcb_cut_bot,
  pt_relative(pcb_sw_pts[2], [+0.5*u, -0.5*u], [pcb_sw_a[2]]),
  pt_relative(pcb_sw_pts[0], [-1.0*u, +0.5*u], [pcb_sw_a[0]]),
  #
#  pt_relative(pcb_sw_pts[17], [+0.5*u,  -0.5*u], [pcb_sw_a[17]]),
#  pt_relative(pcb_sw_pts[17], [-0.5*u,  -0.5*u], [pcb_sw_a[17]]),
#  pt_relative(pcb_sw_pts[22], [+0.5*u,  -0.5*u], [pcb_sw_a[22]]),
#  pt_relative(pcb_sw_pts[22], [-0.5*u,  -0.5*u], [pcb_sw_a[22]]),
#  pt_relative(pcb_sw_pts[27], [+0.5*u,  -0.5*u], [pcb_sw_a[27]]),
#  pt_relative(pcb_sw_pts[27], [-0.5*u,  -0.5*u], [pcb_sw_a[27]]),
#  pt_relative(pcb_sw_pts[32], [+0.5*u,  -0.5*u], [pcb_sw_a[32]]),
  pt_relative(pcb_sw_pts[37], [-0.5*u,  -0.5*u], [pcb_sw_a[37]]),
#  pt_relative(pcb_sw_pts[37], [-0.5*u,  +0.5*u], [pcb_sw_a[37]]),
  pt_relative(pcb_sw_pts[36], [-0.5*u, -0.5*u], [pcb_sw_a[36]]),
  pt_relative(pcb_sw_pts[33], [-0.5*u, +0.5*u], [pcb_sw_a[33]]),
  #
  pt_relative(pcb_sw_pts[28], [+0.5*u,  +0.5*u], [pcb_sw_a[28]]),
  pt_relative(pcb_sw_pts[23], [-0.5*u,  +0.5*u], [pcb_sw_a[23]]),
  pt_relative(pcb_sw_pts[23], [+0.5*u,  +0.5*u], [pcb_sw_a[23]]),
  pt_relative(pcb_sw_pts[18], [-0.5*u,  +0.5*u], [pcb_sw_a[18]]),
  pt_relative(pcb_sw_pts[18], [+0.5*u,  +0.5*u], [pcb_sw_a[18]]),
  pt_relative(pcb_sw_pts[13], [-0.5*u,  +0.5*u], [pcb_sw_a[13]]),
  pt_relative(pcb_sw_pts[13], [+0.5*u,  +0.5*u], [pcb_sw_a[13]]),
  pt_relative(pcb_sw_pts[9],  [-0.5*u,  +0.5*u], [pcb_sw_a[9]]),
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
assert len(sw_pos) == len(pcb_sw_pts)
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
            (-u/2, -u/2),
            (+u/2, -u/2),
            (+u/2, +u/2),
            (-u/2, +u/2),
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
    for h in sw_epts:
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
