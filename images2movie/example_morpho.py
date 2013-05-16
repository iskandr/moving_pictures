

import numpy as np 
import scipy.ndimage 
from scipy.ndimage.morphology import *

from moving_pictures import make_movie 

def main(image_name='tyler.png', image_size = 200, n_frames=150, n_interpolation_frames=0):
  image = Image.open('tyler.png')
  image = resize(image, image_size)
  image = np.array(image)
  print image.shape
  image = image.astype('float') / image.max()
  nrows, ncols = image.shape[:2]
  images = [image]
  print "Generating frames..."
  x_grad_size = 3+np.random.randint(low=0,high=3,size=2)*2 
  y_grad_size = 3+np.random.randint(low=0,high=3,size=2)*2
  structure_size = 3+np.random.randint(low=0,high=6,size=2)*2
  structure = np.random.randn(structure_size[0], structure_size[1]) > np.random.randn()
  def dilate(x):
    return grey_dilation(x, size = structure_size, footprint = structure)
  def erode(x):
    return grey_erosion(x, size = structure_size, footprint = structure)
  progress = progressbar.ProgressBar()
  alpha = np.random.randn() * 0.1
  beta = np.random.rand() * 0.0
  original_g = image[:,:,1]
  for i in progress(xrange(n_frames)):
    r = image[:,:,0]
    g = image[:,:,1]
    b = image[:,:,2]
    gray = 0.21 * r + 0.71 * g + 0.07 * b 
    x_grad = morphological_gradient(gray, x_grad_size, mode = 'nearest')
    y_grad = morphological_gradient(gray, y_grad_size, mode = 'nearest')
    hf = (x_grad + y_grad)**2 
    hf -= hf.min()
    hf /= hf.max()
    er = erode(r)
    dr = dilate(r)
    eg = erode(g)
    dg = dilate(g)
    eb = erode(b)
    db = dilate(b)
    r = r * hf + (1-hf)*(dr -er) + (1-hf)  *  alpha * (1-hf)**2 * original_g
    b = b * hf + (1-hf)*(db - eb) +(1-hf)  *  beta * (1-hf)**2 * original_g
    g = g * hf + (1-hf)  * (dg - eg)
    image = np.dstack([r,b,g])
    
    images.append(image)   
  make_to_movie(images, n_interpolation_frames=n_interpolation_frames)
  
if __name__ == '__main__':
  main('tyler.png', n_frames=100, n_interpolation_frames=7)
