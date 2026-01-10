import sys
import math

position = tuple([10, 20, 5])
spawn = tuple([0, 0, 0])
#coords = position.split(",")

x1 = position[0]
y1 = position[1]
z1 = position[2]

x2 = 0
y2 = 0
z2 = 0

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

print("=== Game Coordinate System ===\n")

print(f"Position created: {position}")
print(f"Distance between {spawn} and {position}: {distance: .2f}\n")

position = tuple("1,sfgaea,fgs".split(","))
try:
	x1 = int(position[0])
	y1 = int(position[1])
	z1 = int(position[2])

	print(x1, y1, z1)

except:
	print(f"Error parsing coordinates: invalid literal for int() with base 10: '{position[0]}'")