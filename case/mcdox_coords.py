#!/usr/bin/env python

import sys
from math import *
from ndim import *

# Naming convention:
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
# M3 module

# {{{ constants

# M3 bolt hole radius.
M3_r = 3.3/2

# Unit width of one switch, standardised at 19mm.
u = 19.0

# Ergonomic angle of rotation for whole hand.
hand_a = radians(-13)

# Ergonomic angle of rotation for thumb cluster, in addition to hand_a.
thumb_a = radians(-25)

# Separation of hand circles.
hand_sep = 29.0

# Case outline border width.
border = 5.0

# Radius of wrist rests.
wrest_r = 93.0

# Center of entire keyboard.
center = (2*wrest_r + hand_sep/2, wrest_r)

# Width of a CherryMX switch.
cherrymx_w = 13.7

# }}} constants

# {{{ PCB switch coords

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


pcb_sw_epts = pcb_sw_thumb_epts + pcb_sw_finger_epts
pcb_sw_pts = [(h[0], h[1]) for h in pcb_sw_epts]

# }}} PCB switch coords

# {{{ case layer enable

case_layers = [
    # Minimalist top of kbd with builtin ALPS keycaps.
    # 1.5mm acrylic.
    # v2 always uses CherryMX so unnecessary.
#    'top2',

    # Minimalist top of kbd.
    # 1.5mm aluminium, acrylic, OR stainless steel.
    'top1',

    # Spacer between mnt and top.
    # 4mm acrylic.
    # Snug fit around ctrlmnt bolt heads, and battery pack keep it solid.
    'top0',

    # Mount plate for switches and controller board.
    # 1.5mm aluminium, acrylic, OR stainless steel.
    # For a barebones build you can use just this layer in stainless steel with
    # M3 10mm standoffs.
    'mnt_cherrymx',
#    'mnt_alps',

    # Spacer for depth of switch pins below mnt, closed end.
    # 4mm acrylic.
    # v2 is thinner and requires both spacer layers around USB to be open.
#    'base2',

    # Spacer for depth of switch pins below mnt, open end.
    # 4mm acrylic.
    'base1',

    # Bottom of kbd.
    # 1.5mm aluminium, acrylic, OR stainless steel.
    'base0',

    # Dimension test
#    'dimtst',
]

# }}} case layer enable

# {{{ case switch coords

n_sw = len(pcb_sw_epts)

# Switch points at opposite corners are used to find the center of the hand.
# Opposite corners are top-left to bottom-right.
# hand_pt: Center between opposite corners.
sw_ptTL = c0[0][:2]
sw_ptBR = pcb_sw_thumb_pts[2]
hand_pt = pt_between_pts(sw_ptTL, sw_ptBR)

# Shift everything onto 400x200 page manually.
page_cR = -0.5
page_cT = -2.0

# Real coordinates of switches.
sw_ptsL = pts_shift(pcb_sw_pts, [-hand_pt[0] + wrest_r, wrest_r])
sw_ptsL = pts_rotate(sw_ptsL, angle=[hand_a], center=(wrest_r, wrest_r))
sw_ptsL = pts_shift(sw_ptsL, [page_cR, page_cT])
sw_ptsR = pts_reflect(sw_ptsL, [center[0], None])
sw_pts = sw_ptsL + sw_ptsR

sw_aL = [h[2] + hand_a for h in pcb_sw_epts]
sw_aR = [-a for a in sw_aL]
sw_a = sw_aL + sw_aR

sw_eptsL = [(sw_ptsL[i][0], sw_ptsL[i][1], sw_aL[i]) for i in range(n_sw)]
sw_eptsR = [(sw_ptsR[i][0], sw_ptsR[i][1], sw_aR[i]) for i in range(n_sw)]
sw_epts = sw_eptsL + sw_eptsR

# }}} case switch coords

# {{{ PCB outline

