from AOLME import *

total_columns = 20
total_rows = 20

frame_0 = [["FF"]*total_columns for row in range(total_rows)]
frame_1 = [["FF"]*total_columns for row in range(total_rows)]
frame_2 = [["FF"]*total_columns for row in range(total_rows)]
frame_3 = [["FF"]*total_columns for row in range(total_rows)]
frame_4 = [["FF"]*total_columns for row in range(total_rows)]
frame_5 = [["FF"]*total_columns for row in range(total_rows)]
frame_6 = [["FF"]*total_columns for row in range(total_rows)]
frame_7 = [["FF"]*total_columns for row in range(total_rows)]
frame_8 = [["FF"]*total_columns for row in range(total_rows)]

#frame 0
#background
im_fill(frame_0,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_0,[15,19],[0,19],"2d1515") #land
im_fill(frame_0,[2,4],[13,17],"fffb19") # sun yellow
im_fill(frame_0,[1,5],[14,16],"fffb19") # sun yellow

#person
im_fill(frame_0,[5,6],[8,11],"d81313")
im_fill(frame_0,[7,7],[4,15],"d81313")
im_fill(frame_0,[8,14],[9,10],"d81313")

#frame 1
im_fill(frame_1,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_1,[15,19],[0,19],"2d1515") #land
im_fill(frame_1,[2,4],[13,17],"fffb19") # sun yellow
im_fill(frame_1,[1,5],[14,16],"fffb19") # sun yellow

im_fill(frame_1,[5,7],[8,12],"6c2384")
im_fill(frame_1,[8,10],[8,11],"6c2384")
im_fill(frame_1,[11,14],[9,10],"6c2384")

#frame 2
#background
im_fill(frame_2,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_2,[15,19],[0,19],"2d1515") #land
im_fill(frame_2,[2,4],[13,17],"fffb19") # sun yellow
im_fill(frame_2,[1,5],[14,16],"fffb19") # sun yellow

im_fill(frame_2,[9,9],[4,12],"171f7a")
im_fill(frame_2,[5,9],[12,12],"171f7a")
im_fill(frame_2,[10,15],[9,10],"171f7a")
im_fill(frame_2,[6,8],[7,11],"171f7a")

#frame 3
#background
im_fill(frame_3,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_3,[15,19],[0,19],"2d1515") #land
im_fill(frame_3,[2,4],[13,17],"fffb19") # sun yellow
im_fill(frame_3,[1,5],[14,16],"fffb19") # sun yellow


im_fill(frame_3,[2,2],[4,6],"931616")
im_fill(frame_3,[3,4],[5,5],"931616")
im_fill(frame_3,[1,1],[4,6],"931616")
frame_3[1][5] = "42cef4"

im_fill(frame_3,[1,4],[8,10],"15568e")
im_fill(frame_3,[2,4],[9,9],"15568e")
frame_3[2][9] = "42cef4"
frame_3[4][9] = "42cef4"

im_fill(frame_3,[1,2],[12,14],"3a2782")
im_fill(frame_3,[2,4],[13,13],"3a2782")
frame_3[1][13] = "42cef4"

#head
im_fill(frame_3,[6,8],[7,11],"f62217")

#left arm
im_fill(frame_3,[7,9],[6,6],"f62217")
im_fill(frame_3,[9,9],[6,8],"f62217")


#right arm
im_fill(frame_3,[7,9],[12,12],"f62217")
im_fill(frame_3,[9,9],[9,12],"f62217")


#legs
im_fill(frame_3,[10,15],[8,9],"f62217")

#frame 4
#background
im_fill(frame_4,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_4,[15,19],[0,19],"2d1515") #land
#im_fill(frame_4,[2,4],[13,17],"fffb19") # sun yellow
#im_fill(frame_4,[1,5],[14,16],"fffb19") # sun yellow

#D
im_fill(frame_4,[0,0],[1,3],"4256f4")
im_fill(frame_4,[4,4],[1,3],"4256f4")
im_fill(frame_4,[1,3],[4,4],"4256f4")
im_fill(frame_4,[0,4],[1,1],"4256f4")
#im_fill(frame_4,

