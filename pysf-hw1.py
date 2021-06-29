from __future__ import print_function
from colorama import init
from termcolor import colored
init()
from colorama import Fore, Back, Style
print("\n")

image_length = 120
image_height = 36


def printf(str, *args):
    print(str % args, end='')

def line(length, color, ended):
	if not ended:
		printf(color + ' '* int(length))
	else:
		print(color + ' '* int(length))

def background_multi_line(num_lines, line_length, color):
	for i in range(int(num_lines)):
		line(line_length, color, True)

background_multi_line(image_height/6, image_length, Back.BLUE)
floor_height = image_height / 4
floor_length = 0
for i in range(int(floor_height)):
	floor_length = int((float(i)/float(floor_height)) * (image_length /4))
	sky_length = int((image_length / 2 ) - floor_length)
	line(sky_length ,Back.BLUE, False)
	line(1, Back.BLACK, False)
	line(floor_length-1 ,Back.RED,  False)
	line(floor_length-1 ,Back.RED,  False)
	line(1, Back.BLACK, False)
	line(sky_length ,Back.BLUE, True)

line(sky_length ,Back.BLUE, False)
line(floor_length ,Back.BLACK,  False)
line(floor_length ,Back.BLACK,  False)
line(sky_length ,Back.BLUE, True)

for j in range(int(image_height/12)):
	line((image_length/2 - floor_length), Back.BLUE, False)
	line(floor_length ,Back.RED,  False)
	line(floor_length ,Back.RED,  False)
	line((image_length/2 - floor_length), Back.BLUE, True)

window_length = image_length/12
door_length = image_length/12
for j in range(int(image_height/24)):
	line((image_length/2 - floor_length), Back.BLUE, False)
	line(floor_length ,Back.RED,  False)
	line(window_length, Back.WHITE, False)
	line(floor_length-window_length ,Back.RED,  False)
	line((image_length/2 - floor_length ), Back.BLUE, True)

for j in range(int(image_height/24)):
	line((image_length/2 - floor_length), Back.BLUE, False)
	line(floor_length - int(1.5*door_length) ,Back.RED,  False)
	line(door_length ,Back.YELLOW,  False)
	line(int(0.5*door_length) ,Back.RED,  False)
	line(window_length, Back.WHITE, False)
	line(floor_length-window_length ,Back.RED,  False)
	line((image_length/2 - floor_length ), Back.BLUE, True)

for j in range(int(image_height/8)):
	line((image_length/2 - floor_length), Back.BLUE, False)
	line(floor_length - int(1.5*door_length) ,Back.RED,  False)
	line(door_length ,Back.YELLOW,  False)
	line(int(0.5*door_length) ,Back.RED,  False)
	line(floor_length ,Back.RED,  False)
	line((image_length/2 - floor_length ), Back.BLUE, True)

print("\n")
