from AOLME import *
# Define the size of the image

rows = 50
cols = 50
# Define all of the colors
b = "0000ff"
g = "008000"
p = "8000ff"
s = "0066ff"
w = "ffffff"
y = "ffff00"
br= "804000"
r = "ff0000"
bl= "000000"
# Create a frame with the same background color
frame0 = np.array([[g]*cols for row in range (rows)])

# Specify the frame row-by-row
#frame0[0] = [r, b, r, b]
#frame0[1] = [b, b, b, b]
#frame0[2] = [r, b, r, b,]

#top part
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

#central part

start_row = 30
end_row = 31
start_col = 38
end_col = 39
im_fill(frame0, [start_row, end_row], [start_col, end_col], y)

#barrel
start_row = 32
end_row = 32
start_col = 35
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 38
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)
#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 35
start_col = 38
end_col = 40
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)
#barrel
start_row = 32
end_row = 32
start_col = 35
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)

#gun
start_row = 33
end_row = 33
start_col = 38
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)

#legs
start_row = 35
end_row = 38
start_col = 38
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 38
start_col = 40
end_col = 40
im_fill(frame0, [start_row, end_row], [start_col, end_col], b)


#feet
start_row = 38
end_row = 38
start_col = 38
end_col = 38
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)

start_row = 38
end_row = 38
start_col = 40
end_col = 40
im_fill(frame0, [start_row, end_row], [start_col, end_col], bl)

#+im_show(frame0)

# Create a frame with the same background color
frame1 = frame0.copy()

# im_fill example
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

start_row = 30
end_row = 31
start_col = 10
end_col = 11
im_fill(frame1, [start_row, end_row], [start_col, end_col], y)


#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 36
start_col = 9
end_col = 12
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

#legs
start_row = 35
end_row = 40
start_col = 9
end_col = 9
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 40
start_col = 12
end_col = 12
im_fill(frame1, [start_row, end_row], [start_col, end_col], b)


#barrel
start_row = 32
end_row = 32
start_col = 11
end_col = 16
im_fill(frame1, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 11
end_col = 11
im_fill(frame1, [start_row, end_row], [start_col, end_col], bl)

#feet
start_row = 41
end_row = 41
start_col = 9
end_col = 9
im_fill(frame1, [start_row, end_row], [start_col, end_col], bl)

start_row = 41
end_row = 41
start_col = 12
end_col = 12
im_fill(frame1, [start_row, end_row], [start_col, end_col], bl)

frame2 = frame0.copy()

# im_fill example
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

start_row = 30
end_row = 31
start_col = 10
end_col = 11
im_fill(frame2, [start_row, end_row], [start_col, end_col], y)


#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame2, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 36
start_col = 9
end_col = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame2, [start_row, end_row], [start_col, end_col], b)

#legs
start_row = 35
end_row = 40
start_col = 9
end_col = 9
im_fill(frame2, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 40
start_col = 12
end_col = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], b)


