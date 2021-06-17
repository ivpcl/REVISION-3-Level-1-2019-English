from AOLME import *

# Define the image size:
rows = 20
cols = 20

# Define the colors:
L="00FF00" # lime grass
o="FF8C00" #orange
R="FF0000"#red
B1="00FF7F"#blue
P="800080"#purple
DP="4B0082"#dark puple
G="ABABAB"#gray
Y="FFFF00"#yellow
JA="FFB3CC"#LIGHT PINK
B2="00F7FF"#light blue
ED="FA8072"#SALMON 
JR="C71585"#MEDIUMVIOLETRED
DR="00008B"#DARKBLUE
v="EE82EE"# violite
BL="000000"
SG="2E8B57"
LG="32cd32"#lime green
SS="320000"#sea green 
LB="add8e6"#light blue
LBG="0000a0"#light blueish green 
backg = np.array([[LB]*cols for row in range (rows)])


# Copy the background into a frame:
frame1 = backg.copy()
# Create the character
im_fill(frame1,[12,19],[0,19], LBG)



# Make a second copy of the character
#frame1[10:13,8:19] = frame1[2:5,8:19]

# Move the character by +2 to the right.
frame2 = frame1.copy() # Copy background.
im_fill(frame2,[4,9],[2,8], LG)
im_fill(frame2,[6,6],[4,4], BL)
im_fill(frame2,[6,6],[6,6], BL)
im_fill(frame2,[7,7],[5,5], BL)
im_fill(frame2,[8,8],[4,6], BL)
im_fill(frame2,[9,9],[4,4], BL)
im_fill(frame2,[9,9],[6,6], BL)
im_fill(frame2,[9,15],[3,7],SS)
# move_r = 2
# for row in range(rows):
#     for col in range(cols-move_r):
#         frame2[row][col+move_r] = frame1[row][col]
# 
# =============================================================================

# Move the object by +2 down
#frame3 = backg.copy() # Copy background.

# =============================================================================
# move_d = 2
# for row in range(rows-move_d):
#     for col in range(cols):
#         frame3[row+move_d][col] = frame2[row][col]
# 
# =============================================================================
#im_show(frame3)

# Move the object by +2 to the left.
#frame4 = backg.copy() # Copy background.

# =============================================================================
# move_l = 2
# for row in range(rows):
#     for col in range(move_l, cols):
#         frame4[row][col-move_l] = frame3[row][col]
# =============================================================================

# Move the object by +2 up
#frame5 = backg.copy() # Copy background.

# =============================================================================
# move_u = 2
# for row in range(move_u, rows):
#     for col in range(cols):
#         frame5[row-move_d][col] = frame4[row][col]
# 
# =============================================================================

# Show a single image:
# Uncommend the im_show() commands to show single images.
#im_show(frame5)

# Create a frame list of all of the frames
frame_list = [frame1, frame2]

# Setup the number of frames per second
fps= 1

# Play the video
play_video= vid_show(frame_list, fps)
