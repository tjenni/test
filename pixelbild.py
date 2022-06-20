from PIL import Image
import matplotlib.pyplot as plt

width = 16
height = 16

img = Image.new( 'RGB', (width,height), "black") # Create a new black image
pixels = img.load() # Create the pixel map

pixels[5,5] = (0,255,0)
pixels[6,5] = (255,0,0)
pixels[5,6] = (255,0,0)
pixels[6,6] = (255,0,0)
pixels[7,7] = (255,255,0)

plt.imshow(img, interpolation="none")
plt.show()
