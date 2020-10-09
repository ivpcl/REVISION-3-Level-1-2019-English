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
frame2[0][0] = v      # CHANGE A SINGLE PIXEL

# Video play
frame_list = [frame1, frame2]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen
