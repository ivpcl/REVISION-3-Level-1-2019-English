from AOLME import *

# Define the size of the image
rows =  20 # num of rows
cols = 20  # num of cols

# Define all of the colors

y = "ffff00" # yellow code
b = "000000" # black code
fg ="228b22" #forest green
g = "00ff00" # green code
s = "c0c0c0" # silver code
dg = "a9a9a9"# dark gray
w ="ffffff"  # white
r="ff0000"   # red
blu="0000ff" # blue
t = "40E0D0" # turquoise code
br= "8b0000" # blood red
o="ff4500"
# Create a frame with the same background color
# Alien comes down from UFO
frame0 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
 # num of rows
cols = 20  # num of cols

# Define all of the colors

y = "ffff00" # yellow code
b = "000000" # black code
fg ="228b22" #forest green
g = "00ff00" # green code
s = "c0c0c0" # silver code
dg = "a9a9a9"# dark gray
w ="ffffff"  # white
r="ff0000"   # red
blu="0000ff" # blue
t = "40E0D0" # turquoise code
br= "8b0000" # blood red
o="ff4500"
# Create a frame with the same background color
# Alien comes down from UFO
frame0 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame0[19] =[g]
frame0[18] =[g]
frame0[17] =[g]
#light
im_fill(frame0,[7,16],[4,14],y)
im_fill(frame0,[6,6],[5,13],y)
im_fill(frame0,[5,5],[6,12],y)
im_fill(frame0,[7,16],[4,14],y)
#UFO
im_fill(frame0,[3,4],[6,12],dg)
im_fill(frame0,[2,2],[7,11],s)
im_fill(frame0,[1,1],[8,10],s)
#Alien
im_fill(frame0,[9,12],[6,10],fg)
im_fill(frame0,[11,11],[8,8],b)
im_fill(frame0,[10,10],[7,7],b)
im_fill(frame0,[10,10],[9,9],b)
im_fill(frame0,[13,13],[7,7],fg)
im_fill(frame0,[13,13],[9,9],fg)
im_fill(frame0,[8,8],[7,7],fg)
im_fill(frame0,[8,8],[9,9],fg)
im_fill(frame0,[7,7],[6,6],fg)
im_fill(frame0,[7,7],[10,10],fg)

#stars
im_fill(frame0,[2,2],[2,2],w)
im_fill(frame0,[5,5],[1,1],w)
im_fill(frame0,[8,8],[2,2],w)
im_fill(frame0,[12,12],[0,0],w)
im_fill(frame0,[0,0],[14,14],w)
im_fill(frame0,[3,3],[16,16],w)
im_fill(frame0,[5,5],[19,19],w)
im_fill(frame0,[9,9],[16,16],w)
im_fill(frame0,[14,14],[17,17],w)


#alien lands on earth
# Create a frame with the same background color
frame1 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame1[19] =[g]
frame1[18] =[g]
frame1[17] =[g]

#UFO is leaving
im_fill(frame1,[3,4],[11,16],dg)
im_fill(frame1,[2,2],[12,15],s)
im_fill(frame1,[1,1],[13,14],s)

#Alien landed on earth
im_fill(frame1,[12,15],[6,10],fg)
im_fill(frame1,[14,14],[8,8],b)
im_fill(frame1,[13,13],[7,7],b)
im_fill(frame1,[13,13],[9,9],b)
im_fill(frame1,[16,16],[7,7],fg)
im_fill(frame1,[16,16],[9,9],fg)
im_fill(frame1,[11,11],[7,7],fg)
im_fill(frame1,[11,11],[9,9],fg)
im_fill(frame1,[10,10],[6,6],fg)
im_fill(frame1,[10,10],[10,10],fg)

#stars
im_fill(frame1,[3,3],[2,2],w)
im_fill(frame1,[6,6],[1,1],w)
im_fill(frame1,[9,9],[2,2],w)
im_fill(frame1,[13,13],[0,0],w)
im_fill(frame1,[6,6],[19,19],w)
im_fill(frame1,[10,10],[16,16],w)
im_fill(frame1,[15,15],[17,17],w)


#alien gets runed over
# Create a frame with the same background color
frame2 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame2[19] =[dg]
frame2[18] =[y]
frame2[17] =[dg]

#Alien walked on the road
im_fill(frame2,[12,15],[6,10],fg)
im_fill(frame2,[14,14],[8,8],b)
im_fill(frame2,[13,13],[7,7],b)
im_fill(frame2,[13,13],[9,9],b)
im_fill(frame2,[16,16],[7,7],fg)
im_fill(frame2,[16,16],[9,9],fg)
im_fill(frame2,[11,11],[7,7],fg)
im_fill(frame2,[11,11],[9,9],fg)
im_fill(frame2,[10,10],[6,6],fg)
im_fill(frame2,[10,10],[10,10],fg)

