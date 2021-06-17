from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20  # num of cols

# Define all of the colors
w = "FFFFFF" # white code
lb= "B45F04" # light brown code
b= "000000" #black code
sb= "00ffff" #sky blue code
br= "613801" #brown code
y= "ffff00" # yellow

# Create frame 0 with the same background color
frame0 = np.array([[sb]*cols for row in range (rows)])

# Specify the frame row-by-row
frame0[1] = [sb, sb, sb, sb, sb, sb, w, w, w, w, sb, sb, sb, sb, sb, y, y, y, sb, sb]
frame0[2] = [sb, sb, sb, sb, sb, w, w, w, w, w, w, sb, sb, sb, y, y, y, y, y, sb]
frame0[3] = [sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, y, y, y, sb, sb]

frame0[11] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame0[12] = [sb, sb, sb, sb, b, b, b, b, b, b, br, br, sb, sb, br, br, sb, sb, sb, sb]
frame0[13] = [sb, sb, sb, sb, br, br, b, b, b, b, br, sb, sb, sb, br, br, sb, sb, sb, sb]
frame0[14] = [sb, sb, sb, sb, br, br, br, br, b, b, b, b, br, br, br, br, sb, sb, sb, sb]
frame0[15] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame0[16] = [sb, sb, sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, sb, sb, sb, sb]
frame0[17] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame0[18] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame0[19] = [lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb]

# Create frame 1 with the same background color
frame1 = np.array([[sb ]*cols for row in range (rows)])

# Specify the second frame row-by-row
frame1[1] = [sb, sb, sb, sb, sb, sb, w, w, w, w, sb, sb, sb, sb, sb, y, y, y, sb, sb]
frame1[2] = [sb, sb, sb, sb, sb, w, w, w, w, w, w, sb, sb, sb, y, y, y, y, y, sb]
frame1[3] = [sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, y, y, y, sb, sb]

frame1[11] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame1[12] = [sb, sb, sb, sb, b, b, b, b, b, b, br, br, sb, sb, br, br, sb, sb, sb, sb]
frame1[13] = [sb, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, sb]
frame1[14] = [sb, sb, sb, sb, br, br, br, br, b, b, b, b, br, br, br, br, sb, sb, sb, sb]
frame1[15] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame1[16] = [sb, sb, sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, sb, sb, sb, sb]
frame1[17] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]   
frame1[18] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame1[19] = [lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb]

# Create frame 2 with the same background color
frame2 = np.array([[sb]*cols for row in range (rows)])

# Specify the frame row-by-row
frame2[1] = [sb, sb, sb, sb, sb, sb, w, w, w, w, sb, sb, sb, sb, sb, y, y, y, sb, sb]
frame2[2] = [sb, sb, sb, sb, sb, w, w, w, w, w, w, sb, sb, sb, y, y, y, y, y, sb]
frame2[3] = [sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, y, y, y, sb, sb]

frame2[11] = [sb, sb, sb, sb, br, br, b, b, b, b, br, br, br, br, br, br, sb, sb, sb, sb]
frame2[12] = [sb, sb, sb, sb, b, b, b, b, b, b, br, br, sb, sb, br, br, sb, sb, sb, sb]
frame2[13] = [sb, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, sb]
frame2[14] = [sb, sb, sb, sb, br, br, br, br, b, b, b, b, br, br, br, br, sb, sb, sb, sb]
frame2[15] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame2[16] = [sb, sb, sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, sb, sb, sb, sb]
frame2[17] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame2[18] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame2[19] = [lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb]


# Create frame 3 with the same background color
frame3 = np.array([[sb ]*cols for row in range (rows)])

# Specify the second frame row-by-row
frame3[1] = [sb, sb, sb, sb, sb, sb, w, w, w, w, sb, sb, sb, sb, sb, y, y, y, sb, sb]
frame3[2] = [sb, sb, sb, sb, sb, w, w, w, w, w, w, sb, sb, sb, y, y, y, y, y, sb]
frame3[3] = [sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, y, y, y, sb, sb]

