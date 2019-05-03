#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

class BFS:

    def __init__(self, matrix, goal, max_plays=None, max_time = None, start_time=None):
        self.matrix = matrix
        self.start = copy.deepcopy(matrix)
        self.goal = goal
        self.max_plays = max_plays
        self.max_time = max_time
        self.start_time = start_time

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

        while True:
            moves = self.valid_moves()
            for move in moves:
                temp = Node(current_node, self.make_move(move), self, current_node.depth + 1)
                # print(temp.matrix)
                if temp.is_finished():
                    print('Parabens, sua resposta foi encontrada :)')
                    print('O numero de passos foi %s' % temp.depth)

                    played = []
                    while temp.parent:
                        played.append(temp.matrix)
                        temp = temp.parent

                    played.reverse()

                    return played
                elif (self.max_plays != None) and self.max_plays < temp.depth:
                    print("Não consegui achar uma resposta nesse tempo :(")
                    print('O numero de passos foi %s' % temp.depth)

                    played = []
                    while temp.parent:
                        played.append(temp.matrix)
                        temp = temp.parent

                    played.reverse()

                    return played
                elif (self.max_time != None) and self.max_time < (self.start_time - time.time()):
                    print("Não consegui achar uma resposta nesse tempo :(")
                    print('O numero de passos foi %s' % temp.depth)

                    played = []
                    while temp.parent:
                        played.append(temp.matrix)
                        temp = temp.parent

                    played.reverse()

                    return played
                else:
                    explored.append(current_node)
                    if temp not in to_visit and temp not in explored: to_visit.append(temp)
            current_node = to_visit.pop(0)
            self.matrix = current_node.matrix
            self.empty = self.find_empty()

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

    def is_finished(self):
        return self.matrix == self.board.goal
    