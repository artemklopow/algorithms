"""import sys


node = [value, left_son, right_son, parent, is_parent_left]
nodes = []
n = int(sys.stdin.readline().strip())
# sys.setrecursionlimit(n**2)
for _ in range(n):
    nodes.append([int(i) for i in sys.stdin.readline().strip().split()])
for node in nodes:
    node.append(None)
    node.append(None)


def left_subtree(index, node, max_val=-(2**31 + 1)):
    global nodes
    if nodes[index][3] is not None:
        return nodes[index][3]
    if node[1] == -1 and node[2] == -1:
        return node[0]
    if node[1] != -1:
        max_val = max(max_val, left_subtree(node[1], nodes[node[1]], max_val))
    if node[2] != -1:
        max_val = max(max_val, left_subtree(node[2], nodes[node[2]], max_val))
    nodes[index][3] = max_val
    return max_val


def right_subtree(index, node, min_val=(2**31 + 1)):
    global nodes
    if nodes[index][4] is not None:
        return nodes[index][4]
    if node[1] == -1 and node[2] == -1:
        return node[0]
    if node[1] != -1:
        min_val = min(min_val, left_subtree(node[1], nodes[node[1]], min_val))
    if node[2] != -1:
        min_val = min(min_val, left_subtree(node[2], nodes[node[2]], min_val))
    nodes[index][4] = min_val
    return min_val


result = 'CORRECT'
for i in range(len(nodes)):
    if len(nodes) == 0:
        result = 'INCORRECT'
        break
    node = nodes[i]
    if node[1] != -1:
        left_val = left_subtree(i, node)
        if left_val > node[0]:
            result = 'INCORRECT'
            break
    if node[2] != -1:
        right_val = right_subtree(i, node)
        if node[0] > right_val:
            result = 'INCORRECT'
            break

print(result)
"""

import sys


nodes = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    nodes.append([int(i) for i in sys.stdin.readline().strip().split()] + [2**31 + 1, -(2**31 + 1)])

result = 'CORRECT'

for i in range(n-1, -1, -1):

    now_node = nodes[i]
    now_value = now_node[0]

    if (now_node[1] != -1 and now_node[3] > now_value) or \
            (now_node[2] != -1 and now_value > now_node[4]):
        result = 'INCORRECT'
        break

    for j in range(i - 1, -1, -1):
        if i == nodes[j][1]:
            if nodes[i][1] != -1 and nodes[i][2] != -1:
                nodes[j][3] = max(now_value, nodes[i][3], nodes[i][4])
            elif nodes[i][1] != -1:
                nodes[j][3] = max(now_value, nodes[i][3])
            elif nodes[i][2] != -1:
                nodes[j][3] = max(now_value, nodes[i][4])
            else:
                nodes[j][3] = now_value
            break

        elif i == nodes[j][2]:
            if nodes[i][1] != -1 and nodes[i][2] != -1:
                nodes[j][4] = min(now_value, nodes[i][3], nodes[i][4])
            elif nodes[i][1] != -1:
                nodes[j][4] = min(now_value, nodes[i][3])
            elif nodes[i][2] != -1:
                nodes[j][4] = min(now_value, nodes[i][4])
            else:
                nodes[j][4] = now_value
            break

print(result)

"""
5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1
CORRECT

4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1
INCORRECT

3
2 1 2
1 -1 -1
3 -1 -1
CORRECT

7
4 1 2
2 3 4
6 5 6
1 -1 -1
3 -1 -1
5 -1 -1
7 -1 -1
CORRECT
"""