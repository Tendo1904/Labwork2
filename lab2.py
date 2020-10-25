import csv
print('What genre do you prefer?')
_genre = input()
print('Which platform you use to play?')
_platform = input()
print('Single- or Multiplayer')
_type = input()
status = True

if _genre == '' and _platform == '' and _type == '':
	print('Sorry I don`t what I`m looking for...')
	status = False
if _genre == '' and _platform != '' and _type != '':
	_genre = _platform
if _genre != '' and _platform == '' and _type != '':
	_platform = _genre
if _genre != '' and _platform != '' and _type == '':
	_type = _platform
if _genre == '' and _platform == '' and _type != '':
	_genre = _type
	_platform = _type
if _genre != '' and _platform == '' and _type == '':
	_platform = _genre
	_type = _genre
if _genre == '' and _platform != '' and _type == '':
	_genre = _platform 
	_type = _platform

def game_suggester(_genre,_platform,_type):
	if status == True:
		with open ('steam.csv', newline = '') as f:
			a = []
			spam = csv.reader(f)
			for row in spam:
				if (_genre) and (_platform) and (_type) in row:
					a.append(row[1])
			a = list(dict.fromkeys(a))
		with open ('final.txt', 'w') as fin:
			for i in range (1,len(a)):
				fin.write(str(a[i]) + '\n')
game_suggester(_genre,_platform,_type)	
