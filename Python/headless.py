# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
x = 2
top = 2
padding = 12
# Load default font.
font = ImageFont.load_default()

dot_arr = []
dot_max = 50
def map_range(a,b, s):
	(a1, a2), (b1, b2) =a,b
	return b1 + ((s -a1) * (b2 -b1) / (a2 - a1))

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
   # draw graph
    draw.line((padding, height-padding, padding, -height+padding), fill=255)
    draw.line((padding, height-padding, padding+width, height-padding), fill=255) 

      # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x = accel[0]

    if len(dot_arr) <= 115:
    	dot_arr.append(accel_x)
    else:
    	del dot_arr[0]
    	dot_arr.append(accel_x)
    x_pos = 15

    for i in range(1,len(dot_arr)):
    	y_pos = map_range((520, -520), (0 , height - padding), dot_arr[i])
    	last_y_pos = map_range((520, -520), (0 , height - padding), dot_arr[i-1])
    	y_pos = round(y_pos)
    	draw.point((x_pos, y_pos), fill=255)
    	draw.line((x_pos,y_pos,x_pos-1,last_y_pos),fill=255)
    	x_pos += 1

    disp.image(image)

    disp.display()
    # Wait half a second and repeat.
    time.sleep(0.5)


