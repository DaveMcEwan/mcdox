#!/usr/bin/env python

from dxfwrite import DXFEngine as dxf
from ndim import *
import os

# {{{ Stems

# Main dimension to be inserted into Matias/ALPS switch.
stem_w = 4.3
stem_h = 5.0

# Nipple to insert into cap.
nipple_w = 2.8
nipple_h = 3.0

# Tactile bump to protrude from top of cap.
ridge_w = 0.3
ridge_h = 0.1
ridge_pos = 4.3
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

tree_w = 3.0

try:
    os.makedirs('dxf')
except:
    pass

# Thickness for stem cuts *must* be 2mm.
filename = 'dxf/alps_stems_2mm.dxf'
d = dxf.drawing(filename)

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
d.blocks.add(stem)

stem_bump = dxf.block(name='stem_bump')
stem_bump.add( dxf.polyline(stem_leaf_pts(left_side=False, bump=True)) )
stem_bump.add( dxf.polyline(stem_leaf_pts(left_side=True,  bump=True)) )
d.blocks.add(stem_bump)

# Tree
tree_len = 20
bump_len = 1

x = total_h + tree_w/2

for i in range(tree_len):
    y = i * stem_sep + stem_sep/2
    # insert2() needs the block definition object as parameter 'blockdef'.
    # See http://packages.python.org/dxfwrite/entities/insert2.html
    # Fill attribtes by creating a dict(), key is the 'tag' name of the
    # attribute.
    insert = dxf.insert2(blockdef=stem, insert=(x, y))

    insert_bump = dxf.insert2(blockdef=stem_bump, insert=(x, y))

    d.add(insert_bump) if i < bump_len else d.add(insert)
d.add( dxf.line((x - tree_w/2, 0.0), (x + tree_w/2, 0.0)) )
d.add( dxf.line((x - tree_w/2, y + stem_sep/2), (x + tree_w/2, y + stem_sep/2)) )

d.save()

# }}} Stems

# {{{ Caps

cap_x = 18.0
cap_y = cap_x
cap_corner_rad = 1.8

cap_10_x = cap_x*1.0
cap_15_x = cap_x*1.5
cap_20_x = cap_x*2.0

# Thickness may be changed as long as nipple_h is changed accordingly.
filename = 'dxf/alps_caps_3mm.dxf'
d = dxf.drawing(filename)

# Receiver hole for stem nipple.
recv_x = nipple_w - 0.1
recv_y = 2.0
recv = [
        (+recv_x/2, +recv_y/2),
        (-recv_x/2, +recv_y/2),
        (-recv_x/2, -recv_y/2),
        (+recv_x/2, -recv_y/2),
       ]
recv.append(recv[0])

# Block definition
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
d.blocks.add(cap_10)

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
d.blocks.add(cap_15)

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
d.blocks.add(cap_20)

rows_10 = 8
cols_10 = 4
rows_15 = 2
cols_15 = 3
rows_20 = 1
cols_20 = 2
cap_sep = 0.8

y = cap_y/2
for r in range(rows_15):
    for c in range(cols_15):
        x = c * (cap_15_x + cap_sep) + cap_15_x/2
        d.add(dxf.insert2(blockdef=cap_15, insert=(x, y)))
    y += cap_y + cap_sep

for r in range(rows_10):
    for c in range(cols_10):
        x = c * (cap_10_x + cap_sep) + cap_10_x/2
        d.add(dxf.insert2(blockdef=cap_10, insert=(x, y)))
    y += cap_y + cap_sep

for r in range(rows_20):
    for c in range(cols_20):
        x = c * (cap_20_x + cap_sep) + cap_20_x/2
        d.add(dxf.insert2(blockdef=cap_20, insert=(x, y)))
    y += cap_y + cap_sep

d.save()

# }}} Caps

