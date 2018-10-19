import random
user = int(input("Pick a number 1-100: "))
num = []
var = 0
while var <= 19:
    var = var + 1
    ran = random.randint(1, 101)
    if ran > user:
        num = num + [ran]
if num is None:
    print('No numbers are larger than the entered number')
