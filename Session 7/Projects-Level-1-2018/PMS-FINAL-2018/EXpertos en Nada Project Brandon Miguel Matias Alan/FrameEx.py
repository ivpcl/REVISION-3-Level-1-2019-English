from AOLME import *

# Define the size of the image
rows = 3  # num of rows
cols = 4  # num of cols

# Define all of the colors
r = "ff0000" # red code
b = "0000ff" # blue code

# Create a frame with the same background color
frame0 = np.array([[r]*cols for row in range (rows)])

# Specify the frame row-by-row
frame0[0] = [r, b, r, b]
frame0[1] = [b, b, b, b]

im_show(frame0)