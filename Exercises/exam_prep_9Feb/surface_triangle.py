import math
first_side_str = input()
second_side_str = input()
third_side_str = input()

try:
    first_side_num = float(first_side_str)
    second_side_num = float(second_side_str)
    third_side_num = float(third_side_str)

    if first_side_num > 0 and second_side_num > 0 and third_side_num > 0:
        if (first_side_num + second_side_num) > third_side_num and\
                (first_side_num + third_side_num) > second_side_num and\
                (second_side_num + third_side_num) > first_side_num:
            half_perimeter = (first_side_num + second_side_num + third_side_num) / 2
            surface = math.sqrt(half_perimeter * (half_perimeter - first_side_num) * (half_perimeter - second_side_num) *
                                (half_perimeter - third_side_num))
    print("{:.2f}".format(surface))
except ValueError:
    print("INVALID INPUT")

