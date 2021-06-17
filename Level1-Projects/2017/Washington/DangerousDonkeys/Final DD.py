from AOLME import *
total_columns = 20
total_rows = 20

background = [["7FC3FF"]*total_columns for rows in range(total_rows)]
background2 = [["7FC3FF"]*total_columns for rows in range(total_rows)]
background3  = [["7FC3FF"]*total_columns for rows in range(total_rows)]
background4  = [["7FC3FF"]*total_columns for rows in range(total_rows)]
background5  = [["353535"]*total_columns for rows in range(total_rows)]
background6  = [["353535"]*total_columns for rows in range(total_rows)]
background7  = [["FF7A2E"]*total_columns for rows in range(total_rows)]
background12  = [["FCAE80"]*total_columns for rows in range(total_rows)]
background13  = [["FCAE80"]*total_columns for rows in range(total_rows)]
background14  = [["FCAE80"]*total_columns for rows in range(total_rows)]
background9 = [["FF95D3"]*total_columns for rows in range(total_rows)]
background10 = [["FF95D3"]*total_columns for rows in range(total_rows)]
background11 = [["FFFFFF"]*total_columns for rows in range(total_rows)]

#frame1
#grass
im_fill(background,[18,19],[0,19],"91FF1D")
#sun
im_fill(background,[0,0],[15,19],"FFA800")
im_fill(background,[1,1],[16,19],"FFA800")
im_fill(background,[2,2],[17,19],"FFA800")
im_fill(background,[3,3],[18,19],"FFA800")
im_fill(background,[4,4],[19,19],"FFA800")
#ear
im_fill(background,[12,12],[5,5],"000000")
#donkey
im_fill(background,[13,13],[3,4],"676767")
im_fill(background,[14,14],[2,4],"676767")
#tail
im_fill(background,[14,14],[7,7],"000000")
#donkey
im_fill(background,[15,15],[4,6],"676767")
im_fill(background,[16,16],[4,4],"676767")
im_fill(background,[16,16],[6,6],"676767")
#feet
im_fill(background,[17,17],[6,6],"000000")
im_fill(background,[17,17],[4,4],"000000")


im_show(background)
#frame2
#grass
im_fill(background3,[18,19],[0,19],"91FF1D")
#sun
im_fill(background3,[0,0],[15,19],"FFA800")
im_fill(background3,[1,1],[16,19],"FFA800")
im_fill(background3,[2,2],[17,19],"FFA800")
im_fill(background3,[3,3],[18,19],"FFA800")
im_fill(background3,[4,4],[19,19],"FFA800")
#ear
im_fill(background3,[14,14],[0,0],"000000")
#donkey
im_fill(background3,[15,15],[1,2],"676767")
im_fill(background3,[16,16],[0,2],"676767")
im_fill(background3,[15,15],[3,3],"676767")
#hair
im_fill(background3,[14,14],[2,3],"A8A8A8")
#tail
im_fill(background3,[14,14],[7,7],"000000")
#legs
im_fill(background3,[15,15],[4,6],"676767")
im_fill(background3,[16,16],[4,4],"676767")
im_fill(background3,[16,16],[6,6],"676767")
#feet
im_fill(background3,[17,17],[6,6],"000000")
im_fill(background3,[17,17],[4,4],"000000")


im_show(background3)
#frame3
#grass
im_fill(background2,[18,19],[0,19],"91FF1D")
#sun
im_fill(background2,[0,0],[15,19],"FFA800")
im_fill(background2,[1,1],[16,19],"FFA800")
im_fill(background2,[2,2],[17,19],"FFA800")
im_fill(background2,[3,3],[18,19],"FFA800")
im_fill(background2,[4,4],[19,19],"FFA800")
#ear
im_fill(background2,[14,14],[0,0],"000000")
#donkey
im_fill(background2,[15,16],[1,1],"676767")
im_fill(background2,[15,17],[2,2],"676767")
im_fill(background2,[15,15],[3,3],"676767")
#hair
im_fill(background2,[14,14],[2,3],"A8A8A8")
#tail
im_fill(background2,[14,14],[7,7],"000000")
#legs
im_fill(background2,[15,15],[4,6],"676767")
im_fill(background2,[16,16],[4,4],"676767")
im_fill(background2,[16,16],[6,6],"676767")
#feet
im_fill(background2,[17,17],[6,6],"000000")
im_fill(background2,[17,17],[4,4],"000000")
#Dopeasscloud
im_fill(background2,[5,6],[12,18],"C1C1C1")
im_fill(background2,[3,4],[14,16],"C1C1C1")
im_fill(background2,[4,4],[17,17],"C1C1C1")
im_fill(background2,[6,6],[19,19],"C1C1C1")
im_fill(background2,[7,7],[15,18],"C1C1C1")
im_show(background2)

