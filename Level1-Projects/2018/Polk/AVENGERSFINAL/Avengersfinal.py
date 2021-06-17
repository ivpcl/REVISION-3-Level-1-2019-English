from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20 # num of cols

# Define all of the colors
lp = "9900ff" # light purple code
p = "be00ff" # purple code
y = "d0f20c" # yellow code
g = "17b013" # green code
lb = "0fa9ec" # light blue code
db = "1e61cc" # dark blue
b = "0050ff" # blue
pk = "f50caf" # pink
lpk = "ec7eeb" # light pink
r = "f20c0c" # red
o = "f2970c" # orange
aq = "26f3f0"# aqua
w = "ffffff" # white
# Create frame 0 with the same background color
frame0 = np.array([[db]*cols for row in range (rows)])

# Specify the frame row-by-row
frame1 = frame0.copy()
frame1[0][1] = p
frame1[0][6] = b
frame1[0][11] = pk
frame1[0][16] = r


frame2 = frame1.copy()
frame2[2][2] = p
frame2[2][7] = b
frame2[2][12] = pk
frame2[2][17] = r

frame3 = frame2.copy()
frame3[4][3] = p
frame3[4][8] = b
frame3[4][13] = pk
frame3[4][18] = r

frame4 = frame3.copy()
frame4[6][2] = p
frame4[6][7] = b
frame4[6][12] = pk
frame4[6][17] = r

frame5 = frame4.copy()
frame5[8][1] = p
frame5[8][6] = b
frame5[8][11] = pk
frame5[8][16] = r

frame6 = frame5.copy()
frame6[10][2] = p
frame6[10][7] = b
frame6[10][12] = pk
frame6[10][17] = r

frame7 = frame6.copy()
frame7[12][3] = p
frame7[12][8] = b
frame7[12][13] = pk
frame7[12][18] = r

frame8 = frame7.copy()
frame8[14][2] = p
frame8[14][7] = b
frame8[14][12] = pk
frame8[14][17] = r

frame9 = frame8.copy()
frame9[16][1] = p
frame9[16][6] = b
frame9[16][11] = pk
frame9[16][16] = r

frame10 = frame9.copy()
frame10[18][2] = p
frame10[18][7] = b
frame10[18][12] = pk
frame10[18][18] = r

#grass
im_fill(frame10,[18,19],[0,19], g)








# Create frame 0 with the same background color
frame0 = np.array([[lb]*cols for row in range (rows)])

#frame10 = np.array([[lb]*cols for row in range (rows)])

# Create frame 1 with the same background color
frame12 = frame0.copy()

# Change pixels
#1st flower
frame12[12][1] = p
frame12[12][2] = lp 
frame12[12][3] = p
frame12[13][3] = lp
frame12[13][1] = lp 
frame12[13][2] = y
frame12[14][1] = p
frame12[14][2] = lp
frame12[14][3] = p
frame12[15][2] = g
frame12[16][2] = g
frame12[17][2] = g

#2nd flower
im_fill(frame12,[12,14],[6,8], b)
im_fill(frame12,[15,17],[7,7], g)
frame12[12][6] = lb
frame12[12][8] = lb
frame12[14][6] = lb
frame12[14][8] = lb
frame12[13][7] = y

#3rd flower
im_fill(frame12,[12,14],[11,13], pk)
im_fill(frame12,[15,17],[12,12], g)
frame12[12][11] = lpk
frame12[13][11] = lpk
frame12[13][13] = lpk
frame12[14][13] = lpk
frame12[13][12] = y

#4th flower
im_fill(frame12,[12,14],[16,18], r)
im_fill(frame12,[15,17],[17,17], g)
frame12[12][16] = o
frame12[12][18] = o
frame12[14][16] = o
frame12[14][18] = o
frame12[13][17] = y

# Grass
im_fill(frame12,[18,19],[0,19], g)

#sun
im_fill(frame12,[0,2],[0,3], y)
im_fill(frame12,[0,5],[0,0], y)
frame12[6][1] = y
frame12[3][1] = y
frame12[4][2] = y
frame12[5][3] = y
frame12[3][4] = y
frame12[4][5] = y
frame12[0][4] = y
frame12[1][5] = y
frame12[2][6] = y

#cloud
im_fill(frame12,[5,7],[10,15], w)
frame12[6][9] = w
frame12[6][16] = w

# im_fill example
start_row = 2
end_row   = 3
start_col = 1
end_col   = 2
 

#im_fill(frame2, [start_row, end_row], [start_col, end_col], p)

# Video play
frame_list = [frame0,frame1,frame2, frame3,frame4,frame5,frame5,frame7,frame8,frame9,frame10,frame12,frame12,frame12]         # list of frames
fps= 10                           # frames per sec
play_video= vid_show(frame_list, fps) # play on screen