#barrel
start_row = 32
end_row = 32
start_col = 11
end_col = 16
im_fill(frame2, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 11
end_col = 11
im_fill(frame2, [start_row, end_row], [start_col, end_col], bl)

#feet
start_row = 41
end_row = 41
start_col = 9
end_col = 9
im_fill(frame2, [start_row, end_row], [start_col, end_col], bl)

start_row = 41
end_row = 41
start_col = 12
end_col = 12
im_fill(frame2, [start_row, end_row], [start_col, end_col], bl)

start_row = 32
end_row = 32
start_col = 22
end_col = 22
im_fill(frame2, [start_row, end_row], [start_col, end_col], bl)

frame3 = frame0.copy()

# im_fill example
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

start_row = 30
end_row = 31
start_col = 10
end_col = 11
im_fill(frame3, [start_row, end_row], [start_col, end_col], y)


#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame3, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 36
start_col = 9
end_col = 12
im_fill(frame3, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame3, [start_row, end_row], [start_col, end_col], b)

#legs
start_row = 35
end_row = 40
start_col = 9
end_col = 9
im_fill(frame3, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 40
start_col = 12
end_col = 12
im_fill(frame3, [start_row, end_row], [start_col, end_col], b)


#barrel
start_row = 32
end_row = 32
start_col = 11
end_col = 16
im_fill(frame3, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 11
end_col = 11
im_fill(frame3, [start_row, end_row], [start_col, end_col], bl)

#feet
start_row = 41
end_row = 41
start_col = 9
end_col = 9
im_fill(frame3, [start_row, end_row], [start_col, end_col], bl)

start_row = 41
end_row = 41
start_col = 12
end_col = 12
im_fill(frame3, [start_row, end_row], [start_col, end_col], bl)

start_row = 31
end_row = 31
start_col = 30
end_col = 30
im_fill(frame3, [start_row, end_row], [start_col, end_col], bl)

frame5 = np.array([[g]*cols for row in range (rows)])

# im_fill example
im_fill(frame5,[0,12],[0,49],s)
im_fill(frame5,[1,10],[1,10],p)
im_fill(frame5,[4,7],[4,7],g)
im_fill(frame5,[5,7],[20,40],w)
im_fill(frame5,[7,8],[25,34],w)
im_fill(frame5,[4,5],[25,34],w)
im_fill(frame5,[5,6],[18,20],w)
im_fill(frame5,[5,6],[40,43],w)

frame6 = frame5.copy()

# im_fill example
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

start_row = 30
end_row = 31
start_col = 10
end_col = 11
im_fill(frame6, [start_row, end_row], [start_col, end_col], y)


#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame6, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 36
start_col = 9
end_col = 12
im_fill(frame6, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame6, [start_row, end_row], [start_col, end_col], b)

#legs
start_row = 35
end_row = 40
start_col = 9
end_col = 9
im_fill(frame6, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 40
start_col = 12
end_col = 12
im_fill(frame6, [start_row, end_row], [start_col, end_col], b)


#barrel
start_row = 32
end_row = 32
start_col = 11
end_col = 16
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 11
end_col = 11
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

#feet
start_row = 41
end_row = 41
start_col = 9
end_col = 9
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

start_row = 41
end_row = 41
start_col = 12
end_col = 12
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

start_row = 30
end_row = 30
start_col = 38
end_col = 38
im_fill(frame6, [start_row, end_row], [start_col, end_col], bl)

frame4 = frame0.copy()

# im_fill example
im_fill(frame0,[0,12],[0,49],s)
im_fill(frame0,[1,10],[1,10],p)
im_fill(frame0,[4,7],[4,7],g)
im_fill(frame0,[5,7],[20,40],w)
im_fill(frame0,[7,8],[25,34],w)
im_fill(frame0,[4,5],[25,34],w)
im_fill(frame0,[5,6],[18,20],w)
im_fill(frame0,[5,6],[40,43],w)

start_row = 30
end_row = 31
start_col = 10
end_col = 11
im_fill(frame4, [start_row, end_row], [start_col, end_col], y)


#torso
start_row = 31
end_row = 31
start_col = 40
end_col = 40
im_fill(frame4, [start_row, end_row], [start_col, end_col], b)

start_row = 32
end_row = 36
start_col = 9
end_col = 12
im_fill(frame4, [start_row, end_row], [start_col, end_col], b)

start_row = 33
end_row = 33
start_col = 37
end_col = 37
im_fill(frame4, [start_row, end_row], [start_col, end_col], b)

#legs
start_row = 35
end_row = 40
start_col = 9
end_col = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], b)

start_row = 35
end_row = 40
start_col = 12
end_col = 12
im_fill(frame4, [start_row, end_row], [start_col, end_col], b)


#barrel
start_row = 32
end_row = 32
start_col = 11
end_col = 16
im_fill(frame4, [start_row, end_row], [start_col, end_col], bl)
#grip
start_row = 33
end_row = 33
start_col = 11
end_col = 11
im_fill(frame4, [start_row, end_row], [start_col, end_col], bl)

#feet
start_row = 41
end_row = 41
start_col = 9
end_col = 9
im_fill(frame4, [start_row, end_row], [start_col, end_col], bl)

start_row = 41
end_row = 41
start_col = 12
end_col = 12
im_fill(frame4, [start_row, end_row], [start_col, end_col], bl)

start_row = 30
end_row = 30
start_col = 38
end_col = 38
im_fill(frame4, [start_row, end_row], [start_col, end_col], bl)

frame7 = frame6.copy()
##
start_row = 2
end_row = 2
start_col = 1
end_col = 5
im_fill(frame7, [start_row, end_row], [start_col, end_col], w)

start_row = 4
end_row = 4
start_col = 1
end_col = 5
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 1
end_row = 5
start_col = 2
end_col = 2
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 1
end_row = 5
start_col = 4
end_col = 4
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#1
start_row = 1
end_row = 5
start_col = 7
end_col = 7
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#V
start_row = 12
end_row = 15
start_col = 1
end_col = 1
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 16
end_row = 16
start_col = 2
end_col = 2
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 15
start_col = 3
end_col = 3
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#I
start_row = 12
end_row = 16
start_col = 5
end_col = 5
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#C
start_row = 12
end_row = 16
start_col = 7
end_col = 7
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 12
start_col = 7
end_col = 9
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 16
end_row = 16
start_col = 7
end_col = 9
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#T
start_row = 12
end_row = 12
start_col = 11
end_col = 13
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 16
start_col = 12
end_col = 12
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#O
start_row = 12
end_row = 12
start_col = 15
end_col = 17
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 16
start_col = 15
end_col = 15
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 16
end_row = 16
start_col = 15
end_col = 17
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 16
start_col = 17
end_col = 17
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#R
start_row = 12
end_row = 22
start_col = 19
end_col = 19
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 12
start_col = 19
end_col = 21
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 15
start_col = 21
end_col = 21
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 16
end_row = 16
start_col = 19
end_col = 21
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 17
end_row = 17
start_col = 20
end_col = 20
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 22
start_col = 21
end_col = 21
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#Y
start_row = 12
end_row = 13
start_col = 23
end_col = 23
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 14
end_row = 16
start_col = 24
end_col = 24
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 12
end_row = 13
start_col = 25
end_col = 25
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)
#================================
#O
start_row = 18
end_row = 22
start_col = 23
end_col = 23
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 18
start_col = 23
end_col = 25
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 22
start_col = 25
end_col = 25
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 22
end_row = 22
start_col = 23
end_col = 25
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#Y
start_row = 18
end_row = 19
start_col = 27
end_col = 27
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 19
start_col = 29
end_col = 29
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 20
end_row = 22
start_col = 28
end_col = 28
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#A
start_row = 19
end_row = 22
start_col = 31
end_col = 31
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 18
start_col = 32
end_col = 32
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 20
end_row = 20
start_col = 32
end_col = 32
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 19
end_row = 22
start_col = 33
end_col = 33
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#L
start_row = 18
end_row = 22
start_col = 35
end_col = 35
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 22
end_row = 22
start_col = 35
end_col = 37
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

#E
start_row = 18
end_row = 22
start_col = 39
end_col = 39
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 18
end_row = 18
start_col = 39
end_col = 41
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 20
end_row = 20
start_col = 39
end_col = 40
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

start_row = 22
end_row = 22
start_col = 39
end_col = 41
im_fill(frame7, [start_row, end_row], [start_col, end_col],  w)

frame8 = frame6.copy()
##
start_row = 2
end_row = 2
start_col = 1
end_col = 5
im_fill(frame8, [start_row, end_row], [start_col, end_col], r)

start_row = 4
end_row = 4
start_col = 1
end_col = 5
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 1
end_row = 5
start_col = 2
end_col = 2
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 1
end_row = 5
start_col = 4
end_col = 4
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

#1
start_row = 1
end_row = 5
start_col = 7
end_col = 7
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

#V
start_row = 12
end_row = 15
start_col = 1
end_col = 1
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 16
end_row = 16
start_col = 2
end_col = 2
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 15
start_col = 3
end_col = 3
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

#I
start_row = 12
end_row = 16
start_col = 5
end_col = 5
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

#C
start_row = 12
end_row = 16
start_col = 7
end_col = 7
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 12
start_col = 7
end_col = 9
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 16
end_row = 16
start_col = 7
end_col = 9
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

#T
start_row = 12
end_row = 12
start_col = 11
end_col = 13
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 16
start_col = 12
end_col = 12
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

#O
start_row = 12
end_row = 12
start_col = 15
end_col = 17
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 16
start_col = 15
end_col = 15
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 16
end_row = 16
start_col = 15
end_col = 17
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 16
start_col = 17
end_col = 17
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

#R
start_row = 12
end_row = 22
start_col = 19
end_col = 19
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 12
end_row = 12
start_col = 19
end_col = 21
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 12
end_row = 15
start_col = 21
end_col = 21
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 16
end_row = 16
start_col = 19
end_col = 21
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 17
end_row = 17
start_col = 20
end_col = 20
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

start_row = 18
end_row = 22
start_col = 21
end_col = 21
im_fill(frame8, [start_row, end_row], [start_col, end_col],  r)

#Y
start_row = 12
end_row = 13
start_col = 23
end_col = 23
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 14
end_row = 16
start_col = 24
end_col = 24
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)

