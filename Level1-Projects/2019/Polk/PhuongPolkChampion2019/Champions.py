from AOLME import *
import sys

# Define the image size:
rows = 20
cols = 20

# Define the colors:
naranja= "ff8000"
griz= "808080"
negro= "1a1a00"
rojo = "e63900"
azul = "1a75ff"
verde = "00ff00"
blanco= "ffffff"
amarillo= "ffd700"
cafe= "8a6029"
# Initialize the background
backg = np.array([[negro]*cols for row in range (rows)])
#FRAME 0
# Copy the background into a frame:
frame0 = backg.copy()



# crear tus peronajes
#La ventana
im_fill(frame0,[1,1],[10,10], blanco)
im_fill(frame0,[2,2],[4,4], blanco)
im_fill(frame0,[2,2],[15,15],blanco)
im_fill(frame0,[4,4],[10,10],blanco)
im_fill(frame0,[4,4],[18,18],blanco)
im_fill(frame0,[5,5],[12,12], blanco)
im_fill(frame0,[5,5],[15,15], blanco)
im_fill(frame0,[6,6],[6,6], blanco)
im_fill(frame0,[9,9],[6,6], blanco)
im_fill(frame0,[9,9],[13,13], blanco)
im_fill(frame0,[9,9],[19,19], blanco)
im_fill(frame0,[11,11],[1,1], blanco)
im_fill(frame0,[11,11],[10,10], blanco)
im_fill(frame0,[15,15],[10,10], blanco)
# arbol
im_fill(frame0,[19,19],[4,6],cafe )
im_fill(frame0,[14,19],[5,5],cafe )
im_fill(frame0,[13,13],[2,8],verde )
im_fill(frame0,[12,12],[3,7],verde )
im_fill(frame0,[11,11],[4,6],verde )
im_fill(frame0,[10,10],[5,5],verde )

# granja
im_fill(frame0,[10,10],[16,17],rojo)
im_fill(frame0,[11,11],[15,18],rojo)
im_fill(frame0,[12,12],[15,18],rojo)
im_fill(frame0,[13,13],[15,18],rojo)

#el terreno
im_fill(frame0,[14,14],[14,19], cafe)
im_fill(frame0,[15,15],[13,19],cafe) 
im_fill(frame0,[16,16],[13,19],cafe) 
im_fill(frame0,[17,17],[13,19],cafe)
im_fill(frame0,[18,18],[13,19],cafe)
im_fill(frame0,[19,19],[13,19],cafe)

# Papa
im_fill(frame0,[11,12],[2,2],naranja)
im_fill(frame0,[16,16],[0,1], amarillo)
im_fill(frame0,[16,16],[6,6],naranja)
im_fill(frame0,[18,19],[2,2],amarillo)
im_fill(frame0,[18,19],[8,8],naranja)
im_fill(frame0,[19,19],[10,11], amarillo)

#FRAME 1
frame1 = backg.copy()
#la ventana
im_fill(frame1,[0,8],[6,10],rojo )
im_fill(frame1,[0,8],[12,14],rojo)
im_fill(frame1,[0,8],[1,4],rojo)
im_fill(frame1,[0,8],[16,18],rojo)
im_fill(frame1,[0,8],[5,5],griz)
im_fill(frame1,[0,8],[11,11],griz)
im_fill(frame1,[0,8],[15,15],griz)
im_fill(frame1,[8,8],[1,18],griz)

#el fondo
im_fill(frame1,[9,18],[1,18],rojo )
im_fill(frame1,[9,18],[10,10],azul )


#FRAME 2
# Copy the background into a frame:
frame2 = backg.copy()

# crear tus peronajes
#La ventana
im_fill(frame2,[0,8],[1,17], rojo)
im_fill(frame2,[0,8],[4,4], griz)
im_fill(frame2,[0,8],[10,10],griz)
im_fill(frame2,[0,8],[14,14],griz)
im_fill(frame2,[0,8],[18,18],rojo)
im_fill(frame2,[8,8],[1,18], griz)
#la granja
im_fill(frame2,[9,18],[1,18],rojo )


# la fondo de garage 
im_fill(frame2,[9,18],[8,9],azul)
im_fill(frame2,[9,9],[12,18],rojo)
im_fill(frame2,[9,9],[9,9],azul)
im_fill(frame2,[12,12],[9,9],azul)
im_fill(frame2,[12,12],[9,9],azul)

