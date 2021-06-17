from AOLME import *


# Define the size of the image
rows =20  # num of rows
cols = 20  # num of cols

# Define all of the colors
br = "A52A2A" # red code
bl = "000000" # black code
w = "ffffff" #white code
p= "9370DB" #purple code
gr= "a8a8a8" #gray code
ch= "8b4513" #brown code
az= "0000ff" #blue code
pu="00ff00"#green code
frame0 = np.array([[gr]*cols for row in range (rows)])

# Specify the frame row-by-row

# Eyes
im_fill(frame0, [2,2],[1,4],bl)
im_fill(frame0, [2,2],[7,10],bl)
im_fill(frame0, [3,3],[2,4],bl)
im_fill(frame0, [3,3],[7,9],bl)

# Hair
im_fill(frame0, [0,0],[1,10],br)
im_fill(frame0, [8,8],[1,1],br)
im_fill(frame0, [9,9],[1,2],br)
im_fill(frame0, [8,8],[10,10],br)
im_fill(frame0, [9,9],[9,10],br)

# Mouth
im_fill(frame0, [6,6],[3,3],bl)
im_fill(frame0, [7,7],[4,7],bl)
im_fill(frame0, [6,6],[8,8],bl)

# creating frame 2
frame2 = np.array([[gr]*cols for row in range (rows)])

# Specify the frame row-by-row

# head_body
im_fill(frame2, [4,5],[7,9],bl)
im_fill(frame2, [6,6],[8,8],bl)
im_fill(frame2, [7,10],[6,6],bl)
im_fill(frame2, [7,10],[10,10],bl)
im_fill(frame2, [7,7],[7,9],bl)
im_fill(frame2, [14,18],[7,7],bl)
im_fill(frame2, [14,18],[9,9],bl)

#hair
im_fill(frame2, [3,3],[6,10],ch)
im_fill(frame2, [4,6],[6,6],ch)
im_fill(frame2, [4,6],[10,10],ch)
im_fill(frame2, [6,6],[7,7],ch)
im_fill(frame2, [6,6],[9,9],ch)

#dress
im_fill(frame2, [8,13],[7,9],az)
im_fill(frame2, [12,13],[6,6],az)
im_fill(frame2, [12,13],[10,10],az)
im_fill(frame2, [13,13],[5,5],az)
im_fill(frame2, [13,13],[11,11],az)


# creating frame 3
frame3 =np.array([[gr]*cols for row in range (rows)])

# Specify the frame row-by-row

# head_body
im_fill(frame3, [4,5],[7,9],az)
im_fill(frame3, [6,6],[8,8],az)
im_fill(frame3, [7,10],[6,6],az)
im_fill(frame3, [7,10],[10,10],az)
im_fill(frame3, [7,7],[7,9],az)
im_fill(frame3, [14,18],[7,7],az)
im_fill(frame3, [14,18],[9,9],az)

#hair
im_fill(frame3, [3,3],[6,10],bl)
im_fill(frame3, [4,6],[6,6],bl)
im_fill(frame3, [4,6],[10,10],bl)
im_fill(frame3, [6,6],[7,7],bl)
im_fill(frame3, [6,6],[9,9],bl)

#dress
im_fill(frame3, [8,13],[7,9],w)
im_fill(frame3, [12,13],[6,6],w)
im_fill(frame3, [12,13],[10,10],w)
im_fill(frame3, [13,13],[5,5],w)
im_fill(frame3, [13,13],[11,11],w)


# creating frame 4
frame4 =np.array([[gr]*cols for row in range (rows)])

# Specify the frame row-by-row

# head_body
im_fill(frame4, [4,5],[7,9],bl)
im_fill(frame4, [6,6],[8,8],bl)
im_fill(frame4, [7,10],[6,6],bl)
im_fill(frame4, [7,10],[10,10],bl)
im_fill(frame4, [7,7],[7,9],bl)
im_fill(frame4, [14,18],[7,7],bl)
im_fill(frame4, [14,18],[9,9],bl)

#hair
im_fill(frame4, [3,3],[8,8],ch)
im_fill(frame4, [2,2],[8,8],ch)
im_fill(frame4, [2,3],[6,7],ch)
im_fill(frame4, [4,6],[6,6],ch)
im_fill(frame4, [6,6],[7,7],ch)
#dress
im_fill(frame4, [8,13],[7,9],pu)
im_fill(frame4, [12,13],[6,6],pu)
im_fill(frame4, [12,13],[10,10],pu)
im_fill(frame4, [13,13],[5,5],pu)
im_fill(frame4, [13,13],[11,11],pu)


