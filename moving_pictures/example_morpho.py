
from PIL import Image 
import numpy as np 
import scipy.ndimage 
from scipy.ndimage.morphology import *
import progressbar 

from moving_pictures import make_movie, resize  

def main(image_name='tyler.png', image_size = 200, n_frames=150, n_interpolation_frames=0):
  image = Image.open('tyler.png')
  image = resize(image, image_size)
  image = np.array(image)
  print image.shape
  image = image.astype('float') / image.max()
  nrows, ncols = image.shape[:2]
  images = [image]
  print "Generating frames..."
  d_structure_size = 3+np.random.randint(low=0,high=6,size=2)*2
  d_structure = np.random.randn(d_structure_size[0], d_structure_size[1]) > np.random.randn() / 5 
  e_structure_size = 3+np.random.randint(low=0,high=6,size=2)*2
  e_structure = np.random.randn(e_structure_size[0], e_structure_size[1]) > np.random.randn() / 5
  def dilate(x):
    return grey_dilation(x, footprint = d_structure)
  def erode(x):
    return grey_erosion(x, footprint = e_structure)
  progress = progressbar.ProgressBar()
  for i in progress(xrange(n_frames)):
    r = image[:,:,0]
    g = image[:,:,1]
    b = image[:,:,2]
    er = erode(r)
    dr = dilate(r)
    eg = erode(g)
    dg = dilate(g)
    eb = erode(b)
    db = dilate(b)
    image = np.dstack([(er+dg)/2,(eg+db)/2,(eb+dr/2)])
    
    images.append(image)   
  make_movie(images, n_interpolation_frames=n_interpolation_frames)
  
if __name__ == '__main__':
  main('tyler.png', n_frames=100, n_interpolation_frames=7)
