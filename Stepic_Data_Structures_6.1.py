import sys


def in_order(node: list, nodes):

    if not node[1] == -1:
        in_order(nodes[node[1]], nodes)
    print(node[0], end=' ')
    if not node[2] == -1:
        in_order(nodes[node[2]], nodes)


def pre_order(node, nodes):

    print(node[0], end=' ')
    if not node[1] == -1:
        pre_order(nodes[node[1]], nodes)
    if not node[2] == -1:
        pre_order(nodes[node[2]], nodes)


def post_order(node, nodes):

    if not node[1] == -1:
        post_order(nodes[node[1]], nodes)
    if not node[2] == -1:
        post_order(nodes[node[2]], nodes)
    print(node[0], end=' ')


nodes = []

for _ in range(int(sys.stdin.readline().strip())):
    nodes.append([int(i) for i in sys.stdin.readline().strip().split()])


in_order(nodes[0], nodes)
print('\n')

pre_order(nodes[0], nodes)
print('\n')

post_order(nodes[0], nodes)
print('\n')