#car is going straight at the alien
im_fill(frame2,[13,13],[0,2],r)
im_fill(frame2,[14,14],[1,2],r)
im_fill(frame2,[15,15],[2,2],r)
im_fill(frame2,[12,12],[0,0],blu)
im_fill(frame2,[14,14],[0,0],t)
im_fill(frame2,[15,15],[0,1],t)
im_fill(frame2,[16,16],[0,0],t)
#moon
im_fill(frame2,[1,1],[15,17],w)
im_fill(frame2,[2,4],[14,18],w)
im_fill(frame2,[5,5],[15,17],w)


#alien gets runed over
# Create a frame with the same background color
frame3 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
          #grass
frame0[19] =[g]
frame0[18] =[g]
frame0[17] =[g]
#light
im_fill(frame0,[7,16],[4,14],y)
im_fill(frame0,[6,6],[5,13],y)
im_fill(frame0,[5,5],[6,12],y)
im_fill(frame0,[7,16],[4,14],y)
#UFO
im_fill(frame0,[3,4],[6,12],dg)
im_fill(frame0,[2,2],[7,11],s)
im_fill(frame0,[1,1],[8,10],s)
#Alien
im_fill(frame0,[9,12],[6,10],fg)
im_fill(frame0,[11,11],[8,8],b)
im_fill(frame0,[10,10],[7,7],b)
im_fill(frame0,[10,10],[9,9],b)
im_fill(frame0,[13,13],[7,7],fg)
im_fill(frame0,[13,13],[9,9],fg)
im_fill(frame0,[8,8],[7,7],fg)
im_fill(frame0,[8,8],[9,9],fg)
im_fill(frame0,[7,7],[6,6],fg)
im_fill(frame0,[7,7],[10,10],fg)

#stars
im_fill(frame0,[2,2],[2,2],w)
im_fill(frame0,[5,5],[1,1],w)
im_fill(frame0,[8,8],[2,2],w)
im_fill(frame0,[12,12],[0,0],w)
im_fill(frame0,[0,0],[14,14],w)
im_fill(frame0,[3,3],[16,16],w)
im_fill(frame0,[5,5],[19,19],w)
im_fill(frame0,[9,9],[16,16],w)
im_fill(frame0,[14,14],[17,17],w)


#alien lands on earth
# Create a frame with the same background color
frame1 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame1[19] =[g]
frame1[18] =[g]
frame1[17] =[g]

#UFO is leaving
im_fill(frame1,[3,4],[11,16],dg)
im_fill(frame1,[2,2],[12,15],s)
im_fill(frame1,[1,1],[13,14],s)

#Alien landed on earth
im_fill(frame1,[12,15],[6,10],fg)
im_fill(frame1,[14,14],[8,8],b)
im_fill(frame1,[13,13],[7,7],b)
im_fill(frame1,[13,13],[9,9],b)
im_fill(frame1,[16,16],[7,7],fg)
im_fill(frame1,[16,16],[9,9],fg)
im_fill(frame1,[11,11],[7,7],fg)
im_fill(frame1,[11,11],[9,9],fg)
im_fill(frame1,[10,10],[6,6],fg)
im_fill(frame1,[10,10],[10,10],fg)

#stars
im_fill(frame1,[3,3],[2,2],w)
im_fill(frame1,[6,6],[1,1],w)
im_fill(frame1,[9,9],[2,2],w)
im_fill(frame1,[13,13],[0,0],w)
im_fill(frame1,[6,6],[19,19],w)
im_fill(frame1,[10,10],[16,16],w)
im_fill(frame1,[15,15],[17,17],w)


#alien gets runed over
# Create a frame with the same background color
frame2 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame2[19] =[dg]
frame2[18] =[y]
frame2[17] =[dg]

#Alien walked on the road
im_fill(frame2,[12,15],[6,10],fg)
im_fill(frame2,[14,14],[8,8],b)
im_fill(frame2,[13,13],[7,7],b)
im_fill(frame2,[13,13],[9,9],b)
im_fill(frame2,[16,16],[7,7],fg)
im_fill(frame2,[16,16],[9,9],fg)
im_fill(frame2,[11,11],[7,7],fg)
im_fill(frame2,[11,11],[9,9],fg)
im_fill(frame2,[10,10],[6,6],fg)
im_fill(frame2,[10,10],[10,10],fg)

#car is going straight at the alien
im_fill(frame2,[13,13],[0,2],r)
im_fill(frame2,[14,14],[1,2],r)
im_fill(frame2,[15,15],[2,2],r)
im_fill(frame2,[12,12],[0,0],blu)
im_fill(frame2,[14,14],[0,0],t)
im_fill(frame2,[15,15],[0,1],t)
im_fill(frame2,[16,16],[0,0],t)
#moon
im_fill(frame2,[1,1],[15,17],w)
im_fill(frame2,[2,4],[14,18],w)
im_fill(frame2,[5,5],[15,17],w)


