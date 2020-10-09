from scene_manager import *
#from AOLMEgame import *

scene = scene(60,60)

#Background
grass = sprite_part(40,20)
grass.fill_part([0,38],[1,18],"004d00")
grass.fill_part([0,38],[1,1],"001a00")
grass.fill_part([38,38],[1,18],"001a00")
grass.fill_part([0,38],[18,18],"001a00")

grass.fill_part([0,37],[2,4],"006600")
grass.fill_part([35,37],[2,17],"006600")
grass.fill_part([0,37],[15,17],"006600")
#grass.view_part()

arrow = sprite_part(60,60)
arrow.fill_part([5,49],[10,10],"000000")
arrow.fill_part([10,49],[50,50],"000000")
arrow.fill_part([50,50],[10,50],"000000")

arrow.fill_part([9,9],[48,52],"000000")
arrow.fill_part([8,8],[49,51],"000000")
arrow.fill_part([7,7],[50,50],"000000")

#Aolme's head
head = sprite_part(10,12)
head.fill_part([1,8],[0,0],"003340")
head.fill_part([1,8],[11,11],"003340")
head.fill_part([0,0],[1,10],"003340")
head.fill_part([9,9],[1,10],"003340")

head.fill_part([1,8],[1,1],"ff")
head.fill_part([1,8],[10,10],"ff")
head.fill_part([1,1],[1,10],"ff")
head.fill_part([8,8],[1,10],"ff")

head.fill_part([2,7],[2,2],"80")
head.fill_part([2,7],[9,9],"80")
head.fill_part([2,2],[2,9],"80")
head.fill_part([7,7],[2,9],"80")

head.fill_part([3,3],[3,8],"d9dcd9")
head.fill_part([6,6],[3,8],"d9dcd9")
head.fill_part([4,5],[5,7],"d9dcd9")

head.part[4,3] = "d9dcd9"
head.part[4,8] = "d9dcd9"
head.part[5,3] = "ffcbcb"
head.part[5,8] = "ffcbcb"
head.part[5,4] = "d9dcd9"
head.part[5,7] = "d9dcd9"
head.part[4,4] = "00"
head.part[4,7] = "00"
#head.view_part()

#Aolme's keyboard
keyboard = sprite_part(6,14)
keyboard.fill_part([0,0],[0,13],"00")
keyboard.fill_part([5,5],[0,13],"00")
keyboard.fill_part([0,5],[0,0],"00")
keyboard.fill_part([0,5],[13,13],"00")
keyboard.fill_part([4,4],[1,12],"d9dcd9")
keyboard.fill_part([1,3],[1,12],"ff")

keyboard.part[1][1] = "80"
keyboard.part[1][3] = "80"
keyboard.part[1][5] = "80"
keyboard.part[1][7] = "80"
keyboard.part[1][9] = "80"
keyboard.part[1][11] = "80"
keyboard.part[3][2] = "80"
keyboard.part[3][4] = "80"
keyboard.part[3][6] = "80"
keyboard.part[3][8] = "80"
keyboard.part[3][10] = "80"
keyboard.part[3][12] = "80"
#keyboard.view_part()

#left arm
left_arm = sprite_part(6,5)
left_arm.fill_part([2,4],[0,0],"07637e")
left_arm.part[2][1] = "07637e"
left_arm.part[1][1] = "07637e"
left_arm.part[0][2] = "07637e"
left_arm.part[4][1] = "07637e"
left_arm.part[1][2] = "07637e"
left_arm.part[5][1] = "07637e"
left_arm.part[5][2] = "07637e"

left_arm.part[2][2] = "02485b"
left_arm.part[3][1] = "02485b"
left_arm.part[4][2] = "02485b"

left_arm.part[4][3] = "b4efff"
left_arm.part[5][3] = "b4efff"
left_arm.part[5][4] = "b4efff"
#left_arm.view_part()

#Right arm
right_arm = sprite_part(7,3)
right_arm.fill_part([4,5],[0,1],"07637e")
right_arm.fill_part([2,5],[1,1],"07637e")

right_arm.fill_part([2,5],[2,2],"02485b")
right_arm.fill_part([6,6],[0,1],"02485b")

right_arm.part[1][1] = "b4efff"
right_arm.part[1][2] = "b4efff"
right_arm.part[0][2] = "b4efff"
#right_arm.view_part()

#legs
legs = sprite_part(3,8)
legs.fill_part([0,2],[0,2],"00")
legs.fill_part([0,2],[5,7],"00")
#legs.view_part()

aolme = sprite(19,19)
aolme.add_part(head,[0,4])
aolme.add_part(keyboard,[10,3])
aolme.add_part(left_arm,[10,0])
aolme.add_part(right_arm,[6,16])
aolme.add_part(legs,[16,6])
aolme.set_name = 'aolme'

#aolme.view_sprite()

grass_sprite = sprite(40,20)
grass_sprite.add_part(grass,[0,0])
grass_sprite.set_name = 'grass'
#grass_sprite.view_sprite()

arrow_sprite = sprite(60,60)
arrow_sprite.add_part(arrow,[0,0])
arrow_sprite.set_name = 'arrow'

scene.add_sprite(grass_sprite,[0,20])
scene.add_sprite(arrow_sprite,[0,0])
scene.add_sprite(aolme,[1,1])
