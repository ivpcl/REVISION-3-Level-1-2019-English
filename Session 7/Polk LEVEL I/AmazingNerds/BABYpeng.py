from AOLME import *
#newframe
rows= 20
cols= 20

M = "D2B48C"
J = "FF1493"
D = "F4A460"
sky = "87CEEB"
G = "008000"
sun = "FFD700"
w = "FFFFFF"
b = "000000"
red = "FF0000"
nb = "000080"
ma = "FF00FF"
gr = "C0C0C0"
frame_0 = [[sky]*cols for row in range(rows)]
frame_1 = [[sky]*cols for row in range(rows)]
frame_2 = [[sky]*cols for row in range(rows)]
frame_3 = [[sky]*cols for row in range(rows)]
frame_4 = [[sky]*cols for row in range(rows)]
frame_5 = [[sky]*cols for row in range(rows)]
frame_6 = [[sky]*cols for row in range(rows)]

#sky
frame_0 = [[sky]*cols for row in range(rows)]
frame_1 = [[sky]*cols for row in range(rows)]
frame_2 = [[sky]*cols for row in range(rows)]
frame_3 = [[sky]*cols for row in range(rows)]
frame_4 = [[sky]*cols for row in range(rows)]
frame_5 = [[sky]*cols for row in range(rows)]
frame_6 = [[sky]*cols for row in range(rows)]
#sun
im_fill(frame_0, [0,2],[17,19], sun)
im_fill(frame_1, [0,2],[17,19], sun)
im_fill(frame_2, [0,2],[17,19], sun)
im_fill(frame_3, [0,2],[17,19], sun)
im_fill(frame_4, [0,2],[17,19], sun)
im_fill(frame_5, [0,2],[17,19], sun)
im_fill(frame_6, [0,2],[17,19], sun)
#im_fill(frame_7, [0,2],[17,19], sun)
#im_fill(frame_8, [0,2],[17,19], sun)
#im_fill(frame_9, [0,2],[17,19], sun)

#grass
im_fill(frame_0, [19,19],[0,19], G)
im_fill(frame_1, [19,19],[0,19], G)
im_fill(frame_2, [19,19],[0,19], G)
im_fill(frame_3, [19,19],[0,19], G)
im_fill(frame_4, [19,19],[0,19], G)
im_fill(frame_5, [19,19],[0,19], G)
im_fill(frame_6, [19,19],[0,19], G)


#cloud2
im_fill(frame_0, [5,5],[8,12], w)
im_fill(frame_0, [4,4],[9,11], w)
im_fill(frame_1, [5,5],[8,12], w)
im_fill(frame_1, [4,4],[9,11], w)
im_fill(frame_2, [5,5],[8,12], w)
im_fill(frame_2, [4,4],[9,11], w)                                   
im_fill(frame_3, [5,5],[8,12], w)
im_fill(frame_3, [4,4],[9,11], w)
im_fill(frame_4, [5,5],[8,12], w)
im_fill(frame_4, [4,4],[9,11], w)
im_fill(frame_5, [5,5],[8,12], w)
im_fill(frame_5, [4,4],[9,11], w)
im_fill(frame_6, [5,5],[8,12], w)
im_fill(frame_6, [4,4],[9,11], w)
#cloud3
im_fill(frame_0, [2,2],[11,13], w)
frame_0[1][12] = w
im_fill(frame_1, [2,2],[11,13], w)
frame_1[1][12] = w
im_fill(frame_2, [2,2],[11,13], w)
frame_2[1][12] = w
im_fill(frame_3, [2,2],[11,13], w)
frame_3[1][12] = w
im_fill(frame_4, [2,2],[11,13], w)
frame_4[1][12] = w
im_fill(frame_5, [2,2],[11,13], w)
frame_5[1][12] = w
im_fill(frame_6, [2,2],[11,13], w)
frame_6[1][12] = w


# frame 0-------------------------
#egg
im_fill(frame_0,[17,19],[3,5], M)
frame_0[18][4] = J


#frame 1---------------------------
#egg
im_fill(frame_1,[17,19],[7,9], M)
frame_1[18][8] = J

#frame 2-----------------------------
#egg
im_fill(frame_2,[17,19],[7,9], M)
frame_2 [18][8] = J

#baby
im_fill(frame_2,[17,18],[10,13], D)
im_fill(frame_2,[15,17],[13,15], D)
im_fill(frame_2,[19,19],[14,15], D)
frame_2 [16][15] = b


#frame 3-----------------------------
#body
im_fill(frame_3,[14,17],[8,10], D)

#left arm
frame_3 [14][7] = D
frame_3 [15][6] = D
frame_3 [16][6] = D

#right arm
frame_3 [14][11] = D
frame_3 [15][12] = D
frame_3 [16][12] = D