pcb_cut_bot = pt_relative(pcb_sw_pts[4], [+0.5*u, +0.5*u], [sw_aL[4]])
pcb_cut_top = pt_relative(pcb_sw_pts[6], [+0.5*u, +0.5*u], [sw_aL[6]])
pcb_outline = [
  pcb_cut_bot,
  pt_relative(pcb_sw_pts[2], [+0.5*u, -0.5*u], [sw_aL[2]]),
  pt_relative(pcb_sw_pts[0], [-1.0*u, +0.5*u], [sw_aL[0]]),
  #
#  pt_relative(pcb_sw_pts[17], [+0.5*u,  -0.5*u], [sw_aL[17]]),
#  pt_relative(pcb_sw_pts[17], [-0.5*u,  -0.5*u], [sw_aL[17]]),
#  pt_relative(pcb_sw_pts[22], [+0.5*u,  -0.5*u], [sw_aL[22]]),
#  pt_relative(pcb_sw_pts[22], [-0.5*u,  -0.5*u], [sw_aL[22]]),
#  pt_relative(pcb_sw_pts[27], [+0.5*u,  -0.5*u], [sw_aL[27]]),
#  pt_relative(pcb_sw_pts[27], [-0.5*u,  -0.5*u], [sw_aL[27]]),
#  pt_relative(pcb_sw_pts[32], [+0.5*u,  -0.5*u], [sw_aL[32]]),
  pt_relative(pcb_sw_pts[37], [-0.5*u,  -0.5*u], [sw_aL[37]]),
#  pt_relative(pcb_sw_pts[37], [-0.5*u,  +0.5*u], [sw_aL[37]]),
  pt_relative(pcb_sw_pts[36], [-0.5*u, -0.5*u], [sw_aL[36]]),
  pt_relative(pcb_sw_pts[33], [-0.5*u, +0.5*u], [sw_aL[33]]),
  #
  pt_relative(pcb_sw_pts[28], [+0.5*u,  +0.5*u], [sw_aL[28]]),
  pt_relative(pcb_sw_pts[23], [-0.5*u,  +0.5*u], [sw_aL[23]]),
  pt_relative(pcb_sw_pts[23], [+0.5*u,  +0.5*u], [sw_aL[23]]),
  pt_relative(pcb_sw_pts[18], [-0.5*u,  +0.5*u], [sw_aL[18]]),
  pt_relative(pcb_sw_pts[18], [+0.5*u,  +0.5*u], [sw_aL[18]]),
  pt_relative(pcb_sw_pts[13], [-0.5*u,  +0.5*u], [sw_aL[13]]),
  pt_relative(pcb_sw_pts[13], [+0.5*u,  +0.5*u], [sw_aL[13]]),
  pt_relative(pcb_sw_pts[9],  [-0.5*u,  +0.5*u], [sw_aL[9]]),
  pcb_cut_top,
]
pcb_outline.append(pcb_outline[0])

pcb_header_pt = pt_between_pts(pcb_cut_bot, pcb_cut_top, 0.5)
pcb_header_dir = dir_between_pts(pcb_cut_top, pcb_cut_bot)[0]
pcb_header_pt = pt_relative(pcb_header_pt, [-(3*0.8+3.0), 0.0], [pcb_header_dir + pi/2])

