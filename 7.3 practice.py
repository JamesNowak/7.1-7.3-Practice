girls = open("GirlNames.txt", 'r')

girl_names = girls.readlines()
girls.close()

indexgirl = 0
while indexgirl < len(girl_names):
    girl_names[indexgirl] = girl_names[indexgirl].rstrip('\n')
    indexgirl += 1

boys = open("BoyNames.txt", 'r')

boy_names = boys.readlines()
boys.close()

indexboy = 0
while indexboy < len(boy_names):
    boy_names[indexboy] = boy_names[indexboy].rstrip('\n')
    indexboy += 1

name1 = input('Enter a boy name: ')
name2 = input('Enter a girl name: ')

if name1 in boy_names:
    print('Yes', name1, 'is in the list.')
else:
    print('No', name1, 'is not in the list.')

if name2 in boy_names:
    print('Yes', name2, 'is in the list.')
else:
    print('No', name2, 'is not in the list.')
