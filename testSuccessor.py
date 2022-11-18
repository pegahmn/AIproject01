import numpy as np
from Node import Node
from Environment import Environment
from Agent import Agent

state = np.asarray(
    [['x', 'x', 'x', 'x', 'x'],
    ['x', '1p', '2b', '1p', 'x'],
    ['1', '1r', '2b', '1', '1'],
    ['1', '1', '2', '1', '1']], dtype= np.str_
)

table = np.asarray(
    [
        ['x', 'x', 'x', 'x', 'x'],
        ['x', '1', '2', '1', 'x'],
        ['1', '1', '2', '1', '1'],
        ['1', '1', '2', '1', '1']
    ]
)

posPs = [[1, 1], [1, 3]]
posBs = [[1, 2], [2, 2]]
posR = [2, 1]

env = Environment(table, posPs)
agent = Agent(env)
root = Node(posR, posBs)
childs = agent.successor(root)

for child in childs:
    print(f"move = {child.move}")
    print(f"depth = {child.depth}")
    print(f"cost = {child.g}")
    for i in range(table.shape[0]):
        print(end= "\t")
        for j in range(table.shape[1]):
            cell = table[i, j]
            cell += 'p' if [i, j] in child.posBs else ''
            cell += 'b' if [i, j] in posPs else ''
            cell += 'r' if [i, j] == child.posR else ''
            print(cell, end= "\t")
        print()
    print("---------------------------------------------")