#el alienigena
im_fill(frame2,[9,18],[9,12], verde)
im_fill(frame2,[10,10],[11,11],azul) # le ojo del alienigena
im_fill(frame2,[10,11],[8,9],verde) 
im_fill(frame2,[13,15],[8,9],verde)

#FRAME 3
# Copy the background into a frame:
    
frame3 = backg.copy()

#La ventana
im_fill(frame3,[0,8],[1,17], rojo)
im_fill(frame3,[0,8],[4,4], griz)
im_fill(frame3,[0,8],[10,10],griz)
im_fill(frame3,[0,8],[14,14],griz)
im_fill(frame3,[0,8],[18,18],rojo)
im_fill(frame3,[8,8],[1,18], griz)

 # la granja   
im_fill(frame3,[9,18],[1,18],rojo)
    
 # fondo de garage
im_fill(frame3,[9,9],[9,9],azul)
im_fill(frame3,[9,18],[6,8],azul)
im_fill(frame3,[16,18],[9,9],azul)
im_fill(frame3,[9,9],[6,8],azul)
im_fill(frame3,[12,12],[9,9],azul)

#el nave
im_fill(frame3,[12,12],[6,6],griz)

 #el alienigena
im_fill(frame3,[9,18],[9,12],verde )
im_fill(frame3,[10,10],[11,11],azul) # le ojo del alienigena
im_fill(frame3,[10,11],[8,9],verde) 
im_fill(frame3,[13,15],[8,9],verde)

#FRAME 4
# Copy the background into a frame:
frame4 = backg.copy()

# crear tus peronajes
#La ventana
im_fill(frame4,[0,8],[1,17], rojo)
im_fill(frame4,[0,8],[4,4], griz)
im_fill(frame4,[0,8],[10,10],griz)
im_fill(frame4,[0,8],[14,14],griz)
im_fill(frame4,[0,8],[18,18],rojo)
im_fill(frame4,[8,8],[1,18], griz)
#la granja
im_fill(frame4,[9,18],[1,18],rojo )


# la fondo de garage 
im_fill(frame4,[9,9],[5,9],azul)
im_fill(frame4,[12,12],[9,9],azul)
im_fill(frame4,[16,18],[9,9],azul)
im_fill(frame4,[9,18],[5,8],azul)


#el nave
im_fill(frame4,[12,12],[6,6],griz)
im_fill(frame4,[11,13],[5,5],griz)

#el alienigena
im_fill(frame4,[9,18],[9,12], verde)
im_fill(frame4,[10,10],[11,11],azul) # el ojo del alienigena
im_fill(frame4,[10,11],[8,9],verde) 
im_fill(frame4,[13,15],[8,9],verde)
im_fill(frame4,[10,10],[13,13],negro) #el ojo del alienigena
im_fill(frame4,[9,18],[10,14],verde) 
im_fill(frame4,[10,10],[11,11],azul) # el ojo del alienigena
im_fill(frame4,[10,10],[13,13],negro) #el ojo del alienigena

#FRAME 5
# Copy the background into a frame:
frame5 = backg.copy()

# First box by Vj
im_fill(frame5,[0,8],[1,4], rojo)

# Victor
#la ventana
im_fill(frame5,[0,8],[6,10],rojo )
im_fill(frame5,[0,8],[12,14],rojo)
im_fill(frame5,[0,8],[16,18],rojo)
im_fill(frame5,[0,8],[5,5],griz)
im_fill(frame5,[0,8],[11,11],griz)
im_fill(frame5,[0,8],[15,15],griz)
im_fill(frame5,[8,8],[1,18],griz)

#el alienigena
im_fill(frame5,[9,18],[10,15],verde)
im_fill(frame5,[10,11],[9,9],verde)
im_fill(frame5,[13,15],[9,9],verde)
im_fill(frame5,[10,11],[16,16],verde)
im_fill(frame5,[13,15],[16,16],verde)

#el fondo
im_fill(frame5,[9,9],[9,9],azul)
im_fill(frame5,[9,18],[1,8],azul)
im_fill(frame5,[9,18],[17,18],azul)
im_fill(frame5,[9,9],[16,16],azul)
im_fill(frame5,[12,12],[16,16],azul)
im_fill(frame5,[16,18],[16,16],azul)
im_fill(frame5,[12,12],[9,9],azul)
im_fill(frame5,[16,18],[9,9],azul)

