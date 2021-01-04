#!/usr/bin/env python3

# NOTE: OpenSCAD is missing from Ubuntu18.04 apt repository so AppImage can be
# found from <https://files.openscad.org/OpenSCAD-2019.05-x86_64.AppImage>.

from os import makedirs, sep
from itertools import product
from subprocess import check_call

stems = {
    "cherrymx": 1,
    "alps": 2,
}

profiles = {
    "dsa": 1,
    "dcs": 2,
}

lengths = (
    "1.0",
    "1.5",
    "2.0",
)

bumps = (False, True)

try:
    makedirs("stl")
except:
    pass

for stem,profile,length,bump in product(stems, profiles, lengths, bumps):
    fnameo = "stl" + sep + \
        '_'.join((stem, profile, length, "bump" if bump else "nobump")) + \
        ".stl"

    cmd = ' '.join((
        "./OpenSCAD-2019.05-x86_64.AppImage",
        "-o %s" % fnameo,
        "-D stemNum=%d" % stems[stem],
        "-D profileNum=%d" % profiles[profile],
        "-D lengthMul=%s" % length,
        "-D doBump=%d" % int(bump),
        "keycap.scad"
    ))

    print(cmd)
    check_call(cmd, shell=True)
