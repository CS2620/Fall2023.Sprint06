print("Start")

from PIL import Image, ImageDraw
import math

im = Image.open("panoramic.jpg")
px = im.load()

width = im.size[0]
height = im.size[1]

size = 200      
im2 = Image.new("RGB", (size, size))
px2 = im2.load()

pixel_span = width/4
print(pixel_span)


for y in range(size):
    for x in range(size):
        offsetX = x - size/2
        offsetY = x - size/2
        percentX = offsetX / (size /2)
        percentY = offsetY / (size/2)
        theta = math.atan2(percentX,1)

        theta2 = theta + math.pi/4
        theta3 = theta2 / (math.pi/2)
        theta4 = theta3 * pixel_span

        y_percent = y/size
        y2 = y_percent * height

        rgb = px[theta4, y2]
        px2[x,y] = rgb


im.save("out.png", "PNG")
im2.save("out2.png", "PNG")

print("Finish")
