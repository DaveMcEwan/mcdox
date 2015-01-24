#!/usr/bin/env python

from dxfwrite import DXFEngine as dxf
from mcdox_coords import *

from copy import *
import os
import shutil
try:
    os.makedirs('dxf')
except:
    pass

def dxf_path_add(drawing, path={}, keywords={}):
    for p in path:
        if 'type' not in p: continue # TODO: maybe warn here?

        t = p['type']
        if t == 'polyline':
            e = dxf.polyline(p['pts'])
        elif t == 'arc':
            e = dxf.arc()

        atts = p.keys()
        atts.remove('type')
        if 'pts' in atts: atts.remove('pts')
        for a in atts:
            e[a] = p[a]

        for k in keywords:
            e[k] = keywords[k]

        drawing.add(e)


filename = 'dxf/mcdox_all.dxf'
d = dxf.drawing(filename)

# {{{ Block definition

sw_mnt = dxf.block(name='sw_mnt')
sw_mnt.add( dxf.polyline(sw_outline_pts('alps')) )
sw_mnt.add( dxf.attdef(insert=(0.0, -0.3), tag='NAME', height=2.0, color=3) )
#sw_mnt.add( dxf.attdef(insert=(0.0, -0.6), tag='X', height=0.25, color=4) )
#sw_mnt.add( dxf.attdef(insert=(0.0, -0.9), tag='Y', height=0.25, color=4) )
#sw_mnt.add( dxf.attdef(insert=(0.0, -1.2), tag='R', height=0.25, color=4) )
d.blocks.add(sw_mnt)

drill_m3 = dxf.block(name='drill_m3')
drill_m3.add( dxf.circle(fix_hole_diameter/2) )
d.blocks.add(drill_m3)

drill_7mm = dxf.block(name='drill_7mm')
drill_7mm.add( dxf.circle(6.0/2) )
d.blocks.add(drill_7mm)

# }}} Block definition

# {{{ MNT

