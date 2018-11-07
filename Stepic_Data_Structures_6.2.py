"""
ITERATIVE. FAILED TEST#2 ON STEPIC. WTF!?


import sys


nodes = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    nodes.append([int(i) for i in sys.stdin.readline().strip().split()] + [2**31 + 1, -(2**31 + 1)])

result = 'CORRECT'

for i in range(n-1, -1, -1):

    now_node = nodes[i]
    now_value = nodes[i][0]

    if (nodes[i][1] != -1 and nodes[i][3] >= now_value) or \
            (nodes[i][2] != -1 and now_value >= nodes[i][4]):
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

"""
def in_order(nodes, now_node, previous_value=-(2**31 + 1), result=True):
    if not result or previous_value >= now_node[0]:
        return False
    if now_node[1] != -1:
        result = in_order(nodes, nodes[now_node[1]], previous_value, result)
        previous_value = now_node[0]
    if previous_value >= now_node[0]:
        return False
    previous_value = now_node[0]
    if now_node[2] != -1:
        result = in_order(nodes, nodes[now_node[2]], previous_value,result)
    return result
"""

import sys


def in_order(nodes, now_node, res: list):
    if now_node[1] != -1:
        in_order(nodes, nodes[now_node[1]], res)
    res.append(now_node[0])
    if now_node[2] != -1:
        in_order(nodes, nodes[now_node[2]], res)
    return res


nodes = []
n = int(sys.stdin.readline().strip())
x = 300 if n < 5 else n**2
sys.setrecursionlimit(x)
res = []
for _ in range(n):
    nodes.append([int(i) for i in sys.stdin.readline().strip().split()] + [2**31 + 1, -(2**31 + 1)])

if n > 0:
    res = in_order(nodes, nodes[0], res)

result = 'CORRECT'
for i in range(n-1):
    if i+1 > n:
        break
    if res[i] >= res[i+1]:
        result = 'INCORRECT'
        break

print(result)




"""
3
2 1 2
1 -1 -1
3 -1 -1
CORRECT

3
1 1 2
2 -1 -1
3 -1 -1
INCORRECT

0
CORRECT

5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1
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

4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1
INCORRECT

6
2 1 2
4 3 -1
5 4 5
3 -1 -1
4 -1 -1
8 -1 -1
INCORRECT

3
2 1 2
2 -1 -1
2 -1 -1
"""