#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

class Board:

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
        while True:
            moves = self.valid_moves()
            for move in moves:
                temp = Node(current_node, self.make_move(move), self, current_node.depth + 1)
                # print(temp.matrix)
                if temp.is_finished():
                    print('Achou !!!!')
                    print('A profundidade é %s' % temp.depth)
                    return True
                else:
                    to_visit.append(temp)
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
    
    def get_similarity(self):
        # print("LEN: ")
        # print(len(self.matrix))
        # print(len(self.matrix[1]))
        g = 0
        for i in range(len(self.matrix)):
            # print("I: %s" % str(i))
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.board.goal[i][j] and self.matrix[i][j] != 0:
                    # print(g)
                    g += 1
        
        return 7 - g

    def is_finished(self):
        return self.matrix == self.board.goal
    

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

board = Board(matrix_start, matrix_end)
board.get_result()
# board.a_star()