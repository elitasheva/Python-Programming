import math
PAINT_PER_SQUARE_METER = 1.76
input_width = input()
input_height = input()

try:
    width = float(input_width)
    height = float(input_height)

    if width == 0 or height == 0:
        raise ValueError

    surface = width * height
    paint_needed = surface / PAINT_PER_SQUARE_METER
    paint_needed = math.trunc(paint_needed) + 1
    print(paint_needed)

except ValueError:
    print("INVALID INPUT")