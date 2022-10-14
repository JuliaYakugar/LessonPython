import random

candies = 2021
max_candies = 28
player = random.randint(1, 2)

def player_turn(player, candies):
    return int(input(f'Осталось {candies} конфет, ход игрока номер {player}: '))

def player_change(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def game_over(player):
    print(f'Победил игрок номер {player}')

def play(player, candies):
    candy = player_turn(player, candies)
    if candy < 1:
        print('Минимум 1 конфета')
        candy = player_turn(player, candies)
    if candy > max_candies:
        print('Максимум 28 конфет')
        candy = player_turn(player, candies)
    if candy > candies:
        print('Осталось меньше конфет')
        candy = player_turn(player, candies)
    if candies-candy == 0:
        game_over(player)
    else:
        candies = candies - candy
        player = player_change(player)
        play(player, candies)

def play_bot(player, candies):
    if player == 2:
        candy = random.randint(1, max_candies)
        print(f'Осталось {candies} конфет, ход игрока номер {player}: {candy}')
    else:
        candy = player_turn(player, candies)
    if candy < 1:
        print('Минимум 1 конфета')
        candy = player_turn(player, candies)
    if candy > max_candies:
        print('Максимум 28 конфет')
        candy = player_turn(player, candies)
    if candy > candies:
        print('Осталось меньше конфет')
        candy = player_turn(player, candies)
    if candies-candy == 0:
        game_over(player)
    else:
        candies = candies - candy
        player = player_change(player)
        play_bot(player, candies)
    
def play_bot2(player, candies):
    if player == 2:
        if candies > 56:
            candy = 28
        if candies == 56:
            candy = 27
        if candies < 56 and candies > 29:
            candy = candies - 29
        if candies == 29:
            candy = 1
        if candies <= 28:
            candy = candies
        print(f'Осталось {candies} конфет, ход игрока номер {player}: {candy}')
    else:
        candy = player_turn(player, candies)
    if candy < 1:
        print('Минимум 1 конфета')
        candy = player_turn(player, candies)
    if candy > max_candies:
        print('Максимум 28 конфет')
        candy = player_turn(player, candies)
    if candy > candies:
        print('Осталось меньше конфет')
        candy = player_turn(player, candies)
    if candies-candy == 0:
        game_over(player)
    else:
        candies = candies - candy
        player = player_change(player)
        play_bot2(player, candies)

game_mode = int(input('1 - против человека, 2 - против бота, 3 - против интеллекта: '))
if game_mode == 1:
    play(player, candies)
if game_mode == 2:
    play_bot(player, candies)
if game_mode == 3:
    play_bot2(player, candies)