from AOLME import *
import sys

# Define the image size:
rows = 20
cols = 20

# Define the colors:
blr = "8A0303" #bloodred
lg = "bbbbbb"  #lightgrey
dg = "333333"  #darkgrey
blu = "0037B1" #blue
gr = "66FF66" #green
br = "B06C49" #brown
bl = "000000" #black
wh = "FFFFFF" #white
dp = "421C52" #darkpurple
red ="FF0000" #red
# Initialize the background
backg = np.array([[lg]*cols for row in range (rows)])

#frame0
# Copy the background into a frame:
frame0 = backg.copy()

# Create the chara0cter

#CAGE 
im_fill(frame0,[1,1],[0,19],dg)
im_fill(frame0,[3,3],[0,19],dg)
im_fill(frame0,[13,13],[0,19],dg)
im_fill(frame0,[18,18],[0,19],dg)
im_fill(frame0,[1,18],[0,0],dg)
im_fill(frame0,[1,18],[5,5],dg)
im_fill(frame0,[1,18],[14,14],dg)
im_fill(frame0,[1,18],[19,19],dg)

#Calender
im_fill(frame0,[5,9],[4,4],blu)
im_fill(frame0,[5,5],[4,12],blu)
im_fill(frame0,[5,9],[12,12],blu)
im_fill(frame0,[9,9],[4,12],blu)

#number
im_fill(frame0,[6,7],[6,6],gr)
im_fill(frame0,[8,8],[6,6],gr)
im_fill(frame0,[6,8],[8,10],gr)
im_fill(frame0,[7,7],[9,9],lg)

#Dog1
im_fill(frame0,[11,11],[6,6],br)
im_fill(frame0,[11,11],[9,9],br)
im_fill(frame0,[11,11],[1,1],br)
im_fill(frame0,[12,12],[2,2],br)
im_fill(frame0,[12,12],[7,8],br)
im_fill(frame0,[14,15],[3,4],br)
im_fill(frame0,[16,16],[3,3],br)
im_fill(frame0,[14,16],[6,6],br)
#im_fill(frame0,[],[],br)


#Dog2
im_fill(frame0,[10,10],[11,11],bl)
im_fill(frame0,[11,12],[12,13],bl)
im_fill(frame0,[11,11],[18,18],bl)
im_fill(frame0,[12,12],[15,17],bl)
im_fill(frame0,[14,14],[15,17],bl)
im_fill(frame0,[15,15],[15,17],bl)
im_fill(frame0,[16,16],[17,17],bl)

# Copy the background into a frame:
frame1 = backg.copy()

# Create the chara0cter



# =============================================================================

# Dog1
im_fill(frame1,[11,11],[6,6],br)
im_fill(frame1,[11,11],[9,9],br)
im_fill(frame1,[12,13],[7,8],br)
im_fill(frame1,[13,14],[3,6],br)
im_fill(frame1,[15,15],[3,3],br)
im_fill(frame1,[15,15],[6,6],br)
im_fill(frame1,[12,12],[2,2],br)
im_fill(frame1,[11,11],[1,1],br)
# =============================================================================

#Dog2

im_fill(frame1,[10,10],[11,11],bl)
im_fill(frame1,[10,10],[14,14],bl)
im_fill(frame1,[11,12],[12,13],bl)
im_fill(frame1,[12,14],[14,17],bl)
im_fill(frame1,[15,15],[17,17],bl)
im_fill(frame1,[15,15],[14,14],bl)
im_fill(frame1,[11,11],[18,18],bl)
im_fill(frame1,[10,10],[19,19],bl)

#CAGE 
im_fill(frame1,[1,1],[0,19],dg)
im_fill(frame1,[3,3],[0,19],dg)
im_fill(frame1,[13,13],[0,19],dg)
im_fill(frame1,[18,18],[0,19],dg)
im_fill(frame1,[1,18],[0,0],dg)
im_fill(frame1,[1,18],[5,5],dg)
im_fill(frame1,[1,18],[14,14],dg)
im_fill(frame1,[1,18],[19,19],dg)


#Calender
im_fill(frame1,[5,9],[4,4],blu)
im_fill(frame1,[5,5],[4,12],blu)
im_fill(frame1,[5,9],[12,12],blu)
im_fill(frame1,[9,9],[4,12],blu)


# #number
im_fill(frame1,[6,6],[5,7],gr)
im_fill(frame1,[7,7],[6,7],gr)
im_fill(frame1,[8,8],[5,7],gr)
im_fill(frame1,[6,6],[9,11],gr)
im_fill(frame1,[7,7],[9,9],gr)
im_fill(frame1,[7,7],[11,11],gr)
im_fill(frame1,[8,8],[9,11],gr)


# Copy the background into a frame:
frame3 = backg.copy()

# Dog1
im_fill(frame3,[11,11],[2,5],br)
im_fill(frame3,[12,12],[3,3],br)
im_fill(frame3,[12,12],[5,5],br)
im_fill(frame3,[14,14],[7,8],blr)
im_fill(frame3,[15,15],[6,6],blr)

# =============================================================================

#Dog2

im_fill(frame3,[10,10],[11,11],bl)
im_fill(frame3,[10,10],[14,14],bl)
im_fill(frame3,[11,12],[12,13],bl)
im_fill(frame3,[12,15],[14,17],bl)
im_fill(frame3,[16,16],[17,17],bl)
im_fill(frame3,[16,16],[14,14],bl)
im_fill(frame3,[11,11],[18,18],bl)
im_fill(frame3,[10,10],[19,19],bl)

# =============================================================================
# #CAGE 
# im_fill(frame3,[1,1],[0,19],dg)
# im_fill(frame3,[3,3],[0,19],dg)
# im_fill(frame3,[13,13],[0,19],dg)
# im_fill(frame3,[18,18],[0,19],dg)
# im_fill(frame3,[1,18],[0,0],dg)
# im_fill(frame3,[1,18],[5,5],dg)
# im_fill(frame3,[1,18],[14,14],dg)
# im_fill(frame3,[1,18],[19,19],dg)
# 
# =============================================================================

#Calender
im_fill(frame3,[5,9],[4,4],blu)
im_fill(frame3,[5,5],[4,12],blu)
im_fill(frame3,[5,9],[12,12],blu)
im_fill(frame3,[9,9],[4,12],blu)


# #number Four
im_fill(frame3,[6,6],[5,5],gr)
im_fill(frame3,[7,7],[5,7],gr)
im_fill(frame3,[8,8],[7,7],gr)
im_fill(frame3,[6,6],[7,7],gr)
# Number Zero
im_fill(frame3,[6,6],[9,11],gr)
im_fill(frame3,[7,7],[9,9],gr)
im_fill(frame3,[7,7],[11,11],gr)
im_fill(frame3,[8,8],[9,11],gr)



# Copy the background into a frame:
frame4 = backg.copy()

# Dog1
im_fill(frame4,[14,14],[2,2],wh)
im_fill(frame4,[14,14],[6,6],wh)
im_fill(frame4,[15,15],[3,5],wh)
im_fill(frame4,[16,16],[2,2],wh)
im_fill(frame4,[16,16],[6,6],wh)

# =============================================================================

#Dog2

im_fill(frame4,[10,10],[11,11],bl)
im_fill(frame4,[10,10],[14,14],bl)
im_fill(frame4,[11,12],[12,13],bl)
im_fill(frame4,[12,15],[14,17],bl)
im_fill(frame4,[16,16],[17,17],bl)
im_fill(frame4,[16,16],[14,14],bl)
im_fill(frame4,[11,11],[18,18],bl)
im_fill(frame4,[10,10],[19,19],bl)

# =============================================================================
# #CAGE 
# im_fill(frame3,[1,1],[0,19],dg)
# im_fill(frame3,[3,3],[0,19],dg)
# im_fill(frame3,[13,13],[0,19],dg)
# im_fill(frame3,[18,18],[0,19],dg)
# im_fill(frame3,[1,18],[0,0],dg)
# im_fill(frame3,[1,18],[5,5],dg)
# im_fill(frame3,[1,18],[14,14],dg)
# im_fill(frame3,[1,18],[19,19],dg)
# 
# =============================================================================




