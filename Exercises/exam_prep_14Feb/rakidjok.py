import math
liters_rakidjok_str = input()
input_path = input()
CONVERT_COEFFICIENT = 10

min_volume = None
name_drum = None
try:
    liters_rakidjok = float(liters_rakidjok_str)
    if liters_rakidjok <= 0:
        raise ValueError

    with open(input_path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                params = line.split(",")
                name = params[0]
                radius = float(params[1]) / CONVERT_COEFFICIENT
                height = float(params[2]) / CONVERT_COEFFICIENT

                if radius <= 0 or height <= 0:
                    raise ValueError

                current_volume = math.pi * (radius**2) * height
                if current_volume >= liters_rakidjok:
                    if min_volume is None or current_volume <= min_volume:
                        min_volume = current_volume
                        name_drum = name

    if name_drum is None:
        print("NO SUITABLE CONTAINER")
    else:
        print(name_drum)

except ValueError:
    print("INVALID INPUT")