# {{{ (column, row) map of switch positions in the matrix.
sw_pos = [
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
assert len(sw_pos) == n_sw
# }}} sw_pos

# }}} PCB outline

# {{{ case outline coords and arcs

# Top edge has arcs at corners.
topedge_arc_ptL = pt_relative(sw_pts[33], [-0.75*u, +0.5*u], [sw_a[33]])
topedge_arc_ptR = pt_reflect(topedge_arc_ptL, [center[0], None])
topedge_arcL = {
    'type':         'arc',
    'center':       topedge_arc_ptL,
    'radius':       border,
    'startangle':   90,
    'endangle':     180 + degrees(hand_a)
}
topedge_arcR = {
    'type':         'arc',
    'center':       topedge_arc_ptR,
    'radius':       border,
    'startangle':   -degrees(hand_a),
    'endangle':     90
}

topedge_T = topedge_arc_ptL[1] + border

topedge_arc_ptTL = (topedge_arc_ptL[0], topedge_T)
topedge_arc_ptTR = (topedge_arc_ptR[0], topedge_T)
topedge_arc_ptBL = pt_relative(topedge_arc_ptL, [+border, 0.0], [radians(180) + hand_a])
topedge_arc_ptBR = pt_relative(topedge_arc_ptR, [+border, 0.0], [-hand_a])

# Points at the boundaries across the case.
far_ptL = pt_relative(sw_pts[36], [-0.75*u-border, -0.5*u-border], [sw_a[36]])
far_ptR = pt_reflect(far_ptL, [center[0], None])

# Wrist rests are large arcs.
wrest_inner_pt = pt_relative(sw_pts[2], [+0.5*u+border, 0.0], [sw_a[2]])
wrest_ptL = (far_ptL[0] + cos(hand_a)*wrest_r, far_ptL[1] + sin(hand_a)*wrest_r)
wrest_ptR = pt_reflect(wrest_ptL, [center[0], None])
wrest_aLs = pi + hand_a
wrest_aLe = dir_between_pts(wrest_ptL, wrest_inner_pt)[0]
wrest_aRs = pi - wrest_aLe
wrest_aRe = -hand_a
wrest_L = {
    'type':         'arc',
    'center':       wrest_ptL,
    'radius':       wrest_r,
    'startangle':   degrees(wrest_aLs),
    'endangle':     degrees(wrest_aLe),
}
wrest_R = {
    'type':         'arc',
    'center':       wrest_ptR,
    'radius':       wrest_r,
    'startangle':   degrees(wrest_aRs),
    'endangle':     degrees(wrest_aRe),
}

# Bottom arc in the middle between the two wrist rests.
botarc_m = tan(wrest_aLe)
botarc_c = wrest_ptL[1] - botarc_m*wrest_ptL[0] # c = y - mx
botarc_pt = (center[0], botarc_m*center[0] + botarc_c)
botarc_r = distance_between_pts(wrest_ptL, botarc_pt) - wrest_r
botarc = {
    'type':         'arc',
    'center':       botarc_pt,
    'radius':       botarc_r,
    'startangle':   degrees(wrest_aRs) - 180,
    'endangle':     degrees(wrest_aLe) - 180,
}

# }}} case outline coords and arcs

# {{{ handbrd cutout coords for base layers

handbrd_co = [
    pt_relative(sw_pts[4],  [+(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[4] ] ),
    pt_relative(sw_pts[2],  [+(0.5*u+0.5), -(0.5*u+0.5)], [sw_a[2] ] ),
    pt_relative(sw_pts[0],  [-(1.0*u+0.5), +(0.5*u+0.5)], [sw_a[0] ] ),
    pt_relative(sw_pts[37], [-(0.5*u+0.5), -(0.5*u+0.5)], [sw_a[37]] ),
    pt_relative(sw_pts[36], [-(0.5*u+0.5), -(0.5*u+0.5)], [sw_a[36]] ),
    pt_relative(sw_pts[33], [-(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[33]] ),
    pt_relative(sw_pts[28], [+(0.5*u-0.5), +(0.5*u+0.5)], [sw_a[28]] ),
    pt_relative(sw_pts[23], [-(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[23]] ),
    pt_relative(sw_pts[23], [+(0.5*u-0.5), +(0.5*u+0.5)], [sw_a[23]] ),
    pt_relative(sw_pts[18], [-(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[18]] ),
    pt_relative(sw_pts[18], [+(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[18]] ),
    pt_relative(sw_pts[13], [-(0.5*u-0.5), +(0.5*u+0.5)], [sw_a[13]] ),
    pt_relative(sw_pts[13], [+(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[13]] ),
    pt_relative(sw_pts[9],  [-(0.5*u-0.5), +(0.5*u+0.5)], [sw_a[9] ] ),
    pt_relative(sw_pts[6],  [+(0.5*u+0.5), +(0.5*u+0.5)], [sw_a[6] ] ),
]

# }}} handbrd cutout coords for base layers

# {{{ ctrlbrd cutout coords for base layers

ctrlbrd_w = 50.0
ctrlbrd_h = 50.0

ctrlmnt_r = 3.5 # Radius of mounting holes on controller board.

ctrlbrd_co_c = 1.0 # Space/offset between ctrlbrd and inner base layers.

ctrlbrd_coL = center[0] - ctrlbrd_w/2 - ctrlbrd_co_c
ctrlbrd_coR = center[0] + ctrlbrd_w/2 + ctrlbrd_co_c
ctrlbrd_coB = handbrd_co[-1][1]
ctrlbrd_coT = topedge_T - border

ctrlbrd_hoT = ctrlbrd_coT - ctrlbrd_co_c - ctrlmnt_r
ctrlbrd_hoL = center[0] - (ctrlbrd_w/2) + ctrlmnt_r
ctrlbrd_hoR = center[0] + (ctrlbrd_w/2) - ctrlmnt_r
ctrlbrd_hoB = ctrlbrd_coT - ctrlbrd_h - ctrlbrd_co_c + ctrlmnt_r
ctrlbrd_ho = [
    (ctrlbrd_hoL, ctrlbrd_hoB),
    (ctrlbrd_hoR, ctrlbrd_hoB),
    (ctrlbrd_hoL, ctrlbrd_hoT),
    (ctrlbrd_hoR, ctrlbrd_hoT),
]

ctrlbrd_co_arc_r = ctrlmnt_r + ctrlbrd_co_c
ctrlbrd_co_arcL = {
    'type':         'arc',
    'center':       (ctrlbrd_hoL, ctrlbrd_hoT),
    'radius':       ctrlbrd_co_arc_r,
    'startangle':   90,
    'endangle':     180
}
ctrlbrd_co_arcR = {
    'type':         'arc',
    'center':       (ctrlbrd_hoR, ctrlbrd_hoT),
    'radius':       ctrlbrd_co_arc_r,
    'startangle':   0,
    'endangle':     90
}

# }}} ctrlbrd cutout coords for base layers

# {{{ devbrd cutout coords for base0 (deprecated)

devbrd_co_w = 24.0 # Just enough to expose the teensy.
devbrd_co_h = 50.0
devbrd_coL = center[0] - devbrd_co_w/2
devbrd_coR = center[0] + devbrd_co_w/2
devbrd_coB = topedge_T - devbrd_co_h - border
devbrd_co = [
    (devbrd_coL, topedge_T),
    (devbrd_coL, devbrd_coB),
    (devbrd_coR, devbrd_coB),
    (devbrd_coR, topedge_T),
]

# }}} devbrd cutout coords for base0 (deprecated)

# {{{ ctrlmnt cutout coords for mnt layer

ctrlmnt_T = ctrlbrd_coT - ctrlbrd_co_c
ctrlmnt_L = center[0] - ctrlbrd_w/2
ctrlmnt_R = center[0] + ctrlbrd_w/2

ctrlmnt_arcTL = {
    'type':         'arc',
    'center':       (ctrlbrd_hoL, ctrlbrd_hoT),
    'radius':       ctrlmnt_r,
    'startangle':   -90,
    'endangle':     0
}
ctrlmnt_arcTR = {
    'type':         'arc',
    'center':       (ctrlbrd_hoR, ctrlbrd_hoT),
    'radius':       ctrlmnt_r,
    'startangle':   180,
    'endangle':     -90
}
ctrlmnt_arcBL = {
    'type':         'arc',
    'center':       (ctrlbrd_hoL, ctrlbrd_hoB),
    'radius':       ctrlmnt_r,
    'startangle':   -90,
    'endangle':     90
}
ctrlmnt_arcBR = {
    'type':         'arc',
    'center':       (ctrlbrd_hoR, ctrlbrd_hoB),
    'radius':       ctrlmnt_r,
    'startangle':   90,
    'endangle':     270
}

# Intermediate cutout coords for middle space in mnt.
midmnt_coL = [
  (ctrlmnt_L-ctrlbrd_co_c,ctrlbrd_hoB-ctrlmnt_r),
  pt_relative(sw_pts[7], [+0.5*cherrymx_w +border, +0.5*cherrymx_w +border], [hand_a]),
  pt_relative(sw_pts[8], [+0.5*cherrymx_w +border, +0.5*cherrymx_w +border], [hand_a]),
  pt_relative(sw_pts[5], [-0.5*cherrymx_w -border, +0.5*cherrymx_w +border], [hand_a + thumb_a]),
  pt_relative(sw_pts[5], [+0.5*cherrymx_w,         +0.5*cherrymx_w +border], [hand_a + thumb_a]),
  pt_relative(sw_pts[4], [-0.5*cherrymx_w -border, +0.5*cherrymx_w +border], [hand_a + thumb_a]),
  pt_relative(sw_pts[4], [+0.5*cherrymx_w +border, +0.5*cherrymx_w +border], [hand_a + thumb_a]),
]
midmnt_coR = pts_reflect(midmnt_coL, [center[0], None])
midmnt_coR.reverse()
midmnt_co = midmnt_coL + midmnt_coR

ctrlmnt = [
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_L+ctrlmnt_r,ctrlbrd_hoB+ctrlmnt_r),
                                 (ctrlmnt_L-ctrlbrd_co_c,ctrlbrd_hoB+ctrlmnt_r),
                                 (ctrlmnt_L-ctrlbrd_co_c,ctrlbrd_hoT-ctrlmnt_r),
                                 (ctrlmnt_L+ctrlmnt_r,ctrlbrd_hoT-ctrlmnt_r),
                                ]},
    ctrlmnt_arcTL,
    {'type': 'polyline', 'pts': [
                                 (ctrlbrd_hoL+ctrlmnt_r,ctrlmnt_T-ctrlmnt_r),
                                 (ctrlbrd_hoL+ctrlmnt_r,ctrlmnt_T+ctrlbrd_co_c),
                                 (ctrlbrd_hoR-ctrlmnt_r,ctrlmnt_T+ctrlbrd_co_c),
                                 (ctrlbrd_hoR-ctrlmnt_r,ctrlmnt_T-ctrlmnt_r),
                                ]},
    ctrlmnt_arcTR,
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_R-ctrlmnt_r,ctrlbrd_hoT-ctrlmnt_r),
                                 (ctrlmnt_R+ctrlbrd_co_c,ctrlbrd_hoT-ctrlmnt_r),
                                 (ctrlmnt_R+ctrlbrd_co_c,ctrlbrd_hoB+ctrlmnt_r),
                                 (ctrlmnt_R-ctrlmnt_r,ctrlbrd_hoB+ctrlmnt_r),
                                ]},
    ctrlmnt_arcBR,
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_R+ctrlbrd_co_c,ctrlbrd_hoB-ctrlmnt_r),
                                 (ctrlmnt_R-ctrlmnt_r,ctrlbrd_hoB-ctrlmnt_r),
                                ]},
    {'type': 'polyline', 'pts': midmnt_co},
    {'type': 'polyline', 'pts': [
                                 (ctrlmnt_L+ctrlmnt_r,ctrlbrd_hoB-ctrlmnt_r),
                                 (ctrlmnt_L-ctrlbrd_co_c,ctrlbrd_hoB-ctrlmnt_r),
                                ]},
    ctrlmnt_arcBL,
]
# }}} ctrlmnt cutout coords for mnt layer

