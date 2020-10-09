from sprites import *

class scene(object):
    def __init__(self,size_x,size_y):
        self.pic =  np.array([["ffffff" for col in range(size_y)] for row in range(size_x)])
        self.x = size_x
        self.y = size_y
        self.sprites = []
        self.frames = []
        
    def add_sprite(self,sprite,loc):
        self.sprites.append({"sprite":sprite, "loc":loc})
        #keep location of all sprites in scene
            
        #if one moves, redraw everything 
        #wait between moves to draw another move
        
    def move_sprite_left(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] -= 1
        self.print_scene()
        
    def move_sprite_right(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] += 1
        self.print_scene()
        
    def move_sprite_up(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] -= 1
        self.print_scene()
        
    def move_sprite_down(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] += 1
        self.print_scene()
 
    def block_move_sprite_left(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] -= self.sprites[idx]['sprite'].full_sprite.shape[0]
        self.print_scene()
        
    def block_move_sprite_right(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] += self.sprites[idx]['sprite'].full_sprite.shape[0]
        self.print_scene()
        
    def block_move_sprite_up(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] -= self.sprites[idx]['sprite'].full_sprite.shape[0]
        self.print_scene()
        
    def block_move_sprite_down(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] += self.sprites[idx]['sprite'].full_sprite.shape[0]
        self.print_scene()
                
    def by_five_move_sprite_right(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] += 5
        self.print_scene()   
                
    def by_five_move_sprite_left(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][1] -= 5
        self.print_scene()
    
    def by_five_move_sprite_up(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] -= 5
        self.print_scene()
        
    def by_five_move_sprite_down(self,which):
        [idx] = [i for i, t in enumerate(self.sprites) if t['sprite'].sprite_name==which]
        self.sprites[idx]['loc'][0] += 5
        self.print_scene()
        
    def clear_scene(self):
        self.pic =  np.array([["ffffff" for col in range(self.y)] for row in range(self.x)])
        
    def print_scene(self):
        self.clear_scene()
        for sprite in self.sprites:
            sprite['sprite'].place_on_frame(self.pic,sprite['loc'])
        self.frames.append(self.pic)
        #im_show(self.pic)
        
        #to play the video, add frames one by one after moving an object to a list
    def play_game(self):
        return vid_show(self.frames,4)
