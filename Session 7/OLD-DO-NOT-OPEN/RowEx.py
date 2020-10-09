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

# Change a single row:
frame2[0] = [v, v, v]  # CHANGE FULL ROW OF 3 PIXELS

# Create a frame list of all of the frames
frame_list = [frame1, frame2]

# Setup the number of frames per second
fps= 2  

# Play the video
play_video= vid_show(frame_list, fps)
