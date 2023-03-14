from olsen import play
from time import time

results = ''

for j in range(6, 15):

    player, rando = 0, 0

    start = time()
    for i in range(2 ** j):
        (player, rando) = play(player, rando)
    stop = time()

    results += "\n"
    results += "Games: " + str(2**j) + "\n"
    results += "Time: " + str(round(stop-start, 5)) + "s\n"
    results += "Player: " + str(player) + "\n"
    results += "Rando: " + str(rando) + "\n"

with open("results.txt", 'w') as file:
    file.write(results)
