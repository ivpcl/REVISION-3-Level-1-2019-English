from AOLME import *

# Define the image size:
rows = 3
cols = 3

# Define the colors:
r="fe0606"
v="157f11"

# Initialize the background
backg = np.array([[r]*cols for row in range (rows)])

# Start with the background:
frame1 = backg.copy()
frame2 = backg.copy()

# im_fill example
start_row = 1
end_row   = 2
start_col = 0
end_col   = 1
im_fill(frame2, [start_row, end_row], [start_col, end_col], v)

im_show(frame1)

# Create a frame list of all of the frames
frame_list = [frame1, frame2]

# Setup the number of frames per second
fps= 2  

# Play the video
play_video= vid_show(frame_list, fps)
