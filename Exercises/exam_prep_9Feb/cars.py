path_info = input()

hours = 0
with open(path_info, encoding="utf-8") as f_info:
    for line in f_info:
        line = line.strip()
        if line:
            params = line.split(",")
            try:
                from_km = int(params[0])
                to_km = int(params[1])
                speed = float(params[2])
                traveled_km = (to_km - from_km) + 1
                hours += traveled_km / speed
            except ValueError:
                print("INVALID INPUT")

print("{:.2f}".format(hours))