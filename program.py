import requests 
import sys
from PIL import Image 
from io import BytesIO

response_img = requests.get("https://picsum.photos/120/20")
print(response_img.url)

img = Image.open(BytesIO(response_img.content))
print(img)

width, height = img.size
print(width, height)

img = img.convert("L")

pixels = img.getdata()

symbols = ["B","S","@","&","$","%","*","!",":","^","."]
display_pixels = [symbols[pixel // 25] for pixel in pixels]
display_pixels = ''.join(display_pixels)

display_pixels_count = len(display_pixels)
result = [display_pixels[index:index + width] for index in range(0, display_pixels_count, width)]
result = "\n".join(result)
print(result)
