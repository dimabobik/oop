def five_task():
    players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
    old_player = 0
    young_player = players[0]
    for elements in players:
        if elements > old_player:
            old_player = elements

    print('Вік найстаршого гравця: ', old_player)

    for el in players:
        if el < young_player:
            young_player = el
    print('Вік наймолодшого гравця: ', young_player)
    print(old_player, '+', young_player, '=', young_player + old_player, '\n '
                                                                          'Сума Наймолодшого і Найстаршого гравців')
