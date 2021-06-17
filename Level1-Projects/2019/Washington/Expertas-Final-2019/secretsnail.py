from AOLME import *

# Define the size of the image
rows = 20  # num of rows
cols = 20  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff" # blue code
g = "80ff00"
w = "FFFFFF"
brown ="663300"
brown2 ="cc6600"
gray ="c0c0c0"
brown3 ="ffb266"
p ="4c0099"
green ="666600"
# Create frame 0 with the same background color
frame0 = np.array([[w]*cols for row in range (rows)])
frame1 = frame0.copy()
frame2 = frame0.copy()
# im_fill example
start_row = 10
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

# im_fill example
start_row = 6
end_row   = 9
start_col = 6
end_col   = 7
im_fill(frame0, [start_row, end_row], [start_col, end_col], brown)


# im_fill example
start_row = 6
end_row   = 9
start_col = 15
end_col   = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], brown)


# im_fill example
start_row = 0
end_row   = 6
start_col = 3
end_col   = 10
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)


# im_fill example
start_row = 1
end_row   = 6
start_col =12 
end_col   =18 
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

# im_fill example
start_row = 8 
end_row   = 9
start_col = 9
end_col   = 10
im_fill(frame0, [start_row, end_row], [start_col, end_col], brown2)

# im_fill example
start_row = 9 
end_row   = 9 
start_col = 11
end_col   = 11
im_fill(frame0, [start_row, end_row], [start_col, end_col], gray)
# Create frame 1 with the same background color

# im_fill example
start_row = 0
end_row   = 4 
start_col = 0
end_col   = 5
im_fill(frame1, [start_row, end_row], [start_col, end_col], r)

# im_fill example
start_row = 0
end_row   = 3
start_col = 0
end_col   = 4
im_fill(frame1, [start_row, end_row], [start_col, end_col], gray)

# im_fill example
start_row = 13
end_row   = 19 
start_col = 0
end_col   = 19
im_fill(frame1, [start_row, end_row], [start_col, end_col], brown3)

# im_fill example
start_row = 9
end_row   = 11 
start_col = 6
end_col   = 12
im_fill(frame1, [start_row, end_row], [start_col, end_col], gray)

# im_fill example
start_row = 12
end_row   = 12 
start_col = 6
end_col   = 6
im_fill(frame1, [start_row, end_row], [start_col, end_col], p)

# im_fill example
start_row = 12
end_row   = 12 
start_col = 11
end_col   = 11
im_fill(frame1, [start_row, end_row], [start_col, end_col], p)

# im_fill example
start_row = 10
end_row   = 10 
start_col = 12
end_col   = 12
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

# im_fill example
start_row = 6
end_row   = 7
start_col = 8
end_col   = 10
im_fill(frame1, [start_row, end_row], [start_col, end_col], brown3)

# im_fill example
start_row = 8
end_row   = 8 
start_col = 9
end_col   = 9
im_fill(frame1, [start_row, end_row], [start_col, end_col], brown3)

# im_fill example
start_row = 5
end_row   = 5 
start_col = 8
end_col   = 10
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

# im_fill example
start_row = 4
end_row   = 4 
start_col = 9
end_col   = 9

im_fill(frame1, [start_row, end_row], [start_col, end_col], b)


# im_fill example
start_row = 5
end_row   = 14 
start_col = 3
end_col   = 15

im_fill(frame2, [start_row, end_row], [start_col, end_col], green)

# im_fill example
start_row = 6
end_row   = 13 
start_col = 4
end_col   = 14

im_fill(frame2, [start_row, end_row], [start_col, end_col], g)

# im_fill example
start_row = 7
end_row   = 8 
start_col = 6
end_col   = 7

im_fill(frame2, [start_row, end_row], [start_col, end_col], green)
# im_fill example
start_row = 7
end_row   = 8 
start_col = 11
end_col   = 12

im_fill(frame2, [start_row, end_row], [start_col, end_col], green)
# im_fill example
start_row = 10
end_row   = 11 
start_col = 6
end_col   = 6
im_fill(frame2, [start_row, end_row], [start_col, end_col], green)
# im_fill example
start_row = 11
end_row   = 11 
start_col = 7
end_col   = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], green)
# im_fill example
start_row = 10
end_row   = 10 
start_col = 12
end_col   = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], green)
# im_fill example
start_row = 12
end_row   = 13 
start_col = 6
end_col   = 6
im_fill(frame2, [start_row, end_row], [start_col, end_col], r)

# im_fill example
start_row = 12
end_row   = 13 
start_col = 12
end_col   = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], r)
# im_fill example
start_row = 17
end_row   = 19 
start_col = 0
end_col   = 19
im_fill(frame2, [start_row, end_row], [start_col, end_col], g)

#im_show(frame2)


# im_fill example
# Video play
frame_list = [frame0, frame1, frame2]         # list of frames
fps= 2                                # frames per sec
play_video= vid_show(frame_list, fps) # play on screen