# {{{ case fixing holes

case_hoL = [
#    pt_relative(sw_pts[4], [+1.0*u, -7.0], [sw_a[4]]),
    (sw_pts[6][0], topedge_T - border - 2.0),
    (sw_pts[28][0], topedge_T - border - 2.0),
    pt_relative(far_ptL, [border + 2.0, -border], [hand_a]),
    pt_relative(wrest_ptL, [5.0, -wrest_r + border + 1.0], [-hand_a]),
    pt_relative(wrest_ptL, [9.0, -wrest_r + border + 2.0], [5*hand_a]),
]

case_hoR = pts_reflect(case_hoL, [center[0], None])
case_hoR.reverse()

case_ho = case_hoL + case_hoR

# }}} case fixing holes

# {{{ switch/keycap cutouts in top layers

fingers_coL = [
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
  pt_relative(sw_pts[8],  [-0.75*u, -0.5*u], [sw_a[8]] ),
  pt_relative(sw_pts[8],  [+0.75*u, -0.5*u], [sw_a[8]] ),
  pt_relative(sw_pts[6],  [+0.5*u,  +0.5*u], [sw_a[6]] ),
  pt_relative(sw_pts[9],  [-0.5*u,  +0.5*u], [sw_a[9]] ),
  pt_relative(sw_pts[13], [+0.5*u,  +0.5*u], [sw_a[13]]),
  pt_relative(sw_pts[13], [-0.5*u,  +0.5*u], [sw_a[13]]),
  pt_relative(sw_pts[18], [+0.5*u,  +0.5*u], [sw_a[18]]),
  pt_relative(sw_pts[18], [-0.5*u,  +0.5*u], [sw_a[18]]),
  pt_relative(sw_pts[23], [+0.5*u,  +0.5*u], [sw_a[23]]),
  pt_relative(sw_pts[23], [-0.5*u,  +0.5*u], [sw_a[23]]),
  pt_relative(sw_pts[28], [+0.5*u,  +0.5*u], [sw_a[28]]),
]
fingers_coL.append(fingers_coL[0])
fingers_coR = pts_reflect(fingers_coL, [center[0], None])

