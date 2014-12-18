#!/usr/bin/env python

from dxfwrite import DXFEngine as dxf
from mcdox_coords import *

from copy import *
import os
try:
    os.makedirs('dxf')
except:
    pass

filename = 'dxf/mcdox_all.dxf'
d = dxf.drawing(filename)

# {{{ Block definition

sw_mnt = dxf.block(name='sw_mnt')
sw_mnt.add( dxf.polyline(sw_outline_pts('cherrymx')) )
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
d_single = dxf.drawing('dxf/mcdox_mnt_2mm.dxf')
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

for (x, y) in fix_holes + pcb_holes:
    insert = dxf.insert2(blockdef=drill_m3,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'MNT'
    d.add(insert)

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'MNT'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'MNT'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'MNT'
d.add(arc_right)

arc_top = dxf.arc()
arc_top['radius'] = r_top
arc_top['center'] = baseD
arc_top['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_top['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_top))
arc_top['layer'] = 'MNT'
d.add(arc_top)

d_single.save()
# }}} End of MNT

# {{{ TOP0

d.add_layer('TOP0')
d_single = dxf.drawing('dxf/mcdox_top0_4mm.dxf')
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

for (x, y) in pcb_holes:
    insert = dxf.insert2(blockdef=drill_7mm,
                         insert=(x, y),
                         xscale=1.0,
                         yscale=1.0)

    d_single.add(deepcopy(insert))

    insert.layer = 'TOP0'
    d.add(insert)

fingersL = dxf.polyline(fingersL_outline)
d_single.add(deepcopy(fingersL))
fingersL['layer'] = 'TOP0'
d.add(fingersL)

thumbsL = dxf.polyline(thumbsL_outline)
d_single.add(deepcopy(thumbsL))
thumbsL['layer'] = 'TOP0'
d.add(thumbsL)

fingersR = dxf.polyline(fingersR_outline)
d_single.add(deepcopy(fingersR))
fingersR['layer'] = 'TOP0'
d.add(fingersR)

thumbsR = dxf.polyline(thumbsR_outline)
d_single.add(deepcopy(thumbsR))
thumbsR['layer'] = 'TOP0'
d.add(thumbsR)

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'TOP0'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'TOP0'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'TOP0'
d.add(arc_right)

arc_top = dxf.arc()
arc_top['radius'] = r_top
arc_top['center'] = baseD
arc_top['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_top['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_top))
arc_top['layer'] = 'TOP0'
d.add(arc_top)

d_single.save()
# }}} End of TOP0

# {{{ TOP1

d.add_layer('TOP1')
d_single = dxf.drawing('dxf/mcdox_top1_4mm.dxf')
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

fingersL = dxf.polyline(fingersL_outline)
d_single.add(deepcopy(fingersL))
fingersL['layer'] = 'TOP1'
d.add(fingersL)

thumbsL = dxf.polyline(thumbsL_outline)
d_single.add(deepcopy(thumbsL))
thumbsL['layer'] = 'TOP1'
d.add(thumbsL)

fingersR = dxf.polyline(fingersR_outline)
d_single.add(deepcopy(fingersR))
fingersR['layer'] = 'TOP1'
d.add(fingersR)

thumbsR = dxf.polyline(thumbsR_outline)
d_single.add(deepcopy(thumbsR))
thumbsR['layer'] = 'TOP1'
d.add(thumbsR)

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'TOP1'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'TOP1'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'TOP1'
d.add(arc_right)

arc_top = dxf.arc()
arc_top['radius'] = r_top
arc_top['center'] = baseD
arc_top['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_top['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_top))
arc_top['layer'] = 'TOP1'
d.add(arc_top)

d_single.save()
# }}} End of TOP1

# {{{ TOP2

d.add_layer('TOP2')
d_single = dxf.drawing('dxf/mcdox_top2_2mm.dxf')
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

fingersL = dxf.polyline(fingersL_outline)
d_single.add(deepcopy(fingersL))
fingersL['layer'] = 'TOP2'
d.add(fingersL)

thumbsL = dxf.polyline(thumbsL_outline)
d_single.add(deepcopy(thumbsL))
thumbsL['layer'] = 'TOP2'
d.add(thumbsL)

fingersR = dxf.polyline(fingersR_outline)
d_single.add(deepcopy(fingersR))
fingersR['layer'] = 'TOP2'
d.add(fingersR)

