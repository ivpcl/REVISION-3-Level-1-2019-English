from AOLME import *
r="fe0606"
v="157f11"
c="f2dc9b"
n="000000"
cp="8E5730"
j="d6ccc5"
w="b0b0b0"
frame=[[n]* 20 for row in range (20)]
frame2=frame
im_fill(frame2,[2,4],[9,11],v)
im_fill(frame2,[7,12],[9,11],v)
im_fill(frame2,[7,7],[6,14],v)
frame2[3][8]=v
frame2[3][12]=v
im_fill(frame2,[13,17],[9,9],w)
im_fill(frame2,[13,16],[11,11],w)
im_fill(frame2,[4,10],[16,16],cp)
frame2[3][18]=cp
frame2[3][17]=cp
frame2[3][16]=cp
im_fill(frame2,[5,6],[10,10],r)
frame2[3][9]=r
frame2[3][11]=r
frame2[7][15]=r
im_fill(frame2,[17,18],[11,11],r)
frame2[18][9]=r
frame2[7][5]=r
#im_show(frame2)

move_by = 2
frame_2a = [["ffffff"]*20 for row in range(20)]
for row in range(20):
    for col in range(20-move_by):
        frame_2a[row][col+move_by] = frame2[row][col]


r="ff0000"
v="006cff"
c="f2dc9b"
n="000000"
cp="8E5730"
j="d6ccc5"
w="960000"
frame1=[[w]* 20 for row in range (20)]
frame3=frame1
im_fill(frame3,[2,4],[9,11],v)
im_fill(frame3,[7,12],[9,11],v)
im_fill(frame3,[7,7],[6,14],v)
frame3[3][8]=v
frame3[3][12]=v
im_fill(frame3,[13,17],[9,9],n)
im_fill(frame3,[13,16],[11,11],n)
im_fill(frame3,[4,10],[16,16],cp)
frame3[3][18]=cp
frame3[3][17]=cp
frame3[3][16]=cp
im_fill(frame3,[5,6],[10,10],r)
frame3[3][9]=r
frame3[3][11]=r
frame3[7][15]=r
im_fill(frame3,[17,18],[11,11],r)
frame3[18][9]=r
frame3[7][5]=r
#im_show(frame3)

r="ffff00"
v="ff5d00"
c="00ff6a"
n="000000"
cp="00ff6a"
j="d6ccc5"
w="00fff2"
frame0=[[w]* 20 for row in range (20)]
frame4=frame0
im_fill(frame4,[2,4],[9,11],v)
im_fill(frame4,[7,12],[9,11],v)
im_fill(frame4,[7,7],[6,14],v)
frame4[3][8]=v
frame4[3][12]=v
im_fill(frame4,[13,17],[9,9],n)
im_fill(frame4,[13,16],[11,11],n)
im_fill(frame4,[4,10],[16,16],cp)
frame4[3][18]=cp
frame4[3][17]=cp
frame4[3][16]=cp
im_fill(frame4,[5,6],[10,10],r)
frame4[3][9]=r
frame4[3][11]=r
frame4[7][15]=r
im_fill(frame4,[17,18],[11,11],r)
frame4[18][9]=r
frame4[7][5]=r
#im_show(frame3)

r="00f2ff"
v="9462ff"
c="00ff6a"
n="000000"
cp="00ff6a"
j="d6ccc5"
w="852323"
frame0b=[[w]* 20 for row in range (20)]
frame6=frame0b
im_fill(frame6,[2,4],[9,11],v)
im_fill(frame6,[7,12],[9,11],v)
im_fill(frame6,[7,7],[6,14],v)
frame6[3][8]=v
frame6[3][12]=v
im_fill(frame6,[13,17],[9,9],n)
im_fill(frame6,[13,16],[11,11],n)
im_fill(frame6,[4,10],[16,16],cp)
frame6[3][18]=cp
frame6[3][17]=cp
frame6[3][16]=cp
im_fill(frame6,[5,6],[10,10],r)
frame6[3][9]=r
frame6[3][11]=r
frame6[7][15]=r
im_fill(frame6,[17,18],[11,11],r)
frame6[18][9]=r
frame6[7][5]=r
#im_show(frame3)


r="fe0606"
v="006cff"
c="f2dc9b"
n="ffee00"
cp="00ff6a"
j="d6ccc5"
w="ff4395"
frames=[[w]* 20 for row in range (20)]
frame5=frames
im_fill(frame5,[2,4],[9,11],v)
im_fill(frame5,[7,12],[9,11],v)
im_fill(frame5,[7,7],[6,14],v)
frame5[3][8]=v
frame5[3][12]=v
im_fill(frame5,[13,17],[9,9],n)
im_fill(frame5,[13,16],[11,11],n)
im_fill(frame5,[4,10],[16,16],cp)
frame5[3][18]=cp
frame5[3][17]=cp
frame5[3][16]=cp
im_fill(frame5,[5,6],[10,10],r)
frame5[3][9]=r
frame5[3][11]=r
frame5[7][15]=r
im_fill(frame5,[17,18],[11,11],r)
frame5[18][9]=r
frame5[7][5]=r
#im_show(frame3)

move_by = 13
frame_6a = [["000000"]*20 for row in range(20)]
for row in range(20):
    for col in range(20-move_by):
        frame_6a[row][col+move_by] = frame5[row][col]

move_by = -2
frame_5a = [["000000"]*20 for row in range(20)]
for row in range(20):
    for col in range(20):
        frame_2a[row][col+move_by] = frame2[row][col]

frame_list = [frame2, frame_2a, frame3, frame4, frame6, frame5, frame_6a, frame_5a]
fps= 2
play_video= vid_show(frame_list,fps)
