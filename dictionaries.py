city_dict = {'city': 'Москва', 'temperature': 20}
print(city_dict['city'])

print(city_dict['temperature'])

city_dict['temperature'] = city_dict['temperature'] - 5

print(city_dict['temperature'])

print(city_dict)

print(city_dict.get('country', 'Россия'))

city_dict["date"] = '27.05.2019'

print(city_dict)

print(len(city_dict))
