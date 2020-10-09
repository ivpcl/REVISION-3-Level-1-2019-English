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


move_by = 2
frame_2 = [["ffffff"]*cols for row in range(rows)]
for row in range(rows):
    for col in range(cols-move_by):
        frame_2[row][col+move_by] = frame_1[row][col]

frame_list = [frame_1, frame_2]
fps = 1
play_video = vid_show(frame_list,fps)
