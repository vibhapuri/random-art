import sys
import itertools
from PIL import Image

images = map(Image.open, ['Test1.jpg', 'Test2.jpg', 'Test3.jpg', 'Test4.jpg', 'Test5.jpg', 'Test6.jpg', 'Test7.jpg'])
widths, heights = zip(*(i.size for i in images))
options = list(itertools.permutations(images))

total_width = sum(widths)
max_height = max(heights)

for i in range(len(options)):
	new_im = Image.new('RGB', (total_width, max_height))
	x_offset = 0
	for im in options[i]:
 		new_im.paste(im, (x_offset,0))
  		x_offset += im.size[0]
	new_im.save("option"+`i`+".jpg")