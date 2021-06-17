from AOLME import *

# Define the size of the image
rows = 35  # num of rows
cols = 35  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff"
g = "00cc44"
y = "ffff66"
p = "ff1a8c"
o = "ff3300"
bl = "000000"
gr = "a9a9a9"
w = "ffffff"
db = "654321"
lb = "b5651d"
wi = "7ef9ff"
sky1 = "95c8d8"
sky2 = "7ef9ff"
dg = "0b6623"
sky3 = "ffa31a"
sky4="000080"




# Create frame 0 with the same background color
frame0 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame0,[0,4],[0,0], b)
im_fill(frame0,[0,0],[0,2], b)
im_fill(frame0,[4,4],[0,2], b)
frame0[1][3]  = b
frame0[3][3]  = b
frame0[2][4]  = b

#v
im_fill(frame0,[0,2],[10,10], b)
im_fill(frame0,[0,2],[6,6], b)
frame0[3][7]  = b
frame0[3][9]  = b
frame0[4][8]  = b

#d
im_fill(frame0,[0,4],[12,12], b)
im_fill(frame0,[0,0],[12,14], b)
im_fill(frame0,[4,4],[12,14], b)
frame0[1][15]  = b
frame0[2][16]  = b
frame0[3][15]  = b

# Create frame 1 with the same background color
frame1 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame1,[10,10],[6,8], b)
im_fill(frame1,[10,14],[6,6], b)
im_fill(frame1,[14 ,14],[7,8], b)
frame1[11][9]  = b
frame1[12][10]  = b
frame1[13][9]  = b

#v
im_fill(frame1,[10,12],[12,12], b)
im_fill(frame1,[10,12],[16,16], b)
frame1[13][13]  = b
frame1[14][14]  = b
frame1[13][15]  = b

#d
im_fill(frame1,[10,14],[18,18], b)
im_fill(frame1,[14,14],[19,20], b)
im_fill(frame1,[10,10],[18,20], b)
frame1[11][21]  = b
frame1[12][22]  = b
frame1[13][21]  = b

frame2 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame2,[20,24],[12,12], b)
im_fill(frame2,[20,20],[12,14], b)
im_fill(frame2,[24 ,24],[12,14], b)
frame2[21][15]  = b
frame2[22][16]  = b
frame2[23][15]  = b

#v
im_fill(frame2,[20,22],[18,18], b)
im_fill(frame2,[20,22],[22,22], b)
frame2[23][19]  = b
frame2[24][20]  = b
frame2[23][21]  = b

#d
im_fill(frame2,[20,24],[24,24], b)
im_fill(frame2,[20,20],[24,26], b)
im_fill(frame2,[24,24],[24,26], b)
frame2[21][27]  = b
frame2[22][28]  = b
frame2[23][27]  = b

frame3 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame3,[30,34],[18,18], r)
im_fill(frame3,[30,30],[18,20], r)
im_fill(frame3,[34,34],[18,20], r)
frame3[31][21]  = r
frame3[32][22]  = r                
frame3[33][21]  = r

#v
im_fill(frame3,[30,32],[24,24], r)
im_fill(frame3,[30,32],[28,28], r)
frame3[33][25]  = r
frame3[34][26]  = r
frame3[33][27]  = r

#d
im_fill(frame3,[30,34],[30,30], r)
im_fill(frame3,[30,30],[30,32], r)
im_fill(frame3,[34,34],[30,32], r)
frame3[31][33]  = r
frame3[32][34]  = r
frame3[33][33]  = r

frame4 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame4,[25,29],[6,6], r)
im_fill(frame4,[25,25],[6,8], r)
im_fill(frame4,[29,29],[6,8], r)
frame4[26][9]  = r
frame4[27][10]  = r                
frame4[28][9]  = r

#v
im_fill(frame4,[25,27],[12,12], r)
im_fill(frame4,[25,27],[16,16], r)
frame4[28][13]  = r
frame4[29][14]  = r
frame4[28][15]  = r

#d
im_fill(frame4,[25,29],[18,18], r)
im_fill(frame4,[25,25],[18,20], r)
im_fill(frame4,[29,29],[18,20], r)
frame4[26][21]  = r
frame4[27][22]  = r
frame4[28][21]  = r

frame4 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)



#d
im_fill(frame4,[25,29],[6,6], r)
im_fill(frame4,[25,25],[6,8], r)
im_fill(frame4,[29,29],[6,8], r)
frame4[26][9]  = r
frame4[27][10]  = r                
frame4[28][9]  = r

#v
im_fill(frame4,[25,27],[12,12], r)
im_fill(frame4,[25,27],[16,16], r)
frame4[28][13]  = r
frame4[29][14]  = r
frame4[28][15]  = r

#d
im_fill(frame4,[25,29],[18,18], r)
im_fill(frame4,[25,25],[18,20], r)
im_fill(frame4,[29,29],[18,20], r)
frame4[26][21]  = r
frame4[27][22]  = r
frame4[28][21]  = r

frame5 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)

#d
im_fill(frame5,[19,23],[0,0], p)
im_fill(frame5,[23,23],[0,2], p)
im_fill(frame5,[19,19],[0,2], p)
frame5[20][3]  = p
frame5[21][4]  = p                
frame5[22][3]  = p

#v
im_fill(frame5,[19,21],[6,6], p)
im_fill(frame5,[19,21],[10,10], p)
frame5[22][7]  = p
frame5[23][8]  = p
frame5[22][9]  = p

#d
im_fill(frame5,[19,23],[12,12], p)
im_fill(frame5,[19,19],[12,14], p)
im_fill(frame5,[23,23],[12,14], p)
frame5[20][15]  = p
frame5[21][16]  = p
frame5[22][15]  = p

frame6 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)

#d
im_fill(frame6,[15,19],[9,9], p)
im_fill(frame6,[15,15],[9,11], p)
im_fill(frame6,[19,19],[9,11], p)
frame6[16][12]  = p
frame6[18][12]  = p                
frame6[17][13]  = p

#v
im_fill(frame6,[15,17],[15,15], p)
im_fill(frame6,[15,17],[19,19], p)
frame6[18][16]  = p
frame6[18][18]  = p
frame6[19][17]  = p

#d
im_fill(frame6,[15,19],[21,21], p)
im_fill(frame6,[15,15],[21,23], p)
im_fill(frame6,[19,19],[21,23], p)
frame6[16][24]  = p
frame6[18][   24]  = p
frame6[17][25]  = p

frame7 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)

#d
im_fill(frame7,[9,13],[18,18], g)
im_fill(frame7,[13,13],[18,20], g)
im_fill(frame7,[9,9],[18,20], g)
frame7[10][21]  = g
frame7[12][21]  = g                
frame7[11][22]  = g

#v
im_fill(frame7,[9,11],[24,24], g)
im_fill(frame7,[9,11],[28,28], g)
frame7[12][25]  = g
frame7[13][26]  = g
frame7[12][27]  = g

#d
im_fill(frame7,[9,13],[30,30], g)
im_fill(frame7,[9,9],[30,32], g)
im_fill(frame7,[13,13],[30,32], g)
frame7[10][33]  = g
frame7[11][34]  = g
frame7[12][33]  = g

frame8 = np.array([[bl]*cols for row in range (rows)])

# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(,[0,4],[0,0], b)

#d
im_fill(frame8,[5,9],[6,6], g)
im_fill(frame8,[5,5],[6,8], g)
im_fill(frame8,[9,9],[6,8], g)
frame8[6][9]  = g
frame8[7][10]  = g                
frame8[8][9]  = g

#v
im_fill(frame8,[5,7],[12,12], g)
im_fill(frame8,[5,7],[16,16], g)
frame8[8][13]  = g
frame8[8][15]  = g
frame8[9][14]  = g

#d
im_fill(frame8,[5,9],[18,18], g)
im_fill(frame8,[5,5],[18,20], g)
im_fill(frame8,[9,9],[18,20], g)
frame8[6][21]  = g
frame8[7][22]  = g
frame8[8][21]  = g

frame9 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame9,[0,34],[0,5], r)
im_fill(frame9,[0,34],[5,10], o)
im_fill(frame9,[0,34],[10,15], g)

#v
im_fill(frame9,[0,34],[15,20], p)
im_fill(frame9,[0,34],[20,25], b)


#d
im_fill(frame9,[0,34],[25,30], bl)
im_fill(frame9,[0,34],[30,34], y)

frame10 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame10,[31,34],[0,34], bl)
im_fill(frame10,[0,19],[0,34], sky1)

im_fill(frame10,[31,32],[0,1], r)
im_fill(frame10,[31,32],[2,3], g)
im_fill(frame10,[33,34],[0,1], b)
im_fill(frame10,[33,34],[2,3], y)

im_fill(frame10,[31,34],[7,14], gr)

im_fill(frame10,[31,34],[17,21], o)
im_fill(frame10,[31,34],[22,26], p)

im_fill(frame10,[20,29],[0,34], dg)

#mountains
im_fill(frame10,[14,19],[0,25], db)
im_fill(frame10,[15,19],[26,27], db)
im_fill(frame10,[12,13],[9,20], db)
im_fill(frame10,[10,11],[12,17], db)
im_fill(frame10,[7,9],[14,17], db)
im_fill(frame10,[6,6],[14,16], db)
im_fill(frame10,[5,5],[15,16], db)
im_fill(frame10,[4,4],[16,16], db)
im_fill(frame10,[10,12],[24,32], db)
im_fill(frame10,[13,13],[24,27], db)
im_fill(frame10,[4,9],[28,31], db)
im_fill(frame10,[6,9],[26,27], db)
im_fill(frame10,[9,9],[24,25], db)
im_fill(frame10,[3,3],[30,30], db)
#icons
im_fill(frame10,[2,4],[2,4], b)

im_fill(frame10,[8,10],[2,4], r)
im_fill(frame10,[14,16],[2,4], g)
im_fill(frame10,[20,22],[2,4], b)
im_fill(frame10,[2,4],[8,10], y)

im_fill(frame10,[8,10],[8,10], gr)
#house
im_fill(frame10,[15,19],[28,34], w)
              
im_fill(frame10,[14,14],[26,34], bl)
im_fill(frame10,[13,13],[30,34], bl)
im_fill(frame10,[16,17],[29,30], wi)
im_fill(frame10,[17,19],[32,33], lb)

frame11 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame11,[31,34],[0,34], bl)
im_fill(frame11,[0,19],[0,34], sky3)

im_fill(frame11,[31,32],[0,1], r)
im_fill(frame11,[31,32],[2,3], g)
im_fill(frame11,[33,34],[0,1], b)
im_fill(frame11,[33,34],[2,3], y)

im_fill(frame11,[31,34],[7,14], gr)

im_fill(frame11,[31,34],[17,21], o)
im_fill(frame11,[31,34],[22,26], p)

im_fill(frame11,[20,29],[0,34], dg)

#mountains
im_fill(frame11,[14,19],[0,25], db)
im_fill(frame11,[15,19],[26,27], db)
im_fill(frame11,[12,13],[9,20], db)
im_fill(frame11,[10,11],[12,17], db)
im_fill(frame11,[7,9],[14,17], db)
im_fill(frame11,[6,6],[14,16], db)
im_fill(frame11,[5,5],[15,16], db)
im_fill(frame11,[4,4],[16,16], db)
im_fill(frame11,[10,12],[24,32], db)
im_fill(frame11,[13,13],[24,27], db)
im_fill(frame11,[4,9],[28,31], db)
im_fill(frame11,[6,9],[26,27], db)
im_fill(frame11,[9,9],[24,25], db)
im_fill(frame11,[3,3],[30,30], db)
#icons
im_fill(frame11,[2,4],[2,4], b)

