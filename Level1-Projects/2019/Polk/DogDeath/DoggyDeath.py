from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20   # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff" # blue code
y = "ffff00" # yellow code
bl= "000000" # black code
br= "443300" # brown code
bb= "aefefd" # baby blue code
o = "ffa500" # orange code
bg= "00aa00" # better green code
w = "FFFFFF" # white

# Create frame 0 with the same background color
frame1 = np.array([[bb]*cols for row in range (rows)])


#Frame 1
im_fill(frame1,[19,19],[0,19], bg)
im_fill(frame1,[18,18],[0,19], bg) # grass
frame1[17] = [bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb]
im_fill(frame1,[0,3],[0,2], y) #sun
im_fill(frame1,[0,3],[2,2], o)    #sun
im_fill(frame1,[3,3],[0,2], o)    #sun
im_fill(frame1,[14,15],[1,4], br) #doggy body
im_fill(frame1,[15,16],[1,1], br) #doggy left leg
im_fill(frame1,[15,16],[4,4], br) #doggy right leg
frame1[13,0] = br                 #doggy tail
im_fill(frame1,[12,13],[4,5], br) #doggy head
frame1[11,3] = br                 #doggy left ear 
frame1[11,6] = br                 #doggy right ear 


# Frame 2
frame2 = frame1.copy()
frame2[9][11] = bl
frame2[9][13] = bl
frame2[9][15] = bl
frame2[9][17] = bl
frame2[9][19] = bl
frame2[10][10] = bl
frame2[10][12] = bl
frame2[10][14] = bl
frame2[10][16] = bl
frame2[10][18] = bl
frame2[11][11] = bl
frame2[11][13] = bl
frame2[11][15] = bl
frame2[11][17] = bl
frame2[11][19] = bl
frame2[12][10] = bl
frame2[12][12] = bl
frame2[12][14] = bl
frame2[12][16] = bl
frame2[12][18] = bl
frame2[13][11] = bl
frame2[13][13] = bl
frame2[13][15] = bl
frame2[13][17] = bl
frame2[13][19] = bl
frame2[14][10] = bl
frame2[14][12] = bl
frame2[14][14] = bl
frame2[14][16] = bl
frame2[14][18] = bl
frame2[15][11] = bl
frame2[15][13] = bl
frame2[15][15] = bl
frame2[15][17] = bl
frame2[15][19] = bl


# Frame 3
frame3 = frame1.copy()
im_fill(frame3,[11,14],[13,16], bl)
frame3[11][13] = bb
frame3[11][16] = bb
frame3[14][13] = bb
frame3[14][16] = bb


# Frame 4
frame4 = frame3.copy()
frame4[10][11] = bl
frame4[11][12] = bl
frame4[15][11] = bl
frame4[14][12] = bl
frame4[10][18] = bl
frame4[11][17] = bl
frame4[15][18] = bl
frame4[14][17] = bl


# Frame 5
frame5 = frame1.copy()
frame5[8][6] = bl
frame5[9][7] = bl
frame5[10][8] = bl
frame5[16][6] = bl
frame5[15][7] = bl
frame5[14][8] = bl
frame5[9][18] = bl
frame5[10][17] = bl
frame5[15][18] = bl
frame5[14][17] = bl
frame5[16][19] = bl
frame5[8][19] = bl
im_fill(frame5,[10,14],[9,16], bl) 
im_fill(frame5,[9,9],[10,15], bl) 
im_fill(frame5,[15,15],[10,15], bl) 


#Frame 6
frame6 = np.array([[bb]*cols for row in range (rows)])
frame6[19] = [bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb]
im_fill(frame6,[16,17],[1,4], br) #doggy body
im_fill(frame6,[17,18],[1,1], br) #doggy left leg
im_fill(frame6,[17,18],[4,4], br) #doggy right leg
frame6[15,0] = br                 #doggy tail
im_fill(frame6,[14,15],[4,5], br) #doggy head
frame6[13,3] = br                 #doggy left ear 
frame6[13,6] = br                 #doggy right ear 
im_fill(frame6,[5,9],[1,10], bl) 
frame6[5,1] = bb
im_fill(frame6,[11,11],[3,8], bl) 
im_fill(frame6,[10,10],[2,9], bl) 
frame6[12,9] = bl                
frame6[13,8] = bl                
frame6[11,1] = bl                
frame6[12,0] = bl                
im_fill(frame6,[3,4],[3,8], bl) 
frame6[4,9] = bl    
im_fill(frame6,[2,2],[5,6], bl) 
frame6[0,0] = bl    
frame6[1,1] = bl    
frame6[2,2] = bl    
frame6[0,11] = bl    
frame6[1,10] = bl    
frame6[2,9] = bl    


