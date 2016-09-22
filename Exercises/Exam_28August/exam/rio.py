import csv

medals_with_points = {
    'gold': 7,
    'silver': 3,
    'bronze': 1
}

result = {}

try:
    path = input()

    count_lines = 0
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line) != 4:
                raise ValueError

            count_lines += 1
            current_medal = line[2]
            current_country = line[3]

            if current_medal not in medals_with_points:
                raise ValueError
            
            if current_country not in result:
                result[current_country] = 0
            result[current_country] += medals_with_points[current_medal]

    if count_lines == 0:
        raise ValueError

    output = list()
    output = [(points, country) for country,points in result.items()]
    # for country, points in result.items():
    #     output.append((points, country))

    output.sort(reverse=True)
    for key,value in output:
        print(value)

except Exception as ex:
    print("INVALID INPUT")
