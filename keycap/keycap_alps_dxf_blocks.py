#!/usr/bin/env python

from dxfwrite import DXFEngine as dxf
from ndim import *
import os

# {{{ Stems

# Main dimension to be inserted into Matias/ALPS switch.
stem_w = 4.3
stem_h = 5.0

# Nipple to insert into cap.
nipple_w = 3.0
nipple_h = 3.15

# Tactile bump to protrude from top of cap.
ridge_w = 0.5
ridge_h = 0.2
ridge_pos = 4.0
assert ridge_w >= 2*ridge_h

# Tactile bump to protrude from top of cap.
bump_w = 1.4
bump_h = 0.7

# Separation between base of each "leaf" in the tree of stems.
leaf_sep = 0.5 + ridge_h
stem_sep = stem_w + leaf_sep

# Separation between base of leafs, and main branch.
branch_sep = 0.5
total_h = branch_sep + stem_h + nipple_h + bump_h

# Width of snap-off tag holding leaf to tree.
tag_w = 0.4

# Thickness of tree to snap stems off.
tree_w = 3.0

def stem_leaf_pts(left_side=False, bump=False):

    pts = [
           (0.0, stem_sep/2),
           (0.0, tag_w),
           (branch_sep + tag_w, tag_w/2),
           (branch_sep, tag_w*2),
           (branch_sep, stem_w/2),
           (branch_sep + ridge_pos - ridge_w/2, stem_w/2),
           (branch_sep + ridge_pos - ridge_w/2 + ridge_h, stem_w/2 + ridge_h),
           (branch_sep + ridge_pos + ridge_w/2 - ridge_h, stem_w/2 + ridge_h),
           (branch_sep + ridge_pos + ridge_w/2, stem_w/2),
           (branch_sep + stem_h, stem_w/2),
           (branch_sep + stem_h, nipple_w/2),
           (branch_sep + stem_h + nipple_h, nipple_w/2),
          ]
    if bump:
        pts += [ (branch_sep + stem_h + nipple_h + bump_h, bump_w/2) ]
    pts += pts_reflect(pts, [None, 0.0])[::-1]

    pts = pts_shift(pts, [tree_w/2, 0.0])
    return pts_reflect(pts, [0.0, None]) if left_side else pts

# Block definition
stem = dxf.block(name='stem')
stem.add( dxf.polyline(stem_leaf_pts(left_side=False)) )
stem.add( dxf.polyline(stem_leaf_pts(left_side=True)) )

stem_bump = dxf.block(name='stem_bump')
stem_bump.add( dxf.polyline(stem_leaf_pts(left_side=False, bump=True)) )
stem_bump.add( dxf.polyline(stem_leaf_pts(left_side=True,  bump=True)) )

# }}} Stems

# {{{ Cap coords

cap_x = 18.0
cap_y = cap_x
cap_corner_rad = 1.8

cap_10_x = cap_x*1.0
cap_15_x = cap_x*1.5
cap_20_x = cap_x*2.0

# Receiver hole for stem nipple.
recv_x = nipple_w - 0.25
recv_y = 1.75
recv = [
        (+recv_x/2, +recv_y/2),
        (-recv_x/2, +recv_y/2),
        (-recv_x/2, -recv_y/2),
        (+recv_x/2, -recv_y/2),
       ]
recv.append(recv[0])

# }}} Cap coords

# {{{ Caps
cap_10 = dxf.block(name='cap_10')
this_L = -cap_10_x/2
this_R = +cap_10_x/2
this_T = +cap_y/2
this_B = -cap_y/2
cap_10.add( dxf.polyline(recv) )
cap_10.add( dxf.line((this_L, this_B + cap_corner_rad), (this_L*1.0, this_T - cap_corner_rad)) )
cap_10.add( dxf.line((this_L + cap_corner_rad, this_T), (this_R*1.0 - cap_corner_rad, this_T)) )
cap_10.add( dxf.line((this_R, this_B + cap_corner_rad), (this_R*1.0, this_T - cap_corner_rad)) )
cap_10.add( dxf.line((this_R - cap_corner_rad, this_B), (this_L*1.0 + cap_corner_rad, this_B)) )
cap_10.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_T - cap_corner_rad), 90, 180) )
cap_10.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_T - cap_corner_rad), 0, 90) )
cap_10.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_B + cap_corner_rad), 270, 0) )
cap_10.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_B + cap_corner_rad), 180, 270) )

cap_15 = dxf.block(name='cap_15')
this_L = -cap_15_x/2
this_R = +cap_15_x/2
this_T = +cap_y/2
this_B = -cap_y/2
cap_15.add( dxf.polyline(recv) )
cap_15.add( dxf.line((this_L, this_B + cap_corner_rad), (this_L*1.0, this_T - cap_corner_rad)) )
cap_15.add( dxf.line((this_L + cap_corner_rad, this_T), (this_R*1.0 - cap_corner_rad, this_T)) )
cap_15.add( dxf.line((this_R, this_B + cap_corner_rad), (this_R*1.0, this_T - cap_corner_rad)) )
cap_15.add( dxf.line((this_R - cap_corner_rad, this_B), (this_L*1.0 + cap_corner_rad, this_B)) )
cap_15.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_T - cap_corner_rad), 90, 180) )
cap_15.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_T - cap_corner_rad), 0, 90) )
cap_15.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_B + cap_corner_rad), 270, 0) )
cap_15.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_B + cap_corner_rad), 180, 270) )

