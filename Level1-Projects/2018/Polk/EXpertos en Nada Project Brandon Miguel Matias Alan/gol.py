#from pygame import mixer

#mixer.init()
#mixer.music.load('./gol.mp3')
#mixer.music.play()


from AOLME import *
import numpy

cols = 20
rows = 20
bl = "000000"
grey = "888888"  
w = "ffffff"
g = "1e8904"
r = "aa0a0a"
b = "090f82"
y = "f4c909"
frame_1 = [[bl]*cols for row in range(rows)]
im_fill(frame_1,[6,8], [7,7],  w)
im_fill(frame_1,[8,8], [4,7], w)
im_fill(frame_1,[3,6], [4,4],  w)
im_fill(frame_1,[6,6], [4,7], w)
im_fill(frame_1,[3,3], [4,7],  w)

frame_1[4][9] = w
frame_1[7][9] = w

im_fill(frame_1,[6,8], [14,14],  w)
im_fill(frame_1,[8,8], [11,14], w)
im_fill(frame_1,[3,6], [11,11],  w)
im_fill(frame_1,[6,6], [11,14], w)
im_fill(frame_1,[3,3], [11,14],  w)

frame_1[11][2] = w
frame_1[12][3] = w
frame_1[13][4] = w
frame_1[14][5] = w
frame_1[15][6] = w
frame_1[15][2] = w
frame_1[14][3] = w
frame_1[13][4] = w
frame_1[12][5] = w
frame_1[11][6] = w
im_fill(frame_1,[11,15], [11,11],  w)
im_fill(frame_1,[15,15], [11,13],  w)
im_fill(frame_1,[11,11], [11,13],  w)
frame_1[12][13] = w
frame_1[13][12] = w
frame_1[14][13] = w

#im_show(frame_1)

frame_2 = [[g]*cols for row in range(rows)]

#goal
im_fill(frame_2,[0,5], [2,2],  w)
im_fill(frame_2,[0,0], [2,17],  w)
im_fill(frame_2,[0,5], [17,17],  w)

#soccer ball
im_fill(frame_2,[15,16], [12,13],  y)

#goalie
im_fill(frame_2,[3,4], [9,10],   bl)
im_fill(frame_2,[5,7], [9,9],  r)
im_fill(frame_2,[5,7], [10,10],  b)
im_fill(frame_2,[5,5], [6,8],  bl)
im_fill(frame_2,[5,5], [11,13],  bl)
frame_2[8][8] = bl
frame_2[8][11] = bl

#player
im_fill(frame_2,[13,14], [15,16],  bl)
im_fill(frame_2,[15,16], [15,16],  w)
frame_2[17][14] = bl
frame_2[17][16] = bl
frame_2[14][17] = bl
frame_2[13][18] = bl

#im_show(frame_2)

#Frame 3
frame_3 = [[g]*cols for row in range(rows)]

#pole
im_fill(frame_3,[0,5], [2,2],  w)
im_fill(frame_3,[0,0], [2,17],  w)
im_fill(frame_3,[0,5], [17,17],  w)

#goalie
im_fill(frame_3,[3,4], [14,15],   bl)
im_fill(frame_3,[2,2], [13,15],  bl)
im_fill(frame_3,[5,5], [13,15],  bl)
im_fill(frame_3,[3,3], [11,13],  r)
im_fill(frame_3,[4,4], [11,13],  b)
frame_3[3][10] = bl
frame_3[4][10] = bl


#soccer ball
im_fill(frame_3,[1,2], [3,4],  y)

#player
im_fill(frame_3,[13,14], [14,15],  bl)
im_fill(frame_3,[15,16], [14,15],  w)
frame_3[13][12] = bl
frame_3[14][13] = bl
frame_3[14][16] = bl
frame_3[13][17] = bl
#leg
frame_3[17][13] = bl
frame_3[17][16] = bl
#im_show(frame_3)

frame_4 = [[bl]*cols for row in range(rows)]

#GOOOOL !
im_fill(frame_4,[1,1], [1,5],  w)
im_fill(frame_4,[1,7], [1,1],  w)
im_fill(frame_4,[7,7], [1,6],  w)
im_fill(frame_4,[4,4], [3,6],  w)
im_fill(frame_4,[4,7], [6,6],  w)
im_fill(frame_4,[2,7], [8,8],  w)
im_fill(frame_4,[2,2], [8,12], w)
im_fill(frame_4,[2,7], [12,12],  w)
im_fill(frame_4,[7,7], [8,12],  w)
im_fill(frame_4,[2,7], [15,15],  w)
im_fill(frame_4,[2,2], [15,19],  w)
im_fill(frame_4,[7,7], [15,19],  w)
im_fill(frame_4,[2,7], [19,19],  w)
im_fill(frame_4,[10,16], [1,1], w)
im_fill(frame_4,[16,16], [1,5], w)
im_fill(frame_4,[10,16], [5,5], w)
im_fill(frame_4,[10,10], [1,5], w)
im_fill(frame_4,[10,10], [8,12], w)
im_fill(frame_4,[10,16], [8,8], w)
im_fill(frame_4,[10,16], [12,12], w)
im_fill(frame_4,[16,16], [8,12], w)
im_fill(frame_4,[10,16], [14,14], w)
im_fill(frame_4,[16,16], [14,17], w)
frame_4[16][19] = w
im_fill(frame_4,[10,14], [19,19], w)