#frame4
#grass
im_fill(background4,[18,19],[0,19],"91FF1D")
#sun
im_fill(background4,[0,0],[15,19],"FFA800")
im_fill(background4,[1,1],[16,19],"FFA800")
im_fill(background4,[2,2],[17,19],"FFA800")
im_fill(background4,[3,3],[18,19],"FFA800")
im_fill(background4,[4,4],[19,19],"FFA800")
#ear
im_fill(background4,[14,14],[0,0],"000000") 
#donkey
im_fill(background4,[15,16],[1,1],"676767")
im_fill(background4,[15,17],[2,2],"676767")
im_fill(background4,[15,15],[3,3],"676767")
#hair
im_fill(background4,[14,14],[2,3],"A8A8A8")
#tail
im_fill(background4,[14,14],[7,7],"000000")
#legs
im_fill(background4,[15,15],[4,6],"676767")
im_fill(background4,[16,16],[4,4],"676767")
im_fill(background4,[16,16],[6,6],"676767")
#feet
im_fill(background4,[17,17],[6,6],"000000")
im_fill(background4,[17,17],[4,4],"000000")
#Dopeasscloud
im_fill(background4,[5,6],[7,13],"C1C1C1")
im_fill(background4,[3,4],[9,11],"C1C1C1")
im_fill(background4,[4,4],[12,12],"C1C1C1")
im_fill(background4,[6,6],[14,14],"C1C1C1")
im_fill(background4,[7,7],[10,13],"C1C1C1")
#frame5
#grass
im_fill(background5,[18,19],[0,19],"91FF1D")
#sun
im_fill(background5,[0,0],[15,19],"FFA800")
im_fill(background5,[1,1],[16,19],"FFA800")
im_fill(background5,[2,2],[17,19],"FFA800")
im_fill(background5,[3,3],[18,19],"FFA800")
im_fill(background5,[4,4],[19,19],"FFA800")
#ear
im_fill(background5,[14,14],[0,0],"000000")
#donkey
im_fill(background5,[15,16],[1,1],"676767")
im_fill(background5,[15,17],[2,2],"676767")
im_fill(background5,[15,15],[3,3],"676767")
#hair
im_fill(background5,[14,14],[2,3],"A8A8A8")
#tail
im_fill(background5,[14,14],[7,7],"000000")
#legs
im_fill(background5,[15,15],[4,6],"676767")
im_fill(background5,[16,16],[4,4],"676767")
im_fill(background5,[16,16],[6,6],"676767")
#feet
im_fill(background5,[17,17],[6,6],"000000")
im_fill(background5,[17,17],[4,4],"000000")
#Dopeasscloud
im_fill(background5,[5,6],[7,13],"C1C1C1")
im_fill(background5,[3,4],[9,11],"C1C1C1")
im_fill(background5,[4,4],[12,12],"C1C1C1")
im_fill(background5,[6,6],[14,14],"C1C1C1")
im_fill(background5,[7,7],[10,13],"C1C1C1")
#lightning bolt
im_fill(background5,[2,2],[9,9],"FFFF8D")
im_fill(background5,[3,3],[8,8],"FFFF8D")
im_fill(background5,[4,4],[7,7],"FFFF8D")
im_fill(background5,[5,5],[6,6],"FFFF8D")
im_fill(background5,[6,6],[7,7],"FFFF8D")
im_fill(background5,[7,7],[8,8],"FFFF8D")
im_fill(background5,[8,8],[9,9],"FFFF8D")
im_fill(background5,[9,9],[10,10],"FFFF8D")
im_fill(background5,[10,10],[9,9],"FFFF8D")
im_fill(background5,[11,11],[8,8],"FFFF8D")
im_fill(background5,[12,12],[7,7],"FFFF8D")
im_fill(background5,[13,13],[6,6],"FFFF8D")
im_fill(background5,[14,14],[5,5],"FFFF8D")
#acidrain
im_fill(background5,[7,7],[2,2],"00FF00")
im_fill(background5,[12,12],[2,2],"00FF00")
im_fill(background5,[4,4],[12,12],"00FF00")
im_fill(background5,[14,14],[12,12],"00FF00")
im_fill(background5,[7,7],[14,14],"00FF00")
#frame6
#grass
im_fill(background6,[18,19],[0,19],"91FF1D")
#ear
im_fill(background6,[14,14],[0,0],"000000")
#donkey
im_fill(background6,[15,16],[1,1],"676767")
im_fill(background6,[15,17],[2,2],"676767")
im_fill(background6,[15,15],[3,3],"676767")
#hair
im_fill(background6,[14,14],[2,3],"A8A8A8")
#tail
im_fill(background6,[14,14],[7,7],"000000")
#legs
im_fill(background6,[15,15],[4,6],"676767")
im_fill(background6,[16,16],[4,4],"676767")
im_fill(background6,[16,16],[6,6],"676767")
#feet
im_fill(background6,[17,17],[6,6],"000000")
im_fill(background6,[17,17],[4,4],"000000")
#Dopeasscloud
im_fill(background6,[5,6],[7,13],"C1C1C1")
im_fill(background6,[3,4],[9,11],"C1C1C1")
im_fill(background6,[4,4],[12,12],"C1C1C1")
im_fill(background6,[6,6],[14,14],"C1C1C1")
im_fill(background6,[7,7],[10,13],"C1C1C1")
#lightning bolt
im_fill(background6,[2,2],[9,9],"FFFF8D")
im_fill(background6,[3,3],[8,8],"FFFF8D")
im_fill(background6,[4,4],[7,7],"FFFF8D")
im_fill(background6,[5,5],[6,6],"FFFF8D")
im_fill(background6,[6,6],[7,7],"FFFF8D")
im_fill(background6,[7,7],[8,8],"FFFF8D")
im_fill(background6,[8,8],[9,9],"FFFF8D")
im_fill(background6,[9,9],[10,10],"FFFF8D")
im_fill(background6,[10,10],[9,9],"FFFF8D")
im_fill(background6,[11,11],[8,8],"FFFF8D")
im_fill(background6,[12,12],[7,7],"FFFF8D")
im_fill(background6,[13,13],[6,6],"FFFF8D")
im_fill(background6,[14,14],[5,5],"FFFF8D")
#acidrain
im_fill(background6,[1,1],[2,2],"00FF00")
im_fill(background6,[13,13],[2,2],"00FF00")
im_fill(background6,[8,8],[12,12],"00FF00")
im_fill(background6,[3,3],[12,12],"00FF00")
im_fill(background6,[9,9],[14,14],"00FF00")

