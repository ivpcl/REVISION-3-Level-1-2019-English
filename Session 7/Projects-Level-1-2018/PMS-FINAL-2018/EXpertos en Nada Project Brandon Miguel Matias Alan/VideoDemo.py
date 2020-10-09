from AOLME import *

# Define the image size:
rows = 20
cols = 20

# Define the colors:
r="fe0606"
v="157f11"

# Initialize the background
backg = np.array([[r]*cols for row in range (rows)])

# Copy the background:
frame1 = backg.copy()

# CREATE THE CHARACTER
im_fill(frame1,[2,4],[9,11], v)
frame1[3][8]  = '0000ff'

# UNCOMMENT the following
frame1[10:13,8:12] = frame1[2:5,8:12]

# Move the character by +2 to the right.
frame2 = backg.copy() # Copy background.

move_r = 2
for row in range(rows):
    for col in range(cols-move_r):
        frame2[row][col+move_r] = frame1[row][col]


# Move the object by +2 down
frame3 = backg.copy() # Copy background.

move_d = 2
for row in range(rows-move_d):
    for col in range(cols):
        frame3[row+move_d][col] = frame2[row][col]

#im_show(frame3)

# Move the object by +2 to the left.
frame4 = backg.copy() # Copy background.

move_l = 2
for row in range(rows):
    for col in range(move_l, cols):
        frame4[row][col-move_l] = frame3[row][col]

# Move the object by +2 up
frame5 = backg.copy() # Copy background.

move_u = 2
for row in range(move_u, rows):
    for col in range(cols):
        frame5[row-move_d][col] = frame4[row][col]


# Show a single image:
# Uncommend the im_show() commands to show single images.
#im_show(frame5)

# Create a frame list of all of the frames
#frame_list = [frame1, frame2, frame3, frame4, frame5]
frame_list = [frame1]
# Setup the number of frames per second
fps= 2  

# Play the video
play_video= vid_show(frame_list, fps)
