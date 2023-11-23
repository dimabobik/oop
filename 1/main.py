from function import *

while True:
    players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
    print('Вибери варіант:')
    message = int(input('1-10 \n'))
    if message == 1:
        print(five_task())
    else:
        print(players)