#left leg
frame_3 [18][8] = D
frame_3 [19][8] = D
frame_3 [18][10] = D
frame_3 [19][10] = D

#neck
frame_3 [13][9] = D

#head
im_fill(frame_3,[10,12],[8,10], D)

#eyes
frame_3 [11][8] = b 
frame_3 [11][10] = b 
#pants
im_fill(frame_3,[17,17],[8,10], nb)
frame_3 [18][8] = nb
frame_3 [18][10] = nb
#hat
im_fill(frame_3,[9,9],[8,10], nb)
frame_3 [9][9] = ma
frame_3 [8][9] = gr

#age
im_fill(frame_3,[8,11],[2,4], b)
im_fill(frame_3,[9,10],[3,3], sky)
im_fill(frame_3,[8,8],[14,16], b)
im_fill(frame_3,[8,11],[16,16], b)

#frame 4---------------------
im_fill(frame_4,[14,17],[8,10],D)

#arms
im_fill(frame_4,[15,16],[6,6],D)
im_fill(frame_4,[14,14],[7,7],D)
im_fill(frame_4,[15,16],[12,12],D)
im_fill(frame_4,[14,14],[11,11],D)
#legs
im_fill(frame_4,[18,19],[8,8],D)
im_fill(frame_4,[18,19],[10,10],D)
#neck
im_fill(frame_4,[13,13],[9,9],D)

#head
im_fill(frame_4,[10,12],[8,10],D)
#eyes
im_fill(frame_4,[11,11],[8,8],b)
im_fill(frame_4,[11,11],[10,10],b)
#age10
im_fill(frame_4,[8,12],[4,4],b)
im_fill(frame_4,[8,12],[14,16],b)
im_fill(frame_4,[9,11],[15,15],sky)
 #hat
im_fill(frame_4,[9,9],[8,10],nb)                            
im_fill(frame_4,[9,9],[9,9],J)
im_fill(frame_4,[8,8],[8,10],gr)
im_fill(frame_4,[8,8],[9,9],sky)
#pants
im_fill(frame_4,[17,19],[8,10],nb)
im_fill(frame_4,[18,19],[9,9],sky)
#grass
im_fill(frame_4,[19,19],[9,9],G)


#frame 5--------------------------------------

im_fill(frame_5,[14,17],[8,10], b)

#leg
frame_5 [18][8] = b
frame_5 [19][8] = b
frame_5 [18][10] = b
frame_5 [19][10] = b
#neck
frame_5 [13][9] = D
#head
im_fill(frame_5,[10,12],[8,10], D)
#left arm
frame_5 [14][7] = D
frame_5 [15][6] = D
frame_5 [16][6] = D

#right arm
frame_5 [14][11] = D
frame_5[15][12] = D
frame_5 [16][12] = D
#eyes
frame_5 [11][8] = b 
frame_5 [11][10] = b 

#mohawk
im_fill(frame_5,[8,9],[9,9], b)

#age
im_fill(frame_5,[9,9],[2,3], b)
im_fill(frame_5,[10,11],[3,3], b)
im_fill(frame_5,[12,12],[2,4], b)

im_fill(frame_5,[9,10],[14,16], b)
frame_5 [9][15] = sky
im_fill(frame_5,[11,12],[16,16], b)
#frame_6
im_fill(frame_6,[14,17],[8,10],D)

#arms
im_fill(frame_6,[15,16],[6,6],D)
im_fill(frame_6,[14,14],[7,7],D)
im_fill(frame_6,[15,16],[12,12],D)
im_fill(frame_6,[14,14],[11,11],D)
#legs
im_fill(frame_6,[18,19],[8,8],D)
im_fill(frame_6,[18,19],[10,10],D)
#neck
im_fill(frame_6,[13,13],[9,9],D)

#head
im_fill(frame_6,[10,12],[8,10],D)
#eyes
im_fill(frame_6,[11,11],[8,8],b)
im_fill(frame_6,[11,11],[10,10],b)
#pants
im_fill(frame_6,[17,19],[8,10],b)
im_fill(frame_6,[18,19],[9,9],sky)
#jersey
im_fill(frame_6,[14,17],[8,10],red)
im_fill(frame_6,[13,13],[9,9],b)
#age16
im_fill(frame_6,[6,12],[4,4],b)
im_fill(frame_6,[8,12],[14,16],b)
im_fill(frame_6,[8,9],[15,16],sky)
im_fill(frame_6,[11,11],[15,15],sky)
#grass
im_fill(frame_6, [19,19],[9,9], G)


#im_show(frame_4)

frame_list = [frame_0,frame_1,frame_2,frame_3,frame_4,frame_5,frame_6]

fps = 1

play_video = vid_show(frame_list,fps)

