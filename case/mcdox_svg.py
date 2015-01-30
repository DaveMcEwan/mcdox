#!/usr/bin/env python

import svgwrite as svg
polyline = svg.shapes.Polyline
circle = svg.shapes.Circle
from mcdox_coords import *

from copy import *
import os
import shutil
try:
    os.makedirs('svg')
except:
    pass

# In SVG path units are always "SVG user units" (px, 90dpi), not mm.
# Inkscape internally converts to mm.
# Therefore scale by 90/25.4 = 3.54
mm_scale = 90/25.4

# Standard line style for cutting.
# Set to 0.3mm to be the same as most laser cutters.
# Cut = Red
# Score/vector etch = Blue
# Raster etch = Black
style_cut = 'fill:none;stroke:#ff0000;stroke-opacity:1;stroke-width:%f' % (0.3*mm_scale)
style_score = 'fill:none;stroke:#0000ff;stroke-opacity:1;stroke-width:%f' % (0.3*mm_scale)

# Define page size which is required for the coordinate calculations since SVG
# specifies that top left is the origin.
page_h = 200
page_w = 400

# Coordinate calculation from mm to SVG user points.
def svg_pt(pt=(0.0, 0.0), page_h=page_h):
    return pt_scale(pt_change_axis(pt, [False, True], [0.0, float(page_h)]), mm_scale)
def svg_pts(pts=[], page_h=page_h):
    return [svg_pt(pt, float(page_h)) for pt in pts]

def svg_sw_pts(swtype='alps',
               center=(0.0, 0.0),
               rotation=0.0,
               args={}):
    pts_at_origin = sw_outline_pts(swtype, args)
    pts_at_origin = pts_rotate(pts_at_origin, [rotation])
    pts_at_origin = pts_scale(pts_at_origin, mm_scale)
    pts = pts_shift(pts_at_origin, list(pt_scale(center, mm_scale)))
    return pts_change_axis(pts, [False, True], [0.0, page_h*mm_scale])

# Inkscape 0.48 does not support symbols (the SVG equivilant to DXF blocks) so
# they are all converted to individual paths.
# TODO: Support for <symbol> and <use> coming in 0.91 so make use of them.


def svg_path_add(drawing, path={}):
    for p in path:
        if 'type' not in p: continue # TODO: maybe warn here?

        t = p['type']
        if t == 'polyline':
            e = polyline(svg_pts(p['pts']), style=style_cut)
        elif t == 'arc':
            a = arcinfo_center_angles(center=p['center'],
                                      radius=p['radius'],
                                      start_a=[radians(p['startangle'])],
                                      end_a=[radians(p['endangle'])])
            e = svg.path.Path('M%f,%f' % svg_pt(a['start_pt']),
                              style=style_cut)
            e.push_arc(target=svg_pt(a['end_pt']),
                       r=a['radius']*mm_scale,
                       rotation=0.0,
                       large_arc=a['big'][0],
                       angle_dir='+' if a['diff_a'] < 0.0 else '-',
                       absolute=True)
        drawing.add(e)

def svg_blk_path_add(drawing, path={}, center=(0.0, 0.0), rotation=0.0):
    for p in path:
        if 'type' not in p: continue # TODO: maybe warn here?

        t = p['type']
        if t == 'polyline':
            pts = p['pts']
            pts = pts_shift(pts, list(center))
            pts = pts_rotate(pts, [rotation], center)
            e = polyline(svg_pts(pts), style=style_cut)
        elif t == 'arc':
            a = arcinfo_center_angles(center=pt_rotate(p['center'], [rotation]),
                                      radius=p['radius'],
                                      start_a=[radians(p['startangle']) + rotation],
                                      end_a=[radians(p['endangle']) + rotation])
            e = svg.path.Path('M%f,%f' % svg_pt(pt_shift(a['start_pt'], list(center))),
                              style=style_cut)
            e.push_arc(target=svg_pt(pt_shift(a['end_pt'], list(center))),
                       r=a['radius']*mm_scale,
                       rotation=0.0,
                       large_arc=a['big'][0],
                       angle_dir='+' if a['diff_a'] < 0.0 else '-',
                       absolute=True)
        drawing.add(e)


####d = svg.Drawing(filename='svg/mcdox_all.svg', size=('%dmm'%page_w, '%dmm'%page_h))

