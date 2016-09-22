box_width_str = input()
box_height_str = input()
box_length_str = input()
path = input()
box_parameters = list()
box_parameters.append(box_width_str)
box_parameters.append(box_height_str)
box_parameters.append(box_length_str)


try:
    box_parameters = [float(num) for num in box_parameters]
    box_parameters.sort()

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                current_box = list()
                tokens = line.split(",")
                name = tokens[0]
                params = tokens[1:]
                current_box = [float(num) for num in params]
                current_box.sort()

                is_bigger = False
                for i in range(len(current_box)):
                    if box_parameters[i] < current_box[i]:
                        is_bigger = True
                        break

                if not is_bigger:
                    print(name)

except ValueError:
    print("INVALID INPUT")

# [package[i] < box[i] for i in range(len(box))]
#  OrderedDict(sorted(od.items(), key=lambda kv: kv[0])) sort orderedDict by keys