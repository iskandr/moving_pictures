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

	moving\_pictures.make\_movie(list\_of\_images, movie\_name="gonzo.mpg") 
    