thumbs_coL = [
  pt_relative(sw_pts[0], [-0.75*u, +0.5*u], [sw_a[0]]),
  pt_relative(sw_pts[1], [-0.75*u, -0.5*u], [sw_a[1]]),
  pt_relative(sw_pts[2], [-0.5*u,  -0.5*u], [sw_a[2]]),
  pt_relative(sw_pts[2], [+0.5*u,  -0.5*u], [sw_a[2]]),
  pt_relative(sw_pts[4], [+0.5*u,  +0.5*u], [sw_a[4]]),
  pt_relative(sw_pts[4], [-0.5*u,  +0.5*u], [sw_a[4]]),
  pt_relative(sw_pts[5], [+0.5*u,  +0.5*u], [sw_a[5]]),
  pt_relative(sw_pts[5], [-0.5*u,  +0.5*u], [sw_a[5]]),
  pt_relative(sw_pts[1], [+0.75*u, +0.5*u], [sw_a[1]]),
  pt_relative(sw_pts[0], [+0.75*u, +0.5*u], [sw_a[0]]),
]
thumbs_coL.append(thumbs_coL[0])
thumbs_coR = pts_reflect(thumbs_coL, [center[0], None])

top_co = [
    {'type': 'polyline', 'pts': fingers_coL},
    {'type': 'polyline', 'pts': fingers_coR},
    {'type': 'polyline', 'pts': thumbs_coL},
    {'type': 'polyline', 'pts': thumbs_coR},
]

# }}} switch/keycap cutouts in top layers

# {{{ weight saving cutouts

wsabove_coL = [
    pt_relative(handbrd_co[-1], [0.0, border], [0.0]),
    pt_relative(handbrd_co[-2], [border, border], [hand_a]),
    pt_relative(handbrd_co[-3], [border, border], [hand_a]),
    pt_relative(handbrd_co[-4], [border, border], [hand_a]),
    pt_relative(handbrd_co[-5], [border, border], [hand_a]),
    pt_relative(handbrd_co[-6], [0.0, border], [hand_a]),
    pt_shift(case_hoL[0], [0.0, -border - M3_r]),
]
wsabove_coL.append((wsabove_coL[0][0], wsabove_coL[-1][1]))
wsabove_coL.append(wsabove_coL[0])
wsabove_coR = pts_reflect(wsabove_coL, [center[0], None])
wsabove_coR.reverse()

wsbelow_arc_r = wrest_r - 3*border

tmp0_pt = pt_relative(handbrd_co[2], [-border, -border], [-hand_a])
tmp1_pt = pt_relative(handbrd_co[3], [-border, -1.5*border], [-hand_a])
tmp2_pt = pt_relative(handbrd_co[1], [-2*border, -border], [hand_a])
tmp1_a = dir_between_pts(wrest_ptL, tmp1_pt)[0]
tmp2_a = dir_between_pts(wrest_ptL, tmp2_pt)[0]

ai = arcinfo_center_angles(center=wrest_ptL,
                          radius=wsbelow_arc_r,
                          start_a=[tmp1_a],
                          end_a=[tmp2_a],
                          direction=True)
wsbelow_arcL = {
    'type':         'arc',
    'center':       wrest_ptL,
    'radius':       wsbelow_arc_r,
    'startangle':   degrees(tmp1_a),
    'endangle':     degrees(tmp2_a),
}
wsbelow_arcR = {
    'type':         'arc',
    'center':       wrest_ptR,
    'radius':       wsbelow_arc_r,
    'startangle':   180 - degrees(tmp2_a),
    'endangle':     180 - degrees(tmp1_a),
}

wsbelow_coL = [
    ai['start_pt'],
    tmp0_pt,
    ai['end_pt'],
]
wsbelow_coR = pts_reflect(wsbelow_coL, [center[0], None])
wsbelow_coR.reverse()

ws_co = [
    {'type': 'polyline', 'pts': wsabove_coL},
    {'type': 'polyline', 'pts': wsabove_coR},
    {'type': 'polyline', 'pts': wsbelow_coL},
    wsbelow_arcL,
    {'type': 'polyline', 'pts': wsbelow_coR},
    wsbelow_arcR,
]

