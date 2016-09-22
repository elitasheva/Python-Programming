import requests
from datetime import datetime, timezone
API_URL = "http://api.openweathermap.org/data/2.5/weather"
KELVIN_CONST = 273.15
user_input_city = input("Въведете град: ")

response = requests.get(API_URL, timeout=20, params={'q': user_input_city, 'appid': "965acdac1ae64cf06761bb563ad34d96"})

print("Извличане на данни...")
if response.status_code == 200:
    response_json_dict = response.json()

    timestamp = response_json_dict.get('dt', None)
    if timestamp:
        current_date = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        print("Информация към: {}".format(current_date.strftime("%d.%m.%Y %H:%M")))
    else:
        print("Няма информация за датата!")

    main_data = response_json_dict.get('main', None)
    if main_data:

        temp_kelvin = main_data.get('temp', None)
        if temp_kelvin:
            temp_celsius = temp_kelvin - KELVIN_CONST
            print("Температура: {:.2f}C".format(temp_celsius))
        else:
            print("Няма данни за температура!")

        pressure = main_data.get('pressure', None)
        if pressure:
            print("Налягане: {}".format(pressure))
        else:
            print("Няма данни за налягане!")

        humidity = main_data.get('humidity', None)
        if humidity:
            print("Влажност: {}%".format(humidity))
        else:
            print("Няма данни за влажност!")

    else:
        print("Няма информация за налягане, влажност и температура!")

    wind = response_json_dict.get('wind', None)
    if wind:

        wind_speed = wind.get('speed', None)
        if wind_speed:
            print("Скорост на вятъра: {}м/с".format(wind_speed))
        else:
            print("Няма данни за скорост на вятъра!")
    else:
        print("Няма данни за вятър!")

else:
    print("Грешка в сървъра!", response.status_code)