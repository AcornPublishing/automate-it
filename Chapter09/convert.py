__author__ = 'Chetan'

from PIL import Image
img = Image.open('beach_sunset.png').convert('L')
img.show()
img.save('beach-sunset-gray.png','png')

from PIL import Image
img = Image.open('beach_sunset.png')
img.save('beach-sunset-conv.jpg','jpeg')