im_show(background6)
#frame7

#grass
im_fill(background7,[18,19],[0,19],"91FF1D")

#Donkey
im_fill(background7,[13,14],[3,4],"7B6E6E")
im_fill(background7,[14,14],[10,10],"7B6E6E")
im_fill(background7,[15,15],[2,3],"7B6E6E")
im_fill(background7,[15,15],[9,9],"7B6E6E")
im_fill(background7,[16,16],[1,8],"7B6E6E")
im_fill(background7,[17,17],[2,3],"7B6E6E")
im_fill(background7,[17,17],[7,9],"7B6E6E")
im_fill(background7,[18,18],[2,2],"7B6E6E")
im_fill(background7,[18,18],[4,5],"7B6E6E")
im_fill(background7,[18,18],[7,9],"7B6E6E")

#nose
im_fill(background7,[12,12],[4,5],"B67E7E")
im_fill(background7,[13,13],[5,5],"B67E7E")
#belly
im_fill(background7,[17,17],[4,6],"E1BABA")
#ear
im_fill(background7,[12,12],[2,2],"301A1A")
#tail
im_fill(background7,[13,13],[10,10],"301A1A")
#feet
im_fill(background7,[17,17],[0,0],"301A1A")
im_fill(background7,[19,19],[1,1],"301A1A")
im_fill(background7,[19,19],[5,5],"301A1A")
im_fill(background7,[19,19],[9,9],"301A1A")

