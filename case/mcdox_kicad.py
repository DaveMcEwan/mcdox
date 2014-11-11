#!/usr/bin/env python

from mcdox_coords import *
import re


# Get switch footprint module and make it suitable for insertion.
with open('../pcb/mcdox.pretty/alpsmx.kicad_mod') as fd:
    alpsmx = fd.readlines()

# Append a zero rotation to all non-rotated features.
pattern = '\(at -?\d+(\.\d+)? -?\d+(\.\d+)?\)'
for i, l in enumerate(alpsmx):
    r = re.search(pattern, l)
    if r is not None:
        e = r.end(0) - 1
        alpsmx[i] = l[:e] + ' 0.0' + l[e:]




def floatf(n):
    ret = (' %0.3f' % n).rstrip('0').rstrip('.')
    if ret == ' 0': ret = ''
    return ret 

pcb = ['''
(kicad_pcb (version 4) (host pcbnew "(2014-09-07 BZR 5117)-product")

  (general
    (links 0)
    (no_connects 0)
    (area 90.670999 -189.829001 269.523651 -50.541247)
    (thickness 1.6)
    (drawings 0)
    (tracks 0)
    (zones 0)
    (modules 38)
    (nets 1)
  )

  (page A4)
  (layers
    (0 F.Cu signal)
    (31 B.Cu signal)
    (32 B.Adhes user)
    (33 F.Adhes user)
    (34 B.Paste user)
    (35 F.Paste user)
    (36 B.SilkS user)
    (37 F.SilkS user)
    (38 B.Mask user)
    (39 F.Mask user)
    (40 Dwgs.User user)
    (41 Cmts.User user)
    (42 Eco1.User user)
    (43 Eco2.User user)
    (44 Edge.Cuts user)
    (45 Margin user)
    (46 B.CrtYd user)
    (47 F.CrtYd user)
    (48 B.Fab user)
    (49 F.Fab user)
  )

  (setup
    (last_trace_width 0.254)
    (trace_clearance 0.254)
    (zone_clearance 1)
    (zone_45_only no)
    (trace_min 0.254)
    (segment_width 0.2)
    (edge_width 0.15)
    (via_size 0.889)
    (via_drill 0.635)
    (via_min_size 0.889)
    (via_min_drill 0.508)
    (uvia_size 0.508)
    (uvia_drill 0.127)
    (uvias_allowed no)
    (uvia_min_size 0.508)
    (uvia_min_drill 0.127)
    (pcb_text_width 0.3)
    (pcb_text_size 1.5 1.5)
    (mod_edge_width 0.15)
    (mod_text_size 1.5 1.5)
    (mod_text_width 0.15)
    (pad_size 1.4 1.4)
    (pad_drill 0.6)
    (pad_to_mask_clearance 0.2)
    (aux_axis_origin 0 0)
    (visible_elements 7FFFFFFF)
    (pcbplotparams
      (layerselection 0x010f0_80000001)
      (usegerberextensions false)
      (excludeedgelayer true)
      (linewidth 0.100000)
      (plotframeref false)
      (viasonmask false)
      (mode 1)
      (useauxorigin false)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15)
      (hpglpenoverlay 2)
      (psnegative false)
      (psa4output false)
      (plotreference true)
      (plotvalue true)
      (plotinvisibletext false)
      (padsonsilk false)
      (subtractmaskfromsilk true)
      (outputformat 1)
      (mirror false)
      (drillshape 0)
      (scaleselection 1)
      (outputdirectory gerber/))
  )

  (net 0 "")

  (net_class Default "This is the default net class."
    (clearance 0.254)
    (trace_width 0.254)
    (via_dia 0.889)
    (via_drill 0.635)
    (uvia_dia 0.508)
    (uvia_drill 0.127)
  )
'''.strip()]

# Per switch stuff...
pattern = '\(at (-?\d+(\.\d+)?) (-?\d+(\.\d+)?) (-?\d+(\.\d+)?)\)'
for (x, y, r) in pcb_sw:
    sw_mod = list(alpsmx)
    for i, l in enumerate(sw_mod):
        p = re.search(pattern, l)
        if p is not None:
            rotate = float(p.group(5))
            rotate = (rotate + degrees(r)) % 360
            sw_mod[i] = re.sub(pattern, '(at \g<1> \g<3>%s)' % floatf(rotate), l)
    
    # Insert coordinates and rotation line after 1st line.
    sw_mod.insert(1, '  (at %s %s%s)\n' % (x+100, -y-100, floatf(degrees(r))))
    sw_mod = ''.join(sw_mod)
    pcb.append(sw_mod)
pcb.append('\n)')

with open('mcdox-generated.kicad_pcb', 'w') as fd:
    alpsmx = fd.write(''.join(pcb))
