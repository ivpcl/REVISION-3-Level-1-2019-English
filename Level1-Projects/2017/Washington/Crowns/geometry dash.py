from AOLME import  *
rows=20
cols=20

y="ff9200"
b="0000ff"
w="ffffff"

# The adventuresof bob the square

# the frame where bob the square is at the top of the stairs
# up
start_row = 0
start_col = 0

frame_1 = [[w]*cols for row in range(rows)]
end_row = start_row+4
end_col = start_col+4
im_fill(frame_1,[start_row,end_row],[start_col,end_col],b)
frame_1[start_row+1][start_col+1] = w
frame_1[start_row+1][start_col+3] = w
frame_1[start_row+3][start_col+1] = w
frame_1[start_row+3][start_col+2] = w
frame_1[start_row+3][start_col+3] = w
#im_show (frame_1)

# the frame where bob is facing right
# right
start_row = 0
start_col = 0

frame_2 = [[w]*cols for row in range(rows)]
end_row = start_row+4
end_col = start_col+4
im_fill(frame_2,[start_row,end_row],[start_col,end_col],b)
frame_2[start_row+1][start_col+1] = w
frame_2[start_row+1][start_col+3] = w
frame_2[start_row+2][start_col+1] = w
frame_2[start_row+3][start_col+1] = w
frame_2[start_row+3][start_col+3] = w
#im_show (frame_2)

# the second frame where he is facing down 
# down
start_row = 0
start_col = 0
frame_3 = [[w]*cols for row in range(rows)]
end_row = start_row+4
end_col = start_col+4
im_fill(frame_3,[start_row,end_row],[start_col,end_col],b)
frame_3[start_row+1][start_col+1] = w
frame_3[start_row+1][start_col+2] = w
frame_3[start_row+1][start_col+3] = w
frame_3[start_row+3][start_col+1] = w
frame_3[start_row+3][start_col+3] = w
#im_show (frame_3)

# the frame where bob is facing left 
# left
start_row = 0
start_col = 0
frame_4 = [[w]*cols for row in range(rows)]
end_row = start_row+4
end_col = start_col+4
im_fill(frame_4,[start_row,end_row],[start_col,end_col],b)
frame_4[start_row+1][start_col+1] = w
frame_4[start_row+1][start_col+3] = w
frame_4[start_row+2][start_col+3] = w
frame_4[start_row+3][start_col+3] = w
frame_4[start_row+3][start_col+1] = w
#im_show (frame_4)

# its not rocket science its the stairs ?
# stairs
stairs = [[w]*cols for row in range(rows)]
start_row = 5
start_col = 0
end_row = 19
end_col = 4
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
start_row = 5
start_col = 0
end_row = 19
end_col = 4
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
start_row = 5
start_col = 0
end_row = 19
end_col = 4
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
start_row = 10
start_col = 5
end_row = 19
end_col = 9
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
start_row = 15
start_col = 10
end_row = 19
end_col = 14
im_fill(stairs,[start_row,end_row],[start_col,end_col],b)
 
# the frame that loads the stairs in the graph 
#im_show (stairs) 

f1up = np.array(list(stairs))

start_row = 0
start_col = 0
end_row = start_row+4
end_col = start_col+4
im_fill(f1up,[start_row,end_row],[start_col,end_col],y)
f1up[start_row+1][start_col+1] = b
f1up[start_row+1][start_col+3] = b
f1up[start_row+3][start_col+1] = b
f1up[start_row+3][start_col+2] = b
f1up[start_row+3][start_col+3] = b
#im_show (f1up) 


f2right = np.array(list(stairs))

# the second frame where bob is geting sucked into the portal
# right
start_row = 5
start_col = 5
end_row = start_row+4
end_col = start_col+4

im_fill(f2right,[start_row,end_row],[start_col,end_col],y)
f2right[start_row+1][start_col+1] = b
f2right[start_row+1][start_col+3] = b
f2right[start_row+2][start_col+1] = b
f2right[start_row+3][start_col+1] = b
f2right[start_row+3][start_col+3] = b


f3down = np.array(list(stairs))

# down
start_row = 10
start_col = 10

end_row = start_row+4
end_col = start_col+4
im_fill(f3down,[start_row,end_row],[start_col,end_col],y)
f3down[start_row+1][start_col+1] = b
f3down[start_row+1][start_col+2] = b
f3down[start_row+1][start_col+3] = b
f3down[start_row+3][start_col+1] = b
f3down[start_row+3][start_col+3] = b


f4left = np.array(list(stairs))

# left
start_row = 15
start_col = 15

end_row = start_row+4
end_col = start_col+4
im_fill(f4left,[start_row,end_row],[start_col,end_col],y)
f4left[start_row+1][start_col+1] = b
f4left[start_row+1][start_col+3] = b
f4left[start_row+2][start_col+3] = b
f4left[start_row+3][start_col+3] = b
f4left[start_row+3][start_col+1] = b



# portal
p = "f442eb"
portal = [[w]*cols for row in range(rows)]
start_row = 3
start_col = 18
end_row = 10
end_col = 19
im_fill(portal,[start_row,end_row],[start_col,end_col],p)
portal[2][19] = p
portal[11][19] = p



jump1 = jump3 = np.array(list(portal))

# left
start_row = 15
start_col = 0

end_row = start_row+4
end_col = start_col+4
im_fill(jump1,[start_row,end_row],[start_col,end_col],y)
jump1[start_row+1][start_col+1] = b
jump1[start_row+1][start_col+3] = b
jump1[start_row+2][start_col+3] = b
jump1[start_row+3][start_col+3] = b
jump1[start_row+3][start_col+1] = b



# up
start_row = 10
start_col = 5

jup2 = np.array(list(portal))
end_row = start_row+4
end_col = start_col+4
im_fill(jup2,[start_row,end_row],[start_col,end_col],y)
jup2[start_row+1][start_col+1] = b
jup2[start_row+1][start_col+3] = b
jup2[start_row+3][start_col+1] = b
jup2[start_row+3][start_col+2] = b
jup2[start_row+3][start_col+3] = b

jump3 = [[w]*cols for row in range(rows)]




# right
start_row = 5
start_col = 10

jump3 = np.array(list(portal))
end_row = start_row+4
end_col = start_col+4
im_fill(jump3,[start_row,end_row],[start_col,end_col],y)
jump3[start_row+1][start_col+1] = b
jump3[start_row+1][start_col+3] = b
jump3[start_row+2][start_col+1] = b
jump3[start_row+3][start_col+1] = b
jump3[start_row+3][start_col+3] = b


# down
start_row = 5
start_col = 15
jup4 = [[w]*cols for row in range(rows)]
end_row = start_row+4
end_col = start_col+4
im_fill(jup4,[start_row,end_row],[start_col,end_col],y)
jup4[start_row+1][start_col+1] = b
jup4[start_row+1][start_col+2] = b
jup4[start_row+1][start_col+3] = b
jup4[start_row+3][start_col+1] = b
jup4[start_row+3][start_col+3] = b

# Portal
start_row = 3
start_col = 18
end_row = 10
end_col = 19
im_fill(jup4,[start_row,end_row],[start_col,end_col],p)
jup4[2][19] = p
jup4[11][19] = p



frame_list = [f1up,f2right,f3down,f4left,jump1,jup2,jump3,jup4]
fps = 5000
play_video = vid_show(frame_list,fps)

save_vid(play_video,fps,'out.gif')
