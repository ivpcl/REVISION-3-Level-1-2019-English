from AOLME import *

# Define the size of the image
rows = 20# num of rows
cols = 20# num of cols

# Define all of the colors
r = "ff0000" # red code
blue = "000055" # blue code
#g = "00ff00" # green code
b = "000000" # black code
#grey = "000fff" # gray code
#p = "ff00ff" # purple code
#y = "3e3e3e" # tan code
#l = "00f0ff" # light blue code
w = "ffffff" # whight code
br = "a52a2a" # brown code


#frame0
frame0 = np.array([[blue]*cols for row in range (rows)])


#frame1
frame1 = frame0.copy()
im_fill(frame1, [0,19], [3, 16], w)
im_fill(frame1, [19,19], [3, 6], blue)
im_fill(frame1, [17,18], [3, 5], blue)
im_fill(frame1, [15,16], [3, 4], blue)
im_fill(frame1, [12,14], [3, 3], blue)
im_fill(frame1, [0,4], [3, 3], blue)
im_fill(frame1, [0,2], [4, 4], blue)
im_fill(frame1, [0,0], [5, 5], blue)
im_fill(frame1, [19,19], [13, 16], blue)
im_fill(frame1, [18,18], [14, 16], blue)
im_fill(frame1, [16,17], [15, 16], blue)
im_fill(frame1, [14,15], [16, 16], blue)
im_fill(frame1, [0,0], [12, 16], blue)
im_fill(frame1, [1,1], [14, 16], blue)
frame1 [2][16] = blue
frame1 [3][16] = blue
frame1 [2][15] = blue


#frame2
frame2 = frame1.copy()
im_fill(frame2, [18,18], [10, 11], b)
im_fill(frame2, [16,17], [9, 12], b)
im_fill(frame2, [14,15], [11, 13], b)
im_fill(frame2, [15,16], [8, 8], b)
im_fill(frame2, [13,15], [7, 7], b)
im_fill(frame2, [12,14], [6, 6], b)
im_fill(frame2, [12,13], [14, 14], b)
frame2 [14][11] = w
frame2 [13][7] = w
frame2 [12][6] = w


#frame3
frame3 = frame2.copy()
im_fill(frame3, [1,4], [5, 5], b)
im_fill(frame3, [5,6], [4, 4], b)
im_fill(frame3, [6,11], [5, 5], b)
im_fill(frame3, [9,10], [4, 4], b)
im_fill(frame3, [8,11], [6, 6], b)
im_fill(frame3, [7,10], [7, 7], b)
im_fill(frame3, [5,9], [8, 8], b)
frame3 [12][6] = w
frame3 [13][7] = w


#frame4
frame4 = frame3.copy()
im_fill(frame4, [4,7], [11, 14], b)
im_fill(frame4, [8,8], [12, 13], b)
im_fill(frame4, [9,11], [13, 13], b)
im_fill(frame4, [3,3], [11, 13], b)
im_fill(frame4, [2,2], [12, 12], b)
im_fill(frame4, [4,7], [15, 15], b)
frame4 [3][14] = b
frame4 [2][13] = b
frame4 [7][15] = w

#frame5
frame5 = frame4.copy()
im_fill(frame5, [3,7], [13, 13], w)
im_fill(frame5, [4,6], [12, 12], w)
im_fill(frame5, [4,6], [14, 14], w)
frame5 [5][13] = r

#frame6
frame6 = np.array([[r]*cols for row in range (rows)])

#A
im_fill(frame6, [5,12], [0, 0], b)
im_fill(frame6, [5,12], [3, 3], b)
im_fill(frame6, [5,5], [1, 2], b)
im_fill(frame6, [8,8], [1, 2], b)

#P
im_fill(frame6, [5,12], [5,5], b)
im_fill(frame6, [5,8], [8,8], b)
im_fill(frame6, [5,5], [6,8], b)
im_fill(frame6, [8,8], [6,8], b)

#E
im_fill(frame6, [5,5], [10,13], b)
im_fill(frame6, [5,12], [10,10], b)
im_fill(frame6, [12,12], [10,13], b)
frame6 [8][11] = b

#X
im_fill(frame6, [5,6], [15,15], b)
frame6 [7][16] = b
im_fill(frame6, [8,9], [17,17], b)
frame6 [10][16] = b
im_fill(frame6, [11,12], [15,15], b)
im_fill(frame6, [11,12], [19,19], b)
frame6 [10][18] = b
frame6 [7][18] = b
im_fill(frame6, [5,6], [19,19], b)



#frame_list = [frame0, frame1, frame2, frame3, frame4, frame5, frame6]
frame_list = [frame6]

fps=1.5


# Play the video
play_video= vid_show(frame_list, fps)