# frame 7
frame7 = np.array([[bb]*cols for row in range (rows)])
frame7[19] = [bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb]
im_fill(frame7,[17,18],[0,7], bl) 
im_fill(frame7,[14,16],[1,8], bl) 
im_fill(frame7,[15,15],[9,12], bl) 
im_fill(frame7,[12,13],[5,7], bl) 
frame7[11,6] = bl    
im_fill(frame7,[13,13],[3,4], bl) 
frame7[13,9] = bl    
frame7[12,10] = bl    
frame7[11,11] = bl   
frame7[10,12] = bl   


# Frame 8
frame8 = np.array([[bb]*cols for row in range (rows)])
frame8[19] = [bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb]
im_fill(frame8,[5,12],[5,14], bl) 
im_fill(frame8,[7,10],[3,4], bl) 
im_fill(frame8,[7,10],[15,16], bl) 
frame8[10,1] = bl
frame8[11,2] = bl
im_fill(frame8,[9,9],[0,2], bl) 
frame8[10,18] = bl
frame8[11,17] = bl
im_fill(frame8,[9,9],[17,19], bl) 
im_fill(frame8,[13,14],[7,12], bl) 
im_fill(frame8,[3,4],[7,12], bl)
frame8[4,6] = bl
frame8[4,13] = bl
frame8[13,6] = bl
frame8[13,13] = bl
im_fill(frame8,[2,2],[9,10], bl)
im_fill(frame8,[15,15],[9,10], bl)
frame8[14,5] = bl
frame8[15,4] = bl
frame8[16,3] = bl
frame8[17,2] = bl
frame8[18,1] = bl
frame8[14,14] = bl
frame8[15,15] = bl
frame8[16,16] = bl
frame8[17,17] = bl
frame8[18,18] = bl


#frame 9
frame9 = frame7.copy()
im_fill(frame9,[10,15],[9,12], bb)


#frame14
frame14 = np.array([[bb]*cols for row in range (rows)])
frame14[19] = [bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb, bg, bb]


#DEATH
im_fill(frame14,[13,17],[0,0], bl)
frame14[13,1] = bl
frame14[17,1] = bl
im_fill(frame14,[14,16],[2,2], bl)
im_fill(frame14,[13,17],[4,4], bl)
im_fill(frame14,[13,13],[5,6], bl)
im_fill(frame14,[17,17],[5,6], bl)
frame14[15,5] = bl
im_fill(frame14,[13,17],[8,8], bl)
im_fill(frame14,[13,17],[10,10], bl)
frame14[13,9] = bl
frame14[15,9] = bl
im_fill(frame14,[13,17],[13,13], bl)
im_fill(frame14,[13,13],[12,14], bl)
im_fill(frame14,[13,17],[16,16], bl)
im_fill(frame14,[15,15],[17,18], bl)
im_fill(frame14,[13,17],[19,19], bl)

#DOG
im_fill(frame14,[2,7],[1,1], bl)
frame14[2,2] = bl
frame14[7,2] = bl
frame14[3,3] = bl
frame14[6,3] = bl
im_fill(frame14,[4,5],[4,4], bl)
im_fill(frame14,[2,7],[7,7], bl)
im_fill(frame14,[2,2],[8,9], bl)
im_fill(frame14,[7,7],[8,9], bl)
im_fill(frame14,[2,7],[10,10], bl)
im_fill(frame14,[3,6],[13,13], bl)
im_fill(frame14,[2,2],[14,16], bl)
im_fill(frame14,[7,7],[14,16], bl)
im_fill(frame14,[5,6],[16,16], bl)
frame14[5,15] = bl



#frame_list = [frame14]
frame_list = [frame1, frame2, frame3, frame4, frame5, frame6, frame9, frame7, frame9, frame7, frame9, frame7, frame8, frame14, frame14]         # list of frames
fps= 1                               # frames per sec
play_video= vid_show(frame_list, fps) # play on screen