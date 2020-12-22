import csv
genre = input('What genre do you prefer?\n')
platform = input('Which platform you use to play?\n')
type_ = input('Single- or Multiplayer?\n')
status = True

if not genre and not platform and not type_:
	print('Sorry I don`t what I`m looking for...')
	status = False
if not genre and platform and type_:
	genre = platform
if genre and not platform and type_:
	platform = genre
if genre and platform and not type_:
	type_ = platform
if not genre and not platform and type_:
	genre = type_
	platform = type_
if genre and not platform and not type_:
	platform = genre
	type_ = genre
if not genre and platform and not type_:
	genre = platform
	type_ = platform

def game_suggester(genre,platform,type_):
	if status == True:
		with open ('steam.csv', newline = '') as f:
			a = []
			spam = csv.reader(f)
			for row in spam:
				if (genre) and (platform) and (type_) in row:
					a.append(row[1])
			a = list(dict.fromkeys(a))
		with open ('final.txt', 'w') as fin:
			for i in range (1,len(a)):
				fin.write(str(a[i]) + '\n')
game_suggester(genre, platform, type_)