im_show(background7)

#frame9
#ground
im_fill(background9,[16,19],[0,19],"E1BABA")

#heartcloud
im_fill(background9,[2,2],[14,15],"FFDAF6")
im_fill(background9,[2,2],[17,18],"FFDAF6")
im_fill(background9,[3,3],[14,18],"FFDAF6")
im_fill(background9,[4,4],[15,17],"FFDAF6")
im_fill(background9,[5,5],[16,16],"FFDAF6")
im_fill(background9,[7,7],[10,11],"FFDAF6")
im_fill(background9,[7,7],[13,14],"FFDAF6")
im_fill(background9,[8,8],[10,14],"FFDAF6")
im_fill(background9,[9,9],[11,13],"FFDAF6")
im_fill(background9,[10,10],[12,12],"FFDAF6")
#ear
im_fill(background9,[12,12],[5,5],"000000")
#donkey
im_fill(background9,[13,13],[3,4],"676767")
im_fill(background9,[14,14],[2,4],"676767")
#tail
im_fill(background9,[14,14],[7,7],"000000")

#donkey
im_fill(background9,[15,15],[4,6],"676767")
im_fill(background9,[16,16],[4,4],"676767")
im_fill(background9,[16,16],[6,6],"676767")
#feet
im_fill(background9,[17,17],[6,6],"000000")
im_fill(background9,[17,17],[4,4],"000000")

im_show(background9)

#frame10
#heartclouds
im_fill(background10,[4,4],[2,3],"FFDAF6")
im_fill(background10,[4,4],[5,6],"FFDAF6")
im_fill(background10,[5,5],[2,6],"FFDAF6")
im_fill(background10,[6,6],[3,5],"FFDAF6")
im_fill(background10,[7,7],[4,4],"FFDAF6")
im_fill(background10,[2,2],[12,13],"FFDAF6")
im_fill(background10,[2,2],[15,16],"FFDAF6")
im_fill(background10,[3,3],[12,16],"FFDAF6")
im_fill(background10,[4,4],[13,15],"FFDAF6")
im_fill(background10,[5,5],[14,14],"FFDAF6")
#ear
im_fill(background10,[8,8],[1,1],"000000")
#wife
im_fill(background10,[9,9],[2,3],"CCC7C7")
im_fill(background10,[10,10],[2,4],"CCC7C7")
im_fill(background10,[11,11],[0,1],"CCC7C7")
im_fill(background10,[12,12],[1,1],"000000")
#ear
im_fill(background10,[8,8],[8,8],"000000")
#husband
im_fill(background10,[9,9],[6,7],"676767")
im_fill(background10,[10,10],[5,7],"676767")
im_fill(background10,[11,11],[8,10],"676767")
im_fill(background10,[12,12],[8,8],"000000")
im_fill(background10,[12,12],[10,10],"000000")
im_fill(background10,[10,10],[11,11],"000000")
#ground
im_fill(background10,[13,19],[0,19],"E1BABA")
#tail
im_fill(background10,[10,10],[13,13],"000000")
#ear
im_fill(background10,[9,9],[15,15],"000000")
#baby
im_fill(background10,[11,11],[13,18],"CEC8C8")
im_fill(background10,[10,10],[16,17],"CEC8C8")
im_fill(background10,[12,12],[13,13],"000000")
im_fill(background10,[12,12],[15,15],"000000")

im_show(background10)

#frame11
#pinkD
im_fill(background11,[3,3],[2,6],"FF95D3")
im_fill(background11,[3,10],[2,2],"FF95D3")
im_fill(background11,[4,4],[7,7],"FF95D3")
im_fill(background11,[5,8],[8,8],"FF95D3")
im_fill(background11,[9,9],[7,7],"FF95D3")
im_fill(background11,[10,10],[2,6],"FF95D3")
#orangeD
im_fill(background11,[11,11],[10,14],"FCAE80")
im_fill(background11,[11,18],[10,10],"FCAE80")
im_fill(background11,[12,12],[14,14],"FCAE80")
im_fill(background11,[13,16],[15,15],"FCAE80")
im_fill(background11,[17,17],[14,14],"FCAE80")
im_fill(background11,[18,18],[10,13],"FCAE80")