frame_5 = [[bl]*cols for row in range(rows)]

#score
im_fill(frame_5,[2,2], [3,6], w)
im_fill(frame_5,[2,7], [3,3], w)
im_fill(frame_5,[7,7], [3,6], w)
im_fill(frame_5,[4,7], [6,6], w)
im_fill(frame_5,[4,4], [3,6], w)
frame_5[5][8] = w
frame_5[7][8] = w
im_fill(frame_5,[2,2], [10,13], w)
im_fill(frame_5,[2,5], [10,10], w)
im_fill(frame_5,[5,5], [10,13], w)
im_fill(frame_5,[7,7], [10,13], w)
im_fill(frame_5,[5,7], [13,13], w)
im_fill(frame_5,[7,7], [10,13], w)


#fcb
im_fill(frame_5,[9,9], [9,11], b)
im_fill(frame_5,[9,12], [9,9], b)
im_fill(frame_5,[11,11], [10,10], b)

im_fill(frame_5,[9,11], [12,12], r)
im_fill(frame_5,[9,9], [12,13], r)
im_fill(frame_5,[11,11], [12,13], r)

im_fill(frame_5,[8,12], [15,15], b)
im_fill(frame_5,[8,8], [15,17], b)
im_fill(frame_5,[10,10], [15,17], b)
im_fill(frame_5,[12,12], [15,17], b)
frame_5[9][18] = b
frame_5[11][18] = b


#x
frame_5[14][0] = w
frame_5[15][1] = w
frame_5[18][1] = w
frame_5[19][0] = w 
frame_5[14][5] = w
frame_5[15][4] = w
frame_5[18][4] = w
frame_5[19][5] = w
im_fill(frame_5,[16,17], [2,3], w)
#win
frame_5[17][5] = b
frame_5[18][6] = b
frame_5[17][7] = b
frame_5[18][8] = b
frame_5[17][9] = b
frame_5[15][11]= r
im_fill(frame_5,[17,18], [11,11], r)
frame_5[18][12] = b
frame_5[17][13] = b
frame_5[18][14] = b
frame_5[17][15] = b








#Frame 6
frame_6 = [[g]*cols for row in range(rows)]

#pole
im_fill(frame_6,[0,5], [2,2],  w)
im_fill(frame_6,[0,0], [2,17],  w)
im_fill(frame_6,[0,5], [17,17],  w)

#goalie
im_fill(frame_6,[3,4], [11,12],   bl)
im_fill(frame_6,[2,2], [10,12],  bl)
im_fill(frame_6,[5,5], [10,12],  bl)
im_fill(frame_6,[3,3], [8,10],  r)
im_fill(frame_6,[4,4], [8,10],  b)
frame_6[3][7] = bl
frame_6[4][7] = bl


#soccer ball
im_fill(frame_6,[8,9], [9,10],  y)

#player
im_fill(frame_6,[13,14], [14,15],  bl)
im_fill(frame_6,[15,16], [14,15],  w)
frame_6[13][12] = bl
frame_6[14][13] = bl
frame_6[14][16] = bl
frame_6[13][17] = bl
#leg
frame_6[17][13] = bl
frame_6[17][16] = bl

frame_7=[[g]*cols for row in range(rows)]
im_fill(frame_7,[3,10], [1,1],  y)                                      
im_fill(frame_7,[3,10], [15,15],  y)
im_fill(frame_7,[5,12], [5,11],  bl)
im_fill(frame_7,[13,16], [7,9],  bl) 
im_fill(frame_7,[17,17], [6,10],  y)
im_fill(frame_7,[10,10], [2,4],  y)
im_fill(frame_7,[10,10], [12,14],  y)

im_fill(frame_7,[3,3], [2,4],  y)
im_fill(frame_7,[3,3], [12,14],  y)
frame_7[4][4] = y
frame_7[4][12] = y


frame_7[6][6] = r

frame_7[7][7] = r

frame_7[8][8] = r

frame_7[9][9] = r
frame_7[10][10] = r
#frame_7[10][16] = r
frame_7[9][7] = r

frame_7[7][9] = r

frame_7[6][10] = r

frame_7[10][6] = r
im_fill(frame_7,[19,19], [4,12],  y)                                      
im_fill(frame_7,[18,18], [5,11],  y)                                      
im_fill(frame_7,[11,16], [2,2],  w)                                      
im_fill(frame_7,[11,16], [3,3],  bl)                                      
im_fill(frame_7,[11,16], [14,14],  r)                                      
im_fill(frame_7,[11,16], [13,13],  b)                                      



fps=1

frame_list = [frame_1,frame_2,frame_6, frame_3,frame_4,frame_5, frame_7]

play_video= vid_show(frame_list, fps)

im_show(frame_1)

im_show(frame_2)
im_show(frame_6)


im_show(frame_1)

im_show(frame_2)
im_show(frame_6)


im_show(frame_3)
im_show(frame_4)

im_show(frame_5)

im_show(frame_3)
im_show(frame_4)

im_show(frame_5)



im_show(frame_7)























