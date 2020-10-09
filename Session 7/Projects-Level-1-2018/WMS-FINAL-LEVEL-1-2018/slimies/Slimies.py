from AOLME import *

# Define the size of the image
rows = 20# num of rows
cols = 20# num of cols

# Define all of the colors
r = "ff0000" # red code
blue = "0000ff" # blue code
g = "00ff00" # green code
b = "000000" # black code
grey = "000fff" # gray code
p = "ff00ff" # purple code
y = "3e3e3e" # tan code
l = "00f0ff" # light blue code
w = "ffffff" # whight code
br = "a52a2a" # brown code

# Create a frame with the same background color
frame0 = np.array([[r]*cols for row in range (rows)])

# im_fill example
start_row = 0
end_row   = 10
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

start_row = 0
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

start_row = 0
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

start_row = 10
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame0, [start_row, end_row], [start_col, end_col], g)

#Julian character
start_row = 16 
end_row = 18
start_col =  3
end_col = 8
im_fill(frame0, [start_row, end_row], [start_col, end_col], r)

start_row = 15
end_row = 19
start_col = 4
end_col = 7
im_fill(frame0, [start_row, end_row], [start_col, end_col], r)
#eyes
start_row = 17
end_row = 17
start_col = 4
end_col = 4
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

start_row = 17
end_row = 17
start_col = 6
end_col = 6
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

#jose character
start_row = 13
end_row = 14
start_col = 14
end_col = 15
im_fill(frame0, [start_row, end_row], [start_col, end_col], y)
#barrel
start_row = 15
end_row = 15
start_col = 11
end_col = 14
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)
#grip
start_row = 16
end_row = 16
start_col = 14
end_col = 14
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)
#torso
start_row = 14
end_row = 14
start_col = 16
end_col = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)

start_row = 15
end_row = 15
start_col = 17
end_col = 17
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)

start_row = 15
end_row = 16
start_col = 15
end_col = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)

start_row = 16
end_row = 16
start_col = 13
end_col = 13
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)
#legs
start_row = 17
end_row = 17
start_col = 14
end_col = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)

start_row = 18
end_row = 18
start_col = 14
end_col = 14
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)

start_row = 18
end_row = 18
start_col = 16
end_col = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], blue)
#feet
start_row = 19
end_row = 19
start_col = 14
end_col = 14
im_fill(frame0, [start_row, end_row], [start_col, end_col], grey)

start_row = 19
end_row = 19
start_col = 16
end_col = 16
im_fill(frame0, [start_row, end_row], [start_col, end_col], grey)

#+im_show(frame0)

# Create a frame with the same background color
frame1 = np.array([[r]*cols for row in range (rows)])

# im_fill example

start_row = 0
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)

start_row = 0
end_row   = 9
start_col = 0
end_col   = 19
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 6
end_row   = 9
start_col = 6
end_col   = 7
im_fill(frame1, [start_row, end_row], [start_col, end_col], br)

start_row = 6
end_row   = 9
start_col = 14
end_col   = 15
im_fill(frame1, [start_row, end_row], [start_col, end_col], br)

start_row = 0
end_row   = 5
start_col = 4
end_col   = 9
im_fill(frame1, [start_row, end_row], [start_col, end_col], g)



#Julian character
start_row = 16 
end_row = 18
start_col =  3
end_col = 8
im_fill(frame1, [start_row, end_row], [start_col, end_col], r)

start_row = 15
end_row = 19
start_col = 4
end_col = 7
im_fill(frame1, [start_row, end_row], [start_col, end_col], r)
#eyes
start_row = 17
end_row = 17
start_col = 4
end_col = 4
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

start_row = 17
end_row = 17
start_col = 6
end_col = 6
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

#jose character
start_row = 13
end_row = 14
start_col = 14
end_col = 15
im_fill(frame1, [start_row, end_row], [start_col, end_col], y)
#barrel
start_row = 15
end_row = 15
start_col = 11
end_col = 14
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)
#grip
start_row = 16
end_row = 16
start_col = 14
end_col = 14
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)
#torso
start_row = 14
end_row = 14
start_col = 16
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 15
end_row = 15
start_col = 17
end_col = 17
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 15
end_row = 16
start_col = 15
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 16
end_row = 16
start_col = 13
end_col = 13
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)
#legs
start_row = 17
end_row = 17
start_col = 14
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 18
end_row = 18
start_col = 14
end_col = 14
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)

start_row = 18
end_row = 18
start_col = 16
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], blue)
#feet
start_row = 19
end_row = 19
start_col = 14
end_col = 14
im_fill(frame1, [start_row, end_row], [start_col, end_col], grey)

start_row = 19
end_row = 19
start_col = 16
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], grey)

#im_show(frame1)

frame2 = frame1.copy()
start_row = 0
end_row   = 5
start_col = 13
end_col   = 18
im_fill(frame2, [start_row, end_row], [start_col, end_col], g)
 
#im_show(frame2)
frame3 = frame2.copy()

#Julian character
start_row = 14
end_row   = 19
start_col = 3
end_col   = 8
im_fill(frame3, [start_row, end_row], [start_col, end_col], g)

frame3[12:18, 3:9] = frame1[14:20, 3:9]

#im_show(frame3)
frame4 = frame3.copy()

#Julian character
start_row = 12
end_row   = 18
start_col = 3
end_col   = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], g)

frame4[0:6, 10:16] = frame3[12:18, 3:9]

frame5 = frame4.copy()

#Julian character
start_row = 0
end_row   = 6
start_col = 10
end_col   = 16
im_fill(frame5, [start_row, end_row], [start_col, end_col], g)

frame5[4:10, 10:16] = frame4[0:6, 10:16]

frame6 = frame5.copy()

start_row = 4
end_row   = 10
start_col = 10
end_col   = 16
im_fill(frame6, [start_row, end_row], [start_col, end_col], g)

frame6[11:17, 10:16] = frame5[4:10, 10:16]

frame7 = frame6.copy()

start_row = 0
end_row   = 19
start_col = 0
end_col   = 19
im_fill(frame7, [start_row, end_row], [start_col, end_col], r)





frame_list = [frame0, frame1, frame2, frame3,frame4,frame5,frame6,frame7]

fps= 2


# Play the video
play_video= vid_show(frame_list, fps)


