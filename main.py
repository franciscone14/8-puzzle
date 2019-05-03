#!/usr/bin/python
# -*- coding: utf-8 -*-
# Adicionar a escolha do tempo de espera em passos ou se o usuario tem tempo para esperar achar a resposta
# Mostra a escolha do melhor metodo
# Distancia de manhatan ou a proximidade da solução (Ou os dois no caso da A*)

import copy

class BuscaAmplitude:

    def __init__(self, matrix, goal):
        self.matrix = matrix
        self.start = copy.deepcopy(matrix)
        self.goal = goal
        self.empty = self.find_empty()

    def find_empty(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0: return (i, j)
        
    def valid_moves(self):
        x, y = self.empty

        moves = []
        if x > 0: moves.append((x - 1, y))
        if y > 0: moves.append((x, y - 1))
        if x < 2: moves.append((x + 1, y))
        if y < 2: moves.append((x, y + 1))

        return moves

    def get_result(self):
        current_node = Node(None, self.matrix, self, 0)
        to_visit = []
        explored = []

        to_visit.append(current_node)

        while len(to_visit) > 0:
            current_node = to_visit.pop(0)
            self.matrix = current_node.matrix
            self.empty = self.find_empty()

            if current_node.h1() == 0:
                print("Parabens gamba, voce ganhou !")
                return
    
            moves = self.valid_moves()
            
            # Expande o node atual verificando todos os filhos
            children = []
            for move in moves:
                children.append(Node(current_node, self.make_move(move), self, current_node.depth + 1))

            for son in children:
                if son.matrix in explored:
                    print("Removed")
                    children.remove(son)
                
            # Verifica meu menor h
            h = 9
            for son in children:
                print(son.matrix)
                if son.h1() < h:
                    h = son.h1()
            
            for son in children:
                if son.h1() == h:
                    to_visit.append(son)
            
            explored.append(current_node.matrix)
            

    def make_move(self, move):
        x, y = self.empty
        x_m, y_m = move

        aux = copy.deepcopy(self.matrix)
        aux[x][y] = aux[x_m][y_m]
        aux[x_m][y_m] = 0

        return aux


class Node:

    def __init__(self, parent, matrix, board, depth):
        self.parent = parent
        self.matrix = matrix
        self.board = board
        self.depth = depth

    def h1(self):
        h1 = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if(self.matrix[i][j] != self.board.goal[i][j]):
                    h1 += 1
        return h1
    

matrix_start = [
    [2,0,3],
    [1,7,4],
    [6,8,5]
]

matrix_end = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]

board = BuscaAmplitude(matrix_start, matrix_end)
moves = board.get_result()

# print("As jogadas foram !")
# k = 1
# for matrix in moves:
#     print(' # %s #' % k)
#     for i in range(len(matrix)):
#         print('| %s | %s | %s |' % (matrix[i][0], matrix[i][1], matrix[i][2]))
#     print('')
#     k += 1
# board.a_star()
