import math
COEFFICIENT_OF_LOST = 0.098
size_of_list_per_square_meter_str = input()
box_height_str = input()
box_width_str = input()
box_length_str = input()

try:
    box_height_num = float(box_height_str)
    box_width_num = float(box_width_str)
    box_length_num = float(box_length_str)
    size_of_list_per_square_meter_num = float(size_of_list_per_square_meter_str)

    surface_of_box = 2 * (box_height_num * box_width_num + box_width_num * box_length_num +
                          box_height_num * box_length_num)

    count_lists_for_box = surface_of_box / size_of_list_per_square_meter_num
    first, second = math.modf(count_lists_for_box)

    area_of_all_lists_needed = count_lists_for_box * size_of_list_per_square_meter_num # площ на листите

    lost_square_meters = area_of_all_lists_needed * COEFFICIENT_OF_LOST
    area_of_box_with_lost = surface_of_box + lost_square_meters
    result = area_of_box_with_lost / size_of_list_per_square_meter_num
    first, second = math.modf(result)
    if second != 0:
        result = math.trunc(result) + 1
    else:
        result = first
    print(result)

except ValueError:
    print("INVALID INPUT")
