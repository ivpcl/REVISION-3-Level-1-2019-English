from AOLME import *

# Define the image size:
rows = 20
cols = 20

# Define the colors:
OW="eae3e2"#off white
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
BL="000000"#Black
SG="2E8B57"# ?
LG="32cd32"#lime green
SS="320000"#sea green
LB="add8e6"#light blue
LBG="0000a0"#light blueish green
MCSC="F5DAA9"#sand
MCCC="CCCCCC"#clouds
MNM="A9A9A9"
WH="FFFAFA"
backg = np.array([[LB]*cols for row in range (rows)])


# Copy the background into a frame:
frame1 = backg.copy()

im_fill(frame1,[12,19],[0,19], LBG)
im_fill(frame1,[0,1],[10,14],MCCC)
im_fill(frame1,[0,1],[11,13],MCCC)
im_fill(frame1,[3,3],[11,14],MCCC)

# Make a second copy of the character
#frame1[10:13,8:19] = frame1[2:5,8:19]

# Move the character by +2 to the right.
frame2 = frame1.copy() # Copy background.
im_fill(frame2,[0,1],[10,14],MCCC)
im_fill(frame2,[0,1],[11,13],MCCC)
im_fill(frame2,[3,3],[11,14],MCCC)
im_fill(frame2,[12,19],[0,9],MCSC)
im_fill(frame2,[4,9],[2,8], LG)
im_fill(frame2,[9,15],[3,7],LG)
im_fill(frame2,[16,18],[2,4],LG)
im_fill(frame2,[16,18],[6,8],LG)
im_fill(frame2,[6,6],[4,4], BL)
im_fill(frame2,[6,6],[6,6], BL)
im_fill(frame2,[7,7],[5,5], BL)
im_fill(frame2,[8,8],[4,6], BL)
im_fill(frame2,[9,9],[4,4], BL)
im_fill(frame2,[9,9],[6,6], BL)
#im_fill(frame2,[9,9],[6,6], BL)
# move_r = 2
# for row in range(rows):
#     for col in range(cols-move_r):
#         frame2[row][col+move_r] = frame1[row][col]
#
# =============================================================================

# Move the object by +2 down
frame3 = frame2.copy() # Copy background.
im_fill(frame3,[12,19],[0,9],MCSC)
im_fill(frame3,[4,9],[2,8],OW)
im_fill(frame3,[9,15],[3,7],OW)
im_fill(frame3,[16,18],[2,4],OW)
im_fill(frame3,[16,18],[6,8],OW)
im_fill(frame3,[6,6],[4,4], OW)
im_fill(frame3,[6,6],[6,6], OW)
im_fill(frame3,[7,7],[5,5], OW)
im_fill(frame3,[8,8],[4,6], OW)
im_fill(frame3,[9,9],[4,4], OW)
#im_fill(frame2,[9,9],[6,6], BL)

# =============================================================================
# move_d = 2
# for row in range(rows-move_d):
#     for col in range(cols):
#         frame3[row+move_d][col] = frame2[row][col]
#
# =============================================================================
#im_show(frame3)

# Move the object by +2 to the left.
frame4 = frame1.copy() # Copy background.

im_fill(frame4,[5,5],[10,10],MNM)
im_fill(frame4,[6,6],[5,5],MNM)
im_fill(frame4,[7,7],[3,3],WH)
im_fill(frame4,[17,17],[3,3],MNM)
im_fill(frame4,[8,8],[7,7],WH)
im_fill(frame4,[8,8],[10,10],WH)
im_fill(frame4,[6,6],[14,14],MNM)
im_fill(frame4,[11,11],[2,2],WH)
im_fill(frame4,[16,16],[7,7],WH)
im_fill(frame4,[13,13],[13,13],MNM)
im_fill(frame4,[10,10],[8,8],WH)
im_fill(frame4,[13,13],[8,8],MNM)
im_fill(frame4,[16,16],[9,9],WH)
im_fill(frame4,[12,12],[5,5],MNM)
im_fill(frame4,[17,17],[16,16],WH)
im_fill(frame4,[16,16],[7,7],MNM)
im_fill(frame4,[19,19],[10,10],MNM)

frame5 = frame1.copy()

im_fill(frame5,[5,5],[10,10],MNM)
im_fill(frame5,[5,5],[10,10],WH)
im_fill(frame5,[5,5],[10,10],WH)
# =============================================================================
# move_l = 2
# for row in range(rows):
#     for col in range(move_l, cols):
#         frame4[row][col-move_l] = frame3[row][col]
# =============================================================================

# Move the object by +2 up
frame5 = frame3.copy() # Copy background.
frame6 = frame3.copy() # Copy background.

im_fill(frame6,[5,5],[10,10],MNM)


# Markus frame
frame_markus = frame3.copy()
im_fill(frame_markus,[3,10],[1,9],OW) # head
im_fill(frame_markus,[8,16],[2,8],OW) #body
im_fill(frame_markus,[15,19],[1,5],OW) # leg1
im_fill(frame_markus,[15,19],[5,9],OW) # leg2

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
#frame_list = [frame1,frame2,frame3,frame4,frame5]
frame_list = [frame1,frame2,frame3,frame_markus,frame4]
# Setup the number of frames per second
fps= 1

# Play the video
play_video= vid_show(frame_list, fps)
