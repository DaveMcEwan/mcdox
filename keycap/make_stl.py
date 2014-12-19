#!/usr/bin/env python

import os
from subprocess import check_call

stems = ['ALPS', 'CHERRYMX']
profiles = ['DSA', 'DCS']
bools = ['bump']
sizes = [1, 1.5, 2]

os.makedirs('stl')

cmds = []
for s, stem in enumerate(stems):
    stem_name = stem.lower()
    stem_num = s + 1
    for p, profile in enumerate(profiles):
        profile_name = profile.lower()
        profile_num = p + 1
        for size in sizes:
            for bool in bools:
                for b in [0, 1]:
                    bool_name = '_%s' % bool if b else ''
                    cmd = 'openscad '
                    cmd += '-o stl/%s_%s_x%s%s.stl ' % (stem_name, profile_name, size, bool_name)
                    cmd += '-D key_type=%d ' % profile_num
                    cmd += '-D stem_type=%d ' % stem_num
                    cmd += '-D key_size=%s ' % size
                    cmd += '-D %s=%d ' % (bool, b)
                    cmd += 'keycap.scad'
                    cmds.append(cmd)
                    print(cmd)
                    check_call(cmd, shell=True)
