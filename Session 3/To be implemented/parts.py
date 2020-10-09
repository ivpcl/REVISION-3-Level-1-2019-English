from sAOLME import *
'''
This class simply creates a part of a sprite and allows it to be placed on a sprite map.
'''

class sprite_part(object):
    def __init__(self,rows,cols):  
        self.row_count = cols
        self.col_count = rows
        self.pic =  np.array([[None for col in range(cols)] for row in range(rows)])
        self.x_loc = 0
        self.y_loc = 0

    @property
    def part(self):
        return self.pic
        
    @part.setter
    def set_part(self, value):
        '''
        Allow storing into class
        
        '''
        self.pic = value

    @part.deleter
    def del_part(self):
        print ("Instance Terminated")
        del self.pic   
         
    def fill_part(self,rng_cols,rng_rows,val):
        nrows_portion = rng_rows[1] - rng_rows[0]
        ncols_portion = rng_cols[1] - rng_cols[0]
    
        if (nrows_portion < 0) or (ncols_portion < 0):
            print ('( getportion) Error: Wrong range declaration!');    
            return None;
    
        if (rng_rows[1] > self.row_count) or (rng_cols[1] > self.col_count):
            print ('( getportion) Error: Index out of range!')
            print (rng_rows[1], self.row_count)
            print (rng_cols[1])  
            return None;
    
        if nrows_portion == 0:
            for i in range(rng_cols[0],rng_cols[1]+1):
                self.pic[i][rng_rows[0]] = val
        elif ncols_portion == 0:
            for i in range(rng_rows[0],rng_rows[1]+1):
                self.pic[rng_cols[0]][i] = val
        elif nrows_portion == 0 and ncols_portion == 0:
                self.pic[rng_cols[0]][rng_rows[0]] = val
        else:   
            for i in range(rng_rows[0], rng_rows[1]+1):
                for j in range(rng_cols[0], rng_cols[1]+1):
                    self.pic[j][i] = val
                    
        #self.pic[rng_cols[0]:rng_cols[1]][rng_rows[0]:rng_rows[1]] = val
    
    
    def place_on_frame(self,frame_name,loc):
        self.x_loc = loc[1]
        self.y_loc = loc[0]
        for i in range(0,self.col_count):
                #if i <= frame_name.shape[1]:
                    for j in range(self.row_count):
                        #if j <= frame_name.shape[0]:
                            if self.pic[i][j] != None:
                                frame_name[loc[0]+i][loc[1]+j] = self.pic[i][j]
        return frame_name
        
    def view_part(self):
        #change None to 1's and display
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.pic[i][j] == None:
                    self.pic[i][j] = "FF"
        im_show(self.pic)