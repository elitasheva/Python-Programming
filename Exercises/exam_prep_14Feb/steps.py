input_path = input()

position_x = 0
position_y = 0
DIRECTIONS = ["left", "right", "up", "down"]
directions = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}

try:
    count_lines = 0
    with open(input_path, encoding="utf-8") as file:

        for line in file:
            line = line.strip()
            if line:
                count_lines += 1
                params = line.split()
                direction = params[0]
                step_str = params[1]
                if direction not in DIRECTIONS:
                    raise ValueError
                step_num = float(step_str)

                position_x += step_num * directions[direction][0]
                position_y += step_num * directions[direction][1]

    if count_lines == 0:
        print("INVALID INPUT")
    else:
        print("X {:.3f}".format(position_x))
        print("Y {:.3f}".format(position_y))

except Exception:
    print("INVALID INPUT")




