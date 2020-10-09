from AOLME import *

# Define the size of the image
rows = 2  # num of rows
cols = 2  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff" # blue code

# Create frame 0 with the same background color
frame0 = np.array([[r]*cols for row in range (rows)])

# Specify the frame row-by-row
frame0[0] = [r, b]
frame0[1] = [b, b]

# Create frame 1 with the same background color
frame1 = np.array([[r]*cols for row in range (rows)])

# Specify the second frame row-by-row
frame1[0] = [b, r]
frame1[1] = [b, b]


# Video play
frame_list = [frame0, frame1]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen