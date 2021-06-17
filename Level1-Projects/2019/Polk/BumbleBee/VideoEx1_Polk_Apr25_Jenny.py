from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20  # num of cols

# Define all of the colors
o ="cc6600"#orange
b ="66d9FF"#blue
y ="FFFF33"#yellow
G ="33FF33"#green
r ="ff0000"#red color
B ="000000"#BLACK
g ="cbc6c6"#GREY
p ="f39cda"#pink
lc="f08080"#light coral
P ="7800ff"#purple
l ="800080"#Lavender
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
im_fill (frame1, [0,5],[0,6],y)
im_fill (frame1, [17,19],[0,19],G) 
frame1[0,7]=r
frame1[2,7]=r
frame1[1,8]=r
frame1[3,8]=b
frame1[5,8]=b
frame1[2,9]=b
frame1[4,9]=b
frame1[4,2]=b
frame1[4,3]=b
frame1[4,4]=b
frame1[4,5]=b
frame1[4,6]=b
frame1[5,4]=b
frame1[5,5]=b
frame1[5,6]=b
frame1[4,0]=B
frame1[4,1]=o
frame1[5,1]=B
frame1[5,2]=o
frame1[5,3]=B
frame1[6,3]=o
#frame1[6,1]=p
frame1[6,4]=B
frame1[6,5]=B
#frame1[5,0]=o
#frame1[6,0]=o
frame1[6,2]=p
#frame1[7,1]=o
frame1[7,3 ]=p
#frame1[8,4 ]=p
frame1[6,6]=o
frame1[6,7]=B
frame1[6,8]=o
frame1[6,9]=B
frame1[6,10]=o
frame1[7,10]=o
frame1[0,7]=r
frame1[2,7]=r
frame1[4,7]=r
frame1[6,2]=r
frame1[3,8]=y
frame1[5,8]=y
frame1[1,8]=y
frame1[7,5]=y
#frame1[7,3]=y
frame1[8,4]=r
frame1[8,6]=r
frame1[6,9]=B
frame1[2,9]=r
frame1[4,9]=r
#frame1[8,2]=o
#frame1[8,4]=o
im_fill (frame1, [7,8],[6,9],g)
im_fill (frame1, [7,9],[5,5],g)
im_fill (frame1, [8,11],[10,10],B)
frame1[8,6]=B 
frame1[4,11 ]=B
frame1[9,6]=B
frame1[8,8]=B
frame1[9,8]=B
frame1[9,7]=g
frame1[9,9]=g
frame1[5,11 ]=B
frame1[4,13 ]=B
frame1[5,13 ]=B
frame1[5,12 ]=B
frame1[6,12 ]=B
frame1[7,12 ]=B
frame1[10,5]=B
frame1[11,5]=B
frame1[7,11 ]=p
frame1[7,13 ]=p
frame1[6,11 ]=G
frame1[6,13 ]=G
frame1[16,3 ]=o
frame1[16,5 ]=o
frame1[16,7 ]=o
frame1[16,9 ]=o
frame1[16,11 ]=o


frame2 = np.array([[b]*cols for row in range (rows)])
im_fill (frame2, [0,5],[0,6],y)
im_fill (frame2, [17,19],[0,19],G)

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
frame2[0,10]=B
frame2[1,10]=lc
frame2[1,11]=B
frame2[2,11]=lc
frame2[3,11]=B
frame2[3,12]=lc
frame2[4,12]=B
frame2[5,12]=B
frame2[6,12]=lc
frame2[7,12]=B
frame2[8,12]=lc
frame2[9,12]=B
frame2[10,12]=g
frame2[11,12]=G
frame2[12,12]=B
frame2[13,12]=G
frame2[5,13]=g
frame2[6,13]=g
frame2[7,13]=g
frame2[8,13]=g
frame2[9,13]=g
frame2[10,13]=g
frame2[11,13]=p
frame2[12,13]=B
frame2[13,13]=p
frame2[5,14]=g
frame2[6,14]=B
frame2[7,14]=g
frame2[8,14]=B
frame2[9,14]=g
frame2[10,14]=B
frame2[5,15]=g
frame2[6,15]=B
frame2[7,15]=g
frame2[8,15]=B
frame2[9,15]=g
frame2[10,15]=B
frame2[3,16]=B
frame2[4,16]=B
frame2[5,16]=B
frame2[6,16]=b
frame2[7,16]=b
frame2[8,16]=b
frame2[9,16]=b
frame2[10,16]=B
frame2[11,16]=B
frame2[12,16]=B
frame2[11,10]=B
frame2[13,10]=B
frame2[11,11]=B
frame2[12,11]=B
frame2[13,11]=B
frame2[16,3 ]=o
frame2[16,5 ]=o
frame2[16,7 ]=o
frame2[16,9 ]=o
frame2[16,11 ]=o

frame3 = np.array([[b]*cols for row in range (rows)])
im_fill (frame3,[17,19],[0,19],G) 
im_fill(frame3,[1,2],[0,19],lc)
im_fill(frame3,[3,4],[0,19],y)
im_fill(frame3,[3,16],[19,19],y)
im_fill(frame3,[5,6],[0,18],g)  
im_fill(frame3,[5,6],[17,18],l)
im_fill(frame3,[1,2],[0,19],lc)
im_fill(frame3,[7,17],[16,17],l)
im_fill(frame3,[9,10],[0,15],P)
im_fill(frame3,[9,17],[14,15],P)
im_fill(frame3,[9,17],[1,2],P)

im_fill(frame3,[10,11],[11,12],b)
im_fill(frame3,[10,11],[2,12],b)
im_fill(frame3,[12,13],[4,10],r)
im_fill(frame3,[12,16],[4,5],r)
im_fill(frame3,[12,16],[9,10],r)

im_fill(frame3,[14,16],[6,8],o)
frame3[15,7]=B
im_fill(frame3,[3,7],[3,3],B)
im_fill(frame3,[3,3],[3,5],B)
frame3[5,5]=B
im_fill(frame3,[7,7],[3,5],B)
im_fill(frame3,[3,7],[8,8],B)
frame3[3,8]=B
frame3[5,9]=B
frame3[6,10]=B
im_fill(frame3,[3,7],[12,12],B) 
im_fill(frame3,[3,7],[14,14],B)
im_fill(frame3,[3,3],[14,17],B)
im_fill(frame3,[4,6],[17,17],B)
im_fill(frame3,[7,7],[14,16],B)

#Specify the frame row-by-row
#frame0[0] = [b, b]
#frame0[1] = [b, b]

#Create frame 1 with the same background color
#frame1 = np.array([[b]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]

frame_list = [frame0, frame1,frame2, frame3]
fps=1
play_video=vid_show(frame_list,fps)

# Video play
"""
frame_list = [frame0, frame1]         # list of frames
fps= 1                               # frames per sec
play_video= vid_show(frame_list, fps) # play on screen
"""