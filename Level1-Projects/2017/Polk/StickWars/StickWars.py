from AOLME import *
import numpy

cols = 20
rows = 20
b = "000000"
grey = "888888"  
w = "ffffff"
g = "540000"
r = "ff0000"
frame_1 = [[b]*cols for row in range(rows)]
im_fill(frame_1, [4, 6], [7, 12], r) # head
frame_1[5][8]  = b # eye 1
frame_1[5][11] = b # eye 2

im_fill(frame_1, [7,7],  [9, 10], r)
im_fill(frame_1, [13,13], [15,16], r)
im_fill(frame_1, [8,13], [5,6], g)
im_fill(frame_1, [8,8], [7,7], g)
im_fill(frame_1, [8,13], [8,11], g)
im_fill(frame_1, [8,8], [12,12], g)
im_fill(frame_1, [8,13], [13,14], g)
frame_1[14][9]  = g
frame_1[14][10] = g
frame_1[15][8]  = g 
frame_1[16][7]  = g
frame_1[17][6]  = g
frame_1[18][7]  = grey
frame_1[18][8]  = grey
frame_1[18][6]  = grey
frame_1[15][10] = g
frame_1[16][11] = g
frame_1[17][12] = g
frame_1[18][12] = grey
frame_1[18][13] = grey
frame_1[18][14] = grey
im_fill(frame_1, [2,3], [7,12],grey) # hat
im_fill(frame_1, [1,1], [9,10],grey) # hat
im_fill(frame_1, [3,3], [6,13],grey)

# Copy and move the frame
frame_0 = [[b]*cols for row in range(rows)]
for row in range(0,20):
    for col in range(0,16):
        frame_0[row][col] = frame_1[row][col+3]

im_fill(frame_0, [12, 12], [13, 18], r)
im_fill(frame_0, [11,14 ], [13,13 ], r)
im_fill(frame_0, [11,12 ], [14,16 ], r)   
im_fill(frame_0, [12,12 ], [15,15 ], r)


frame_1 = np.array(list(frame_0))
y = "dbd11c"
im_fill(frame_1, [12,12], [19,19] , y)


frame_2 =  [[b]*cols for row in range(rows)]
im_fill(frame_2, [12,12], [0,0] , y)

frame_3 =  [[b]*cols for row in range(rows)]
im_fill(frame_3, [12,12], [1,1] , y)

frame_4 = [[b]*cols for row in range(rows)]
im_fill(frame_4, [12,12], [2,2] , y)

frame_5 = [[b]*cols for row in range(rows)]
im_fill(frame_5, [12,12], [3,3] , y)

frame_6 = [[b]*cols for row in range(rows)]
im_fill(frame_6, [12,12], [4,4] , y)

frame_7 = [[b]*cols for row in range(rows)]
im_fill(frame_7, [12,12], [5,5] , y)

frame_8 = [[b]*cols for row in range(rows)]
im_fill(frame_8, [12,12], [6,6] , y)

frame_9 = [[b]*cols for row in range(rows)]
im_fill(frame_9, [12,12], [7,7] , y)

frame_10 = [[b]*cols for row in range(rows)]
im_fill(frame_10, [12,12], [8,8] , y)

frame_11 = [[b]*cols for row in range(rows)]
im_fill(frame_11, [12,12], [9,9] , y)

frame_12 = [[b]*cols for row in range(rows)]
im_fill(frame_12, [12,12], [10,10] , y)

frame_13 = [[b]*cols for row in range(rows)]
im_fill(frame_13, [12,12], [11,11] , y)

frame_14 = [[b]*cols for row in range(rows)]
im_fill(frame_14, [12,12], [12,12] , y)

frame_15 = [[b]*cols for row in range(rows)]
im_fill(frame_15, [12,12], [13,13] , y)

frame_16 = [[b]*cols for row in range(rows)]
im_fill(frame_16, [12,12], [14,14] , y)

frame_17 = [[b]*cols for row in range(rows)]
im_fill(frame_17, [12,12], [15,15] , y)

frame_18 = [[b]*cols for row in range(rows)]
im_fill(frame_18, [12,12], [16,16] , y)

frame_19 = [[b]*cols for row in range(rows)]
im_fill(frame_19, [12,12], [17,17] , y)

frame_20 = [[b]*cols for row in range(rows)]
im_fill(frame_20, [12,12], [18,18] , y)

frame_21 = [[b]*cols for row in range(rows)]
im_fill(frame_21, [12,12], [19,19] , y)

red    = "f81800"
yellow = "ffff24"
blue   = "00dbff"
black  = "000000"
white = "ffffff"

total_rows = 20
total_cols = 20

target = [[black]*total_cols for rows in range(total_rows)]
im_fill(target, [5, 5], [6, 14], red)
im_fill(target, [6, 6], [6, 14], blue)
im_fill(target, [6,13], [5,5], red)
im_fill(target, [14,14], [6,14], red)
im_fill(target, [6,13], [6,6], blue) 
im_fill(target, [13,13], [6,14], blue) 
im_fill(target, [6,13], [14,14], blue) 
im_fill(target, [14,14], [6,14], red) 
im_fill(target, [6,13], [15,15], red) 
# Drawing inner red
im_fill(target, [12,12], [7,13], red) 
im_fill(target, [7,12], [7,7], red) 
im_fill(target, [7,12], [13,13], red) 
im_fill(target, [7,7], [7,13], red) 
#yellow
im_fill(target, [8,11], [8,8], yellow) 
im_fill(target, [11,11], [8,12], yellow) 
im_fill(target, [8,11], [12,12], yellow) 
im_fill(target, [8,8], [8,12], yellow) 
 #target