#alien gets runed over
# Create a frame with the same background color
frame3 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame3[19] =[dg]
frame3[18] =[y]
frame3[17] =[dg]

#Alien is squished
im_fill(frame3,[12,15],[6,10],fg)
im_fill(frame3,[14,14],[8,8],b)
im_fill(frame3,[13,13],[7,7],b)
im_fill(frame3,[13,13],[9,9],b)
im_fill(frame3,[16,16],[7,7],fg)
im_fill(frame3,[16,16],[9,9],fg)
im_fill(frame3,[11,11],[7,7],fg)
im_fill(frame3,[11,11],[9,9],fg)
im_fill(frame3,[10,10],[6,6],fg)
im_fill(frame3,[10,10],[10,10],fg)

#car 
im_fill(frame3,[11,15],[0,5],r)
im_fill(frame3,[13,15],[6,9],r)
im_fill(frame3,[12,12],[1,3],blu)
im_fill(frame3,[12,12],[6,7],blu)
im_fill(frame3,[15,15],[0,2],t)
im_fill(frame3,[14,14],[1,1],t)
im_fill(frame3,[16,16],[1,1],t)
im_fill(frame3,[15,15],[6,8],t)
im_fill(frame3,[14,14],[7,7],t)
im_fill(frame3,[16,16],[7,7],t)
#moon
im_fill(frame3,[1,1],[15,17],w)
im_fill(frame3,[2,4],[14,18],w)
im_fill(frame3,[5,5],[15,17],w)

#alien is volando
# Create a frame with the same background color
frame4 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#stret
frame4[19] =[dg]
frame4[18] =[y]
frame4[17] =[dg]
#Alien is volando
im_fill(frame4,[4,7],[6,10],fg)
im_fill(frame4,[8,8],[7,7],fg)
im_fill(frame4,[8,8],[9,9],fg)
im_fill(frame4,[5,5],[7,7],b)
im_fill(frame4,[5,5],[9,9],b)
im_fill(frame4,[6,6],[8,8],b)
im_fill(frame4,[3,3],[7,7],fg)
im_fill(frame4,[3,3],[9,9],fg)
im_fill(frame4,[2,2],[6,6],fg)
im_fill(frame4,[2,2],[10,10],fg)

#car run
im_fill(frame4,[11,12],[17,19],r)
im_fill(frame4,[13,15],[15,19],r)
im_fill(frame4,[12,12],[18,19],blu)
im_fill(frame4,[15,15],[17,19],t)
im_fill(frame4,[14,14],[18,18],t)
im_fill(frame4,[16,16],[18,18],t)
#moon
im_fill(frame4,[1,1],[15,17],w)
im_fill(frame4,[2,4],[14,18],w)
im_fill(frame4,[5,5],[15,17],w)

# Create a frame with the same background color
#alien si golpiado
frame5 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#gras
frame5[19] =[dg]
frame5[18] =[y]
frame5[17] =[dg]
#alien is sangrando
im_fill(frame5,[12,15],[6,10],fg)
im_fill(frame5,[14,14],[8,8],b)
im_fill(frame5,[12,14],[6,6],br)
im_fill(frame5,[14,14],[7,7],br)
im_fill(frame5,[13,13],[7,7],b)
im_fill(frame5,[13,13],[9,9],b)
im_fill(frame5,[16,16],[7,7],fg)
im_fill(frame5,[16,16],[9,9],fg)
im_fill(frame5,[11,11],[7,7],fg)
im_fill(frame5,[11,11],[9,9],fg)
im_fill(frame5,[10,10],[6,6],fg)
im_fill(frame5,[10,10],[10,10],fg)

# Create a frame with the same background color
# rayo
frame6 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame6[19] =[dg]
frame6[18] =[y]
frame6[17] =[dg]
#Alien
im_fill(frame6,[12,15],[6,10],fg)
im_fill(frame6,[14,14],[8,8],b)
im_fill(frame6,[12,14],[6,6],br)
im_fill(frame6,[14,14],[7,7],br)
im_fill(frame6,[12,12],[9,10],br)
im_fill(frame6,[13,13],[7,7],b)
im_fill(frame6,[13,13],[9,9],b)
im_fill(frame6,[16,16],[7,7],fg)
im_fill(frame6,[16,16],[9,9],fg)
im_fill(frame6,[11,11],[7,7],fg)
im_fill(frame6,[11,11],[9,9],fg)
im_fill(frame6,[10,10],[6,6],fg)
im_fill(frame6,[10,10],[10,10],fg)

