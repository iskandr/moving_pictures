MovingPictures 
=================

Create a movie from a sequence of images in Python (uses PIL and ffmpeg). The images can be any grid of numbers stored as an array. 

Installation:

	pip install moving\_pictures

Requires:

  * [NumPy](http://www.numpy.org/)
  * [ffmpeg](http://www.ffmpeg.org/)
  * [PIL](http://www.pythonware.com/products/pil/) -- Python Imaging Library 
  * [progressbar](https://code.google.com/p/python-progressbar/)

Usage:
        start = np.random.randn(200,200) > 0
        stop = np.random.randn(200,200) > 0
        images = []
        for step_size in np.arange(0,1,0.001):
          images.append(start*step_size + stop*(1-step_size))
	moving_pictures.make_movie(images, movie_name="random_blend.mpg") 
    