thumbsR = dxf.polyline(thumbsR_outline)
d_single.add(deepcopy(thumbsR))
thumbsR['layer'] = 'TOP2'
d.add(thumbsR)

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'TOP2'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'TOP2'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'TOP2'
d.add(arc_right)

arc_top = dxf.arc()
arc_top['radius'] = r_top
arc_top['center'] = baseD
arc_top['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_top['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_top))
arc_top['layer'] = 'TOP2'
d.add(arc_top)

d_single.save()
# }}} End of TOP2

# {{{ BASE0

d.add_layer('BASE0')
d_single = dxf.drawing('dxf/mcdox_base0_2mm.dxf')
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

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'BASE0'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'BASE0'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'BASE0'
d.add(arc_right)

arc_topR = dxf.arc()
arc_topR['radius'] = r_top
arc_topR['center'] = baseD
arc_topR['startangle'] = degrees(dir_between_pts(baseD, base0J)[0])
arc_topR['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_topR))
arc_topR['layer'] = 'BASE0'
d.add(arc_topR)

cutout = dxf.polyline(base0_cutout)
d_single.add(deepcopy(cutout))
cutout['layer'] = 'BASE0'
d.add(cutout)

arc_topL = dxf.arc()
arc_topL['radius'] = r_top
arc_topL['center'] = baseD
arc_topL['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_topL['endangle']   = degrees(dir_between_pts(baseD, base0I)[0])
d_single.add(deepcopy(arc_topL))
arc_topL['layer'] = 'BASE0'
d.add(arc_topL)

d_single.save()
# }}} End of BASE0

# {{{ BASE1

d.add_layer('BASE1')
d_single = dxf.drawing('dxf/mcdox_base1_4mm.dxf')
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

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'BASE1'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'BASE1'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'BASE1'
d.add(arc_right)

arc_topR = dxf.arc()
arc_topR['radius'] = r_top
arc_topR['center'] = baseD
arc_topR['startangle'] = degrees(dir_between_pts(baseD, base0J)[0])
arc_topR['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_topR))
arc_topR['layer'] = 'BASE1'
d.add(arc_topR)

cutout = dxf.polyline(base1_cutout)
d_single.add(deepcopy(cutout))
cutout['layer'] = 'BASE1'
d.add(cutout)

arc_topL = dxf.arc()
arc_topL['radius'] = r_top
arc_topL['center'] = baseD
arc_topL['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_topL['endangle']   = degrees(dir_between_pts(baseD, base0I)[0])
d_single.add(deepcopy(arc_topL))
arc_topL['layer'] = 'BASE1'
d.add(arc_topL)

d_single.save()
# }}} End of BASE1

# {{{ BASE2

d.add_layer('BASE2')
d_single = dxf.drawing('dxf/mcdox_base2_4mm.dxf')
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

cutout = dxf.polyline(base2_cutout)
d_single.add(deepcopy(cutout))
cutout['layer'] = 'BASE2'
d.add(cutout)

arc_left = dxf.arc()
arc_left['radius'] = radius
arc_left['center'] = baseA
arc_left['startangle'] = degrees(dir_between_pts(baseA, baseD)[0])
arc_left['endangle']   = degrees(dir_between_pts(baseA, baseB)[0])
d_single.add(deepcopy(arc_left))
arc_left['layer'] = 'BASE2'
d.add(arc_left)

arc_bot = dxf.arc()
arc_bot['radius'] = r_bot
arc_bot['center'] = baseB
arc_bot['startangle'] = degrees(dir_between_pts(baseB, baseC)[0])
arc_bot['endangle']   = degrees(dir_between_pts(baseB, baseA)[0])
d_single.add(deepcopy(arc_bot))
arc_bot['layer'] = 'BASE2'
d.add(arc_bot)

arc_right = dxf.arc()
arc_right['radius'] = radius
arc_right['center'] = baseC
arc_right['startangle'] = degrees(dir_between_pts(baseC, baseB)[0])
arc_right['endangle']   = degrees(dir_between_pts(baseC, baseD)[0])
d_single.add(deepcopy(arc_right))
arc_right['layer'] = 'BASE2'
d.add(arc_right)

arc_top = dxf.arc()
arc_top['radius'] = r_top
arc_top['center'] = baseD
arc_top['startangle'] = degrees(dir_between_pts(baseD, baseA)[0])
arc_top['endangle']   = degrees(dir_between_pts(baseD, baseC)[0])
d_single.add(deepcopy(arc_top))
arc_top['layer'] = 'BASE2'
d.add(arc_top)

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
