from AOLME import *

# Define the size of the image
rows = 4  # num of rows
cols = 3  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff" # blue code

# Create frame 0 with the same background color
frame0 = np.array([[r]*cols for row in range (rows)])

# Create frame 1 with the same background color
frame1 = frame0.copy()

# Change pixels
frame1[0][2] = b
frame1[3][2] = b

# im_fill example
start_row = 1
end_row   = 2
start_col = 0
end_col   = 1
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)


# Video play
frame_list = [frame0, frame1]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen