#!/usr/bin/env python

from dxfwrite import DXFEngine as dxf
from ndim import *
import os
from copy import *
from keycap_alps_dxf_blocks import *

try:
    os.makedirs('dxf')
except:
    pass

# {{{ Stems

# Thickness for stem cuts *must* be 2mm.
d = dxf.drawing('dxf/alps_stems_2mm.dxf')
d.blocks.add(stem)
d.blocks.add(stem_bump)

# Tree
tree_len = 20
bump_len = 1
n_tree = 2
tree_sep = 0.5

for t in range(n_tree):
    x = t*(total_h*2 + tree_w + tree_sep) + total_h + tree_w/2

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

# {{{ Cap coords

rows_10 = 8
cols_10 = 4
rows_15 = 2
cols_15 = 3
rows_20 = 1
cols_20 = 2
cap_sep = 0.6

min_x = 0.0
min_y = 0.0
max_10_x = (cols_10*cap_10_x + (cols_10-1)*cap_sep)
max_15_x = (cols_15*cap_15_x + (cols_15-1)*cap_sep)
max_20_x = (cols_20*cap_20_x + (cols_20-1)*cap_sep)
max_x = max(max_10_x, max_15_x, max_20_x)

# Centering for ergodox layout.
row_10_shift = (max_15_x - max_10_x)/2
row_20_shift = (max_15_x - max_20_x)/2
assert row_10_shift >= 0
assert row_20_shift >= 0

# Positions of each cap in format ((x, y), <type>)
# This is used for cap cutting, cardpack, and jig.
# Should be symmetrical around a point on the x axis.
pos = []

y = cap_y/2
for r in range(rows_15):
    for c in range(cols_15):
        x = c * (cap_15_x + cap_sep) + cap_15_x/2
        pos.append(((x, y), 'cap_15'))
    y += cap_y + cap_sep

for r in range(rows_10):
    for c in range(cols_10):
        x = c * (cap_10_x + cap_sep) + cap_10_x/2 + row_10_shift
        pos.append(((x, y), 'cap_10'))
    y += cap_y + cap_sep

for r in range(rows_20):
    for c in range(cols_20):
        x = c * (cap_20_x + cap_sep) + cap_20_x/2 + row_20_shift
        pos.append(((x, y), 'cap_20'))
    y += cap_y + cap_sep

max_y = y - cap_y/2

edge_sep = 5.0
edge = [
        (min_x - edge_sep, min_y - edge_sep),
        (max_x + edge_sep, min_y - edge_sep),
        (max_x + edge_sep, max_y + edge_sep),
        (min_x - edge_sep, max_y + edge_sep),
       ]
edge.append(edge[0])

# }}} Cap coords

# {{{ Caps

# Thickness may be changed as long as nipple_h is changed accordingly.
d = dxf.drawing('dxf/alps_caps_3mm.dxf')
d.blocks.add(cap_10)
d.blocks.add(cap_15)
d.blocks.add(cap_20)

def caps(j):
    if j == 'cap_10': return cap_10
    if j == 'cap_15': return cap_15
    if j == 'cap_20': return cap_20

for p in pos:
    d.add(dxf.insert2(blockdef=caps(p[1]), insert=p[0]))

d.add( dxf.polyline(edge) )

d.save()

# }}} Caps

# {{{ Labelled

labelsL = [
 ('BkSpc',  0, -5.4, +4.0),
 ('~L1',    0, -3.0, +4.0),
 ('Tab',    0, -3.5, +4.0),
 ('Esc',    0, -3.0, +4.0),
 ('Home',   90, -8.5, -4.0),
 ('End',    90, -8.5, -2.8),
 ('1',      0, -0.8, +3.0),
 ('2',      0, -0.8, +3.0),
 ('3',      0, -0.8, +3.0),
 ('4',      0, -0.8, +3.0),
 ('5',      0, -0.8, +3.0),
 ('F4',     0, -1.6, +3.0),
 ('\'',     0, -0.3, +3.0),
 ('<',      0, -0.8, +3.0),
 ('>',      0, -0.8, +3.0),
 ('P',      0, -0.8, +3.0),
 ('Y',      0, -0.8, +3.0),
 ('A',      0, -0.8, +3.0),
 ('O',      0, -0.8, +3.0),
 ('E',      0, -0.8, +3.0),
 ('U',      0, -0.8, +3.0),
 ('I',      0, -0.8, +3.0),
 (':',      0, -0.0, +3.0),
 ('Q',      0, -0.8, +3.0),
 ('J',      0, -0.8, +3.0),
 ('K',      0, -0.8, +3.0),
 ('X',      0, -0.8, +3.0),
 ('PgDn',   0, -4.3, +3.0),
 ('PgUp',   0, -4.8, +3.0),
 ('App',    0, -3.0, +3.0),
 None, # Unused
 None, # Unused
 ('`',      0, -0.5, +2.5),
 ('Alt',    0, -3.0, +3.0),
 ('Del',    0, -3.0, +3.0),
 ('~L2',    0, -3.0, +3.0),
 None, # Spare
 None, # Spare
 ('Shift',  90, -13.0, -4.7),
 ('Ctrl',   90, -13.0, -3.5),
]

