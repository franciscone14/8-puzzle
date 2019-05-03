#!/usr/bin/python
# -*- coding: utf-8 -*-
# Adicionar a escolha do tempo de espera em passos ou se o usuario tem tempo para esperar achar a resposta
# Mostra a escolha do melhor metodo
# Distancia de manhatan ou a proximidade da solução (Ou os dois no caso da A*)

import copy
import time

class Heuristics:

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

        to_visit.append(current_node)

        while len(to_visit) > 0:
            current_node = to_visit.pop(0)
            self.matrix = current_node.matrix
            
            # matrix = self.matrix
            # for i in range(len(matrix)):
            #     print('| %s | %s | %s |' % (matrix[i][0], matrix[i][1], matrix[i][2]))
            # print('')

            self.empty = self.find_empty()

            # Se não existem peças fora da posição então ganhou
            if current_node.h1() == 0:
                print("Parabens, voce ganhou !")
                temp = current_node
                # Prepara a lista de nós para a exibição
                played = []
                while temp.parent:
                    played.append(temp.matrix)
                    temp = temp.parent

                played.reverse()

                return played
            # Se não ganhou verifica se o número máximo de jogadas foi atingida, caso
            # Definido
            elif (self.max_plays != None) and (self.max_plays - 1) < current_node.depth:
                print("Não consegui achar uma resposta nesse tempo :(")
                print('O numero de passos foi %s' % current_node.depth)

                temp = current_node
                played = []
                while temp.parent:
                    played.append(temp.matrix)
                    temp = temp.parent

                played.reverse()

                return played
            # Verifica se o tempo maximo foi atingido caso seja definido
            elif (self.max_time != None) and self.max_time < (time.time() - self.start_time):
                print("Não consegui achar uma resposta nesse tempo :(")
                print('O numero de passos foi %s' % current_node.depth)

                temp = current_node
                played = []
                while temp.parent:
                    played.append(temp.matrix)
                    temp = temp.parent

                played.reverse()

                return played
    
            moves = self.valid_moves()
            
            # Expande o node atual verificando todos os filhos
            children = []
            for move in moves:
                children.append(Node(current_node, self.make_move(move), self, current_node.depth + 1))

            # Remove as instancias ja existentes (ou percorridas)
            for son in children:
                if son.matrix in explored:
                    children.remove(son)
                
            # Verifica meu menor h
            h = 9
            for son in children:
                if son.h1() < h:
                    h = son.h1()
            
            for son in children:
                if son.h1() == h:
                    to_visit.append(son)
            
            explored.append(current_node.matrix)
            
    # Com base na lista de movimentos (move), expande o no atual nas opções possiveis
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

    # Heuristica que calcula o numero de elementos fora da sua posição
    # E retorna para o algoritmo de busca a melhor opção de nó a ser expandido
    def h1(self):
        h1 = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                # print("valores %d, %d => H: %d" %(self.matrix[i][j], self.board.goal[i][j], h1))
                if(self.matrix[i][j] != self.board.goal[i][j]):
                    h1 += 1
        return h1