from AOLME import *

# Define the size of the image
rows =  20 # num of rows
cols =  20 # num of cols

# Define all of the colors
r = "ff0000" # red code
green ="99ff33"#green code
darkgreen ='009900'#darkgreen code
gray  ="808080"#gray code
g = '336600'#darker green
bk = "1c1917" # black code
tq = "4AC2b0" # turqois code
bk = "1c1917" # black code
pk = "ff30f3" # pink code
bl = "f5f5f5" #azul code
lp = "7765b5g" #ligh purple code
db = "22678d" #dark blue code
wh = "d7f2ea" #white code
gy = "71757a" #gray code
oj = "e98204" #orange code 
bw = "8b4513" #brown code
# Create a frame with the same background color
frame0 = np.array([[bk]*cols for row in range (rows)])

# im_fill example

# Create frame 1 with the same background color
# DID NOT USE THIS CODEEE
frame1 = frame0.copy()

# Create frame 2 with the same background color
# Scene 2 MARCOS!!!!!!!!
frame2 = frame0.copy()
im_fill(frame2, [12, 17], [0, 1], pk) #bed
im_fill(frame2, [17 , 18] , [0, 10], pk) #bed
im_fill(frame2, [0, 4] ,[0,4 ], oj)#window background
im_fill(frame2, [2, 2] ,[0,4 ], wh)#frame
im_fill(frame2, [0, 4] ,[2, 2], wh)#frame
#im_fill(frame2, [0, 5] ,[2, 5], wh)#frame
im_fill(frame2, [15, 16] ,[2, 3], bw)#girlhead
im_fill(frame2, [16, 16] ,[4, 10], db)#girlbody







# Create frame 1 with the same background color
# Scene 3 CREEPY GUY
frame3 = frame2.copy()
im_fill(frame3, [9, 12] , [11, 14], tq)#momhead
frame3[10][11] = bk#eyyeholes
frame3[10][13] = bk#eyyeholes
#im_fill(frame3, [10, 11] ,[10frame2[10][12] = bk,#eyyeholes,11], bk)#urmomeyes
im_fill(frame3, [12, 18] ,[13,14 ], tq)#body

# WEB!!
start_row = 0
end_row   = 0
start_col = 11
end_col  = 11
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 0
end_row   = 0
start_col = 13
end_col  = 13
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 1
end_row   = 1
start_col = 16
end_col  = 16
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 3
end_row   = 3
start_col = 16
end_col  = 16
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 1
end_row   = 1
start_col = 18
end_col  = 18
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 3
end_row   = 3
start_col = 18
end_col  = 18
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 4
end_row   = 4
start_col = 19
end_col  = 19
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 5
end_row   = 5
start_col = 16
end_col  = 16
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 17
end_col  = 17
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 19
end_col  = 19
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 7
end_row   = 7
start_col = 18
end_col  = 18
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 8
end_row   = 8
start_col = 19
end_col  = 19
im_fill(frame3, [start_row, end_row], [start_col, end_col], gray)




# Create frame 1 with the same background color
# Scene 4 SPIDER AND WEB!
frame4 = frame3.copy()
# im_fill example
start_row = 0
end_row   = 3
start_col = 19
end_col  = 19
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 0
end_row   = 0
start_col =4 
end_col  = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 2
end_row   = 2
start_col = 5
end_col  = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)





# im_fill example
start_row = 4
end_row   = 4
start_col = 6
end_col  = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 1
end_row   = 1
start_col = 4
end_col  = 4
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 3
end_row   = 4
start_col = 5
end_col  = 5
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 5
end_row   = 5
start_col = 6
end_col  = 6
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 0
end_row   = 0
start_col = 14
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 2
end_row   = 2
start_col = 15
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 4
end_row   = 4
start_col = 15
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 5
end_row   = 5
start_col = 18
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 1
end_row   = 4
start_col = 10
end_col  = 14
im_fill(frame4, [start_row, end_row], [start_col, end_col], g)
# im_fill example
start_row = 2
end_row   = 3
start_col = 11
end_col  = 11
im_fill(frame4, [start_row, end_row], [start_col, end_col], r)






# im_fill example
start_row = 2
end_row   = 3
start_col = 13
end_col  = 13
im_fill(frame4, [start_row, end_row], [start_col, end_col], r)
# im_fill example
start_row = 0
end_row   = 0
start_col = 11
end_col  = 11
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 0
end_row   = 0
start_col = 13
end_col  = 13
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 1
end_row   = 1
start_col = 16
end_col  = 16
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 3
end_row   = 3
start_col = 16
end_col  = 16
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 1
end_row   = 1
start_col = 18
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 3
end_row   = 3
start_col = 18
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 4
end_row   = 4
start_col = 19
end_col  = 19
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 5
end_row   = 5
start_col = 16
end_col  = 16
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 17
end_col  = 17
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 19
end_col  = 19
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 7
end_row   = 7
start_col = 18
end_col  = 18
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 8
end_row   = 8
start_col = 19
end_col  = 19
im_fill(frame4, [start_row, end_row], [start_col, end_col], gray)