#A
im_fill(frame_4,[0,0],[6,8],"ff6600")
im_fill(frame_4,[2,2],[6,8],"ff6600")
im_fill(frame_4,[0,4],[6,6],"ff6600")
im_fill(frame_4,[0,4],[8,8],"ff6600")

#B
im_fill(frame_4,[0,4],[10,13],"4256f4")
frame_4[0][13] = "42cef4"
frame_4[1][11] = "42cef4"
frame_4[3][11] = "42cef4"
frame_4[1][12] = "42cef4"
frame_4[3][12] = "42cef4"
frame_4[4][13] = "42cef4"

#!
im_fill(frame_4,[0,3],[16,17],"ff6600")
im_fill(frame_4,[5,5],[16,17],"ff6600")

#head
im_fill(frame_4,[4,8],[6,10],"ffc291")
frame_4[5][7] = "931616" #eye
frame_4[5][9] = "931616" #eye
im_fill(frame_4,[7,7],[7,9],"931616") #mouth



#right arm
frame_4[9][9] = "15568e"
frame_4[8][10] = "15568e"
frame_4[7][11] = "15568e"
frame_4[6][12] = "15568e"

#left arm
im_fill(frame_4,[9,9],[9,12],"15568e") 
frame_4[8][12] = "15568e"

#body
im_fill(frame_4,[9,14],[7,8],"15568e") 


#frame 5
#background
im_fill(frame_5,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_5,[15,19],[0,19],"2d1515") #land
#im_fill(frame_5,[2,4],[13,17],"fffb19") # sun yellow
#im_fill(frame_5,[1,5],[14,16],"fffb19") # sun yellow

#D
im_fill(frame_5,[0,0],[1,3],"4256f4")
im_fill(frame_5,[4,4],[1,3],"4256f4")
im_fill(frame_5,[1,3],[4,4],"4256f4")
im_fill(frame_5,[0,4],[1,1],"4256f4")
#im_fill(frame_4,

#A
im_fill(frame_5,[0,0],[6,8],"ff6600")
im_fill(frame_5,[2,2],[6,8],"ff6600")
im_fill(frame_5,[0,4],[6,6],"ff6600")
im_fill(frame_5,[0,4],[8,8],"ff6600")

#B
im_fill(frame_5,[0,4],[10,13],"4256f4")
frame_5[0][13] = "42cef4"
frame_5[1][11] = "42cef4"
frame_5[3][11] = "42cef4"
frame_5[1][12] = "42cef4"
frame_5[3][12] = "42cef4"
frame_5[4][13] = "42cef4"

#!
im_fill(frame_5,[0,3],[16,17],"ff6600")
im_fill(frame_5,[5,5],[16,17],"ff6600")

#head rolling 1
im_fill(frame_5,[6,10],[2,6],"ffc291")
frame_5[7][3] = "931616" #eye
frame_5[9][3] = "931616" #eye
im_fill(frame_5,[7,9],[5,5],"931616") #mouth



#right arm
frame_5[9][9] = "15568e"
frame_5[8][10] = "15568e"
frame_5[7][11] = "15568e"
frame_5[6][12] = "15568e"

#left arm
im_fill(frame_5,[9,9],[9,12],"15568e") 
frame_5[8][12] = "15568e"

#body
im_fill(frame_5,[9,14],[7,8],"15568e") 


#frame 6
#background
im_fill(frame_6,[0,14],[0,19],"42cef4") #skyblue
im_fill(frame_6,[15,19],[0,19],"2d1515") #land
#im_fill(frame_6,[2,4],[13,17],"fffb19") # sun yellow
#im_fill(frame_6,[1,5],[14,16],"fffb19") # sun yellow

#D
im_fill(frame_6,[0,0],[1,3],"4256f4")
im_fill(frame_6,[4,4],[1,3],"4256f4")
im_fill(frame_6,[1,3],[4,4],"4256f4")
im_fill(frame_6,[0,4],[1,1],"4256f4")
#im_fill(frame_4,

