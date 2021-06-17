from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20  # num of cols

# Define all of the colors
b ="66d9FF"#blue
y ="FFFF33"#yellow
G ="33FF33"#green
r ="ff0000"#red color
o ="cc6600"#orange
B ="000000"#BLACK
g ="cbc6c6"#GREY
p ="f39cda"#pink
# Create frame 0 with the same background color
frame0 = np.array([[b]*cols for row in range (rows)])
im_fill (frame0, [0,5],[0,6],y)
im_fill (frame0, [17,19],[0,19],G) 
frame0[0,7]=r
frame0[2,7]=r
frame0[4,7]=r
frame0[6,2]=r
frame0[6,4]=r
frame0[3,8]=y
frame0[5,8]=y
frame0[1,8]=y
frame0[7,5]=y
frame0[7,3]=y
frame0[8,4]=r
frame0[8,6]=r
frame0[6,9]=r
frame0[2,9]=r
frame0[4,9]=r
frame0[16,5]=o
frame0[16,7]=o
frame0[16,9]=o
frame0[16,11]=o
frame0[16,3]=o
frame0[15,10 ]=B
frame0[14,10 ]=B
frame0[13,10 ]=B
frame0[12,10 ]=B
frame0[14,5 ]=B
frame0[15,5 ]=B
frame0[8,0 ]=B
frame0[9,1 ]=B
frame0[8,1 ]=g
frame0[8,0 ]=B
frame0[9,2 ]=g
frame0[9,3 ]=B
frame0[10,4 ]=B
frame0[10,3 ]=g
frame0[10,5 ]=B
frame0[12,5 ]=g
frame0[13,5 ]=g
frame0[14,5 ]=B
frame0[11,5 ]=g
frame0[10,6 ]=g
frame0[10,7 ]=B
frame0[10,8 ]=g
frame0[10,9 ]=B
frame0[10,10 ]=g
im_fill (frame0, [11,11],[6,10],g)
frame0[13,6 ]=B
frame0[12,6 ]=B
frame0[13,7]=g
frame0[12,7 ]=g
frame0[13,8]=B
frame0[12,8 ]=B
frame0[13,9 ]=g
frame0[12,9 ]=g
frame0[11,11 ]=p
frame0[11,12 ]=B
frame0[11,13]=p
frame0[12,10]=B
frame0[12,9 ]=B
frame0[13,9 ]=g
frame0[11,9 ]=g
frame0[10,12 ]=B
frame0[10,11 ]=G
frame0[12,9 ]=g
frame0[10,13 ]=G
frame0[9,13 ]=B
frame0[9,12 ]=B
frame0[9,11 ]=B
frame0[8,11]=B
frame0[8,13 ]=B

frame1 = np.array([[b]*cols for row in range (rows)])



frame2 = np.array([[b]*cols for row in range (rows)])
im_fill (frame1, [0,5],[0,6],y)
im_fill (frame1, [17,19],[0,19],G)

frame2[0,7]=r
frame2[2,7]=r
frame2[4,7]=r
frame2[6,2]=r
frame2[6,4]=r
frame2[3,8]=y
frame2[5,8]=y
frame2[1,8]=y
frame2[7,5]=y
frame2[7,3]=y
frame2[8,4]=r
frame2[8,6]=r
frame2[6,9]=r
frame2[2,9]=r
frame2[4,9]=r

frame3 = np.array([[b]*cols for row in range (rows)])
#Specify the frame row-by-row
#frame0[0] = [b, b]
#frame0[1] = [b, b]

#Create frame 1 with the same background color
#frame1 = np.array([[b]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]

frame_list = [frame0, frame1]
fps= 2
play_video=vid_show(frame_list,fps)

# Video play
"""
frame_list = [frame0, frame1]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen
"""