frame3[10] = [sb, sb, sb, sb, sb, sb, b, b, b, b, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb]
frame3[11] = [sb, sb, sb, sb, b, b, b, b, b, b, br, br, br, br, br, br, sb, sb, sb, sb]
frame3[12] = [sb, sb, sb, sb, br, br, sb, sb, br, br, br, br, sb, sb, br, br, sb, sb, sb, sb]
frame3[13] = [sb, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, br, br, sb, sb, sb, sb]
frame3[14] = [sb, sb, sb, sb, br, br, br, br, b, b, b, b, br, br, br, br, sb, sb, sb, sb]
frame3[15] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame3[16] = [sb, sb, sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, sb, sb, sb, sb]
frame3[17] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]   
frame3[18] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame3[19] = [lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb]


# Create frame 3 with the same background color
frame4 = np.array([[sb ]*cols for row in range (rows)])

# Specify the second frame row-by-row
frame4[1] = [sb, sb, sb, sb, sb, sb, w, w, w, w, sb, sb, sb, sb, sb, y, y, y, sb, sb]
frame4[2] = [sb, sb, sb, sb, sb, w, w, w, w, w, w, sb, sb, sb, y, y, y, y, y, sb]
frame4[3] = [sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb, y, y, y, sb, sb]

frame4[10] = [sb, sb, sb, sb, sb, sb, b, b, b, b, sb, sb, sb, sb, sb, sb, sb, sb, sb, sb]
frame4[11] = [sb, sb, sb, sb, b, b, b, b, b, b, br, br, br, br, br, br, sb, sb, sb, sb]
frame4[12] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, br, br, sb, sb, sb, sb]
frame4[13] = [sb, sb, sb, sb, br, br, lb, lb, lb, br, br, sb, sb, sb, br, br, sb, sb, sb, sb]
frame4[14] = [sb, sb, sb, sb, br, br, br, br, b, b, b, b, br, br, br, br, sb, sb, sb, sb]
frame4[15] = [sb, sb, sb, sb, br, br, br, br, br, br, br, br, br, br, br, br, sb, sb, sb, sb]
frame4[16] = [sb, sb, sb, sb, sb, sb, br, br, br, br, br, br, br, br, sb, sb, sb, sb, sb, sb]
frame4[17] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]   
frame4[18] = [sb, sb, lb, lb, lb, lb, br, br, lb, lb, lb, lb, br, br, lb, lb, lb, lb, sb, sb]
frame4[19] = [lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb, lb]

# Create frame 5 with the same background color
frame5 = np.array([[sb ]*cols for row in range (rows)])

# Specify the second frame row-by-row
frame5[0] = [w, w, w, w, w, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b]
frame5[1] = [b, b, w, b, b, b, w, b, b, b, w, w, w, b, b, b, b, b, b, b]
frame5[2] = [b, b, w, b, b, b, w, w, w, b, w, b, b, b, b, b, b, b, b, b]
frame5[3] = [b, b, w, b, b, b, w, b, w, b, w, w, b, b, b, b, b, b, b, b]
frame5[4] = [b, b, w, b, b, b, w, b, w, b, w, b, b, b, b, b, b, b, b, b]
frame5[5] = [w, w, w, b, b, b, b, b, b, b, w, w, w, b, b, b, b, w, w, w]
frame5[6] = [w, b, w, b, w, b, b, b, b, b, b, b, b, b, w, b, b, w, b, b]
frame5[7] = [w, w, w, b, b, b, b, b, b, w, w, w, b, w, w, w, b, w, w, b]
frame5[8] = [w, b, b, b, w, b, w, w, b, w, b, w, b, b, w, b, b, w, b, b]
frame5[9] = [w, b, b, b, w, b, w, b, b, w, w, w, w, b, w, b, b, w, w, w]
frame5[10] = [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
frame5[11] = [w, w, w, b, w, b, w, b, w, w, w, b, w, w, w, b, w, b, b, w]
frame5[12] = [w, b, w, b, w, b, w, b, w, b, w, b, w, b, w, b, b, w, b, w]
frame5[13] = [w, w, w, b, w, w, w, b, w, w, w, b, w, w, w, b, b, b, w, w]
frame5[14] = [w, b, b, b, b, b, b, b, w, b, b, b, w, b, b, b, b, b, b, w]
frame5[15] = [w, b, b, b, b, b, b, b, w, b, b, b, w, b, b, b, b, b, b, w]
frame5[16] = [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
frame5[17] = [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]   
frame5[18] = [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
frame5[19] = [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]

# Video play
frame_list = [frame0, frame1, frame2, frame3, frame4, frame5]         # list of frames
fps= 10                               # frames per sec
play_video= vid_show(frame_list, fps) # play on screen