cap_20 = dxf.block(name='cap_20')
this_L = -cap_20_x/2
this_R = +cap_20_x/2
this_T = +cap_y/2
this_B = -cap_y/2
cap_20.add( dxf.polyline(recv) )
cap_20.add( dxf.line((this_L, this_B + cap_corner_rad), (this_L*1.0, this_T - cap_corner_rad)) )
cap_20.add( dxf.line((this_L + cap_corner_rad, this_T), (this_R*1.0 - cap_corner_rad, this_T)) )
cap_20.add( dxf.line((this_R, this_B + cap_corner_rad), (this_R*1.0, this_T - cap_corner_rad)) )
cap_20.add( dxf.line((this_R - cap_corner_rad, this_B), (this_L*1.0 + cap_corner_rad, this_B)) )
cap_20.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_T - cap_corner_rad), 90, 180) )
cap_20.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_T - cap_corner_rad), 0, 90) )
cap_20.add( dxf.arc(cap_corner_rad, (this_R - cap_corner_rad, this_B + cap_corner_rad), 270, 0) )
cap_20.add( dxf.arc(cap_corner_rad, (this_L + cap_corner_rad, this_B + cap_corner_rad), 180, 270) )

# }}} Caps

# {{{ Cardpack

# Receiver hole for stem.
# Add just a little room to make them easier to insert.
card_recv_x = stem_w + 0.2
card_recv_y = 2.2
card_recv = [
        (+card_recv_x/2, +card_recv_y/2),
        (-card_recv_x/2, +card_recv_y/2),
        (-card_recv_x/2, -card_recv_y/2),
        (+card_recv_x/2, -card_recv_y/2),
       ]
card_recv.append(card_recv[0])

# Block definition
socket = dxf.block(name='socket')
socket.add( dxf.polyline(pts_shift(card_recv, [0.0, +2.0])) )
socket.add( dxf.polyline(pts_shift(card_recv, [0.0, -2.0])) )

# }}} Cardpack

# {{{ Jig

endmill = 3.2

# Block definition
jig_10_outline = [
                  (-cap_10_x/2 + endmill/2, -cap_y/2 + endmill/2),
                  (-cap_10_x/2, -cap_y/2 + endmill/2),
                  (+cap_10_x/2, -cap_y/2 + endmill/2),
                  (+cap_10_x/2 - endmill/2, -cap_y/2 + endmill/2),
                  (+cap_10_x/2 - endmill/2, +cap_y/2 - endmill/2),
                  (+cap_10_x/2, +cap_y/2 - endmill/2),
                  (-cap_10_x/2, +cap_y/2 - endmill/2),
                  (-cap_10_x/2 + endmill/2, +cap_y/2 - endmill/2),
                 ]
jig_10_outline.append(jig_10_outline[0])
jig_10 = dxf.block(name='jig_10')
jig_10.add( dxf.circle(endmill/2) )
jig_10.add( dxf.polyline(jig_10_outline) )

jig_15_outline = [
                  (-cap_15_x/2 + endmill/2, -cap_y/2 + endmill/2),
                  (-cap_15_x/2, -cap_y/2 + endmill/2),
                  (+cap_15_x/2, -cap_y/2 + endmill/2),
                  (+cap_15_x/2 - endmill/2, -cap_y/2 + endmill/2),
                  (+cap_15_x/2 - endmill/2, +cap_y/2 - endmill/2),
                  (+cap_15_x/2, +cap_y/2 - endmill/2),
                  (-cap_15_x/2, +cap_y/2 - endmill/2),
                  (-cap_15_x/2 + endmill/2, +cap_y/2 - endmill/2),
                 ]
jig_15_outline.append(jig_15_outline[0])
jig_15 = dxf.block(name='jig_15')
jig_15.add( dxf.circle(endmill/2) )
jig_15.add( dxf.polyline(jig_15_outline) )

jig_20_outline = [
                  (-cap_20_x/2 + endmill/2, -cap_y/2 + endmill/2),
                  (-cap_20_x/2, -cap_y/2 + endmill/2),
                  (+cap_20_x/2, -cap_y/2 + endmill/2),
                  (+cap_20_x/2 - endmill/2, -cap_y/2 + endmill/2),
                  (+cap_20_x/2 - endmill/2, +cap_y/2 - endmill/2),
                  (+cap_20_x/2, +cap_y/2 - endmill/2),
                  (-cap_20_x/2, +cap_y/2 - endmill/2),
                  (-cap_20_x/2 + endmill/2, +cap_y/2 - endmill/2),
                 ]
jig_20_outline.append(jig_20_outline[0])
jig_20 = dxf.block(name='jig_20')
jig_20.add( dxf.circle(endmill/2) )
jig_20.add( dxf.polyline(jig_20_outline) )

# }}} Jig

