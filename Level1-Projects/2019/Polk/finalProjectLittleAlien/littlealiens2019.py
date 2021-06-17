# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:41:33 2019

@author: aolme4
"""

from AOLME import *

# Define the size of the image
rows = 20 # num of rows
cols = 20  # num of cols

# Define all of the colors

# Define all of the colors

p = "ff9999" # pink code
b = "000000" # black code
fg ="228b22" #forest green
g = "00ff00" # green code
s = "c0c0c0" # silver code
dg = "a9a9a9"# dark gray
w ="ffffff"  # white
y="ffff4d"   # yellow code
blu="0000ff" # blue
t = "744d25" # turquoise code
br= "8b0000" # blood red
tan="ffcc99" # tan
o="ff8533"   # orange
bro="996633" # brown
r="e62e00" # red

# Alien comes down from UFO
frame0 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
 # num of rows
#cols = 20  # num of cols

# Create a frame with the same background color
# Alien comes down from UFO
frame0 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass
frame0[19] =[g]
frame0[18] =[g]
#UFO
im_fill(frame0,[1,1],[15,16],dg)
im_fill(frame0,[2,2],[14,17],s)
im_fill(frame0,[3,3],[13,18],s)
#Alien
im_fill(frame0,[11,11],[1,1],fg)
im_fill(frame0,[11,11],[5,5],fg)
im_fill(frame0,[12,12],[2,2],fg)
im_fill(frame0,[12,12],[4,4],fg)
im_fill(frame0,[13,13],[1,5],fg)
im_fill(frame0,[14,14],[1,5],fg)
im_fill(frame0,[15,15],[1,5],fg)
im_fill(frame0,[16,16],[1,5],fg)
im_fill(frame0,[17,17],[2,2],fg)
im_fill(frame0,[17,17],[4,4],fg)
im_fill(frame0,[14,14],[2,2],b)
im_fill(frame0,[14,14],[4,4],b)
im_fill(frame0,[15,15],[3,3],b)
# girl alien
im_fill(frame0,[11,11],[7,7],p)
im_fill(frame0,[11,11],[11,11],p)
im_fill(frame0,[12,12],[8,8],p)
im_fill(frame0,[12,12],[10,10],p)
im_fill(frame0,[13,13],[7,11],p)
im_fill(frame0,[14,14],[7,11],p)
im_fill(frame0,[15,15],[7,11],p)
im_fill(frame0,[16,16],[7,11],p)
im_fill(frame0,[17,17],[8,8],p)
im_fill(frame0,[17,17],[10,10],p)
im_fill(frame0,[14,14],[8,*-8],b)
im_fill(frame0,[14,14],[10,10],b)
im_fill(frame0,[15,15],[9,9],b)
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


##little aliens in the grave yard
## Create a frame with the same background color
frame1 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#grass

frame1[19] =[g]
frame1[18] =[g]

#tomb
im_fill(frame1,[14,14],[16,18],w)
im_fill(frame1,[13,13],[17,17],w)
im_fill(frame1,[15,15],[17,17],w)
im_fill(frame1,[16,16],[16,18],s)
im_fill(frame1,[17,17],[15,19],s)
#little alien crying ///**** this is where we left on last week
im_fill(frame1,[11,11],[1,1],fg)
im_fill(frame1,[11,11],[5,5],fg)
im_fill(frame1,[12,12],[2,2],fg)
im_fill(frame1,[12,12],[4,4],fg)
im_fill(frame1,[13,13],[1,5],fg)
im_fill(frame1,[14,14],[1,5],fg)
im_fill(frame1,[15,15],[1,5],fg)
im_fill(frame1,[16,16],[1,5],fg)
im_fill(frame1,[17,17],[2,2],fg)
im_fill(frame1,[17,17],[4,4],fg)
im_fill(frame1,[14,14],[2,2],b)
im_fill(frame1,[14,14],[4,4],b)
im_fill(frame1,[15,15],[3,3],b)
im_fill(frame1,[15,15],[2,2],blu)
im_fill(frame1,[16,16],[1,1],blu)
im_fill(frame1,[17,17],[0,0],blu)
im_fill(frame1,[15,15],[4,4],blu)
im_fill(frame1,[16,16],[5,5],blu)
im_fill(frame1,[17,17],[6,6],blu)
#Little girl alien crying
im_fill(frame1,[11,11],[7,7],p)
im_fill(frame1,[11,11],[11,11],p)
im_fill(frame1,[12,12],[8,8],p)
im_fill(frame1,[12,12],[10,10],p)
im_fill(frame1,[13,13],[7,11],p)
im_fill(frame1,[14,14],[7,11],p)
im_fill(frame1,[15,15],[7,11],p)
im_fill(frame1,[16,16],[7,11],p)
im_fill(frame1,[17,17],[8,8],p)
im_fill(frame1,[17,17],[10,10],p)
im_fill(frame1,[14,14],[8,8],b)
im_fill(frame1,[14,14],[10,10],b)
im_fill(frame1,[15,15],[9,9],b)
im_fill(frame1,[15,15],[8,8],blu)
im_fill(frame1,[16,16],[7,7],blu)
im_fill(frame1,[17,17],[6,6],blu)
im_fill(frame1,[15,15],[10,10],blu)
im_fill(frame1,[16,16],[11,11],blu)
im_fill(frame1,[17,17],[12,12],blu)
#stars
im_fill(frame1,[3,3],[2,2],w)
im_fill(frame1,[6,6],[1,1],w)
im_fill(frame1,[9,9],[2,2],w)
im_fill(frame1,[0,0],[3,3],w)
im_fill(frame1,[6,6],[19,19],w)
im_fill(frame1,[10,10],[16,16],w)
im_fill(frame1,[1,1],[6,6],w)
im_fill(frame1,[5,5],[4,4],w)
im_fill(frame1,[8,8],[4,4],w)
im_fill(frame1,[6,6],[7,7],w)
im_fill(frame1,[9,9],[9,9],w)
im_fill(frame1,[6,6],[11,11],w)
im_fill(frame1,[4,4],[8,8],w)
im_fill(frame1,[2,2],[10,10],w)
im_fill(frame1,[4,4],[13,13],w)
im_fill(frame1,[0,0],[13,13],w)
im_fill(frame1,[3,3],[15,15],w)
im_fill(frame1,[1,1],[17,17],w)
im_fill(frame1,[0,0],[19,19],w)
im_fill(frame1,[8,8],[13,13],w)
im_fill(frame1,[7,7],[16,16],w)
##alien gets runed over
## Create a frame with the same background color
frame2 = np.array([[b]*cols for row in range (rows)])
#
## Specify the frame row-by-row
##grass
frame2[19] =[fg]
im_fill(frame2,[18,18],[0,0],fg)
im_fill(frame2,[18,18],[19,19],fg)
#Jungle
im_fill(frame2,[11,13],[0,0],fg)
im_fill(frame2,[14,14],[1,5],fg)
im_fill(frame2,[11,13],[6,6],fg)
im_fill(frame2,[10,10],[1,1],fg)
im_fill(frame2,[10,10],[5,5],fg)
im_fill(frame2,[9,9],[2,4],fg)
im_fill(frame2,[14,14],[7,7],fg)
im_fill(frame2,[15,15],[6,6],fg)
im_fill(frame2,[15,15],[8,8],fg)
im_fill(frame2,[16,16],[5,5],fg)
im_fill(frame2,[16,16],[9,9],fg)
im_fill(frame2,[17,17],[6,6],fg)
im_fill(frame2,[17,17],[8,8],fg)
im_fill(frame2,[17,17],[11,13],fg)
im_fill(frame2,[16,16],[12,12],fg)
im_fill(frame2,[16,16],[15,15],fg)
im_fill(frame2,[16,16],[17,17],fg)
im_fill(frame2,[15,15],[14,14],fg)
im_fill(frame2,[15,15],[18,18],fg)
im_fill(frame2,[14,14],[15,15],fg)
im_fill(frame2,[14,14],[17,17],fg)
im_fill(frame2,[13,13],[16,16],fg)
im_fill(frame2,[15,19],[3,3],bro)
im_fill(frame2,[18,19],[7,7],bro)
im_fill(frame2,[18,19],[12,12],bro)
im_fill(frame2,[17,19],[16,16],bro)
## Create a frame with the same background color
frame3 = np.array([[b]*cols for row in range (rows)])
#
## Specify the frame row-by-row
##grass
frame3[19] =[fg]
im_fill(frame3,[18,18],[0,0],fg)
im_fill(frame3,[18,18],[19,19],fg)
#trees
im_fill(frame3,[6,6],[2,4],fg)
im_fill(frame3,[7,7],[1,1],fg)
im_fill(frame3,[7,7],[5,5],fg)
im_fill(frame3,[8,10],[0,0],fg)
im_fill(frame3,[8,10],[6,6],fg)
im_fill(frame3,[11,11],[1,5],fg)
im_fill(frame3,[2,2],[15,17],fg)
im_fill(frame3,[4,6],[13,13],fg)
im_fill(frame3,[4,6],[19,19],fg)
im_fill(frame3,[3,3],[14,14],fg)
im_fill(frame3,[3,3],[18,18],fg)
im_fill(frame3,[7,7],[14,18],fg)
im_fill(frame3,[12,18],[2,3],bro)
im_fill(frame3,[8,18],[16,17],bro)



#monkey
im_fill(frame3,[10,14],[7,11],bro)
im_fill(frame3,[12,12],[6,6],bro)
im_fill(frame3,[12,12],[12,12],bro)
im_fill(frame3,[14,14],[6,6],bro)
im_fill(frame3,[14,14],[12,12],bro)
im_fill(frame3,[15,16],[8,10],bro)
im_fill(frame3,[16,17],[7,7],bro)
im_fill(frame3,[16,17],[11,11],bro)
im_fill(frame3,[17,17],[8,8],bro)
im_fill(frame3,[17,17],[10,10],bro)
im_fill(frame3,[11,13],[8,10],tan)
im_fill(frame3,[13,13],[6,6],tan)
im_fill(frame3,[13,13],[12,12],tan)
im_fill(frame3,[18,18],[6,8],tan)
im_fill(frame3,[18,18],[10,12],tan)
im_fill(frame3,[12,12],[8,8],b)
im_fill(frame3,[12,12],[10,10],b)
im_fill(frame3,[13,13],[9,9],b)


#stars
im_fill(frame3,[1,1],[10,10],w)
im_fill(frame3,[2,2],[3,3],w)
im_fill(frame3,[4,4],[1,1],w)
im_fill(frame3,[4,4],[7,7],w)
im_fill(frame3,[7,7],[11,11],w)
im_fill(frame3,[15,15],[14,14],w)
im_fill(frame3,[16,16],[5,5],w)




##alien is volando
## Create a frame with the same background color
frame4 = np.array([[b]*cols for row in range (rows)])

# Specify the frame row-by-row
#stret
frame4[19] =[g]
frame4[18] =[g]

#Boy Alien
im_fill(frame4,[11,11],[4,4],fg)
im_fill(frame4,[12,12],[5,5],fg)
im_fill(frame4,[11,11],[8,8],fg)
im_fill(frame4,[12,12],[7,7],fg)
im_fill(frame4,[13,16],[4,8],fg)
im_fill(frame4,[17,17],[5,5],fg)
im_fill(frame4,[17,17],[7,7],fg)
im_fill(frame4,[14,14],[5,5],b)
im_fill(frame4,[14,14],[7,7],b)
im_fill(frame4,[15,15],[6,6],b)
im_fill(frame4,[16,16],[3,3],bro)
im_fill(frame4,[17,17],[2,2],bro)
im_fill(frame4,[17,17],[6,6],bro)
im_fill(frame4,[16,16],[9,9],bro)
im_fill(frame4,[17,17],[10,10],bro)
#Girl Alien
im_fill(frame4,[11,11],[11,11],p)
im_fill(frame4,[12,12],[12,12],p)
im_fill(frame4,[12,12],[14,14],p)
im_fill(frame4,[11,11],[15,15],p)
im_fill(frame4,[13,13],[11,15],p)
im_fill(frame4,[14,14],[11,15],p)
im_fill(frame4,[15,15],[11,15],p)
im_fill(frame4,[16,16],[11,15],p)
im_fill(frame4,[17,17],[12,12],p)
im_fill(frame4,[17,17],[14,14],p)
im_fill(frame4,[14,14],[12,12],b)
im_fill(frame4,[15,15],[13,13],b)
im_fill(frame4,[14,14],[14,14],b)
im_fill(frame4,[16,16],[10,10],y)
im_fill(frame4,[17,17],[9,9],y)
im_fill(frame4,[17,17],[13,13],y)
im_fill(frame4,[16,16],[16,16],y)
im_fill(frame4,[17,17],[17,17],y)
#spaceship Alert!
## Create a frame with the same background colo    
frame5 = np.array([[b]*cols for row in range (rows)])
#
## Specify the frame row-by-row
##gras
frame5[19] =[g]
frame5[18] =[g]
#alien attackn alert!

im_fill(frame5,[11,11],[4,4],fg)
im_fill(frame5,[12,12],[5,5],fg)
im_fill(frame5,[11,11],[8,8],fg)
im_fill(frame5,[13,16],[4,8],fg)
im_fill(frame5,[17,17],[5,5],fg)
im_fill(frame5,[17,17],[7,7],fg)
im_fill(frame5,[14,14],[5,5],b)
im_fill(frame5,[14,14],[7,7],b)
im_fill(frame5,[15,15],[6,6],b)

im_fill(frame5,[12,12],[7,7],fg)
im_fill(frame5,[4,4],[10,10],fg)
im_fill(frame5,[5,5],[10,10],fg)
im_fill(frame5,[6,6],[10,10],fg)
im_fill(frame5,[7,7],[10,10],fg)
im_fill(frame5,[4,4],[11,11],fg)
im_fill(frame5,[4,7],[12,12],fg)
im_fill(frame5,[6,6],[11,11],fg)

im_fill(frame5,[4,4],[15,17],fg)
im_fill(frame5,[5,5],[16,16],b)
im_fill(frame5,[5,5],[15,15],fg)
im_fill(frame5,[5,5],[17,17],fg)
im_fill(frame5,[6,6],[15,17],fg)
im_fill(frame5,[7,7],[15,15],fg)
im_fill(frame5,[7,7],[17,17],fg)



frame6 = np.array([[b]*cols for row in range (rows)])
im_fill(frame6,[10,10],[4,4],b)
im_fill(frame6,[11,11],[5,5],b)
im_fill(frame6,[10,10],[6,6],b)
im_fill(frame6,[8,8],[3,7],bro)
im_fill(frame6,[9,9],[3,3],bro)
im_fill(frame6,[10,10],[3,3],bro)
im_fill(frame6,[11,11],[3,3],bro)
im_fill(frame6,[9,9],[7,7],bro)
im_fill(frame6,[10,10],[7,7],bro)
im_fill(frame6,[11,11],[7,7],bro)
im_fill(frame6,[10,10],[2,2],bro)
im_fill(frame6,[10,10],[8,8],bro)

im_fill(frame6,[12,12],[2,8],bro)
im_fill(frame6,[13,13],[4,6],bro)
im_fill(frame6,[14,14],[4,6],bro)
im_fill(frame6,[15,15],[3,7],bro)
im_fill(frame6,[16,16],[3,4],bro)
im_fill(frame6,[16,16],[6,7],bro)

im_fill(frame6,[9,9],[4,6],tan)
im_fill(frame6,[10,10],[5,5],tan)
im_fill(frame6,[11,11],[4,4],tan)
im_fill(frame6,[11,11],[6,6],tan)
im_fill(frame6,[13,13],[2,2],tan)
im_fill(frame6,[12,12],[9,9],tan)
im_fill(frame6,[17,17],[2,4],tan)
im_fill(frame6,[17,17],[6,8],tan)

im_fill(frame6,[11,11],[10,10],p)
im_fill(frame6,[12,12],[11,11],p)
im_fill(frame6,[11,11],[14,14],p)


im_fill(frame6,[13,13],[10,14],p)
im_fill(frame6,[13,13],[11,11],p)
im_fill(frame6,[13,13],[12,12],p)
im_fill(frame6,[12,12],[13,13],p)
im_fill(frame6,[13,16],[10,14],p)
im_fill(frame6,[17,17],[11,11],p)
im_fill(frame6,[17,17],[13,13],p)


im_fill(frame6,[14,14],[11,11],b)
im_fill(frame6,[14,14],[13,13],b)
im_fill(frame6,[15,15],[12,12],b)

im_fill(frame6,[15,15],[11,11],blu)
im_fill(frame6,[16,16],[10,10],blu)
im_fill(frame6,[17,17],[9,9],blu)
im_fill(frame6,[15,15],[13,13],blu)
im_fill(frame6,[16,16],[14,14],blu)
im_fill(frame6,[17,17],[15,15],blu)
##frame 7 spaceship
#
frame7 = np.array([[b]*cols for row in range (rows)])
#space ship
im_fill(frame7,[3,3],[3,8],s)
im_fill(frame7,[4,4],[2,2],s)
im_fill(frame7,[5,5],[1,1],s)
im_fill(frame7,[6,6],[0,0],s)
im_fill(frame7,[7,7],[0,12],s)
im_fill(frame7,[4,4],[9,9],s)
im_fill(frame7,[5,5],[10,10],s)
im_fill(frame7,[6,6],[11,11],s)
im_fill(frame7,[8,17],[0,0],dg)
im_fill(frame7,[9,19],[1,1],dg)
im_fill(frame7,[10,18],[2,2],dg)
im_fill(frame7,[11,18],[3,3],dg)
im_fill(frame7,[12,18],[4,4],dg)
im_fill(frame7,[13,18],[5,5],dg)
im_fill(frame7,[14,18],[6,6],dg)
im_fill(frame7,[15,18],[7,7],dg)
im_fill(frame7,[16,18],[8,8],dg)
im_fill(frame7,[17,18],[9,9],dg)
im_fill(frame7,[18,18],[10,10],dg)
# grass
im_fill(frame7,[18,18],[0,0],fg)
im_fill(frame7,[18,18],[19,19],fg)
im_fill(frame7,[19,19],[0,19],fg)
#little girl Alien
im_fill(frame7,[10,13],[6,10],p)
im_fill(frame7,[9,9],[7,7],p)
im_fill(frame7,[9,9],[9,9],p)
im_fill(frame7,[8,8],[6,6],p)
im_fill(frame7,[8,8],[10,10],p)
im_fill(frame7,[14,14],[7,7],p)
im_fill(frame7,[14,14],[9,9],p)
im_fill(frame7,[11,11],[7,7],b)
im_fill(frame7,[11,11],[9,9],b)
im_fill(frame7,[12,12],[8,8],b)
# Mounkey 
im_fill(frame7,[9,13],[13,17],bro)
im_fill(frame7,[11,11],[12,12],bro)
im_fill(frame7,[11,11],[18,18],bro)
im_fill(frame7,[13,13],[12,12],bro)
im_fill(frame7,[13,13],[18,18],bro)
im_fill(frame7,[14,14],[12,12],tan)
im_fill(frame7,[14,14],[18,18],tan)
im_fill(frame7,[10,12],[14,16],tan)
im_fill(frame7,[11,11],[14,14],b)
im_fill(frame7,[11,11],[16,16],b)
im_fill(frame7,[12,12],[15,15],b)
im_fill(frame7,[14,15],[14,16],bro)
im_fill(frame7,[16,17],[13,14],bro)
im_fill(frame7,[16,17],[16,17],bro)
im_fill(frame7,[16,16],[15,15],bro)
im_fill(frame7,[18,18],[12,14],tan)
im_fill(frame7,[18,18],[16,18],tan)


## Create a frame with the same background color
frame8 = np.array([[b]*cols for row in range (rows)])
##fin
im_fill(frame8,[0,0],[2,2],fg)
im_fill(frame8,[1,5],[1,4],fg)
im_fill(frame8,[2,2],[0,0],fg)
im_fill(frame8,[4,4],[0,0],fg)
im_fill(frame8,[6,6],[2,2],fg)
im_fill(frame8,[2,2],[5,5],fg)
im_fill(frame8,[4,4],[5,5],fg)
im_fill(frame8,[1,1],[6,6],fg)

im_fill(frame8,[5,5],[6,6],fg)
im_fill(frame8,[2,2],[3,3],b)
im_fill(frame8,[3,3],[2,2],b)
im_fill(frame8,[4,4],[3,3],b)

im_fill(frame8,[7,7],[2,2],bro)
im_fill(frame8,[7,8],[3,4],dg)
im_fill(frame8,[8,8],[4,4],r)

im_fill(frame8,[9,13],[2,6],bro)
im_fill(frame8,[14,15],[3,5],bro)
im_fill(frame8,[16,17],[2,3],bro)
im_fill(frame8,[16,16],[4,4],bro)
im_fill(frame8,[16,17],[5,6],bro)
im_fill(frame8,[13,13],[1,1],bro)
im_fill(frame8,[13,13],[7,7],bro)

im_fill(frame8,[10,12],[3,5],tan)
im_fill(frame8,[14,14],[1,1],tan)
im_fill(frame8,[12,12],[7,7],tan)
im_fill(frame8,[18,18],[1,3],tan)
im_fill(frame8,[18,18],[5,7],tan)

im_fill(frame8,[11,11],[3,3],b)
im_fill(frame8,[12,12],[4,4],b)
im_fill(frame8,[11,11],[5,5],b)
im_fill(frame8,[9,10],[5,6],r)


im_fill(frame8,[0,0],[13,13],dg)
im_fill(frame8,[1,1],[12,12],dg)
im_fill(frame8,[1,1],[14,14],dg)
im_fill(frame8,[2,2],[13,13],dg)
im_fill(frame8,[3,3],[12,12],dg)
im_fill(frame8,[3,3],[14,14],dg)
im_fill(frame8,[4,4],[13,13],dg)
im_fill(frame8,[5,5],[12,12],dg)
im_fill(frame8,[5,5],[14,14],dg)
im_fill(frame8,[6,6],[13,13],dg)
im_fill(frame8,[7,7],[12,12],dg)
im_fill(frame8,[7,7],[14,14],dg)
im_fill(frame8,[8,8],[13,13],dg)
im_fill(frame8,[9,9],[12,12],dg)
im_fill(frame8,[9,9],[14,14],dg)

#girl alien
im_fill(frame8,[11,11],[11,11],p)
im_fill(frame8,[11,11],[15,15],p)
im_fill(frame8,[12,12],[12,12],p)
im_fill(frame8,[12,12],[14,14],p)
im_fill(frame8,[13,13],[11,15],p)
im_fill(frame8,[14,14],[11,15],p)
im_fill(frame8,[15,15],[11,15],p)
im_fill(frame8,[16,16],[11,15],p)
im_fill(frame8,[17,17],[12,12],p)
im_fill(frame8,[17,17],[14,14],p)

im_fill(frame8,[14,14],[12,12],b)
im_fill(frame8,[15,15],[13,13],b)
im_fill(frame8,[14,14],[14,14],b)

im_fill(frame8,[10,10],[9,17],dg)
im_fill(frame8,[10,18],[9,9],dg)
im_fill(frame8,[18,18],[9,17],dg)
im_fill(frame8,[10,18],[17,17],dg)

im_fill(frame8,[15,15],[12,12],blu)
im_fill(frame8,[16,16],[11,11],blu)
im_fill(frame8,[17,17],[10,10],blu)
im_fill(frame8,[15,15],[14,14],blu)
im_fill(frame8,[16,16],[15,15],blu)
im_fill(frame8,[17,17],[16,16],blu)

frame9 = np.array([[b]*cols for row in range (rows)])
#space ship
im_fill(frame9,[3,3],[3,8],s)
im_fill(frame9,[4,4],[2,2],s)
im_fill(frame9,[5,5],[1,1],s)
im_fill(frame9,[6,6],[0,0],s)
im_fill(frame9,[7,7],[0,12],s)
im_fill(frame9,[4,4],[9,9],s)
im_fill(frame9,[5,5],[10,10],s)
im_fill(frame9,[6,6],[11,11],s)
im_fill(frame9,[8,17],[0,0],dg)
im_fill(frame9,[9,19],[1,1],dg)
im_fill(frame9,[10,18],[2,2],dg)
im_fill(frame9,[11,18],[3,3],dg)
im_fill(frame9,[12,18],[4,4],dg)
im_fill(frame9,[13,18],[5,5],dg)
im_fill(frame9,[14,18],[6,6],dg)
im_fill(frame9,[15,18],[7,7],dg)
im_fill(frame9,[16,18],[8,8],dg)
im_fill(frame9,[17,18],[9,9],dg)
im_fill(frame9,[18,18],[10,10],dg)
# grass
im_fill(frame9,[18,18],[0,0],fg)
im_fill(frame9,[18,18],[19,19],fg)
im_fill(frame9,[19,19],[0,19],fg)
#little girl Alien
im_fill(frame9,[10,13],[6,10],p)
im_fill(frame9,[9,9],[7,7],p)
im_fill(frame9,[9,9],[9,9],p)
im_fill(frame9,[8,8],[6,6],p)
im_fill(frame9,[8,8],[10,10],p)
im_fill(frame9,[14,14],[7,7],p)
im_fill(frame9,[14,14],[9,9],p)
im_fill(frame9,[11,11],[7,7],b)
im_fill(frame9,[11,11],[9,9],b)
im_fill(frame9,[12,12],[8,8],b)

#little boy alien
im_fill(frame9,[14,17],[13,17],fg)
im_fill(frame9,[12,12],[13,13],fg)
im_fill(frame9,[12,12],[17,17],fg)
im_fill(frame9,[13,13],[14,14],fg)
im_fill(frame9,[13,13],[16,16],fg)
im_fill(frame9,[18,18],[16,16],fg)
im_fill(frame9,[15,15],[14,14],b)
im_fill(frame9,[16,16],[15,15],b)
im_fill(frame9,[15,15],[16,16],b)
im_fill(frame9,[18,18],[14,14],fg)


frame10 = np.array([[b]*cols for row in range (rows)])
#THE END!
im_fill(frame10,[7,7],[2,2],bro)
im_fill(frame10,[7,8],[3,4],dg)
im_fill(frame10,[8,8],[4,4],r)

im_fill(frame10,[9,13],[2,6],bro)
im_fill(frame10,[14,15],[3,5],bro)
im_fill(frame10,[16,17],[2,3],bro)
im_fill(frame10,[16,16],[4,4],bro)
im_fill(frame10,[16,17],[5,6],bro)
im_fill(frame10,[13,13],[1,1],bro)
im_fill(frame10,[13,13],[7,7],bro)

im_fill(frame10,[10,12],[3,5],tan)
im_fill(frame10,[14,14],[1,1],tan)
im_fill(frame10,[12,12],[7,7],tan)
im_fill(frame10,[18,18],[1,3],tan)
im_fill(frame10,[18,18],[5,7],tan)

im_fill(frame10,[11,11],[3,3],b)
im_fill(frame10,[12,12],[4,4],b)
im_fill(frame10,[11,11],[5,5],b)
im_fill(frame10,[9,10],[5,6],r)
#alien falling down and criying!
im_fill(frame10,[0,0],[0,2],w)
im_fill(frame10,[1,1],[0,0],w)
im_fill(frame10,[2,2],[0,1],w)
im_fill(frame10,[3,3],[0,0],w)
im_fill(frame10,[4,4],[0,2],w)
im_fill(frame10,[2,2],[4,6],w)
im_fill(frame10,[3,4],[4,4],w)
im_fill(frame10,[3,4],[6,6],w)
im_fill(frame10,[0,4],[10,10],w)
im_fill(frame10,[2,4],[8,9],w)
im_fill(frame10,[3,3],[9,9],b)


im_fill(frame10,[3,6],[13,17],fg)
im_fill(frame10,[1,1],[13,13],fg)
im_fill(frame10,[2,2],[14,14],fg)
im_fill(frame10,[1,1],[17,17],fg)
im_fill(frame10,[2,2],[16,16],fg)
im_fill(frame10,[4,6],[13,13],fg)
im_fill(frame10,[6,6],[14,17],fg)
im_fill(frame10,[3,6],[17,17],fg)
im_fill(frame10,[7,7],[14,14],fg)
im_fill(frame10,[7,7],[16,16],fg)
im_fill(frame10,[4,4],[14,14],b)
im_fill(frame10,[4,4],[16,16],b)
im_fill(frame10,[5,5],[15,15],b)

im_fill(frame10,[11,14],[13,17],p)
im_fill(frame10,[9,9],[13,13],p)
im_fill(frame10,[10,10],[14,14],p)
im_fill(frame10,[9,9],[17,17],p)
im_fill(frame10,[10,10],[16,16],p)
im_fill(frame10,[5,5],[15,15],b)
im_fill(frame10,[12,12],[14,14],b)
im_fill(frame10,[12,12],[16,16],b)
im_fill(frame10,[13,13],[15,15],b)
im_fill(frame10,[15,15],[14,14],p)
im_fill(frame10,[15,15],[16,16],p)
# Video play            
frame_list = [frame0,frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10] # list of frames

fps= 1

#frame_list = [frame0] 


# frames per sec
play_video= vid_show(frame_list, fps) # play on screen