#rain
im_fill(frame6,[2,2],[2,2],blu)
im_fill(frame6,[5,5],[1,1],blu)
im_fill(frame6,[8,8],[2,2],blu)
im_fill(frame6,[12,12],[0,0],blu)
im_fill(frame6,[0,0],[14,14],blu)
im_fill(frame6,[5,5],[19,19],blu)
im_fill(frame6,[9,9],[16,16],blu)
im_fill(frame6,[14,14],[17,17],blu)

#lightning
im_fill(frame6,[3,5],[14,14],y)
im_fill(frame6,[6,8],[12,12],y)
im_fill(frame6,[8,10],[11,11],y)
im_fill(frame6,[11,11],[11,11],r)
im_fill(frame6,[11,11],[10,10],y)
im_fill(frame6,[5,6],[13,13],y)
im_fill(frame6,[3,3],[14,15],y)
im_fill(frame6,[1,3],[15,15],y)
im_fill(frame6,[1,1],[15,16],y)
im_fill(frame6,[0,1],[16,16],y)

# Create a frame with the same background color
frame7 = np.array([[b]*cols for row in range (rows)])
#esqueleto 


#Alien
im_fill(frame7,[12,15],[6,10],s)
im_fill(frame7,[14,14],[8,8],b)
im_fill(frame7,[14, 14],[6,7],w)
im_fill(frame7,[15,16],[7,7],w)
im_fill(frame7,[14,14],[9,10],w)
im_fill(frame7,[15,16],[9,9],w)
im_fill(frame7,[13,13],[7,7],b)
im_fill(frame7,[13,13],[9,9],b)
im_fill(frame7,[11,11],[7,7],s)
im_fill(frame7,[11,11],[9,9],s)
im_fill(frame7,[10,10],[6,6],s)
im_fill(frame7,[10,10],[10,10],s)

# Create a frame with the same background color
frame8 = np.array([[b]*cols for row in range (rows)])
#fin
im_fill(frame8,[4,11],[4,4],w)
im_fill(frame8,[4,4],[4,7],w)
im_fill(frame8,[7,7],[4,7],w)
im_fill(frame8,[7,11],[9,9],w)
im_fill(frame8,[4,4],[9,9],w)
im_fill(frame8,[7,7],[11,14],w)
im_fill(frame8,[8,11],[11,11],w)
im_fill(frame8,[8,11],[14,14],w)
#Alien
im_fill(frame8,[14,18],[13,17],fg)
im_fill(frame8,[18,18],[14,14],fg)
im_fill(frame8,[18,18],[16,18],fg)
im_fill(frame8,[12,12],[14,14],fg)
im_fill(frame8,[12,12],[13,13],fg)
im_fill(frame8,[12,12],[17,17],fg)
im_fill(frame8,[13,13],[14,14],fg)
im_fill(frame8,[13,13],[16,16],fg)
im_fill(frame8,[15,15],[14,14],b)
im_fill(frame8,[16,16],[15,15],b)
im_fill(frame8,[15,15],[16,16],b)


# Create a frame with the same background color
frame9 = np.array([[b]*cols for row in range (rows)])
#moon
im_fill(frame9,[1,1],[15,17],w)
im_fill(frame9,[2,4],[14,18],w)
im_fill(frame9,[5,5],[15,17],w)

#stars
im_fill(frame9,[2,2],[2,2],y)
im_fill(frame9,[5,5],[1,1],y)
im_fill(frame9,[8,8],[2,2],y)
im_fill(frame9,[12,12],[0,0],y)
im_fill(frame9,[0,0],[14,14],y)
im_fill(frame9,[5,5],[19,19],y)
im_fill(frame9,[9,9],[16,16],y)
im_fill(frame9,[14,14],[17,17],y)
#grass
frame9[19] =[g]
frame9[18] =[g]
frame9[17] =[g]
#tombstone
im_fill(frame9,[10,10],[3,13],s)
im_fill(frame9,[11,16],[2,14],s)

#R
im_fill(frame9,[12,15],[3,3],b)
im_fill(frame9,[12,12],[4,5],b)
im_fill(frame9,[13,13],[5,5],b)
im_fill(frame9,[14,14],[4,4],b)
im_fill(frame9,[15,15],[5,5],b)

#I
im_fill(frame9,[12,12],[7,9],b)
im_fill(frame9,[13,14],[8,8],b)
im_fill(frame9,[15,15],[7,9],b)

#P
im_fill(frame9,[12,15],[11,11],b)
im_fill(frame9,[12,14],[12,13],b)
im_fill(frame9,[13,13],[12,12],s)


# Video play
frame_list = [frame0,frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame9,frame8]         # list of frames
fps= 1
# frames per sec
play_video= vid_show(frame_list, fps) # play on screen