# }}} weight saving cutouts

# {{{ case layer outlines

case_outline = [
    {'type': 'polyline', 'pts': [far_ptL, topedge_arc_ptBL]},
    topedge_arcL,
    {'type': 'polyline', 'pts': [topedge_arc_ptTL, topedge_arc_ptTR]},
    topedge_arcR,
    {'type': 'polyline', 'pts': [topedge_arc_ptBR, far_ptR]},
    wrest_R,
    botarc,
    wrest_L,
]

# Alternative base0 outline with cutout for devbrd.
base0_outline = [
    {'type': 'polyline', 'pts': [far_ptL, topedge_arc_ptBL]},
    topedge_arcL,
    {'type': 'polyline', 'pts': [topedge_arc_ptTL] + devbrd_co + [topedge_arc_ptTR]},
    topedge_arcR,
    {'type': 'polyline', 'pts': [topedge_arc_ptBR, far_ptR]},
    wrest_R,
    botarc,
    wrest_L,
]


base1_co_topL = [
    (devbrd_coL, topedge_T),
    (devbrd_coL, ctrlbrd_coT),
    (ctrlbrd_coL + ctrlbrd_co_arc_r, ctrlbrd_coT),
]
base1_co_topR = pts_reflect(base1_co_topL, [center[0], None])
base1_co_topR.reverse()

base1_co_mainL = [
    (ctrlbrd_coL, ctrlbrd_coT - ctrlbrd_co_arc_r),
    (ctrlbrd_coL, ctrlbrd_coB),
] + handbrd_co[::-1]
base1_co_mainR = pts_reflect(base1_co_mainL, [center[0], None])
base1_co_mainR.reverse()
base1_co_main = base1_co_mainL + base1_co_mainR

base1_outline = [
    {'type': 'polyline', 'pts': [far_ptL, topedge_arc_ptBL]},
    topedge_arcL,
    {'type': 'polyline', 'pts': [topedge_arc_ptTL] + base1_co_topL},
    ctrlbrd_co_arcL,
    {'type': 'polyline', 'pts': base1_co_main},
    ctrlbrd_co_arcR,
    {'type': 'polyline', 'pts': base1_co_topR + [topedge_arc_ptTR]},
    topedge_arcR,
    {'type': 'polyline', 'pts': [topedge_arc_ptBR, far_ptR]},
    wrest_R,
    botarc,
    wrest_L,
]


base2_coL = [
    (ctrlbrd_coL, ctrlbrd_coT - ctrlbrd_co_arc_r),
    (ctrlbrd_coL, ctrlbrd_coB),
] + handbrd_co[::-1]
base2_coR = pts_reflect(base2_coL, [center[0], None])
base2_coR.reverse()
base2_co = base2_coL + base2_coR
base2_outline = [
    {'type': 'polyline', 'pts': [
                                 (ctrlbrd_coR - ctrlbrd_co_arc_r, ctrlbrd_coT),
                                 (ctrlbrd_coL + ctrlbrd_co_arc_r, ctrlbrd_coT),
                                ]},
    ctrlbrd_co_arcL,
    {'type': 'polyline', 'pts': base2_co},
    ctrlbrd_co_arcR,
]

# }}} case layer outlines


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
        width = cherrymx_w if 'width' not in args else args['width']
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

# {{{ keycap labels

# These labels are only used for etching if you choose to cut the TOP2 layer

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

keycap_labels_qwerty = labelsL_qwerty + labelsR_qwerty
keycap_labels_dvorak = labelsL_dvorak + labelsR_dvorak

keycap_labels = keycap_labels_dvorak

# }}} keycap labels

if __name__ == '__main__':
    out = []
    out += ['Switch holes:']
    for h in sw_epts:
        out += ['\t(%0.2f, %0.2f) rotate=%d' % (h[0], h[1], degrees(h[2]))]
    out += ['Fixing holes:']
    for h in fix_holes:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['PCB holes:']
    for h in ctrlbrd_ho:
        out += ['\t(%0.2f, %0.2f)' % (h[0], h[1])]
    out += ['Outer:']
    out += ['\theight=%0.2f' % topedge_T]
    out += ['\twidth=%0.2f' % (wrest_ptR[0] + wrest_r)]
    print('\n'.join(out))
