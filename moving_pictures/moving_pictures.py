
import math 
import os
import shutil
import sys
import tempfile

from subprocess import check_output, check_call  


import numpy as np 
from PIL import Image 
import progressbar 

def ensure_ffmpeg():
  devnull = open('/dev/null', 'w')
  try:
    check_call(['ffmpeg', '--help'], stderr = devnull, stdout = devnull)
  except:
    assert False, "Can't find ffmpeg"

def image_from_array(image, normalize=False):
  if isinstance(image, np.ndarray):
    maxval = image.max()
    if maxval <= 1:
      image *= 256 
    if normalize:
      image /= maxval 
    image = Image.fromarray(image.astype('uint8'))
  assert Image.isImageType(image)
  return image 

def resize(img, target_size = 300):
  """
  Resize so at least that the smallest dimension matches 
  the desired target size
  """
  img = image_from_array(img)
  width, height = img.size
  ratio = max( float(target_size) / width, float(target_size) / height) 
  return img.resize( (int(width * ratio), int(height * ratio)), Image.ANTIALIAS)

def make_movie(images, movie_name = 'movie.mpg', 
               overwrite = True, 
               n_interpolation_frames = 2,
               frame_rate = 30, 
               bitrate = '5000k'):

  """
  Takes a list of images, writes them to disk, uses ffmpeg to
  create a movie 
  """
  ensure_ffmpeg()
  # wrap directory creation so files get deleted afterward 
  try:
    base = tempfile.mkdtemp()

    n = len(images)
    total = 1 + (n-1)*(n_interpolation_frames+1)

    n_digits = int(math.ceil(np.log10(total)))
    format_string = "img%%0%dd.png" % n_digits
    print "Writing %d images" % total 
    progress = progressbar.ProgressBar(maxval=total).start()
    last_image = None 
    def write_image(image):
      i = progress.currval
      filename = os.path.join(base, format_string % i)
      f = open(filename, 'w')
      image = image_from_array(image) 
      image.save(f, format='PNG')
      progress.update(i+1)
   
    for image in images:
      if last_image is not None: 
        # interpolate between successive images 
        for j in xrange(n_interpolation_frames):
          weight = float(j) / (n_interpolation_frames+1)
          
          new_image = last_image * (1-weight) + weight * image
          write_image(new_image)
      write_image(image)
      last_image = image  
    progress.finish()
    movie_cmd = ["ffmpeg",
                 '-an', # no sound! 
                 '-r',  '%d' % frame_rate, 
                 '-i', os.path.join(base, format_string), 
                 '-y' if overwrite else '-n', 
                 #'-vcodec', codec,
                 '-b:v', bitrate, 
                 movie_name]
    check_call(movie_cmd)
  finally:
    try:
        shutil.rmtree(base) # delete directory
    except OSError, e:
        if e.errno != 2: # code 2 - no such file or directory
            raise  