#frame12
#ground
im_fill(background12,[18,19],[0,19],"E1BABA")
#donkey
im_fill(background12,[9,9],[4,4],"301A1A")
im_fill(background12,[9,9],[6,7],"B6787E")
im_fill(background12,[10,10],[7,7],"B6787E")
im_fill(background12,[10,11],[5,6],"7B6E6E")
im_fill(background12,[12,12],[3,5],"7B6E6E")
im_fill(background12,[13,13],[2,6],"7B6E6E")
im_fill(background12,[14,14],[2,4],"7B6E6E")
im_fill(background12,[14,14],[6,6],"301A1A")
im_fill(background12,[15,16],[1,2],"7B6E6E")
im_fill(background12,[16,16],[4,5],"7B6E6E")
im_fill(background12,[16,16],[6,6],"301A1A")
im_fill(background12,[17,17],[2,5],"7B6E6E")
im_fill(background12,[18,18],[2,4],"7B6E6E")
im_fill(background12,[19,19],[5,6],"7B6E6E")
im_fill(background12,[18,18],[7,7],"301A1A")
im_fill(background12,[15,16],[3,3],"E1BABA")

im_show(background12)

#frame13
im_fill(background13,[12,13],[4,12],"7B6E6E")
im_fill(background13,[14,14],[3,6],"7B6E6E")
im_fill(background13,[14,15],[2,2],"7B6E6E")
im_fill(background13,[13,13],[3,3],"7B6E6E")
im_fill(background13,[11,11],[5,7],"7B6E6E")
im_fill(background13,[11,12],[10,11],"7B6E6E")
im_fill(background13,[13,13],[10,10],"7B6E6E")
im_fill(background13,[14,14],[11,11],"7B6E6E")
im_fill(background13,[15,15],[5,6],"7B6E6E")
im_fill(background13,[14,15],[9,9],"7B6E6E")
im_fill(background13,[11,11],[3,3],"7B6E6E")
im_fill(background13,[10,10],[2,2],"7B6E6E")
im_fill(background13,[9,9],[2,2],"301A1A")
im_fill(background13,[16,16],[2,2],"301A1A")
im_fill(background13,[16,16],[5,5],"301A1A")
im_fill(background13,[10,10],[9,9],"301A1A")
im_fill(background13,[16,16],[10,10],"301A1A")
im_fill(background13,[15,15],[12,12],"301A1A")
im_fill(background13,[13,13],[11,12],"E1BABA")
im_fill(background13,[12,12],[12,12],"E1BABA")
im_fill(background13,[13,13],[5,8],"B67E7E")

im_show(background13)

#frame14
im_fill(background14,[13,13],[11,11],"301A1A")
im_fill(background14,[14,15],[10,10],"7B6E6E")
im_fill(background14,[14,14],[16,16],"301A1A")
im_fill(background14,[15,15],[17,18],"7B6E6E")
im_fill(background14,[16,16],[11,18],"7B6E6E")
im_fill(background14,[16,16],[19,19],"B6787E")
im_fill(background14,[17,18],[10,11],"7B6E6E")
im_fill(background14,[17,18],[15,15],"7B6E6E")
im_fill(background14,[18,18],[13,15],"7B6E6E")
im_fill(background14,[19,19],[9,9],"301A1A")
im_fill(background14,[17,17],[18,19],"B6787E")
im_fill(background14,[17,17],[12,14],"E1BABA")
im_fill(background14,[17,17],[16,16],"E1BABA")
im_fill(background14,[16,18],[15,15],"7B6E6E")
im_fill(background14,[19,19],[13,13],"301A1A")
im_fill(background14,[19,19],[15,15],"301A1A")
im_fill(background14,[19,19],[17,17],"301A1A")

im_show(background14)

frame_list=[background,background3,background2,background4,
            background5,background6,background7,background12,
            background13,background14,background9,background10,background11]
fps=1
play_video=vid_show(frame_list,fps)





