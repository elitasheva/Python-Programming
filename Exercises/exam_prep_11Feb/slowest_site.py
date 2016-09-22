input_path = input()
SEARCHED_URL_FIELD = "url"
SEARCHED_RESP_FIELD = "resp_t"
EXCLUDED_FIELDS = "/ws/"
END_OF_FIELDS = " "

'''url(key of dict): list()(value of dict contains two values...index 0 -> sum of all times; index 1 -> count)'''
result_dict = {}
with open(input_path, encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            start_index_url = line.find(SEARCHED_URL_FIELD)
            end_index_url = line.find(END_OF_FIELDS, start_index_url)
            full_url_field = line[start_index_url:end_index_url]
            index_equal_sign = full_url_field.find("=")
            url = full_url_field[index_equal_sign + 2:-1]

            index_of_question_mark = url.find("?")
            if index_of_question_mark != -1:
                url = url[:index_of_question_mark]

            if url.endswith(EXCLUDED_FIELDS):
                continue
            else:
                if url not in result_dict:
                    result_dict[url] = [0, 0]

            start_index_resp = line.find(SEARCHED_RESP_FIELD)
            end_index_resp = line.find(END_OF_FIELDS, start_index_resp)
            full_resp_field = line[start_index_resp:end_index_resp]
            params_resp = full_resp_field.split("=")
            resp_str = params_resp[1][1:-1]

            try:
                resp = float(resp_str)
                result_dict[url][0] += resp
                result_dict[url][1] += 1

            except ValueError:
                print("INVALID INPUT")

max_time = None
url_with_min_time = None
for url, list_time in result_dict.items():
    current_time = list_time[0] / list_time[1]
    if max_time is None or current_time > max_time:
        max_time = current_time
        url_with_min_time = url

print(url_with_min_time)
print("{:.3f}".format(max_time))






