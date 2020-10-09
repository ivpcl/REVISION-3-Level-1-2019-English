from AOLME import *

lg = "00ff00"
dg = "00cc00"
ld = "996623"
dd = "663300"
lb ="33ccff"
db = "0066cc"
b = "000000"
s = "80aaff"
y = "ffff00"

total_columns= 20
total_rows = 20
checkerboard = np.array([[s]*total_columns for row  in range(total_rows)])

checkerboard  [1][3]=dg
checkerboard  [2][3]=dg
checkerboard  [2][4]=dg
checkerboard  [3][0]=dg
checkerboard  [3][3]=dg
checkerboard  [3][5]=dg
checkerboard  [4][3]=dg
checkerboard  [4][6]=dg
checkerboard  [4][1]=dg
im_fill(checkerboard,[5,5],[2,7],dg)
checkerboard  [4][0]=lg
checkerboard  [5][0]=lg
checkerboard  [5][1]=lg
checkerboard  [3][4]=lg
checkerboard  [4][4]=lg
checkerboard  [4][5]=lg
im_fill(checkerboard,[6,6],[1,7],lg)
im_fill(checkerboard,[5,8],[1,1],lg)
im_fill(checkerboard,[7,7],[2,7],dg)
checkerboard  [8][0]=lg
checkerboard  [8][2]=dg
checkerboard  [8][4]=dg
checkerboard  [8][6]=dg
checkerboard  [9][1]=dg
checkerboard  [9][4]=dg
checkerboard  [9][5]=dg
checkerboard  [10][0]=dg
checkerboard  [10][4]=dg
checkerboard  [8][0]=lg
checkerboard  [9][0]=lg
checkerboard  [4][13]=dd
checkerboard  [4][14]=dd

## Code for Bird ##

im_fill(checkerboard,[5,5],[8,12],dd)
im_fill(checkerboard,[6,6],[8,15],ld)
im_fill(checkerboard,[7,7],[8,12],dd)
checkerboard  [5][13]=ld
checkerboard  [5][14]=b
checkerboard  [5][15]=dd
checkerboard  [6][16]=y
checkerboard  [6][17]=y
checkerboard  [7][13]=ld
checkerboard  [7][14]=dd
checkerboard  [7][15]=dd
checkerboard  [8][13]=dd
checkerboard  [8][5]=lg
im_fill(checkerboard,[18,18],[0,19],lb)
im_fill(checkerboard,[19,19],[0,19],lb)

frame_2=checkerboard.copy()
frame_3=checkerboard.copy()
frame_4=checkerboard.copy()

##code for island ##
checkerboard  [15][12]=lg
checkerboard  [14][13]=lg
checkerboard  [15][13]=lg
checkerboard  [14][14]=lg
checkerboard  [15][14]=lg
checkerboard  [14][15]=lg
checkerboard  [15][15]=lg
checkerboard  [15][16]=lg
checkerboard  [16][14]=ld
checkerboard  [17][14]=ld
checkerboard  [19][12]=y
checkerboard  [19][13]=y
checkerboard  [19][14]=y
checkerboard  [19][15]=y
checkerboard  [19][16]=y
checkerboard  [18][13]=y
checkerboard  [18][14]=y
checkerboard  [18][15]=y

##im_show (checkerboard)

##code for wings ##
frame_2  [8][8]=dd
frame_2  [9][8]=dd
frame_2  [10][8]=dd
frame_2  [11][8]=ld
frame_2  [12][8]=dd
frame_2  [11][9]=dd
frame_2  [10][10]=dd
frame_2  [9][11]=dd
frame_2  [8][12]=dd
frame_2  [8][9]=ld
frame_2  [9][10]=ld
frame_2  [10][9]=ld
frame_2  [8][11]=ld
frame_2  [11][8]=dd
frame_2  [9][9]=ld
frame_2  [8][10]=ld
##pixel shift for island ##
frame_2  [15][10]=lg
frame_2   [14][11]=lg
frame_2   [15][11]=lg
frame_2   [14][12]=lg
frame_2   [15][12]=lg
frame_2   [14][13]=lg
frame_2   [15][13]=lg
frame_2   [15][14]=lg
frame_2   [16][12]=ld
frame_2   [17][12]=ld
frame_2   [19][10]=y
frame_2   [19][11]=y
frame_2   [19][12]=y
frame_2   [19][13]=y
frame_2   [19][14]=y
frame_2   [18][11]=y
frame_2   [18][12]=y
frame_2   [18][13]=y