#el nave
im_fill(frame5,[11,12],[1,5],griz)
im_fill(frame5,[13,13],[2,5],griz)
im_fill(frame5,[14,14],[3,4],griz)
im_fill(frame5,[12,12],[6,6],griz)
#los ojos
frame5[10,11] = azul
frame5[10,13] = negro


#FRAME 6
frame6 = backg.copy()

#el fondo
im_fill(frame6,[1,10],[0,19],azul)
im_fill(frame6,[0,0],[0,19],negro)


#POTATO WORD
#P
im_fill(frame6,[2,3],[0,1],naranja)
im_fill(frame6,[4,4],[0,0],naranja)

#0
im_fill(frame6,[2,4],[3,4],amarillo)

## T
im_fill(frame6,[2,2],[6,8],naranja)
im_fill(frame6,[3,4],[7,7],naranja)
im_fill(frame6,[3,4],[7,7],naranja)

#A
im_fill(frame6,[3,4],[10,10],amarillo)

im_fill(frame6,[2,2],[11,11],amarillo)

im_fill(frame6,[3,4],[12,12],amarillo)

im_fill(frame6,[3,3],[11,11],amarillo)
#T
im_fill(frame6,[2,2],[16,16],naranja)

im_fill(frame6,[2,2],[15,15],naranja)

im_fill(frame6,[2,2],[14,14],naranja)

im_fill(frame6,[3,4],[15,15],naranja)
#O
im_fill(frame6,[2,4],[18,19],amarillo)

#CONERS
#C
im_fill(frame6,[7,9],[0,0],naranja)
im_fill(frame6,[7,7],[0,1],naranja)
im_fill(frame6,[9,9],[0,1],naranja)

#O
im_fill(frame6,[7,9],[3,4],amarillo)

#R
im_fill(frame6,[7,9],[6,6],naranja)
im_fill(frame6,[7,7],[7,7],naranja)

#N

im_fill(frame6,[7,9],[9,9],amarillo)

im_fill(frame6,[7,7],[10,10],amarillo)

im_fill(frame6,[7,7],[11,11],amarillo)

im_fill(frame6,[8,9],[11,11],amarillo)

#E
im_fill(frame6,[5,9],[13,13],naranja)

im_fill(frame6,[5,5],[14,14],naranja)

im_fill(frame6,[5,5],[15,15],naranja)

im_fill(frame6,[7,7],[14,15],naranja)

im_fill(frame6,[9,9],[14,15],naranja)
#r
im_fill(frame6,[7,9],[18,18],naranja)

im_fill(frame6,[7,7],[19,19],naranja)


#EL ALIEN
im_fill(frame6,[11,11],[1,6],verde)
im_fill(frame6,[12,13],[0,7],verde)
im_fill(frame6,[14,14],[1,6],verde)

im_fill(frame6,[15,17],[0,7],verde)
im_fill(frame6,[18,19],[1,6],verde)

im_fill(frame6,[12,12],[2,2],azul)
im_fill(frame6,[12,12],[4,4],negro)

#el fondo    
im_fill(frame6,[11,19],[8,19],negro)
im_fill(frame6,[11,11],[7,7],negro)
im_fill(frame6,[18,19],[7,7],negro)
im_fill(frame6,[14,14],[7,7],negro)
    
#papa 1
im_fill(frame6,[14,14],[9,10],naranja)


#papa 2
im_fill(frame6,[16,16],[12,13],amarillo)

#papa 3
im_fill(frame6,[16,17],[15,15],naranja)

#papa 4
im_fill(frame6,[13,13],[14,14],naranja)
im_fill(frame6,[12,12],[14,14],amarillo)
im_fill(frame6,[13,13],[15,15],amarillo)
im_fill(frame6,[13,13],[16,16],naranja)
im_fill(frame6,[13,13],[17,17],amarillo)
im_fill(frame6,[13,13],[18,18],naranja)
im_fill(frame6,[12,12],[18,18],amarillo)





# Create a frame list of all of the frames
frame_list = [frame0,frame1,frame2,frame3,frame4,frame5,frame6]

# Setup the number of frames per second
fps= 2  

# Play the video
play_video= vid_show(frame_list, fps)