frame5 = np.array([[gr]*cols for row in range (rows)])

# Specify the frame row-by-row

# Eyes
im_fill(frame5, [2,2],[1,4],bl)
im_fill(frame5, [2,2],[7,10],bl)
im_fill(frame5, [3,3],[2,4],bl)
im_fill(frame5, [3,3],[7,9],bl)

# Hair
im_fill(frame5, [0,0],[1,10],br)
im_fill(frame5, [8,8],[1,1],br)
im_fill(frame5, [9,9],[1,2],br)
im_fill(frame5, [8,8],[10,10],br)
im_fill(frame5, [9,9],[9,10],br)

# Mouth
im_fill(frame5, [6,6],[3,3],bl)
im_fill(frame5, [7,7],[4,7],bl)
im_fill(frame5, [6,6],[8,8],bl)

# little people
im_fill(frame5, [14,15],[1,3],bl)
im_fill(frame5, [14,15],[6,8],bl)
im_fill(frame5, [14,15],[11,13],az)
im_fill(frame5, [14,15],[16,18],bl)
im_fill(frame5, [16,17],[2,2],pu)
im_fill(frame5, [16,17],[7,7],p)
im_fill(frame5, [16,17],[12,12],w)
im_fill(frame5, [16,17],[17,17],az)

# liga
im_fill(frame5, [12,13],[0,2],ch)
im_fill(frame5, [14,15],[0,0],ch)
im_fill(frame5, [18,18],[1,3],pu)
im_fill(frame5, [19,19],[2,2],bl)

# purple girl
im_fill(frame5, [14,16],[5,5],ch)
im_fill(frame5, [18,18],[6,8],p)
im_fill(frame5, [19,19],[7,7],bl)

# white girl
im_fill(frame5, [16,16],[10,11],bl)
im_fill(frame5, [13,15],[10,10],bl)
im_fill(frame5, [13,13],[11,14],bl)
im_fill(frame5, [14,15],[14,14],bl)
im_fill(frame5, [16,16],[13,14],bl)
im_fill(frame5, [18,18],[11,13],w)
im_fill(frame5, [19,19],[12,12],bl)

# blue girl
im_fill(frame5, [16,16],[15,16],ch)
im_fill(frame5, [13,15],[15,15],ch)
im_fill(frame5, [13,13],[16,19],ch)
im_fill(frame5, [14,15],[19,19],ch)
im_fill(frame5, [16,16],[18,19],ch)
im_fill(frame5, [18,18],[16,18],az)
im_fill(frame5, [19,19],[17,17],bl)

# Create a frame with the same background color
frame6 = np.array([[gr]*cols for row in range (rows)])


# im_fill example
start_row = 1
end_row   = 3
start_col = 2
end_col   = 6
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

# im_fill example
start_row = 10
end_row   = 12
start_col = 3
end_col   = 3
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)


start_row = 10
end_row   = 12
end_col   = 5
start_col = 5
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

#leftarm
start_row = 6
end_row   = 6
end_col   = 2
start_col =2
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)


#rigtharm
start_row = 6
end_row   = 6
end_col   = 6
start_col = 6
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)



#dress

start_row = 6
end_row   = 9
end_col   = 3
start_col = 3
im_fill(frame6, [start_row, end_row], [start_col, end_col], p)

start_row = 6
end_row   = 9
end_col   = 5
start_col = 5
im_fill(frame6, [start_row, end_row], [start_col, end_col], p)

start_row = 8
end_row   = 9
end_col   = 4
start_col = 4
im_fill(frame6, [start_row, end_row], [start_col, end_col], p)

start_row = 8
end_row   = 8
end_col   = 2
start_col = 2
im_fill(frame6, [start_row, end_row], [start_col, end_col], p)

start_row = 8
end_row   = 8
end_col   = 6
start_col = 6
im_fill(frame6, [start_row, end_row], [start_col, end_col], p)

#neck
start_row = 4
end_row   = 7
end_col   = 4
start_col = 4
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

start_row = 5
end_row   = 5
end_col   = 3
start_col = 3
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

start_row = 5
end_row   = 5
end_col   = 5
start_col = 5
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

start_row = 4
end_row   = 7
start_col = 6
end_col   = 4
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

#hair
start_row = 1
end_row   = 6
start_col = 7
end_col   = 8
im_fill(frame6, [start_row, end_row], [start_col, end_col], br)
# Video play
frame_list = [frame0,frame2,frame3,frame4,frame6,frame5]         # list of frames
fps= 1                               # frames per sec
play_video= vid_show(frame_list, fps) # play on screen


#im_show(frame0)