##im_show(frame_2)


## code for lower wing##
frame_3  [8][8]=dd
frame_3  [9][8]=dd
frame_3  [10][8]=dd
frame_3  [10][9]=dd
frame_3  [9][10]=dd
frame_3  [8][11]=dd
frame_3  [8][9]=ld
frame_3  [8][10]=ld
frame_3  [9][9]=ld
frame_3  [9][10]=ld
frame_3  [8][12]=ld
frame_3  [9][10]=dd
frame_3  [8][13]=s
frame_3  [8][12]=s
##pixel shift code for island##
frame_3   [15][8]=lg
frame_3   [14][9]=lg
frame_3   [15][8]=lg
frame_3   [14][10]=lg
frame_3   [15][10]=lg
frame_3   [15][9]=lg
frame_3   [14][11]=lg
frame_3   [15][11]=lg
frame_3   [15][12]=lg
frame_3   [16][10]=ld
frame_3   [17][10]=ld
frame_3   [19][8]=y
frame_3   [19][9]=y
frame_3   [19][10]=y
frame_3   [19][11]=y
frame_3   [19][12]=y
frame_3   [18][9]=y
frame_3   [18][10]=y
frame_3   [18][11]=y

## Code for Upper wing##

frame_3  [4][8] =dd
frame_3  [3][8] =dd
frame_3  [2][8] =dd
frame_3  [2][9] =dd
frame_3  [3][10] =dd
frame_3  [4][11] =dd
frame_3  [3][9] =ld
frame_3  [4][9] =ld
frame_3  [4][10] =ld

##im_show (frame_3)

##code for wings ##
frame_4  [8][8]=dd
frame_4  [9][8]=dd
frame_4  [10][8]=dd
frame_4  [11][8]=ld
frame_4  [12][8]=dd
frame_4  [11][9]=dd
frame_4  [10][10]=dd
frame_4  [9][11]=dd
frame_4  [8][12]=dd
frame_4  [8][9]=ld
frame_4  [9][10]=ld
frame_4  [10][9]=ld
frame_4  [8][11]=ld
frame_4  [11][8]=dd
frame_4  [9][9]=ld
frame_4  [8][10]=ld

##code for upper wing ##

frame_4  [1][8]=dd
frame_4  [2][8]=dd
frame_4  [2][9]=ld
frame_4  [2][10]=dd
frame_4  [3][8]=dd
frame_4  [3][9]=ld
frame_4  [3][10]=ld
frame_4  [3][11]=dd
frame_4  [4][8]=dd
frame_4  [4][9]=ld
frame_4  [4][10]=ld
frame_4  [4][11]=ld
frame_4  [4][12]=dd


##pixel shift for island ##
frame_4  [15][6]=lg
frame_4   [14][7]=lg
frame_4   [14][8]=lg
frame_4   [15][7]=lg
frame_4   [14][8]=lg
frame_4   [15][8]=lg
frame_4   [14][9]=lg
frame_4   [15][9]=lg
frame_4   [15][10]=lg
frame_4   [16][8]=ld
frame_4   [17][8]=ld
frame_4   [19][6]=y

frame_4   [19][8]=y
frame_4   [19][7]=y
frame_4   [19][9]=y
frame_4   [19][10]=y
frame_4   [18][7]=y
frame_4   [18][8]=y
frame_4   [18][9]=y

##im_show (frame_4)


##Code for running the video##

frame_list = [checkerboard, frame_2, frame_3, frame_4]

fps = 4

play_video = vid_show(frame_list, fps)
#save_vid(frame_list,fps,'output_Happywheels.gif')

















