# Define the size of the image
from AOLME import *

rows = 20 # num of rows
cols = 20 # num of cols

# Define all of the colors
bl = "000000" #black code
w  = "ffffff" #white
r = "ff0000" # red code
g = "00ff00" #green code
b = "0f0fff" # blue code
br = "8b4513" # brown code
y = "ffff00" #yellow code

# Create a frame with the same background color
frame0 = np.array([[r]*cols for row in range (rows)])


# head
start_row = 9
end_row   = 11 
start_col = 2
end_col   = 5
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#body
start_row = 13
end_row   = 15 
start_col = 2
end_col   = 5
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)
#neck
start_row = 12
end_row   = 13 
start_col = 3
end_col   = 4
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#left arm
start_row = 13
end_row   = 13 
start_col = 0
end_col   = 1
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#right arm
start_row = 13
end_row   = 13 
start_col = 6
end_col   = 7
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#left leg
start_row = 16
end_row   = 16 
start_col = 2
end_col   = 2
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#right leg
start_row = 16
end_row   = 16 
start_col = 5
end_col   = 5
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

# shoe
start_row = 17
end_row   = 17 
start_col = 2
end_col   = 3
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)
start_row = 17
end_row   = 17 
start_col = 5
end_col   = 6
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#eyes
start_row = 10 
end_row   = 10 
start_col = 3
end_col   = 3
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)
start_row = 10
end_row   = 10 
start_col = 5
end_col   = 5
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

#floor 
start_row = 18
end_row   = 19 
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], br)

#hair
start_row = 6
end_row   = 8
start_col = 3
end_col   = 4
im_fill(frame0, [start_row, end_row], [start_col, end_col], y)

im_show(frame0)

frame1 = frame0.copy()

# Base
start_row = 15
end_row   = 15
start_col = 10
end_col   = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)
im_fill(frame1, [16, 17], [11, 15], g)

# stem
frame1[14,13] = g
im_fill(frame1, [13, 13], [11, 15], y)

# eyes
start_row = 12
end_row   = 12
start_col = 11
end_col   = 11
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)
start_row = 12
end_row   = 12
start_col = 13
end_col   = 13
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)
start_row = 12
end_row   = 12
start_col = 15
end_col   = 15
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)
start_row = 11
end_row   = 11
start_col = 12
end_col   = 14
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)
start_row = 10
end_row   = 10
start_col = 13
end_col   = 13
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)

frame2 = frame1.copy()
im_fill(frame2, [10, 13], [11, 15], r)

frame2[7:11, 11:16] = frame1[10:14, 11:16]
# stem
frame2[14,13] = g

im_fill(frame2, [11, 13], [13, 13], g)

frame3 = frame1.copy()
im_fill(frame3, [10, 13], [11, 15], r)

frame3[4:8, 11:16] = frame1[10:14, 11:16]
# stem
frame3[14,13] = g

im_fill(frame3,[8,15], [13, 13], g)

im_show(frame3)

frame4 = frame1.copy()
im_fill(frame4, [10, 13], [11, 15], r)

frame4[2:6, 11:16] = frame1[10:14, 11:16]
# stem
frame4[14,13] = g

im_fill(frame4, [6, 13], [13, 13], g)

# Video play
frame_list = [frame0, frame1,frame2,frame3,frame4]         # list of frames
fps= 1                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen