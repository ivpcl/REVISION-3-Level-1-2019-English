from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20  # num of cols

# Define all of the colors 
r = "ff0000" # red code
g = "009933" #green code
b = "0000ff" #blue code             #hexadecimal
p = "7300e6" #purple code
y = "ffcc00" #yellow code
o = "ff3300" #orange code
bl = "000000" #black code
pi = "ffb3ff" #pink code
tu = "33ffff" #turquesa cide
ac = "ccffff" #azul clarito  
w = "ffffff" #white code
rf = "ff1a75" # rosa fuerte
# Create frame 0 with the same background color
frame0 = np.array([[bl]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b]
#frame0[1] = [b, b]

im_fill(frame0,[5,5],[9,11], y)
im_fill(frame0,[6,6],[8,12], y)
im_fill(frame0,[7,7],[7,13], y)
im_fill(frame0,[8,8],[7,13], y)
im_fill(frame0,[9,9],[7,13], y)
im_fill(frame0,[10,10],[7,9], y)
im_fill(frame0,[10,10],[11,13], y)
im_fill(frame0,[11,11],[7,8], y)
im_fill(frame0,[11,11],[12,13], y)
im_fill(frame0,[12,12],[8,8], y )
im_fill(frame0,[12,12],[12,12], y)
im_fill(frame0,[15,15],[10,10], rf)
im_fill(frame0,[16,16],[9,11], tu)
im_fill(frame0,[17,17],[9,11], ac)
im_fill(frame0,[18,18],[10,10], p)



#frame0[1][3]  = y
#frame0[3][3]  = y
#frame0[2][4]  = y
##v
#im_fill(frame0,[0,0],[0,0],y)
#im_fill(frame0,[0,2],[6,6], y)
#frame0[3][7]  = y
#frame0[3][9]  = y
#frame0[4][8]  = y
#
##d
#im_fill(frame0,[0,4],[12,12], y)
#im_fill(frame0,[0,0],[12,14], y)
#im_fill(frame0,[4,4],[12,14], y)
#frame0[1][15]  = y
#frame0[2][16]  = y
#frame0[3][15]  = y
#
### Create frame 1 with the same background color
frame1 = np.array([[bl]*cols for row in range (rows)])
#
im_fill(frame1,[10,10],[9,11], tu)
im_fill(frame1,[11,11],[8,12], ac)
im_fill(frame1,[12,12],[7,13], p)
im_fill(frame1,[13,13],[7,13], rf)
im_fill(frame1,[14,14],[7,13], tu)
im_fill(frame1,[15,15],[7,9], ac)
im_fill(frame1,[15,15],[11,13], p)
im_fill(frame1,[16,16],[7,8], tu)
im_fill(frame1,[16,16],[12,13], ac)
im_fill(frame1,[17,17],[8,8], p)
im_fill(frame1,[17,17],[12,12], rf)
im_fill(frame1,[15,15],[10,10], ac)
im_fill(frame1,[16,16],[9,11], p)
im_fill(frame1,[17,17],[9,11], tu)
im_fill(frame1,[18,18],[10,10], rf)




frame2 = np.array([[ac]*cols for row in range (rows)])


im_fill(frame2,[5,5],[9,11], b)
im_fill(frame2,[6,6],[8,12], r )
im_fill(frame2,[7,7],[7,13], p)
im_fill(frame2,[8,8],[7,13], y)
im_fill(frame2,[9,9],[7,13], tu)
im_fill(frame2,[10,10],[7,9], pi)
im_fill(frame2,[10,10],[11,13], g)
im_fill(frame2,[11,11],[7,8], r)
im_fill(frame2,[11,11],[12,13], y)
im_fill(frame2,[12,12],[8,8], o)
im_fill(frame2,[12,12],[12,12], p)

frame3 = np.array([[b]*cols for row in range (rows)])


im_fill(frame3,[5,5],[9,11], y)
im_fill(frame3,[6,6],[8,12], y)
im_fill(frame3,[7,7],[7,13], y)
im_fill(frame3,[8,8],[7,13], y)
im_fill(frame3,[9,9],[7,13], y)
im_fill(frame3,[10,10],[7,9], y)
im_fill(frame3,[10,10],[11,13], y)
im_fill(frame3,[11,11],[7,8], y)
im_fill(frame3,[11,11],[12,13], y)
im_fill(frame3,[12,12],[8,8], y)
im_fill(frame3,[12,12],[12,12], y)

#fantasmita
im_fill(frame3,[6,6],[1,2], w)
im_fill(frame3,[7,7],[0,3], w)
im_fill(frame3,[8,8],[0,0], w)
im_fill(frame3,[8,8],[2,2], w)
im_fill(frame3,[9,9],[0,3], w)
im_fill(frame3,[10,10],[0,3], w)
im_fill(frame3,[11,11],[0,3], w)
im_fill(frame3,[12,12],[1,1], w)
im_fill(frame3,[12,12],[3,3], w)

#ojitos mentirosos
im_fill(frame3,[8,8],[1,1], bl)
im_fill(frame3,[8,8],[3,3], bl)


#para abaja

frame4 = np.array([[b]*cols for row in range (rows)])

im_fill(frame4,[10,10],[9,11], y)
im_fill(frame4,[11,11],[8,12], y)
im_fill(frame4,[12,12],[7,13], y)
im_fill(frame4,[13,13],[7,13], y)
im_fill(frame4,[14,14],[7,13], y)
im_fill(frame4,[15,15],[7,9], y)
im_fill(frame4,[15,15],[11,13], y)
im_fill(frame4,[16,16],[7,8], y)
im_fill(frame4,[16,16],[12,13], y)
im_fill(frame4,[17,17],[8,8], y)
im_fill(frame4,[17,17],[12,12], y)

#fantasmita

im_fill(frame4,[6,6],[1,2], w)
im_fill(frame4,[7,7],[0,3], w)
im_fill(frame4,[8,8],[0,0], w)
im_fill(frame4,[8,8],[2,2], w)
im_fill(frame4,[9,9],[0,3], w)
im_fill(frame4,[10,10],[0,3], w)
im_fill(frame4,[11,11],[0,3], w)
im_fill(frame4,[12,12],[1,1], w)
im_fill(frame4,[12,12],[3,3], w) 
        
#ojitos mentirosos
im_fill(frame4,[8,8],[1,1], bl)
im_fill(frame4,[8,8],[3,3], bl)

frame5 = np.array([[b]*cols for row in range (rows)])

im_fill(frame5,[17,17],[9,11], y)
im_fill(frame5,[18,18],[8,12], y)
im_fill(frame5,[19,19],[7,13], y)

#fantasmita

im_fill(frame5,[6,6],[7,8], w)
im_fill(frame5,[7,7],[6,9], w)
im_fill(frame5,[8,8],[6,6], w)
im_fill(frame5,[8,8],[8,8], w)
im_fill(frame5,[9,9],[6,9], w)
im_fill(frame5,[10,10],[6,9], w)
im_fill(frame5,[11,11],[6,9], w)
im_fill(frame5,[12,12],[7,7], w)
im_fill(frame5,[12,12],[9,9], w) 
        
#ojitos mentirosos
im_fill(frame5,[8,8],[7,7], bl)
im_fill(frame5,[8,8],[9,9], bl)


frame6 = np.array([[b]*cols for row in range (rows)])


#fantasmita
im_fill(frame6,[6,6],[9,10], w)
im_fill(frame6,[7,7],[8,11], w)
im_fill(frame6,[8,8],[8,8], w)
im_fill(frame6,[8,8],[10,10], w)
im_fill(frame6,[9,9],[8,11], w)
im_fill(frame6,[10,10],[8,11], w)
im_fill(frame6,[11,11],[8,11], w)
im_fill(frame6,[12,12],[9,9], w)
im_fill(frame6,[12,12],[11,11], w) 
                    
#ojitos mentirosos                                      
im_fill(frame6,[8,8],[9,9], bl)
im_fill(frame6,[8,8],[11,11], bl)

frame7 = np.array([[b]*cols for row in range (rows)])

#fantasmita

im_fill(frame7,[6,6],[14,15], rf)
im_fill(frame7,[7,11],[13,16], rf)
im_fill(frame7,[12,12],[14,14], rf)
im_fill(frame7,[12,12],[16,16], rf)

#ojitos mentirosos
im_fill(frame7,[8,8],[14,14], bl)
im_fill(frame7,[8,8],[16,16], bl)

#boca de fantasma
im_fill(frame7,[9,10],[15,15], r)


frame8 = np.array([[b]*cols for row in range (rows)])

#pac-man
im_fill(frame8,[0,1],[6,12], y)
im_fill(frame8,[2,2],[6,8], y)
im_fill(frame8,[2,2],[10,12], y)
im_fill(frame8,[3,3],[11,12], y)
im_fill(frame8,[4,4],[11,11], y)
im_fill(frame8,[3,3],[6,7], y)
im_fill(frame8,[4,4],[7,7], y)


frame9 = np.array([[b]*cols for row in range (rows)])

#pac-man

im_fill(frame9,[5,5],[9,11], y)
im_fill(frame9,[6,6],[8,12], y)
im_fill(frame9,[7,7],[7,13], y)
im_fill(frame9,[8,8],[7,8], y)
im_fill(frame9,[8,8],[10,13], y)
im_fill(frame9,[9,9],[7,13], y)
im_fill(frame9,[10,10],[7,9], y)
im_fill(frame9,[10,10],[11,13], y)
im_fill(frame9,[11,11],[7,8], y)
im_fill(frame9,[11,11],[12,13], y)
im_fill(frame9,[12,12],[8,8], y)
im_fill(frame9,[12,12],[12,12], y)



frame10 = np.array([[b]*cols for row in range (rows)])

#decaparecer

im_fill(frame10,[0,0],[0,0], b)
im_fill(frame10,[0,0],[0,0],  b)


# Specify the second frame row-by-row
#frame1[0] = [b, r]
#frame1[1] = [b, b]
#im_fill(frame1,[5,9],[6,6], y)
#im_fill(frame1,[5,5],[6,8], y)
#im_fill(frame1,[5,9],[6,8], y)
#frame1[1][3]  = y 
#frame1[3][3]  = y
#frame1[2][4]  = y
#
# 
#im_fill(frame1,[5,7],[16,16], y)
#im_fill(frame1,[5,7],[12,12], y)
#frame1[8][13]  = y
#frame1[8][15]  = y
#frame1[9][14]  = y

#d
#im_fill(frame1,[5,10],[18,18], y) 
#im_fill(frame1,[5,6],[18,20],  y)
#im_fill(frame1,[9,10],[18,20], y)
#frame1[1][15]  = y
#frame1[2][16]  = y
#frame1[3][15]  = y

# Video play                                        
frame_list = [frame0, frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]           # list of frames
fps= 1                            # frames per sec
play_video= vid_show(frame_list, fps) # play on screen