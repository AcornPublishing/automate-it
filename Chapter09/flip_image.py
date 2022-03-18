from PIL import Image
img = Image.open('sunset.jpg')
img.rotate(180).save('sunset180deg.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save('sunset_horizontal_flip.png')
img.transpose(Image.FLIP_TOP_BOTTOM).save('sunset_vertical_flip.png')
