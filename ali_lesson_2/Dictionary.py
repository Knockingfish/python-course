Capital = {
	'Finland': 'Helsinki',
	'Sweden': 'Stockholm',
	'Norway': 'Oslo',
	'Denmark': 'Copenhagen'
	}
print(Capital)

Sanakirja = {
	'kirja': ['book', 'libro', 'libro'],
	'kurkku': [('cucumber', 'cetriolo', 'pepino'), ('throat', 'gola', 'garganta')],
	'pala': ['piece', 'petzo', 'pieza'],
	}

Sanakirja['ruoka'] = ['food', 'cibo', 'comida']
Sanakirja['yksi'] = ['one', 'uno', 'uno']

x = Sanakirja.get('kurkku')
print(x)

a = 'kurkku'
x = Sanakirja.get(a)
print(x)

print(Sanakirja)