from AOLME import *

# Define the size of the image
rows = 50  # num of rows
cols = 50  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff"
g = "00cc44"
y = "ffff66"
p = "ff1a8c"
o = "ff3300"
bl = "000000"
# Create frame 0 with the same background color
frame0 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame0,[0,4],[0,0], b)
im_fill(frame0,[0,0],[0,2], b)
im_fill(frame0,[4,4],[0,2], b)
frame0[1][3]  = b
frame0[3][3]  = b
frame0[2][4]  = b

#v
im_fill(frame0,[0,2],[10,10], b)
im_fill(frame0,[0,2],[6,6], b)
frame0[3][7]  = b
frame0[3][9]  = b
frame0[4][8]  = b

#d
im_fill(frame0,[0,4],[12,12], b)
im_fill(frame0,[0,0],[12,14], b)
im_fill(frame0,[4,4],[12,14], b)
frame0[1][15]  = b
frame0[2][16]  = b
frame0[3][15]  = b

# Create frame 1 with the same background color
frame1 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame1,[10,10],[6,8], b)
im_fill(frame1,[10,14],[6,6], b)
im_fill(frame1,[14 ,14],[7,8], b)
frame1[11][9]  = b
frame1[12][10]  = b
frame1[13][9]  = b

#v
im_fill(frame1,[10,12],[12,12], b)
im_fill(frame1,[10,12],[16,16], b)
frame1[13][13]  = b
frame1[14][14]  = b
frame1[13][15]  = b

#d
im_fill(frame1,[10,14],[18,18], b)
im_fill(frame1,[14,14],[19,20], b)
im_fill(frame1,[10,10],[18,20], b)
frame1[11][21]  = b
frame1[12][22]  = b
frame1[13][21]  = b

frame2 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame2,[20,24],[12,12], b)
im_fill(frame2,[20,20],[12,14], b)
im_fill(frame2,[24 ,24],[12,14], b)
frame2[21][15]  = b
frame2[22][16]  = b
frame2[23][15]  = b

#v
im_fill(frame2,[20,22],[18,18], b)
im_fill(frame2,[20,22],[22,22], b)
frame2[23][19]  = b
frame2[24][20]  = b
frame2[23][21]  = b

#d
im_fill(frame2,[10,14],[18,18], b)
im_fill(frame2,[14,14],[19,20], b)
im_fill(frame2,[10,10],[18,20], b)
frame2[11][21]  = b
frame2[12][22]  = b
frame2[13][21]  = b

# Video play
frame_list = [frame0, frame1, frame2]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen