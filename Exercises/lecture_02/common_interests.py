interests_ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
interests_maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

interests_ivan_set = set(interests_ivan)
interests_maria_set = set(interests_maria)
common_interests = interests_ivan_set.intersection(interests_maria_set)
print(common_interests)

