import requests 
import sys
from PIL import Image 
from io import BytesIO

response_img = requests.get("https://picsum.photos/100/20")
img = Image.open(BytesIO(response_img.content))
# print(response_img.url)

width, height = img.size
img = img.convert("L")
pixels = img.getdata()

# symbols = ["B","S","@","&","$","%","*","!",":","^","."] #dark to light
symbols = [".","^",":","!","*","%","$","&","@","S","B"] #light to dark
display_pixels = [symbols[pixel // 25] for pixel in pixels]
display_pixels = ''.join(display_pixels)

display_pixels_count = len(display_pixels)
result = [display_pixels[index:index + width] for index in range(0, display_pixels_count, width)]
result = "\n".join(result)
print(result)
