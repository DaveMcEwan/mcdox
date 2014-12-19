#!/usr/bin/env python

import os
from subprocess import check_call

stems = {
#         'cherrymx': 1,
         'alps': 2,
        }

profiles = {
#            'dcs': 1,
            'dsa': 2,
           }

bools = ['bump']

sizes = [
         1.0,
         1.5,
         2.0,
        ]

try:
    os.makedirs('stl')
except:
    pass

for stem in stems:
    for profile in profiles:
        for size in sizes:
            for bool in bools:
                for b in [0, 1]:
                    bool_name = '_%s' % bool if b else ''
                    cmd = 'openscad '
                    cmd += '-o stl/%s_%s_x%s%s.stl ' % (stem, profile, size, bool_name)
                    cmd += '-D key_type=%d ' % profiles[profile]
                    cmd += '-D stem_type=%d ' % stems[stem]
                    cmd += '-D key_size=%s ' % size
                    cmd += '-D %s=%d ' % (bool, b)
                    cmd += 'keycap.scad'
                    print(cmd)
                    check_call(cmd, shell=True)
