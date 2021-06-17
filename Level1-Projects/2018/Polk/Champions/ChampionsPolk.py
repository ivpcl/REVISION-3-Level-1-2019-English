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
back  = [["ff"]*total_columns for row in range(total_rows)]
# Define all of the colors
lava = "FF4000"
stage = "00fFBF"
night= "000000"
sky= "610b0b"
scorpion = "610b4b"
scorpion_laser = "e0f8f7"
creeper_body = "0b610b"
creeper_eye= "424242"
creeper_mouth= "b40431"
exp1  = "b40404"
exp2  = "df7401"
exp3 = "d8d8d8"

# Background
im_fill(back, [0,4],[0,19],sky)
im_fill(back, [5,17],[0,19],night)
im_fill(back,[18,19],[0,19],lava)
im_fill(back,[18,19],[6,12],stage)
im_fill(back,[17,17],[4,14],stage)

im_show(back)

# Frame 1
frame_1 = np.copy(back)

im_fill(frame_1,[9,16],[11,11],scorpion)
im_fill(frame_1,[9,13],[10,10],scorpion)
im_fill(frame_1,[11,16],[9,9],scorpion)
im_fill(frame_1,[11,11],[8,8],scorpion)

im_fill(frame_1,[9,10],[5,7],creeper_body)
im_fill(frame_1,[11,13],[6,6],creeper_body)
im_fill(frame_1,[14,16],[5,5],creeper_body)
im_fill(frame_1,[14,14],[6,6],creeper_body)
im_fill(frame_1,[14,16],[7,7],creeper_body)
im_fill(frame_1,[9,9],[5,5],creeper_eye)
im_fill(frame_1,[9,9],[7,7],creeper_eye)
im_fill(frame_1,[10,10],[6,6],creeper_mouth)


# FRAME 2
frame_2 = np.copy(frame_1)
im_fill(frame_2,[11,11],[3,7],scorpion_laser)# scorpion laser

im_fill(frame_2,[9,10],[5,7],night)  # removing head
im_fill(frame_2,[11,12],[2,4],creeper_body) # face
im_fill(frame_2,[11,11],[2,2],creeper_eye) # eye 1
im_fill(frame_2,[11,11],[4,4],creeper_eye) # eye 2
im_fill(frame_2,[12,12],[3,3],creeper_mouth)# mouth

im_show(frame2)
# frame 3
frame_3 = np.copy(frame_1)
im_fill(frame_3,[9,10],[5,7],night)  # removing head
im_fill(frame_3,[6,10],[8,8],scorpion_laser)  # scorpion laser
im_fill(frame_3,[17,17],[1,3],creeper_body) # face
im_fill(frame_3,[17,17],[1,1],creeper_eye) # eye 1
im_fill(frame_3,[17,17],[3,3],creeper_eye) # eye 2

# frame 4
frame_4 = np.copy(back)
im_fill(frame_4,[10,19],[0,11],exp1)

# frame 5
frame_5 = np.copy(back)
im_fill(frame_5,[6,19],[0,15],exp2)

# frame 6
frame_6 = np.copy(back)
im_fill(frame_6,[0,19],[0,19],exp3)


# putting all together
frame_list = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]         # list of frames
fps= 10                           # frames per sec
play_video= vid_show(frame_list, fps) # play on screen