d.add_layer('MNT')
d_single = dxf.drawing('dxf/mcdox_mnt_3mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y, r) in enumerate(sw_holes):
    # insert2() needs the block definition object as parameter 'blockdef'.
    # See http://packages.python.org/dxfwrite/entities/insert2.html
    # Fill attribtes by creating a dict(), key is the 'tag' name of the
    # attribute.
    attribs = {
        'NAME': "%d" % number,
        'X': "x = %.3f" % x,
        'Y': "y = %.3f" % y,
        'R': "r = %.3f" % r,
    }
    insert = dxf.insert2(blockdef=sw_mnt,
                         insert=(x, y),
                         attribs=attribs,
                         xscale=1.0,
                         yscale=1.0,
                         rotation=degrees(r))

    d_single.add(deepcopy(insert))

    insert.layer = 'MNT'
    d.add(insert)

for (x, y) in fix_holes + lollybrd_holes:
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'MNT'
    d.add(insert)

dxf_path_add(d, mnt_outline_path, {'layer': 'MNT'})
dxf_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of MNT

# {{{ TOP0

d.add_layer('TOP0')
d_single = dxf.drawing('dxf/mcdox_top0_5mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for (x, y) in fix_holes:
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'TOP0'
    d.add(insert)

for (x, y) in lollybrd_holes:
    insert = dxf.insert2(blockdef=drill_7mm,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'TOP0'
    d.add(insert)

dxf_path_add(d, top_cutout_paths, {'layer': 'TOP0'})
dxf_path_add(d_single, top_cutout_paths)

dxf_path_add(d, mnt_outline_path, {'layer': 'TOP0'})
dxf_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of TOP0

# {{{ TOP1

d.add_layer('TOP1')
d_single = dxf.drawing('dxf/mcdox_top1_3mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y) in enumerate(fix_holes):
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'TOP1'
    d.add(insert)

dxf_path_add(d, top_cutout_paths, {'layer': 'TOP1'})
dxf_path_add(d_single, top_cutout_paths)

dxf_path_add(d, mnt_outline_path, {'layer': 'TOP1'})
dxf_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of TOP1

# {{{ TOP2

d.add_layer('TOP2')
d_single = dxf.drawing('dxf/mcdox_top2_3mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y) in enumerate(fix_holes):
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'TOP2'
    d.add(insert)

dxf_path_add(d, top_cutout_paths, {'layer': 'TOP2'})
dxf_path_add(d_single, top_cutout_paths)

dxf_path_add(d, mnt_outline_path, {'layer': 'TOP2'})
dxf_path_add(d_single, mnt_outline_path)

# Cut caps from same sheet as a 2 or 3mm top layer.
# This is also useful to confirm the profiling gap is enough.
if 1:
    sys.path.insert(0, '../keycap')
    from keycap_alps_dxf_blocks import *
    d.blocks.add(cap_10)
    d.blocks.add(cap_15)
    d.blocks.add(cap_20)
    d_single.blocks.add(cap_10)
    d_single.blocks.add(cap_15)
    d_single.blocks.add(cap_20)

    for number, (x, y, r) in enumerate(sw_holes):
        attribs = {
            'NAME': "%d" % number,
            'X': "x = %.3f" % x,
            'Y': "y = %.3f" % y,
            'R': "r = %.3f" % r,
        }

        if cap_size(number) == 'cap_20': cap = cap_20
        elif cap_size(number) == 'cap_15': cap = cap_15
        elif cap_size(number) == 'cap_10': cap = cap_10

        insert = dxf.insert2(blockdef=cap,
                             insert=(x, y),
                             attribs=attribs,
                             xscale=1.0,
                             yscale=1.0,
                             rotation=degrees(r))

        d_single.add(deepcopy(insert))

        insert.layer = 'TOP2'
        d.add(insert)

d_single.save()
# }}} End of TOP2

# {{{ BASE0

d.add_layer('BASE0')
d_single = dxf.drawing('dxf/mcdox_base0_3mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y) in enumerate(fix_holes):
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'BASE0'
    d.add(insert)

dxf_path_add(d, base0_outline_path, {'layer': 'BASE0'})
dxf_path_add(d_single, base0_outline_path)

d_single.save()
# }}} End of BASE0

# {{{ BASE1

d.add_layer('BASE1')
d_single = dxf.drawing('dxf/mcdox_base1_5mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y) in enumerate(fix_holes):
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'BASE1'
    d.add(insert)

dxf_path_add(d, base1_outline_path, {'layer': 'BASE1'})
dxf_path_add(d_single, base1_outline_path)

d_single.save()
# }}} End of BASE1

# {{{ BASE2

d.add_layer('BASE2')
d_single = dxf.drawing('dxf/mcdox_base2_5mm.dxf')
d_single.blocks.add(sw_mnt)
d_single.blocks.add(drill_m3)
d_single.blocks.add(drill_7mm)

for number, (x, y) in enumerate(fix_holes):
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'BASE2'
    d.add(insert)

dxf_path_add(d, base2_cutout_path, {'layer': 'BASE2'})
dxf_path_add(d_single, base2_cutout_path)

dxf_path_add(d, mnt_outline_path, {'layer': 'BASE2'})
dxf_path_add(d_single, mnt_outline_path)

d_single.save()
# }}} End of BASE2

d.save()

if 1:
    filename = 'dxf/dim_test.dxf'
    t = dxf.drawing(filename)
    
    cherry = [dxf.block(name='cherry_%d' % i) for i in range(10)]
    for i in range(10):
        args = {'width': 13.2 + i*0.1}
        cherry[i].add( dxf.polyline(sw_outline_pts('cherrymx', args)) )
        t.blocks.add(cherry[i])
        t.add(dxf.insert2(blockdef=cherry[i], insert=(0+10, 10+i*18)))
    
    alps = [dxf.block(name='alps_%d' % i) for i in range(10)]
    for i in range(10):
        args = {'width': 14.5 + i*0.1, 'height': 11.8 + i*0.1,}
        alps[i].add( dxf.polyline(sw_outline_pts('alps', args)) )
        t.blocks.add(alps[i])
        t.add(dxf.insert2(blockdef=alps[i], insert=(0+30, 10+i*18)))
    
    m7 = [dxf.block(name='m7_%d' % i) for i in range(10)]
    for i in range(10):
        m7[i].add( dxf.circle((5.5 + i*0.3)/2) )
        t.blocks.add(m7[i])
        t.add(dxf.insert2(blockdef=m7[i], insert=(0+45, 10+i*18)))
    
    m3 = [dxf.block(name='m3_%d' % i) for i in range(10)]
    for i in range(10):
        m3[i].add( dxf.circle((2.7 + i*0.1)/2) )
        t.blocks.add(m3[i])
        t.add(dxf.insert2(blockdef=m3[i], insert=(0+55, 10+i*18)))
    
    t.save()
