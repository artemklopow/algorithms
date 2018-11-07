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
    if res[i] > res[i+1]:
        result = 'INCORRECT'
        break

if result == 'CORRECT':
    for node in nodes:
        if node[1] != -1 and nodes[node[1]][0] >= node[0]:
            result = 'INCORRECT'
            break

print(result)