labelsR = [
 ('Ctrl',   0,      -3.5, +3.0),
 ('-',      0,      -0.8, +3.0),
 ('=',      0,      -0.8, +3.0),
 ('/',      0,      -0.8, +3.0),
 ('[',      90,     -7.8, +0.0),
 (']',      90,     -7.8, +0.0),
 ('6',      0,      -0.8, +3.0),
 ('7',      0,      -0.8, +3.0),
 ('8',      0,      -0.8, +3.0),
 ('9',      0,      -0.8, +3.0),
 ('0',      0,      -0.8, +3.0),
 ('F5',     0,      -0.8, +3.0),
 ('F',      0,      -0.8, +3.0),
 ('G',      0,      -0.8, +3.0),
 ('C',      0,      -0.8, +3.0),
 ('R',      0,      -0.8, +3.0),
 ('L',      0,      -0.8, +3.0),
 ('D',      0,      -0.8, +3.0),
 ('H',      0,      -0.8, +3.0),
 ('T',      0,      -0.8, +3.0),
 ('N',      0,      -0.8, +3.0),
 ('S',      0,      -0.8, +3.0),
 ('B',      0,      -0.8, +3.0),
 ('M',      0,      -0.8, +3.0),
 ('W',      0,      -0.8, +3.0),
 ('V',      0,      -0.8, +3.0),
 ('Z',      0,      -0.8, +3.0),
 ('Right',  0,      -4.3, +3.0),
 ('Left',   0,      -3.8, +3.0),
 ('Dn',     0,      -1.8, +3.0),
 ('Up',     0,      -1.8, +3.0),
 ('\\',     0,      -0.8, +3.0),
 ('Mute',   0,      -4.8, +3.0),
 ('Super',  0,      -5.5, +3.0),
 ('Shift',  0,      -4.8, +3.0),
 ('~L2',    0,      -3.0, +3.0),
 None, # Spare
 None, # Spare
 ('Enter',  90,     -13.0, -4.5),
 ('Space',  90,     -13.0, -4.5),
]

assert len(pos) == len(labelsL)
assert len(pos) == len(labelsR)

text = dxf.text('blah', height=3.0, layer='ETCH')

l = deepcopy(d)
l.filename = 'dxf/alps_caps_mcdoxleft_3mm.dxf'
l.add_layer('ETCH', color=2)
for i, label in enumerate(labelsL):
    if label is None: continue
    x, y = pos[i][0]
    t = deepcopy(text)
    t['text'] = label[0]
    t['rotation'] = label[1]
    t['insert'] = (label[2] + x, label[3] + y)
    l.add(t)
l.save()

l = deepcopy(d)
l.filename = 'dxf/alps_caps_mcdoxright_3mm.dxf'
l.add_layer('ETCH', color=2)
for i, label in enumerate(labelsR):
    if label is None: continue
    x, y = pos[i][0]
    t = deepcopy(text)
    t['text'] = label[0]
    t['rotation'] = label[1]
    t['insert'] = (label[2] + x, label[3] + y)
    l.add(t)
l.save()

# }}} Labelled

# {{{ Cardpack

# Thickness should keep two layers of oppositely oriented keycaps apart enough
# to be suitable for shipping.
d = dxf.drawing('dxf/alps_cardpack_6mm.dxf')
d.blocks.add(socket)

# Pattern does not necessarily need to be the same as the cap cutting.
# However, it must be the same as the jig.

for p in pos:
    d.add(dxf.insert2(blockdef=socket, insert=p[0]))

d.add( dxf.polyline(edge) )

d.save()

# }}} Cardpack

# {{{ Jig

# Jig is to hold all caps in place while stem/caps are bonded then the packing
# card can be placed on top for shipping.
# Since the cardpack is double sided, two jigs will be needed unless the
# cardpack is symmetrical on at least one axis.
# Circles should be drilled.
# Blocks should be followed then in-filled.
# Edge should be outside-profiled.
d = dxf.drawing('dxf/alps_jig_cnc.dxf')
d.blocks.add(jig_10)
d.blocks.add(jig_15)
d.blocks.add(jig_20)

def jigs(j):
    if j == 'cap_10': return jig_10
    if j == 'cap_15': return jig_15
    if j == 'cap_20': return jig_20

for p in pos:
    d.add(dxf.insert2(blockdef=jigs(p[1]), insert=p[0]))

d.add( dxf.polyline(edge) )

d.save()

# }}} Jig

