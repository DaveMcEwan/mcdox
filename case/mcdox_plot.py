#!/usr/bin/env python

from mcdox_coords import *

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    
    ax = plt.subplot(111, aspect=1)
    
    ## Plot path for cutout.
    #x = [p[0] for p in base0_cutout]
    #y = [p[1] for p in base0_cutout]
    #ax.plot(x, y, marker='x', color='r')
    #ax.scatter(baseD[0], baseD[1])
    #c = mpatches.Circle(baseD, r_top, fill=False)
    #ax.add_patch(c)
    
    # Plot fixing holes.
    x = [p[0] for p in fix_holes + pcb_holes]
    y = [p[1] for p in fix_holes + pcb_holes]
    ax.scatter(x, y, marker='x', color='g')
    
    # Plot paths for each switch
    from cherrymx_hole import *
    for h in sw_holes:
        pts = pts_shift(cherrymx_points(rotate=h[2]), [h[0], h[1]])
        x = [p[0] for p in pts] + [pts[0][0]]
        y = [p[1] for p in pts] + [pts[0][1]]
        ax.plot(x, y, color='g')

    # Left arc
    a = mpatches.Arc(
                     xy=baseA,
                     width=2*radius,
                     height=2*radius,
                     theta1=degrees(dir_between_pts(baseA, baseD)[0]),
                     theta2=degrees(dir_between_pts(baseA, baseB)[0]),
                     )
    ax.add_patch(a)
    # Bottom arc
    b = mpatches.Arc(
                     xy=baseB,
                     width=2*r_bot,
                     height=2*r_bot,
                     theta1=degrees(dir_between_pts(baseB, baseC)[0]),
                     theta2=degrees(dir_between_pts(baseB, baseA)[0]),
                     )
    ax.add_patch(b)
    # Right arc
    c = mpatches.Arc(
                     xy=baseC,
                     width=2*radius,
                     height=2*radius,
                     theta1=degrees(dir_between_pts(baseC, baseB)[0]),
                     theta2=degrees(dir_between_pts(baseC, baseD)[0]),
                     )
    ax.add_patch(c)
    # Top arc
    d = mpatches.Arc(
                     xy=baseD,
                     width=2*r_top,
                     height=2*r_top,
                     theta1=degrees(dir_between_pts(baseD, baseA)[0]),
                     theta2=degrees(dir_between_pts(baseD, baseC)[0]),
                     )
    ax.add_patch(d)
    plt.show()