im_fill(frame11,[8,10],[2,4], r)
im_fill(frame11,[14,16],[2,4], g)
im_fill(frame11,[20,22],[2,4], b)
im_fill(frame11,[2,4],[8,10], y)

im_fill(frame11,[8,10],[8,10], gr)
#house
im_fill(frame11,[15,19],[28,34], w)
              
im_fill(frame11,[14,14],[26,34], bl)
im_fill(frame11,[13,13],[30,34], bl)
im_fill(frame11,[16,17],[29,30], wi)
im_fill(frame11,[17,19],[32,33], lb) 

#d
im_fill(frame9,[0,34],[25,30], bl)
im_fill(frame9,[0,34],[30,34], y)

frame12 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame12,[31,34],[0,34], bl)
im_fill(frame12,[0,19],[0,34], sky4)

im_fill(frame12,[31,32],[0,1], r)
im_fill(frame12,[31,32],[2,3], g)
im_fill(frame12,[33,34],[0,1], b)
im_fill(frame12,[33,34],[2,3], y)

im_fill(frame12,[31,34],[7,14], gr)

im_fill(frame12,[31,34],[17,21], o)
im_fill(frame12,[31,34],[22,26], p)

im_fill(frame12,[20,29],[0,34], dg)

#mountains
im_fill(frame12,[14,19],[0,25], db)
im_fill(frame12,[15,19],[26,27], db)
im_fill(frame12,[12,13],[9,20], db)
im_fill(frame12,[10,11],[12,17], db)
im_fill(frame12,[7,9],[14,17], db)
im_fill(frame12,[6,6],[14,16], db)
im_fill(frame12,[5,5],[15,16], db)
im_fill(frame12,[4,4],[16,16], db)
im_fill(frame12,[10,12],[24,32], db)
im_fill(frame12,[13,13],[24,27], db)
im_fill(frame12,[4,9],[28,31], db)
im_fill(frame12,[6,9],[26,27], db)
im_fill(frame12,[9,9],[24,25], db)
im_fill(frame12,[3,3],[30,30], db)
#icons
im_fill(frame12,[2,4],[2,4], b)

im_fill(frame12,[8,10],[2,4], r)
im_fill(frame12,[14,16],[2,4], g)
im_fill(frame12,[20,22],[2,4], b)
im_fill(frame12,[2,4],[8,10], y)

im_fill(frame12,[8,10],[8,10], gr)
#house
im_fill(frame12,[15,19],[28,34], w)
              
im_fill(frame12,[14,14],[26,34], bl)
im_fill(frame12,[13,13],[30,34], bl)
im_fill(frame12,[16,17],[29,30], wi)
im_fill(frame12,[17,19],[32,33], lb) 

#stars
frame12[4][24]  = w
frame12[2][22]  = w
frame12[7][19]  = w
frame12[1][30]  = w
frame12[1][15]  = w


#d
im_fill(frame9,[0,34],[25,30], bl)
im_fill(frame9,[0,34],[30,34], y)

frame13 = frame12.copy()
frame14 = frame13.copy()
frame15 = frame14.copy()
frame16 = frame15.copy()
frame17 = frame16.copy()
frame18 = frame17.copy()
frame19 = frame9.copy()
frame20 = frame9.copy()
# Video play
frame_list = [frame9, frame19, frame20, frame0, frame1, frame2, frame3, frame4,frame5,frame6,frame7,frame8,frame10, frame11,frame12,frame13,frame14,frame15,frame16,frame17,frame18]   
#frame_list = [frame10]      # list of frames
fps= 9                                 # frames per sec
play_video= vid_show(frame_list, fps) # play on screen