# {{{ MNT
####d.add_layer('MNT')
d_single = svg.Drawing(filename='svg/mcdox_mnt_3mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for number, (x, y, r) in enumerate(sw_holes):
    d_single.add(polyline(svg_sw_pts(swtype='alps',
                                     center=(x, y),
                                     rotation=r),
                                     style=style_cut))
####    insert.layer = 'MNT'
####    d.add(insert)

for (x, y) in fix_holes + lollybrd_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'MNT'
####    d.add(insert)

####svg_path_add(d, mnt_outline_path, {'layer': 'MNT'})
svg_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of MNT

# {{{ TOP0
####
####d.add_layer('TOP0')
d_single = svg.Drawing(filename='svg/mcdox_top0_5mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'TOP0'
####    d.add(insert)

for (x, y) in lollybrd_holes:
    d_single.add(circle(r=6.0*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'TOP0'
####    d.add(insert)

####svg_path_add(d, top_cutout_paths, {'layer': 'TOP0'})
svg_path_add(d_single, top_cutout_paths)

####svg_path_add(d, mnt_outline_path, {'layer': 'TOP0'})
svg_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of TOP0

# {{{ TOP1
####d.add_layer('TOP1')
d_single = svg.Drawing(filename='svg/mcdox_top1_3mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'TOP1'
####    d.add(insert)

####svg_path_add(d, top_cutout_paths, {'layer': 'TOP1'})
svg_path_add(d_single, top_cutout_paths)

####svg_path_add(d, mnt_outline_path, {'layer': 'TOP1'})
svg_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of TOP1

# {{{ TOP2
####d.add_layer('TOP2')
d_single = svg.Drawing(filename='svg/mcdox_top2_3mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'TOP2'
####    d.add(insert)

####svg_path_add(d, top_cutout_paths, {'layer': 'TOP2'})
svg_path_add(d_single, top_cutout_paths)

####svg_path_add(d, mnt_outline_path, {'layer': 'TOP2'})
svg_path_add(d_single, mnt_outline_path)

# Cut caps from same sheet as a 2 or 3mm top layer.
# This is also useful to confirm the profiling gap is enough.
if 1:
    sys.path.insert(0, '../keycap')
    from keycap_alps_dxf_blocks import *

    for number, (x, y, r) in enumerate(sw_holes):
        if cap_size(number) == 'cap_20': blk = cap_20_path
        elif cap_size(number) == 'cap_15': blk = cap_15_path
        elif cap_size(number) == 'cap_10': blk = cap_10_path

        svg_blk_path_add(d_single, blk, (x, y), r)
####    insert.layer = 'TOP2'
####    d.add(insert)

d_single.save()
# }}} End of TOP2

# {{{ BASE0
####d.add_layer('BASE0')
d_single = svg.Drawing(filename='svg/mcdox_base0_3mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'BASE0'
####    d.add(insert)

####svg_path_add(d, base0_outline_path, {'layer': 'BASE0'})
svg_path_add(d_single, base0_outline_path)

d_single.save()
# }}} End of BASE0

# {{{ BASE1
d_single = svg.Drawing(filename='svg/mcdox_base1_5mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'BASE1'
####    d.add(insert)

####svg_path_add(d, base1_outline_path, {'layer': 'BASE1'})
svg_path_add(d_single, base1_outline_path)

d_single.save()
# }}} End of BASE1

# {{{ BASE2
d_single = svg.Drawing(filename='svg/mcdox_base2_5mm.svg',
                       size=('%dmm'%page_w, '%dmm'%page_h))

for (x, y) in fix_holes:
    d_single.add(circle(r=fix_hole_diameter*mm_scale/2,
                        center=svg_pt((x, y)),
                        style=style_cut))
####    insert.layer = 'BASE2'
####    d.add(insert)

####svg_path_add(d, base2_cutout_path, {'layer': 'BASE2'})
svg_path_add(d_single, base2_cutout_path)

####svg_path_add(d, mnt_outline_path, {'layer': 'BASE2'})
svg_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of BASE2

####d.save()

if 1:
    t = svg.Drawing(filename='svg/dim_test.svg', size=('%dmm'%page_w, '%dmm'%page_h))
    
    for i in range(10):
        args = {'width': 13.2 + i*0.1}
        t.add(polyline(svg_sw_pts(swtype='cherrymx',
                                  center=(10.0, 10.0+i*18),
                                  args=args), style=style_cut))
    
    for i in range(10):
        args = {'width': 14.5 + i*0.1, 'height': 11.8 + i*0.1,}
        t.add(polyline(svg_sw_pts(swtype='alps',
                                  center=(30.0, 10.0+i*18),
                                  args=args), style=style_cut))
    
    for i in range(10):
        t.add(circle(r=(5.5 + i*0.3)*mm_scale/2,
                     center=svg_pt((45.0, 10.0+i*18)),
                     style=style_cut))
    
    for i in range(10):
        t.add(circle(r=(2.7 + i*0.1)*mm_scale/2,
                     center=svg_pt((55.0, 10.0+i*18)),
                     style=style_cut))
    
    t.save()