# RIP
im_fill(frame4,[1,1],[1,3],dp)
im_fill(frame4,[2,2],[1,1],dp)
im_fill(frame4,[2,2],[3,3],dp)
im_fill(frame4,[3,3],[1,2],dp)
im_fill(frame4,[4,4],[1,1],dp)
im_fill(frame4,[4,4],[3,3],dp)
im_fill(frame4,[1,1],[5,7],dp)
im_fill(frame4,[2,3],[6,6],dp)
im_fill(frame4,[1,1],[9,11],dp)
im_fill(frame4,[2,2],[9,9],dp)
im_fill(frame4,[2,2],[11,11],dp)
im_fill(frame4,[3,3],[9,11],dp)
im_fill(frame4,[4,4],[9,9],dp)
im_fill(frame4,[4,4],[5,7],dp)

#frame2
# Copy the background into a frame:
frame2 = backg.copy()

# Create the chara0cter

#CAGE 
im_fill(frame2,[1,1],[0,19],dg)
im_fill(frame2,[3,3],[0,19],dg)
im_fill(frame2,[13,13],[0,19],dg)
im_fill(frame2,[18,18],[0,19],dg)
im_fill(frame2,[1,18],[0,0],dg)
im_fill(frame2,[1,18],[5,5],dg)
im_fill(frame2,[1,18],[14,14],dg)
im_fill(frame2,[1,18],[19,19],dg)

#Calender
im_fill(frame2,[5,9],[4,4],blu)
im_fill(frame2,[5,5],[4,12],blu)
im_fill(frame2,[5,9],[12,12],blu)
im_fill(frame2,[9,9],[4,12],blu)

#number
im_fill(frame2,[8,8],[6,8],gr)
im_fill(frame2,[7,7],[7,8],gr)
im_fill(frame2,[6,6],[6,8],gr)
im_fill(frame2,[6,6],[10,10],gr)
im_fill(frame2,[6,8],[10,10],gr)
#Dog1
#ears and tail
im_fill(frame2,[11,11],[6,6],br)
im_fill(frame2,[11,11],[9,9],br)
im_fill(frame2,[11,11],[1,1],br)
im_fill(frame2,[12,12],[2,2],br)

im_fill(frame2,[12,12],[7,8],br)
im_fill(frame2,[14,14],[3,3],br)
im_fill(frame2,[14,14],[7,7],br)



#Dog
#ear
im_fill(frame2,[10,10],[11,11],bl)

im_fill(frame2,[11,12],[12,13],bl)
#tail
im_fill(frame2,[11,11],[18,18],bl)
im_fill(frame2,[12,12],[15,17],bl)
im_fill(frame2,[14,14],[14,14],bl)
im_fill(frame2,[14,14],[17,17],bl)


# Create a frame list of all of the frames
frame_list = [frame0,frame1,frame2,frame3,frame4]

# Setup the number of frames per second
fps= 1 

# Play the video
play_video= vid_show(frame_list, fps)

#
#
#
#
#
#
#
#frame1[3][8]  = v
#
## Make a second copy of the character
#frame1[10:13,8:12] = frame1[2:5,8:12]
#
## Move the character by +2 to the right.
#frame2 = backg.copy() # Copy background.
#
#move_r = 2
#for row in range(rows):
#    for col in range(cols-move_r):
#        frame2[row][col+move_r] = frame1[row][col]
#
#
## Move the object by +2 down
#frame3 = backg.copy() # Copy background.
#
#move_d = 2
#for row in range(rows-move_d):
#    for col in range(cols):
#        frame3[row+move_d][col] = frame2[row][col]
#
##im_show(frame3)
#
## Move the object by +2 to the left.
#frame4 = backg.copy() # Copy background.
#
#move_l = 2
#for row in range(rows):
#    for col in range(move_l, cols):
#        frame4[row][col-move_l] = frame3[row][col]
#
## Move the object by +2 up
#frame5 = backg.copy() # Copy background.
#
#move_u = 2
#for row in range(move_u, rows):
#    for col in range(cols):
#        frame5[row-move_d][col] = frame4[row][col]
#
#
## Show a single image:
## Uncommend the im_show() commands to show single images.
##im_show(frame5)
#
## Create a frame list of all of the frames
#frame_list = [frame1, frame2, frame3, frame4, frame5]
#
## Setup the number of frames per second
#fps= 2  
#
## Play the video
#play_video= vid_show(frame_list, fps)
