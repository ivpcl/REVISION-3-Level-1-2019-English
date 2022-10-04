#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:25:20 2022

@author: sherry
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:27:16 2022

@author: sherry
"""
import cv2
import os
import sys
import matplotlib.pyplot as pyplot
from matplotlib import animation as animation
import numpy as np
import re 
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from IPython.display import HTML
from base64 import b64encode
import os
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow


SAFE = True 
grid_lines = True

class Fraction():
    def __init__(self):
        #self.numerator_list   = []
        #self.denominator_list = []
        self.frame_list = []
        self.comment_list = []
        self.frame_array_list = []
        self.frame_comb_array_list = []
        self.white = "ffffff"
        self.color_dict = {"red":"ff0000",
                           "green":"00ff00",
                           "blue":"0000ff", 
                           "yellow":"ffff00",
                           "cyan":"00ffff",
                           "magenta":"ff00ff"}
        
        
    def AddFrac(self, numerator, 
                denominator, 
                aspect = 'None', 
                #fps = 1, 
                comment = ' '):
        
        if denominator == 0:
            print("Error: The denominator cannot be zero!")
            return 
        
        if aspect == 'None':
            aspect = 0.1*denominator
            
        if numerator == 0:
            # Create a frame with white background color
            frame = np.array([["ffffff"]*denominator for row in range (1)])
            # Video play
            #play_video= vid_show([frame], numerator, fps, comment, aspect) # play on screen
            #return play_video
        else:
            re = divmod(numerator, denominator)
            quo = re[0]
            rem = re[1]
        
            if rem == 0:
              rows = quo
            else:
              rows = quo + 1
            
            # Create a frame with white background color
            frame = np.array([["ffffff"]*denominator for row in range (rows)])
             
            if numerator<denominator:     
                # Fill the vector
                im_fill(frame, [0, 0], [0, numerator-1], self.color_dict.get("red"))
            else:
                im_fill(frame, [0, quo-1], [0, denominator-1], self.color_dict.get("red"))
        
                if rem != 0:
                    im_fill(frame, [rows-1, rows-1], [0, rem-1], self.color_dict.get("red"))
    
       
        #self.numerator_list.append(numerator)
        #self.denominator_list.append(denominator)
        # Video play
        #play_video, matrixf= vid_show([frame], numerator, fps, comment, aspect) # play on screen
        frame_rgb = make_rgb(frame) 
        
        self.frame_list.append(frame_rgb)
        self.comment_list.append(comment)
        frame_array = self.plot_to_frame_single(frame_rgb, comment)
        #Frame = plot_to_frame(matrixf, comment)
        #return play_video
        return frame_array
    
    
    def AddMult(self, numerator,
                denominator,
                mult, 
                aspect = 'None',
                comment = ' '):
        
        if aspect == 'None':
            aspect = 0.1*denominator
        
        if numerator == 0 or denominator == 0 or mult == 0 or mult == 1:
            return self.AddFrac(numerator*mult, denominator, comment)
        
        else:
          
            # Decide number of rows
            re = divmod(numerator*mult, denominator)
            quo = re[0]
            rem = re[1]
          
            if rem == 0:
              rows = quo
            else:
              rows = quo + 1
          
            # Create a frame with white background color
            frame = np.array([["ffffff"]*denominator for row in range (rows)])
            #frame_copy = frame.copy()
            #frame_list.append(frame_copy) 
            
            for i in range(0, mult):
                # Decide color
                result = divmod(i, len(list(self.color_dict)))
                
                start_grid = numerator * i
                end_grid = numerator * (i+1)
                
                
                frame_reshape = np.reshape(frame, (1, rows*denominator))
                im_fill(frame_reshape, [0, 0], [start_grid, end_grid-1], list(self.color_dict.values())[result[1]])
    
                frame = np.reshape(frame_reshape, (rows, denominator))
                frame_copy = frame.copy()
                frame_rgb = make_rgb(frame_copy) 
                
                #print('append frame')
                #print(frame_rgb)
                self.frame_list.append(frame_rgb)
                self.comment_list.append(comment)
                self.plot_to_frame_single(frame_rgb, comment)
                #frame_list.append(frame_copy) 
      
            return 
        
    def plot_to_frame_single(self, frame, comment):
        fig,ax = self.grid_lines_on_procedure(frame.shape[0],
                                              frame.shape[1], 
                                              comment = comment)
        
        canvas = FigureCanvasAgg(fig)
        #plt.tight_layout()
        pyplot.imshow(frame, interpolation='none', aspect =0.1*frame.shape[1])
        pyplot.show()
        fig.savefig('plot.jpg')
        buf = canvas.buffer_rgba()
        X = np.asarray(buf)  
        X_new = X[:,:,0:3]
        self.frame_array_list.append(X_new)
        #print(X_new.shape)
        return X_new
        
        
    
    
# =============================================================================
#     def plot_to_frame(self):      
#         for index, frame in enumerate(self.frame_list):
#             fig,ax = self.grid_lines_on_procedure(frame.shape[0],
#                                                   frame.shape[1], 
#                                                   comment = self.comment_list[index])
#             canvas = FigureCanvasAgg(fig)
#             #plt.tight_layout()
#             pyplot.imshow(frame, interpolation='none', aspect =0.1*frame.shape[1])
#             pyplot.show()
#             fig.savefig('plot.jpg')
#             buf = canvas.buffer_rgba()
#             X = np.asarray(buf)  
#             X_new = X[:,:,0:3]
#             self.frame_array_list.append(X_new)
#         return 
# 
# =============================================================================

    def grid_lines_on_procedure(self, width, height, comment = ' '):        
        fig, ax = pyplot.subplots() # make figure 
        ax.grid(linestyle='-',linewidth=1)
        xticks = np.arange(-0.5,height+0.5 ,1)
        
        yticks = np.arange(-0.5, width-0.5,1)
        
    
        ax.set_xticks(xticks)
        x_middle_labels = [(str(y)+'/'+str(height)) for y in np.arange(1, height)]
        x_labels = [' ']
        x_labels.extend(x_middle_labels)
        x_labels.append(1)
        ax.set_xticklabels(x_labels)
        
        
        ax.set_yticks(yticks)
        
        y_middle_labels = [int(x) for x in np.arange(1, width)]
        y_labels = [' ']
        y_labels.extend(y_middle_labels)
       
        
        ax.set_yticklabels(y_labels)    
        ax.yaxis.tick_right()
        ax.xaxis.tick_top()
       
        if comment != ' ':
            ax.set_title(comment, fontsize = 15)
    
        return fig,ax
       
    
    def padding(self, frame, video, h_video, w_video):
        old_h, old_w, channels = frame.shape
        if divmod(h_video - old_h, 2)[1] != 0:
          pad_h_t = int((h_video - 1 - old_h) /2)
          pad_h_b = int((h_video + 1 - old_h) /2)
    
        else:
          pad_h_t = int((h_video - old_h) /2)
          pad_h_b = int((h_video - old_h) /2)
    
        if divmod(w_video - old_w, 2)[1] != 0:
          pad_w_l = int((w_video - 1 - old_w) /2)
          pad_w_r = int((w_video + 1 - old_w) /2)
    
        else:
          pad_w_l = int((w_video - old_w) /2)
          pad_w_r = int((w_video - old_w) /2)
    
        padding_image = cv2.copyMakeBorder(frame, 
                                           pad_h_t, pad_h_b,
                                           pad_w_l, pad_w_r,
                                           cv2.BORDER_CONSTANT, 
                                           None, 
                                           value = [255, 255, 255])
        
        new_h, new_w, channels = padding_image.shape
        #plt.imshow(padding_image)
        #plt.show()
        padding_image = cv2.cvtColor(padding_image, cv2.COLOR_BGR2RGB)
        video.write(padding_image)
        return video


    def CreateVideo(self, video_name, fps):
        #self.plot_to_frame()
        height_list = []
        width_list = []
    
        for frame in self.frame_array_list:
            height, width = frame.shape[0:2]
            height_list.append(height)
            width_list.append(width)
        
        #print(height_list)
        h_video=np.max(height_list)
        w_video=np.max(width_list)
        
        
        #fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        video = cv2.VideoWriter(video_name, 
                                cv2.VideoWriter_fourcc(*'MJPG'), 
                                fps, 
                                (w_video, h_video))
        
        
        for frame in self.frame_array_list:
            video =  self.padding(frame, video, h_video, w_video)
        
        video.release()
    
        return


    def CreateCombVideo(self, video_name, fps):
    
        h_video, w_video = self.frame_comb_array_list[0].shape[0:2]
        #print('h, w = ', h_video, w_video)
        #fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        video = cv2.VideoWriter(video_name, 
                                cv2.VideoWriter_fourcc(*'MJPG'), 
                                fps, 
                                (w_video, h_video))
        
        
        for frame in self.frame_comb_array_list:
            video.write(frame)
        
        video.release()
    
        return
    
    
    def combine_two_fracs(self, frac1, frac2):
        im_v = cv2.vconcat([frac1, frac2])
        im_v_new = cv2.cvtColor(im_v, cv2.COLOR_BGR2RGB)
        cv2_imshow(im_v_new)
        self.frame_comb_array_list.append(im_v_new)
        return im_v_new
    
        
  



def make_rgb(matrix): #helper function for vidfill
    '''
    Helper function used in vidfill to convert hex code to rgb.
  
    Inputs:
    matrix: A nxn matrix filled with hex values.
  
    Outputs:
    A nxn numpy array filled with rgb tuples.
  
    '''
    matrix = np.array(matrix)
    if len(matrix[0][0]) == 1:
        matrix = bnw_to_hex(matrix)
    if matrix.shape[0]*matrix.shape[1] > 400:
        print ("Image too large!! Shrinking...")
        matrix = matrix[0:20,0:20]
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    matrix2 = [[]]*rows
    for i in range(rows):
        matrix2[i] = [[]]*columns
        for j in range(columns):
            if len(matrix[i][j]) == 2:
                t = matrix[i][j]+matrix[i][j]+matrix[i][j]
                t = check_format(t)
                color = hex_to_color('#'+t)
                matrix2[i][j] = (color[0],color[1],color[2])
            elif len(matrix[i][j]) == 1:
                print ("Invalid length for matrix["+str(i)+"]["+str(j)+"]'s element, please use hexadecimal format.")
            else:
                t = matrix[i][j]
                t = check_format(t)
                color = hex_to_color('#'+t)
                matrix2[i][j] = (color[0],color[1],color[2])    
    return np.array(matrix2)





    
    


def Frac(numerator, denominator, aspect = 'None', fps = 1, comment = ' '):
    if denominator == 0:
        print("Error: The denominator cannot be zero!")
        return 
    
    if aspect == 'None':
        aspect = 0.1*denominator
        
    if numerator == 0:
        # Create a frame with white background color
        frame = np.array([["ffffff"]*denominator for row in range (1)])
        # Video play
        play_video= vid_show([frame], numerator, fps, comment, aspect) # play on screen
        return play_video
    
    re = divmod(numerator, denominator)
    quo = re[0]
    rem = re[1]

    if rem == 0:
      rows = quo
    else:
      rows = quo + 1
    
    # Create a frame with white background color
    frame = np.array([["ffffff"]*denominator for row in range (rows)])
     
    if numerator<denominator:     
        # Fill the vector
        im_fill(frame, [0, 0], [0, numerator-1], color_dict.get("red"))
    else:
        im_fill(frame, [0, quo-1], [0, denominator-1], color_dict.get("red"))

        if rem != 0:
            im_fill(frame, [rows-1, rows-1], [0, rem-1], color_dict.get("red"))

   
    
    # Video play
    play_video = vid_show([frame], numerator, fps, comment, aspect) # play on screen
    
    #return play_video
    return play_video












        


def check_input(img,which_lib):
    if img is None:
        #only need to do this once for the entire thing
        raise TypeError('You input an image with '+str(type(img))+', check your file path, you may have typed it incorrectly.')
            
    if which_lib == 'cv':
        if isinstance(img,np.ndarray):
            if SAFE:
                if img.dtype!=np.uint8:
                    print('Type mismatch...converting for you...')
                    #im_show(img)
                    img = matrix_to_img(img)
                    return img
                else:
                    return img
            else:
                if img.dtype!=np.uint8:
                    raise TypeError("Type mismatch...check your input! You may need to use matrix_to_img().")
                else:
                    return img
        else: #this case is a list
            if SAFE:
                    print ("Type mismatch...converting for you...")
                    #im_show(img)
                    img = matrix_to_img(img)
                    return img
            else:
                    raise TypeError("Type mismatch...check your input! You may need to use matrix_to_img().")
            
    if which_lib == 'custom':
        if isinstance(img,np.ndarray):
                if img.dtype==np.uint8:
                    raise TypeError ("Type mismatch...Check your input! These functions do not work with OpenCV images.")
    if which_lib == 'save_list':
        if isinstance(img,np.ndarray):
            if img.dtype!=np.uint8:
                img = matrix_to_img(img)
                return img
            else:
                return img
        else: 
            raise TypeError("Type mismatch...Check your input!")

def check_format(input):
    '''
    Function to check that student input is in string format, will correct for them in safe mode.
    '''	
    if type(input) != np.string_:
        #print type(input)
        if SAFE:
	        #print "Input was not in string format, be sure to use quotes, correcting for you..."
	        return str(input)
        else:
	        raise TypeError ("Input is not in string format, please correct this by using quotes.")
    else:
        return input
    
def hex_to_color(s):
    ''' Helper function for translating hex input to RGB color strings, used in makergb.
  
    Inputs: 
    s: hex color string without # prefix
  
    Outputs:
    RGB tuple as (r,g,b) in decimal format
    '''    
    hexColorPattern = re.compile("\A#[a-fA-F0-9]{6}\Z")
    #if not isinstance(s, basestring):
    #    raise TypeError('hex2color requires a string argument')
    if hexColorPattern.match(s) is None:
        raise ValueError('invalid hex color string "%s"' % s)
    return tuple([int(n, 16)/255.0 for n in (s[1:3], s[3:5], s[5:7])])

def bnw_to_hex(bnw):
    '''
    Converts '0' digit to correct '000000' pattern.
    
    Inputs:
    bnw: A user created matrix containing '0' or '1' values for black or white.
        
    Outputs:
    Returns the same matrix but in hex format.
    '''
    bnw=np.array(bnw)
    rows = bnw.shape[0]
    columns = bnw.shape[1]
    hex_bnw=[[]]*rows
    for i in range(rows):
        hex_bnw[i]=[[]]*columns
        for j in range(columns):
            if bnw[i][j]=='0':
                hex_bnw[i][j]='000000'
            elif bnw[i][j]=='1':
                hex_bnw[i][j]='FFFFFF'
    return np.array(hex_bnw)
            
def rgb_to_gray(rgb):
    '''
    Helper function for making images grayscale in vidfill.
  
    Inputs:
    rgb: An nxn matrix filled with RGB tuples.
  
    Outputs:
    A nxn matrix with gray value tuples.
    '''
    if rgb.shape[0]*rgb.shape[1]>400:
        print( "Image too large!! Shrinking...")
        rgb = rgb[0:20,0:20]
    rows = rgb.shape[0]
    columns = rgb.shape[1]
    gray=[[]]*rows
    for i in range(rows):
        gray[i]=[[]]*columns
        for j in range(columns):
            r,g,b= rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
            gray[i][j]=0.2125 *r + 0.7154 *g + 0.0721 *b 
    return gray


    
def im_show(matrix): #previously aolme_imshow
    '''
    A function that shows a single nxn matrix frame on the screen.
  
    Inputs:
    matrix: A nxn matrix filled with hex values (without leading #) or 0's and 1's.
  
    Outputs:
    A figure containing the designed image frame in color, grayscale or black and white.
  
    '''
    check_input(matrix,'custom')
    matrix = make_rgb(matrix)
    if matrix.shape[0]*matrix.shape[1]>400:
        print ("Image too large!! Shrinking...")
        matrix = matrix[0:20,0:20] 
    if (len(matrix[0][0])>1):
        if not grid_lines:
            pyplot.figure()
            pyplot.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
            pyplot.imshow(matrix, interpolation='none')
            pyplot.tight_layout()
        else:
            fig,x =grid_lines_on(matrix.shape[0],matrix.shape[1])
            pyplot.grid(linestyle='-', linewidth=0.5)
            pyplot.imshow(matrix, interpolation='none')
            pyplot.tight_layout()
    else:
        if not grid_lines:
            pyplot.figure()
            pyplot.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
            pyplot.imshow(matrix, interpolation='none')
            pyplot.tight_layout()
        else:
            grid_lines_on(matrix.shape[0],matrix.shape[1])
            pyplot.grid(linestyle='-', linewidth=0.5)
            pyplot.imshow(matrix, interpolation='none')
            pyplot.tight_layout()
    pyplot.show()

def im_fill(matrix, rng_rows, rng_cols, val): #previously aolme_imfill
    '''
  A function that fills a range of rows and columns with a single color value.
  
  Inputs:
  matrix: A nxn sized matrix. Can be empty or have been previously filled.
  rng_rows: A range of rows input as [from,to].
  rng_cols: A range of columns input as [from,to].
  val: A hex color value or 0 or 1 which will fill the requested ranges of rows and columns.
  
  Outputs:
  The same nxn matrix but with range of rows and columns filled with val.
  
  '''
    check_input(matrix,'custom')
    col_0 = [row[0] for row in matrix] # Getting column zero   
    ncols = len(matrix[0])
    nrows = len(col_0)

    nrows_portion = rng_rows[1] - rng_rows[0] 
    ncols_portion = rng_cols[1] - rng_cols[0] 

    if (nrows_portion < 0) or (ncols_portion < 0):
        print ('( getportion) Error: Wrong range declaration!');    
        return None;

    if (rng_rows[1] > nrows) or (rng_cols[1] > ncols):
        print ('( getportion) Error: Index out of range!');    
        return None;
    
    for i in range(rng_rows[0], rng_rows[1] + 1):
        for j in range(rng_cols[0], rng_cols[1] + 1):
            matrix[i][j] = val;

    return matrix;   
    
def im_print(matrix): #previously aolme_imprint
    '''
    A function that will print the contents of a matrix.
  
    Inputs:
    matrix: A nxn matrix.
  
    Outputs:
    Text printout of the entire matrix's contents.
  
    '''
    check_input(matrix,'custom')
    matrix = np.array(matrix)
    print( "img = ",matrix)       

    return None;
    

def vid_show(vid,numerator, fps, comment = ' ', asp = 'None'):    #previously aolme_vidshow
    '''
    A function that 'plays' a list of frame, creating a 2d video. Note, this must be set equal to some value to work!!!
    
    Inputs:
    vid: A list of frames, set as [frame0,frame1,...,framen], where each frame is a nxn matrix of the same size.
    fps: A number which represents the number of frames that should be played per second.
    
    Outputs:
    A visual animation containing each frame in the order listed. Returns the animation.
    
    '''
    matrixf = make_rgb(vid[-1]) 
    if not grid_lines:
        fig = pyplot.figure(2)
        pyplot.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
    else:
        fig1,ax = grid_lines_on(matrixf.shape[0],matrixf.shape[1], numerator,comment)
    fps = 1000./fps  
    if len(vid) < 1:
        print ("Incorrect input, make sure you give function a video to play!")
        
    if matrixf.shape[0]*matrixf.shape[1]>400:
            print ("Image too large!! Shrinking...")
            i = 0
            for frame in vid:
                frame = frame[0:20,0:20]
                vid[i]=frame
                i+=1
    #im = pyplot.imshow(matrixf, interpolation='none', aspect='auto')
    if asp == 'None':
        asp = 0.1*matrixf.shape[1]
    im = pyplot.imshow(matrixf, interpolation='none', aspect=asp)
    pyplot.show() 
    # function to update figure
    def update_fig(j):
        # set the data in the axesimage object
        frame = make_rgb(vid[j])
        im.set_array(frame)
        pyplot.draw()        
        return im
    # kick off the animation
    if (grid_lines):
        ani = animation.FuncAnimation(fig1, update_fig, frames=range(len(vid)), 
                                interval=fps, blit=False, repeat=True)
    else:
        ani = animation.FuncAnimation(fig, update_fig, frames=range(len(vid)),
                                interval = fps, blit=True, repeat=True)
    pyplot.tight_layout()
    pyplot.show()
	
    return ani
	

def vid_show_procedure(vid, fps, comment = ' ', asp = 'None'):    #previously aolme_vidshow
    '''
    A function that 'plays' a list of frame, creating a 2d video. Note, this must be set equal to some value to work!!!
    
    Inputs:
    vid: A list of frames, set as [frame0,frame1,...,framen], where each frame is a nxn matrix of the same size.
    fps: A number which represents the number of frames that should be played per second.
    
    Outputs:
    A visual animation containing each frame in the order listed. Returns the animation.
    
    '''
    fps1 = 1000./fps  
    # function to update figure
    def update_fig(j):
        # set the data in the axesimage object
        matrixf = make_rgb(vid[j])
        
        fig1,ax = grid_lines_on_procedure(matrixf.shape[0],matrixf.shape[1], comment)
        
        if len(vid) < 1:
            print ("Incorrect input, make sure you give function a video to play!")
        
        if matrixf.shape[0]*matrixf.shape[1]>400:
            print ("Image too large!! Shrinking...")
            i = 0
            for frame in vid:
                frame = frame[0:20,0:20]
                vid[i]=frame
                i+=1
        #im = pyplot.imshow(matrixf, interpolation='none', aspect='auto')
        if asp == 'None':
            aspect = 0.1*matrixf.shape[1]
        
        im = pyplot.imshow(matrixf, interpolation='none', aspect=aspect)
        pyplot.show() 
        im.set_array(matrixf)
        pyplot.draw()        
        return fig1, im
    # kick off the animation
    
    ani = animation.FuncAnimation(update_fig, frames=range(len(vid)), 
                                interval=fps1, blit=False, repeat=True)
   
    
    pyplot.tight_layout()
    pyplot.show()
	
    return ani
def save_vid(vid,fps,name):
    if os.name != 'nt':
        vid.save(name,fps = fps, writer='imagemagick')

def matrix_to_img(matrix): #previously me_matrix2img
    '''
    Takes a nxn image frame and converts it to jpg format, saves it and shows the image.
  
    Inputs:
    matrix: A nxn matrix filled with hex colors.
  
    Outputs:
    A .jpg file saved to disc as picture.jpg, and the image is also displayed on screen.
    Returns the matrix as an opencv image.
   
    '''
    check_input(matrix,'custom')
    try: 
        os.remove("picture.jpg")
    except: 
        pass
    matrix = make_rgb(matrix)
    pyplot.axis('off')
    pyplot.imshow(matrix, interpolation='none')
    pyplot.savefig('picture.jpg',format='jpg',bbox_inches='tight', pad_inches=0)
    pyplot.show()
    pyplot.axis('on')
    c = cv2.imread('picture.jpg', 1)
    c = cv2.resize(c, (600, 400)) 
    #cv2.imshow('picture',c)
    try: 
        os.remove("picture.jpg")
    except: 
        pass

    return c
    
def make_img_gray(img):#previously me_rgb2gray
    '''
    Convert an open image to grayscale.
  
    Inputs:
    img: An open image file.
  
    Outputs:
    Returns the same image except converted to grayscale.
  
    '''
    img = check_input(img,'cv')
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_img(gray_img)
    return gray_img

def show_img(img):#previously me_imshow
    '''
    Displays an open image on screen.
  
    Inputs:
    img: An open image file.
  
    Outputs:
    Displays the open image file on screen.
    '''
    check_input(img,'cv')
    cv2.imshow('picture',img)
    #this part looks ridiculous but it's a bug in cv2 with live interpreters.
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    
def read_img(img): #previously me_imread
    '''
    Reads an image from disc.
  
    Inputs:
    img: A string containing the name of the image to be read on disc, with the file extension.
  
    Outputs:
    Returns the read image as a numpy array.
    
    '''
    c = cv2.imread(img,1)
    return c    

def save_img(img,name):#previously me_imsave
    '''
    Saves an open image from variable to disc.
  
    Inputs:
    img: An open image file in a variable in numpy array format.
    name: A string containing the name the image should be saved as, including the file extension.
  
    Outputs:
    A saved image file on disc inside the same folder as the python script.
  
    '''
    img = check_input(img,'save_list')
    cv2.imwrite(name,img)
 
def get_pixel(img,loc): #previously me_impix
    '''
    Gets a single pixel from an open image.
  
    Inputs:
    img: The image from which to get a pixel, stored as a numpy array in a variable.
    loc: The x,y location of the desired pixel, input as [x,y]
  
    Outputs:
    Returns the color of the pixel at the desired location as (r,g,b).
   
   '''
    check_input(img,'cv')
    
    pixel = img[loc[0],loc[1]]
	
    return [pixel[2],pixel[1],pixel[0]]

def img_size(img):#previously me_imsize
    '''
    Returns the size of the image.
  
    Inputs:
    img: The image from which to get a pixel, stored as a numpy array in a variable.
   
    Outputs:
    Returns the number of rows and columns in the array in (numberofrows, numberofcolums).
   
    '''
    check_input(img,'cv')

    print ('# of rows: ' + str(img.shape[1])) # of rows
    print ('# of cols: ' + str(img.shape[0])) # of columns
    size = (img.shape[1], img.shape[0]) # (nrows, ncols)
    return size;
    
def show_comps(img): #previously me_showcomps
    '''
    Displays the red, blue, and green components of an image on screen.
  
    Inputs:
    img: An image stored as a numpy array in a variable.
  
    Outputs:
    Displays on screen the red, green and blue components of the given image. Returns nothing.
  
    '''
    check_input(img,'cv')
    #image = cv2.imread(img)
    #zero = np.zeros(image.shape)

    #zero = np.zeros((image.shape[0],image.shape[1],3), np.float64)
    zeros = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    B,G,R = cv2.split(img)

    blue_component = cv2.merge((B, zeros, zeros))
    green_component = cv2.merge((zeros, G, zeros))
    red_component = cv2.merge((zeros, zeros, R))
            
    cv2.imshow('blue',blue_component)
    cv2.waitKey(0)
    cv2.imshow('red',red_component)
    cv2.waitKey(0)
    cv2.imshow('green',green_component)
    cv2.waitKey(0)
    #more of this due to cv2 bug...maybe put in a loop to look 'nicer'
    cv2.destroyWindow('green')
    cv2.waitKey(-1)
    cv2.destroyWindow('green')
    cv2.waitKey(-1)
    cv2.destroyWindow('green')
    cv2.waitKey(-1)
    cv2.destroyWindow('green')
    cv2.waitKey(-1)    
    return [red_component,green_component,blue_component]

def get_comps(img):#previously me_getcomps
    '''
    Returns a list of the different combinations of rgb components of an image in a list.
  
    Inputs: 
    img: An image stored as a numpy array in a variable.
  
    Outputs:
    Returns a list of images stored as numpy arrays for each combination of components RGB.
    Val[0] is an image of only red component.
    Val[1] is an image of only green component.
    Val[2] is an image of only blue component. 
    Val[3] is an image of only green and red components creating yellow.
    Val[4] is an image of only blue and green components creating cyan.
    Val[5] is an image of only blue and red components creating magenta.
  
    '''
    check_input(img,'cv')
    #image = cv2.imread(img)
    #zero = np.zeros(image.shape)

    #zero = np.zeros((image.shape[0],image.shape[1],3), np.float64)
    zeros = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    B,G,R = cv2.split(img)

    Ir = cv2.merge((B, zeros, zeros))
    Ig = cv2.merge((zeros, G, zeros))
    Ib = cv2.merge((zeros, zeros, R))
    Iy = cv2.merge((zeros, G, R))
    Ic = cv2.merge((B, G, zeros))
    Im = cv2.merge((B, zeros, R))
    return (Ir, Ig, Ib, Iy, Ic, Im) # these are  RGB images
    
def rotate_img(img,degrees): #previously  me_imrotate
    '''
    Rotates an image.
  
    Inputs:
    img: An image file stored in a variable as a numpy array.
    degrees: The amount of degrees the image should be rotated by.

    Outputs:
    Displays the rotated image on screen.

    '''
    check_input(img,'cv')
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
            
    M = cv2.getRotationMatrix2D(center, degrees, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    show_img(rotated)
    return rotated
    
def crop_img(img,ranges):#previously me_imcrop
    '''
    Trims edges off of an image.
  
    Inputs:
    img: An image file saved as a numpy array in a variable.
    ranges: An array filled with pixel values saved as int.
    ranges[0]: the x1 value from where to start cropping as part of (x1,y1) coordinates.
    ranges[1]: the x2 value from where to end cropping as part of (x2,y2) coordinates.
    ranges[2]: the y1 value from where to start the cropping as part of (x1,y1) coordinates.
    ranges[3]: the y2 value from where to end the cropping as part of (x2,y2) coordinates.
  
    Outputs:
    Displays the cropped image on screen.
  
    '''
    check_input(img,'cv')
    cropped = img[ranges[0]:ranges[1],ranges[2]:ranges[3]]
    show_img(cropped)
    return cropped

def put_pixel(img, position, val):#previously me_putpixel
    '''
    Places a pixel on an image at a chosen location.
   
    Inputs:
    img: An image file saved as a numpy array in a variable.
    position: the position at which to place the pixel, given in (x,y) coordinates as position[0] for x and position [1] for y.
    val: the rbg or black and white value or color of the pixel to be placed on the image, with val = 0 or 1 or val=[r,g,b] where r, g, and b are float values which define a color.
  
    Outputs:
    No outputs, the pixel is saved on the original image and must be displayed using showimg(img).
  
    '''
    check_input(img,'cv')
    if len(img.shape) < 3: # grayscale
        img[position[1],position[0]] = val
    else: # RGB
        img[position[1],position[0]] = (val[2], val[1], val[0])
    return None

def put_pixel_group(img, ranges, val): #previously me_putpixelgroup
    '''
    Places a group of pixels onto an image at a chosen location.
   
    Inputs:
    img: An image file saved as a numpy array in a variable.
    range: An array filled with pixel values saved as int.
    range[0]: the x1 value from where to start paste as part of (x1,y1) coordinates.
    range[1]: the x2 value from where to end paste as part of (x2,y2) coordinates.
    range[2]: the y1 value from where to start the paste as part of (x1,y1) coordinates.
    range[3]: the y2 value from where to end the paste as part of (x2,y2) coordinates.
    val: the rbg or black and white value or color of the pixel to be placed on the image, with val = 0 or 1 or val=[r,g,b] where r, g, and b are float values which define a color.
  
    Outputs:
    No outputs, the pixel range is saved on the original image and must be displayed using showimg(img).
   
    '''
    check_input(img,'cv')
    nra = ranges[0]
    nrb = ranges[1]
    nca = ranges[2]
    ncb = ranges[3]
    for i in range(nra, nrb+1):
        for j in range(nca, ncb+1):
            if len(img.shape) < 3: # grayscale
                img[i,j] = val
            else: # RGB
                img[i,j] = (val[2], val[1], val[0])
    return None
    
def print_img_info(img):
    '''
    Prints information about a user-created 2d image.
  
    Inputs:
    img: A user created 2d matrix filled with color values.
  
    Outputs:
    Prints on screen the number of pixes (rows*columns), image type (grayscale, color or black and white), height (number of rows), and width (number of columns)
    '''	
    #check_input(img,'cv')
    if isinstance(img,list):
      im_show(img)
      img = np.array(img)
    elif img.dtype != np.uint8:
        im_show(img)
    else:
        show_img(img)
    print ("Num of pixels: ", img.shape[0]*img.shape[1])
    print ("Height: ", img.shape[1])
    print ("Width: ", img.shape[0])
    if len(img[0][0]) == 3:
        print ("RGB color")
    else:
        print ("black and white")
    
    return None
    
def print_vid_info(vid):
    '''
    Prints information about a user created video.
  
    Inputs:
    vid: A list of 2d matrices filled with color values, created by the user in format [frame0,frame1,frame2...]
  
    Outputs:
    Prints the number of pixels on each frame (height*width), the height(number of rows), width (number of columns), number of frames, and whether the video is color, graysale or black and white.
    '''
    for i in range(len(vid)):
        vid[i] = np.array(vid[i])
    print ("Num of pixels: ", vid[0].shape[0]*vid[0].shape[1])
    print ("Height: ", vid[0].shape[1])
    print ("Width: ", vid[0].shape[0])
    print ("Num of frames: ", len(vid))
    if len(vid[0][0][0]) == 3:
        print ("RGB color")
    else:
        print ("black and white")
    return None

def print_img_segment(img,ranges):
    '''
    Prints a portion of a user created image.
  
    Inputs:
    img: A user defined 2d matrix filled with color values.
    ranges: A list of ranges which define the portion of the matrix to be printed, defined as a list of numbers with [x1,x2,y1,y2] coordinates.
  
    Outputs:
    Displays an image on screen containing only the portion of the original image requested by the user.
  
    '''
    check_input(img,'custom')
    img = np.array(img)
    im_seg = img[ranges[0]:ranges[1],ranges[2]:ranges[3]]
    im_show(im_seg)
    return None
    
def print_vid_segment(vid,ranges,frames,fps):
    '''
    Prints a portion of a user created video.
  
    Inputs:
    vid: A list of 2d matrices filled with color values, created by the user in format [frame0,frame1,frame2...]
    ranges: A list of ranges which define the portion of the matrix to be printed, defined as a list of numbers with [x1,x2,y1,y2] coordinates.
    frames: A range of frames to play on the video, must be continuous, input as [startframe,endframe]...need to add all as an option.
    fps: The rate at which the video should be played.
  
    Outputs:
    Displays an image on screen containing only the portion of the original image requested by the user.
  
    '''
    if len(vid) < 2:
        print("Please pass a video to the function.")
    vid_seg=[]
    for vids in vid:
        vids = np.array(vids)
        vid_seg.append(vids[ranges[0]:ranges[1],ranges[2]:ranges[3]])
    vid_seg = vid_seg[frames[0]:frames[1]]
    return vid_show(vid_seg,fps)


def display_video(save_path):
    # Input video path
    # save_path = "video.mp4"
    
    # Compressed video path
    compressed_path = "video_compressed.mp4"
    
    os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")
    
    # Show video
    mp4 = open(compressed_path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    HTML("""
    <video width=400 controls loop autoplay>
          <source src="%s" type="video/mp4">
    </video>
    """ % data_url)
    return