# Create frame 1 with the same background color
# Scene 5 MOVING SPIDER and WEB down 3 rows!
frame5 = frame3.copy()

### im_fill example
start_row = 3
end_row   = 6
start_col = 19
end_col  = 19
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 3
end_row   = 3
start_col =4 
end_col  = 9                                        
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 5
end_row   = 5 
start_col = 5
end_col  = 9
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)





# im_fill example
start_row = 7
end_row   = 7
start_col = 6
end_col  = 9
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 4
end_row   = 4
start_col = 4
end_col  = 4
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 6
end_row   = 7
start_col = 5
end_col  = 5
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 8
end_row   = 8
start_col = 6
end_col  = 6
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 3
end_row   = 3
start_col = 14
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 5
end_row   = 5
start_col = 15
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 7
end_row   = 7
start_col = 15
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 8
end_row   = 8
start_col = 18
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 4
end_row   = 7
start_col = 10
end_col  = 14
im_fill(frame5, [start_row, end_row], [start_col, end_col], g)
# im_fill example
start_row = 5
end_row   = 6
start_col = 11
end_col  = 11
im_fill(frame5, [start_row, end_row], [start_col, end_col], r)






# im_fill example
start_row = 5
end_row   = 6
start_col = 13
end_col  = 13
im_fill(frame5, [start_row, end_row], [start_col, end_col], r)
# im_fill example
start_row = 3
end_row   = 3
start_col = 11
end_col  = 11
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 3
end_row   = 3
start_col = 13
end_col  = 13
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 4
end_row   = 4
start_col = 16
end_col  = 16
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 16
end_col  = 16
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 4
end_row   = 4
start_col = 18
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 18
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 7
end_row   = 7
start_col = 19
end_col  = 19
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 8
end_row   = 8
start_col = 16
end_col  = 16
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 9
end_row   = 9
start_col = 17
end_col  = 17
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 9
end_row   = 9
start_col = 19
end_col  = 19
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 10
end_row   = 10
start_col = 18
end_col  = 18
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 11
end_row   = 11
start_col = 19
end_col  = 19
im_fill(frame5, [start_row, end_row], [start_col, end_col], gray)










# Create frame 1 with the same background color
# Scene 6 Moving Spider and row 3 more rows
frame6 = frame3.copy()
# im_fill example
start_row = 6
end_row   = 9
start_col = 19
end_col  = 19
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 6
end_row   = 6
start_col =4 
end_col  = 9
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)

# im_fill example
start_row = 8
end_row   = 8
start_col = 5
end_col  = 9
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)





# im_fill example
start_row = 10
end_row   = 10
start_col = 6
end_col  = 9
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 7
end_row   = 7
start_col = 4
end_col  = 4
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 9
end_row   = 10
start_col = 5
end_col  = 5
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 11
end_row   = 11
start_col = 6
end_col  = 6
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 6
end_row   = 6
start_col = 14
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 8
end_row   = 8
start_col = 15
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 10
end_row   = 10
start_col = 15
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 11
end_row   = 11
start_col = 18
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], darkgreen)
# im_fill example
start_row = 7
end_row   = 10
start_col = 10
end_col  = 14
im_fill(frame6, [start_row, end_row], [start_col, end_col], g)
# im_fill example
start_row = 8
end_row   = 9
start_col = 11
end_col  = 11
im_fill(frame6, [start_row, end_row], [start_col, end_col], r)






# im_fill example
start_row = 8
end_row   = 9
start_col = 13
end_col  = 13
im_fill(frame6, [start_row, end_row], [start_col, end_col], r)
# im_fill example
start_row = 6
end_row   = 6
start_col = 11
end_col  = 11
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 6
end_row   = 6
start_col = 13
end_col  = 13
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 7
end_row   = 7
start_col = 16
end_col  = 16
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 9
end_row   = 9
start_col = 16
end_col  = 16
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 7
end_row   = 7
start_col = 18
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 9
end_row   = 9
start_col = 18
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 10
end_row   = 10
start_col = 19
end_col  = 19
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 11
end_row   = 11
start_col = 16
end_col  = 16
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 12
end_row   = 12
start_col = 17
end_col  = 17
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 12
end_row   = 12
start_col = 19
end_col  = 19
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 13
end_row   = 13
start_col = 18
end_col  = 18
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)
# im_fill example
start_row = 14
end_row   = 14
start_col = 19
end_col  = 19
im_fill(frame6, [start_row, end_row], [start_col, end_col], gray)




# Create frame 1 with the same background color
# Scene 4
frame7 = frame6.copy()



# Video play
frame_list = [frame0, frame1,frame2,frame3,frame4,frame5,frame6]         # list of frames
fps= 1                                             # frames per sec
play_video= vid_show(frame_list, fps) # play on screen



#im_fill(frame0, [1,5] ,[0,0], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
#im_fill(frame0, [1,5] ,[0,3], wh)
