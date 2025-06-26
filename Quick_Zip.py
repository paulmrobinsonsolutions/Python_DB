# Just some dabbling with zip. It's slick.

names = ['Keanu', 'Dwayne Johnson', 'Chris Farley']
heroes = ['John Wick', 'The Rock', 'American Ninja']

print()
for name, hero in zip(names, heroes):
    print(f'{name} really is {hero}')
