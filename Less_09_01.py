import os
from progress.bar import ChargingBar
import time

pf = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
player = 1

def player_turn(player):
    return int(input(f'Ход игрока {player}: '))

def player_change(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def play(player, pf):
    num = player_turn(player)
    if player == 1:
        pf[num] = 'x'
    else:
        pf[num] = 'o'
    
    if pf[0] == pf[1] == pf[2] or pf[3] == pf[4] == pf[5] or pf[6] == pf[7] == pf[8]  or pf[0] == pf[4] == pf[8]  or pf[2] == pf[4] == pf[6]:
        print(f'Победил игрок {player}')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{pf[0]}|{pf[1]}|{pf[2]}\n- - -\n{pf[3]}|{pf[4]}|{pf[5]}\n- - -\n{pf[6]}|{pf[7]}|{pf[8]}')

        player = player_change(player)
        play(player, pf)

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    bar = ChargingBar('Processing', max=20)
    for i in range(20):
        time.sleep(0.2)
        bar.next()
    bar.finish()
    print('Загрузка завершена, приятной игры!')
    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{pf[0]}|{pf[1]}|{pf[2]}\n- - -\n{pf[3]}|{pf[4]}|{pf[5]}\n- - -\n{pf[6]}|{pf[7]}|{pf[8]}')

    play(player, pf)

start()