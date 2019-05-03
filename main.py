#!/usr/bin/python
# -*- coding: utf-8 -*-

from heuristica.heuristics import *
from bfs.bfs import *

import time


def main():

    matrix_start = [[2,0,3],[1,7,5],[6,4,8]]
    matrix_end = [[1,2,3],[8,0,4],[7,6,5]]

    print("###### 8 Puzzle game ########")
    print("Vamos jogar, mas antes precisamos de algumas informações")
    
    print("1 - Você quer uma solucação focada no tempo")
    print("2 - Você quer uma solucação baseada no número de jogadas")
    opc = int(input("Escolha o melhor criterio para definir as regras do jogo:"))

    if opc == 1:
        max_time = float(input("Digite o tempo máximo que você está disposto a esperar: "))
        print("")
        if max_time <= 1:
            # Time of right before the execution starts
            start = time.time()
            # Instance of the heuristics board to solve the problem
            board = Heuristics(matrix_start, matrix_end, max_time=max_time, start_time=start)
            # Solve the game
            moves = board.get_result()
            # Get finish time
            end = time.time()
            print("O tempo gasto foi de %.2fs" % (end - start))
        else:
            # Time of right before the execution starts
            start = time.time()
            # Breadth First Search so solve the game
            board = BFS(matrix_start, matrix_end, max_time=max_time, start_time=start)
            # Get result
            moves = board.get_result()
            # Get finishe time
            end = time.time()
            print("O tempo gasto foi de %.2fs" % (end - start))
    elif opc == 2:
        plays = input("Digite o número máximo de jogadas: ")
        print("")
        if plays <= 30:
            board = Heuristics(matrix_start, matrix_end, max_plays=plays)
            moves = board.get_result()
        else:
            board = BFS(matrix_start, matrix_end, max_plays=plays)
            moves = board.get_result()

    print("")
    print("As jogadas foram !")
    k = 1
    for matrix in moves:
        print(' # %s #' % k)
        for i in range(len(matrix)):
            print('| %s | %s | %s |' % (matrix[i][0], matrix[i][1], matrix[i][2]))
        print('')
        k += 1

if __name__ == "__main__":
    main()