start_row = 12
end_row = 13
start_col = 25
end_col = 25
im_fill(frame8, [start_row, end_row], [start_col, end_col],  b)
#================================
#O
start_row = 18
end_row = 22
start_col = 23
end_col = 23
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 18
end_row = 18
start_col = 23
end_col = 25
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 18
end_row = 22
start_col = 25
end_col = 25
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 22
end_row = 22
start_col = 23
end_col = 25
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

#Y
start_row = 18
end_row = 19
start_col = 27
end_col = 27
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 18
end_row = 19
start_col = 29
end_col = 29
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 20
end_row = 22
start_col = 28
end_col = 28
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

#A
start_row = 19
end_row = 22
start_col = 31
end_col = 31
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 18
end_row = 18
start_col = 32
end_col = 32
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 20
end_row = 20
start_col = 32
end_col = 32
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 19
end_row = 22
start_col = 33
end_col = 33
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

#L
start_row = 18
end_row = 22
start_col = 35
end_col = 35
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 22
end_row = 22
start_col = 35
end_col = 37
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

#E
start_row = 18
end_row = 22
start_col = 39
end_col = 39
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 18
end_row = 18
start_col = 39
end_col = 41
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 20
end_row = 20
start_col = 39
end_col = 40
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

start_row = 22
end_row = 22
start_col = 39
end_col = 41
im_fill(frame8, [start_row, end_row], [start_col, end_col],  y)

frame9 = frame8.copy()
frame10 = frame9.copy()
frame11 = frame10.copy()
frame12 = frame11.copy()




#im_show(frame3)
#im_show(frame2)
#im_show(frame1)
#im_show(frame0)

frame_list = [frame0, frame1, frame2, frame3, frame4,frame6,frame7,frame8, frame9,frame10, frame11,frame12 ]         # list of frames
fps= 9                         # frames per sec
play_video= vid_show(frame_list, fps)
