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

imgpath_fmt = 'svg/mcdox_%s.svg'

# In SVG path units are always "SVG user units" (px, 90dpi), not mm.
# Inkscape internally converts to mm.
# Therefore scale by 90/25.4 = 3.54
mm = 90/25.4

# Standard line style for cutting.
# Set to 0.3mm to be the same as most laser cutters.
# Cut = Red
# Score/vector etch = Blue
# Raster etch = Black
style_cut = 'fill:none;stroke:#ff0000;stroke-opacity:1;stroke-width:%f' % (0.3*mm)
style_score = 'fill:none;stroke:#0000ff;stroke-opacity:1;stroke-width:%f' % (0.3*mm)

# Define page size which is required for the coordinate calculations since SVG
# specifies that top left is the origin.
page_h = 200 +10 # TODO: rm the +10 which is just for easier debug viewing.
page_w = 400 +10 # TODO: rm the +10 which is just for easier debug viewing.

# Inkscape 0.48 does not support symbols (the SVG equivilant to DXF blocks) so
# they are all converted to individual paths.
# TODO: Support for <symbol> and <use> coming in 0.91 so make use of them.

# Coordinate calculation from mm to SVG user points.
def svg_pt(pt=(0.0, 0.0), page_h=page_h):
    return pt_scale(pt_change_axis(pt, [False, True], [0.0, float(page_h)]), mm)
def svg_pts(pts=[], page_h=page_h):
    return [svg_pt(pt, float(page_h)) for pt in pts]

def svg_sw_pts(swtype='alps',
               center=(0.0, 0.0),
               rotation=0.0,
               args={}): # {{{
    pts_at_origin = sw_outline_pts(swtype, args)
    pts_at_origin = pts_rotate(pts_at_origin, [rotation])
    pts_at_origin = pts_scale(pts_at_origin, mm)
    pts = pts_shift(pts_at_origin, list(pt_scale(center, mm)))
    return pts_change_axis(pts, [False, True], [0.0, page_h*mm])
# }}} svg_sw_pts()

def svg_path_add(drawing, path={}): # {{{
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
                       r=a['radius']*mm,
                       rotation=0.0,
                       large_arc=a['big'][0],
                       angle_dir='+' if a['diff_a'] < 0.0 else '-',
                       absolute=True)
        drawing.add(e)
# }}} svg_path_add()

def svg_blk_path_add(drawing, path={}, center=(0.0, 0.0), rotation=0.0): # {{{
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
                       r=a['radius']*mm,
                       rotation=0.0,
                       large_arc=a['big'][0],
                       angle_dir='+' if a['diff_a'] < 0.0 else '-',
                       absolute=True)
        drawing.add(e)
# }}} svg_blk_path_add()

layername = 'top2' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, top_co)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    # Cut caps from same sheet as a 2 or 3mm top layer.
    # This is also useful to confirm the profiling gap is enough.
    sys.path.insert(0, '../keycap')
    from keycap_alps_dxf_blocks import *

    for i, (x, y, r) in enumerate(sw_epts):
        if cap_size(i) == 'cap_20': blk = cap_20_path
        elif cap_size(i) == 'cap_15': blk = cap_15_path
        elif cap_size(i) == 'cap_10': blk = cap_10_path

        svg_blk_path_add(d_single, blk, (x, y), r)

        l = keycap_labels[i]
        r = degrees(r) + l[0]
        style = "stroke:#0000ff;-inkscape-font-specification:sans-serif;font-family:sans-serif;font-weight:normal;font-style:normal;font-stretch:normal;font-variant:normal;font-size:14px"
        for text, x_sh, y_sh in l[1]:
            this_x, this_y = pt_relative((x, y), [x_sh, y_sh], [radians(r)])
            this_x, this_y = svg_pt((this_x, this_y))
            transform = 'rotate(%f, %f, %f)' % (-r, this_x, this_y)
            d_single.add(svg.text.Text(text, x=[this_x], y=[this_y], transform=transform, style=style))

    d_single.save()
# }}} top2

layername = 'top1' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, top_co)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} top1

layername = 'top0' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, top_co)

    svg_path_add(d_single, wsco_paths)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    for (x, y) in ctrlbrd_ho:
        d_single.add(circle(r=6.0*mm/2,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} top0

layername = 'mnt_cherrymx' # {{{
if layername in case_layers:
    if 'mnt_alps' not in case_layers:
        layername = 'mnt'
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, ctrlmnt)

    svg_path_add(d_single, wsco_paths)

    for i, (x, y, r) in enumerate(sw_epts):
        d_single.add(polyline(svg_sw_pts(swtype='cherrymx',
                                         center=(x, y),
                                         rotation=r),
                                         style=style_cut))

    for (x, y) in case_ho + ctrlbrd_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} mnt cherrymx

layername = 'mnt_alps' # {{{
if layername in case_layers:
    if 'mnt_cherrymx' not in case_layers:
        layername = 'mnt'
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, ctrlmnt)

    svg_path_add(d_single, wsco_paths)

    for i, (x, y, r) in enumerate(sw_epts):
        d_single.add(polyline(svg_sw_pts(swtype='alps',
                                         center=(x, y),
                                         rotation=r),
                                         style=style_cut))

    for (x, y) in case_ho + ctrlbrd_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} mnt_alps

layername = 'base2' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    svg_path_add(d_single, base2_outline)

    svg_path_add(d_single, wsco_paths)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} base2

layername = 'base1' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, base1_outline)

    svg_path_add(d_single, wsco_paths)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} base1

layername = 'base0' # {{{
if layername in case_layers:
    d_single = svg.Drawing(filename=imgpath_fmt % layername,
                           size=('%dmm'%page_w, '%dmm'%page_h))

    svg_path_add(d_single, case_outline)

    for (x, y) in case_ho:
        d_single.add(circle(r=M3_r*mm,
                            center=svg_pt((x, y)),
                            style=style_cut))

    d_single.save()
# }}} base0

layername = 'dimtst' # {{{
if layername in case_layers:
    t = svg.Drawing(filename=imgpath_fmt % layername,
                    size=('%dmm'%page_w, '%dmm'%page_h))

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
        t.add(circle(r=(5.5 + i*0.3)*mm/2,
                     center=svg_pt((45.0, 10.0+i*18)),
                     style=style_cut))

    for i in range(10):
        t.add(circle(r=(2.7 + i*0.1)*mm/2,
                     center=svg_pt((55.0, 10.0+i*18)),
                     style=style_cut))

    t.save()
# }}} dimtst