#A
im_fill(frame_6,[0,0],[6,8],"ff6600")
im_fill(frame_6,[2,2],[6,8],"ff6600")
im_fill(frame_6,[0,4],[6,6],"ff6600")
im_fill(frame_6,[0,4],[8,8],"ff6600")

#B
im_fill(frame_6,[0,4],[10,13],"4256f4")
frame_6[0][13] = "42cef4"
frame_6[1][11] = "42cef4"
frame_6[3][11] = "42cef4"
frame_6[1][12] = "42cef4"
frame_6[3][12] = "42cef4"
frame_6[4][13] = "42cef4"

#!
im_fill(frame_6,[0,3],[16,17],"ff6600")
im_fill(frame_6,[5,5],[16,17],"ff6600")

#head rolling 2
im_fill(frame_6,[10,14],[0,4],"ffc291")
frame_6[13][3] = "931616" #eye
frame_6[13][1] = "931616" #eye
im_fill(frame_6,[11,11],[1,3],"931616") #mouth



#right arm
frame_6[9][9] = "15568e"
frame_6[8][10] = "15568e"
frame_6[7][11] = "15568e"
frame_6[6][12] = "15568e"

#left arm
im_fill(frame_6,[9,9],[9,12],"15568e") 
frame_6[8][12] = "15568e"

#body
im_fill(frame_6,[9,14],[7,8],"15568e") 


#Frane 7
#background
im_fill(frame_7,[0,19],[0,19],"1F45FC")  


#B
im_fill(frame_7,[2,7],[2,5],"6CC417") 
im_fill(frame_7,[3,3],[3,4],"1F45FC") 
im_fill(frame_7,[5,6],[3,4],"1F45FC") 

#A
im_fill(frame_7,[2,7],[6,9],"6CC417") #green
im_fill(frame_7,[3,7],[8,8],"1F45FC")  
frame_7[5][8] = "6CC417"


#M
im_fill(frame_7,[2,7],[12,16],"6CC417") 
im_fill(frame_7,[3,7],[13,13],"1F45FC")  
im_fill(frame_7,[3,7],[15,15],"1F45FC")  

frame_7[2][11] = "6CC417"
frame_7[7][11] = "6CC417"
frame_7[2][17] = "6CC417"
frame_7[7][17] = "6CC417"

im_fill(frame_7,[2,7],[6,6],"1F45FC") 

#!
im_fill(frame_7,[2,5],[19,19],"6CC417") 
frame_7[7][19] = "6CC417"


#Frame 8
#background
im_fill(frame_8,[0,19],[0,19],"6CC417")  

#G
im_fill(frame_8,[1,5],[3,7],"1F45FC") 
im_fill(frame_8,[2,2],[4,7],"6CC417")  
im_fill(frame_8,[2,4],[4,4],"6CC417")  
im_fill(frame_8,[4,4],[4,6],"6CC417") 

#O
im_fill(frame_8,[1,5],[10,14],"1F45FC") 
im_fill(frame_8,[2,4],[11,13],"6CC417")

#H
im_fill(frame_8,[7,11],[0,2],"1F45FC") 
im_fill(frame_8,[7,8],[1,1],"6CC417")
im_fill(frame_8,[10,11],[1,1],"6CC417")

#O
im_fill(frame_8,[7,11],[4,7],"1F45FC") 
im_fill(frame_8,[8,10],[5,6],"6CC417")

#M
im_fill(frame_8,[7,11],[10,14],"1F45FC") 
im_fill(frame_8,[8,11],[11,11],"6CC417")  
im_fill(frame_8,[8,11],[13,13],"6CC417")  

frame_8[7][9] = "1F45FC"
frame_8[11][9] = "1F45FC"
frame_8[7][15] = "1F45FC"
frame_8[11][15] = "1F45FC"



#E
im_fill(frame_8,[7,11],[17,19],"1F45FC") 
im_fill(frame_8,[8,8],[18,19],"6CC417")  
im_fill(frame_8,[10,10],[18,19],"6CC417") 


#im_show(frame_7)





frame_list = [frame_0,frame_1,frame_2,frame_3,frame_4,frame_5,frame_6, frame_7, frame_8]
fps = 1

play_video = vid_show(frame_list,fps)