im_fill(target, [9,10], [9,11], red)   


# Target hit
target_hit = [[black]*total_cols for rows in range(total_rows)]
#small pieces
target_hit[2][4] = yellow
target_hit[2][14] = yellow
target_hit[13][4] = yellow
target_hit[13][14] = yellow
#outer ring
im_fill(target_hit, [4,11], [5,5], yellow)
im_fill(target_hit, [11,11], [5,13], yellow)
im_fill(target_hit, [4,11], [13,13], yellow)
im_fill(target_hit, [4,4], [5,13], yellow)
#inner ring
im_fill(target_hit, [6,6], [7,11], yellow)
im_fill(target_hit, [6,9], [7,7], yellow)
im_fill(target_hit, [9,9], [7,11], yellow)
im_fill(target_hit, [6,9], [11,11], yellow)
#outer pieces
im_fill(target_hit, [1,1], [8,10], yellow)
im_fill(target_hit, [0,2], [9,9], yellow)
im_fill(target_hit, [7,7], [1,2], yellow)
im_fill(target_hit, [6,8], [2,2], yellow)
im_fill(target_hit, [7,7], [15,16], yellow)
im_fill(target_hit, [6,8], [15,15], yellow)
im_fill(target_hit, [13,15], [9,9], yellow)
im_fill(target_hit, [14,14], [8,10], yellow)
target_2 = np.array([])
target_2 = np.array(list(target))
move_by = 2
#wrap-around y axis code, include include in move_by 
for col in range (numpy.array(target).shape[0]-move_by):
    for row in range (numpy.array(target).shape[1]):
        target_2[col+move_by][row] = target[col][row]
         
for col in range(move_by,-1,-1):
    for row in range (numpy.array(target).shape[1]):
        target_2[move_by - col][row] = target[numpy.array(target).shape[0]-1-col][row]




# Target bullet 1 
target_bullet1 = map(list,target_2)
target_bullet1[12][0] = yellow
# target_bullet 2
target_bullet2 = map(list,target_2)
target_bullet2[12][1] = yellow
# target_bullet 3
target_bullet3=map(list,target_2)
target_bullet3[12][2] = yellow
#target_bullet 4
target_bullet4 = map(list,target_2)
target_bullet4[12][3] = yellow
#target_bullet5
target_bullet5=map(list,target_2)
target_bullet5[12][4] = yellow
#intro
frame_a = [[b]*cols for row in range(rows)]
frame_a[0][3] = r
frame_a[0][2] = r
frame_a[0][4] = r
frame_a[1][2] = r
frame_a[2][3] = r
frame_a[3][2] = r
frame_a[3][3] = r
frame_a[3][4] = r
frame_a[0][6] = r
frame_a[0][7] = r
frame_a[0][8] = r
frame_a[1][7] = r
frame_a[2][7] = r
frame_a[3][7] = r
frame_a[0][10] = r
frame_a[0][11] = r
frame_a[0][12] = r
frame_a[1][11] = r
frame_a[2][11] = r
frame_a[3][10] = r
frame_a[3][11] = r
frame_a[3][12] = r
frame_a[1][14] = r
frame_a[1][15] = r
frame_a[2][14] = r
frame_a[3][14] = r
frame_a[3][15] = r
frame_a[0][17] = r
frame_a[1][17] = r
frame_a[1][18] = r
frame_a[0][19] = r
frame_a[2][18] = r
frame_a[2][19] = r
frame_a[3][19] = r
im_fill(frame_a,[6,9], [12,12], r)
im_fill(frame_a,[6,6], [12,14], r)
im_fill(frame_a,[8,8], [12,14], r)
im_fill(frame_a,[6,9], [14,14], r)
im_fill(frame_a,[6,9], [6,6], r)
im_fill(frame_a,[9,9], [6,7], r)
im_fill(frame_a,[8,8], [8,8], r)
im_fill(frame_a,[9,9], [9,10], r)
im_fill(frame_a,[6,9], [6,9], r)
im_fill(frame_a,[6,9], [16,16], r)
im_fill(frame_a,[2,3], [17,17], r)
im_fill(frame_a,[6,8], [7,7], b)
im_fill(frame_a,[6,8], [9,9], b)
im_fill(frame_a,[6,8], [10,10], r)
im_fill(frame_a,[6,6], [17,18], r)
frame_a[7][18] = r
frame_a[8][17] = r
frame_a[9][18] = r
frame_a[1][15] = b
frame_a[0][14] = r
frame_a[0][15] = r








frame_list = [frame_a,frame_0,frame_1,frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,
frame_8,frame_9,frame_10,frame_11,frame_12,frame_13,frame_14,frame_15,frame_16,
frame_17,frame_18,frame_19,frame_20,frame_21, target_2, target_bullet1, target_bullet2,
target_bullet3, target_bullet4, target_bullet5, target_hit, target_hit, target_hit,
target_hit,target_hit]

fps =5
play_video = vid_show(frame_list,fps)
#save_vid(frame_list,fps,'output_fast.gif')
