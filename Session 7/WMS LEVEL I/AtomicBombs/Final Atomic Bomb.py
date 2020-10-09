from AOLME import * 

total_columns = 20
total_rows = 20
background="ffe84e"
bed_sheet= "00b3ff"
bed_trim= "0000ff"
pillow= "ffeeca"
floor= "33f02c"
bed_frame= "651a0e"
floor_shadow= "33562c"
sky = "002246"
window = "5c5c5c"
snow= "ffffff"

frame_0 = [[background]*total_columns for rows in range(total_rows)]

im_fill(frame_0,[18,19],[0,19],floor)
im_fill(frame_0,[19,19],[2,13],floor_shadow)
im_fill(frame_0,[14,15],[2,13],bed_sheet)
frame_0[14][14]=bed_sheet
frame_0[14][15]=bed_sheet
frame_0[14][16]=bed_sheet
im_fill(frame_0,[19,19],[2,13],floor_shadow)
im_fill(frame_0,[16,16],[2,14],bed_trim)
frame_0[15][14]=bed_trim
frame_0[15][15]=bed_trim
frame_0[15][16]=bed_trim
im_fill(frame_0,[9,19],[1,1],bed_frame)
im_fill(frame_0,[10,13],[3,3],bed_frame)
im_fill(frame_0,[17,18],[3,3],bed_frame)
im_fill(frame_0,[17,19],[14,14],bed_frame)
im_fill(frame_0,[16,18],[16,16],bed_frame)
im_fill(frame_0,[4,11],[5,16],window)
frame_0[11][4]=window
frame_0[11][17]=window
im_fill(frame_0,[4,10],[6,9],sky)
im_fill(frame_0,[4,10],[11,15],sky)
im_fill(frame_0,[12,13],[4,6],pillow)

im_fill(frame_0,[2,10],[4,4],bed_sheet)
im_fill(frame_0,[2,2],[5,16],bed_sheet)
im_fill(frame_0,[2,10],[17,17],bed_sheet)

im_fill(frame_0,[3,3],[5,16],bed_trim)

frame_0[4][9]=snow
frame_0[4][12]=snow
frame_0[4][14]=snow
frame_0[6][7]=snow
frame_0[6][11]=snow
frame_0[7][9]=snow
frame_0[7][13]=snow
frame_0[7][15]=snow
frame_0[9][6]=snow
frame_0[10][8]=snow
frame_0[10][11]=snow
frame_0[10][14]=snow




im_show(frame_0)

frame_1=[[background]*total_columns for row in range(total_rows)]

im_fill(frame_1,[18,19],[0,19],floor)
im_fill(frame_1,[9,19],[1,1],bed_frame)
im_fill(frame_1,[10,13],[3,3],bed_frame)
im_fill(frame_1,[17,18],[3,3],bed_frame)
im_fill(frame_1,[17,19],[14,14],bed_frame)
im_fill(frame_1,[16,18],[16,16],bed_frame)
im_fill(frame_1,[4,11],[5,5],window)
im_fill(frame_1,[4,11],[10,10],window)
im_fill(frame_1,[4,11],[16,16],window)
im_fill(frame_1,[11,11],[4,17],window)
im_fill(frame_1,[2,2],[4,17],bed_sheet)
im_fill(frame_1,[2,10],[4,4],bed_sheet)
im_fill(frame_1,[2,10],[17,17],bed_sheet)
im_fill(frame_1,[3,3],[5,16],bed_trim)
im_fill(frame_1,[4,10],[6,9],sky)
im_fill(frame_1,[4,10],[11,15],sky)
im_fill(frame_1,[14,15],[2,13],bed_sheet)
im_fill(frame_1,[14,14],[14,16],bed_sheet)
im_fill(frame_1,[16,16],[2,14],bed_trim)
im_fill(frame_1,[15,15],[14,16],bed_trim)
im_fill(frame_1,[4,4],[6,6],snow)
im_fill(frame_1,[6,6],[8,8],snow)
im_fill(frame_1,[9,9],[8,8],snow)
im_fill(frame_1,[7,7],[14,14],snow)
im_fill(frame_1,[9,9],[12,12],snow)
im_fill(frame_1,[4,4],[13,13],snow)
im_fill(frame_1,[10,10],[15,15],snow)
im_fill(frame_1,[12,13],[4,6],pillow)
im_fill(frame_1,[19,19],[2,13],floor_shadow)   
im_show(frame_1)
frame_2=[[background]*total_columns for row in range(total_rows)]
im_fill(frame_2,[18,19],[0,19],floor)
im_fill(frame_2,[9,19],[1,1],bed_frame)
im_fill(frame_2,[10,13],[3,3],bed_frame)
im_fill(frame_2,[17,18],[3,3],bed_frame)
im_fill(frame_2,[17,19],[14,14],bed_frame)
im_fill(frame_2,[16,18],[16,16],bed_frame)
im_fill(frame_2,[4,11],[5,5],window)
im_fill(frame_2,[4,11],[10,10],window)
im_fill(frame_2,[4,11],[16,16],window)
im_fill(frame_2,[11,11],[4,17],window)
im_fill(frame_2,[2,2],[4,17],bed_sheet)
im_fill(frame_2,[2,10],[4,4],bed_sheet)
im_fill(frame_2,[2,10],[17,17],bed_sheet)
im_fill(frame_2,[3,3],[5,16],bed_trim)
im_fill(frame_2,[4,10],[6,9],sky)
im_fill(frame_2,[4,10],[11,15],sky)
im_fill(frame_2,[14,15],[2,13],bed_sheet)
im_fill(frame_2,[14,14],[14,16],bed_sheet)
im_fill(frame_2,[16,16],[2,14],bed_trim)
im_fill(frame_2,[15,15],[14,16],bed_trim)
im_fill(frame_2,[4,4],[8,8],snow)
im_fill(frame_2,[5,5],[8,8],snow)
im_fill(frame_2,[9,9],[7,7],snow)
im_fill(frame_2,[6,6],[12,12],snow)
im_fill(frame_2,[4,4],[13,13],snow)
im_fill(frame_2,[10,10],[13,13],snow)
im_fill(frame_2,[12,13],[4,6],pillow)
im_fill(frame_2,[19,19],[2,13],floor_shadow)   
im_show(frame_2)

frame_list = [frame_0,frame_1,frame_2]
fps = 1
play_video = vid_show(frame_list,fps)