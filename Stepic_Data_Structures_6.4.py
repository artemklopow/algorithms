import sys
import doctest

class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.is_parent_left = False
        self.left_son = None
        self.right_son = None
        self.sum = value

    @staticmethod
    def left_zigzig(u, a, b, A, B, C, D):

        main_parent = b.parent
        main_is_parent_left = b.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.right_son = a
        a.parent = u
        a.is_parent_left = True

        a.left_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = False

        a.right_son = b
        b.parent = a
        b.is_parent_left = True

        b.left_son = C
        if C is not None:
            C.parent = b
            C.is_parent_left = False

        C_sum = C.sum if C is not None else 0
        D_sum = D.sum if D is not None else 0
        B_sum = B.sum if B is not None else 0
        A_sum = A.sum if A is not None else 0

        b.sum = C_sum + D_sum + b.value
        a.sum = B_sum + b.sum + a.value
        u.sum = A_sum + a.sum + u.value

    @staticmethod
    def right_zigzig(u, a, b, A, B, C, D):

        main_parent = b.parent
        main_is_parent_left = b.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.left_son = a
        a.parent = u
        a.is_parent_left = False

        a.right_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = True

        a.left_son = b
        b.parent = a
        b.is_parent_left = False

        b.right_son = C
        if C is not None:
            C.parent = b
            C.is_parent_left = True

        C_sum = C.sum if C is not None else 0
        D_sum = D.sum if D is not None else 0
        B_sum = B.sum if B is not None else 0
        A_sum = A.sum if A is not None else 0

        b.sum = C_sum + D_sum + b.value
        a.sum = B_sum + b.sum + a.value
        u.sum = A_sum + a.sum + u.value

    @staticmethod
    def left_zigzag(u, a, b, A, B, C, D):

        main_parent = a.parent
        main_is_parent_left = a.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.left_son = a
        a.parent = u
        a.is_parent_left = False

        a.right_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = True

        u.right_son =b
        b.parent = u
        b.is_parent_left = True

        b.left_son = C
        if C is not None:
            C.parent = b
            C.is_parent_left = False

        C_sum = C.sum if C is not None else 0
        D_sum = D.sum if D is not None else 0
        B_sum = B.sum if B is not None else 0
        A_sum = A.sum if A is not None else 0

        b.sum = C_sum + D_sum + b.value
        a.sum = A_sum + B_sum + a.value
        u.sum = a.sum + b.sum + u.value

    @staticmethod
    def right_zigzag(u, a, b, A, B, C, D):

        main_parent = a.parent
        main_is_parent_left = a.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.right_son = a
        a.parent = u
        a.is_parent_left = True

        a.left_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = False

        u.left_son = b
        b.parent = u
        b.is_parent_left = False

        b.right_son = C
        if C is not None:
            C.parent = b
            C.is_parent_left = True

        C_sum = C.sum if C is not None else 0
        D_sum = D.sum if D is not None else 0
        B_sum = B.sum if B is not None else 0
        A_sum = A.sum if A is not None else 0

        b.sum = C_sum + D_sum + b.value
        a.sum = A_sum + B_sum + a.value
        u.sum = a.sum + b.sum + u.value

    @staticmethod
    def left_zig(u, a, A, B, C):

        main_parent = a.parent
        main_is_parent_left = a.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.right_son = a
        a.parent = u
        a.is_parent_left = True

        a.left_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = False

        A_sum = A.sum if A is not None else 0
        B_sum = B.sum if B is not None else 0
        C_sum = C.sum if C is not None else 0

        a.sum = B_sum + C_sum + a.value
        u.sum = a.sum + A_sum + u.value

    @staticmethod
    def right_zig(u, a, A, B, C):

        main_parent = a.parent
        main_is_parent_left = a.is_parent_left

        if main_parent is not None and not main_is_parent_left:
            main_parent.left_son = u
        elif main_parent is not None and main_is_parent_left:
            main_parent.right_son = u

        u.parent = main_parent
        u.is_parent_left = main_is_parent_left

        u.left_son = a
        a.parent = u
        a.is_parent_left = False

        a.right_son = B
        if B is not None:
            B.parent = a
            B.is_parent_left = True

        A_sum = A.sum if A is not None else 0
        B_sum = B.sum if B is not None else 0
        C_sum = C.sum if C is not None else 0

        a.sum = B_sum + C_sum + a.value
        u.sum = a.sum + A_sum + u.value

    def splay(self, u):

        while u.parent is not None:

            if not u.is_parent_left and u.parent.parent is not None and not u.parent.is_parent_left:
                A = u.left_son
                B = u.right_son
                a = u.parent
                C = a.right_son
                b = a.parent
                D = b.right_son
                self.left_zigzig(u, a, b, A, B, C, D)

            elif u.is_parent_left and u.parent.parent is not None and u.parent.is_parent_left:
                A = u.right_son
                B = u.left_son
                a = u.parent
                C = a.left_son
                b = a.parent
                D = b.left_son
                self.right_zigzig(u, a, b, A, B, C, D)

            elif not u.is_parent_left and u.parent.parent is not None and u.parent.is_parent_left:
                B = u.left_son
                C = u.right_son
                b = u.parent
                D = b.right_son
                a = b.parent
                A = a.left_son
                self.left_zigzag(u, a, b, A, B, C, D)

            elif u.is_parent_left and u.parent.parent is not None and not u.parent.is_parent_left:
                C = u.left_son
                B = u.right_son
                b = u.parent
                D = b.left_son
                a = b.parent
                A = a.right_son
                self.right_zigzag(u, a, b, A, B, C, D)

            elif not u.is_parent_left and u.parent.parent is None:
                A = u.left_son
                B = u.right_son
                a = u.parent
                C = a.right_son
                self.left_zig(u, a, A, B, C)

            elif u.is_parent_left and u.parent.parent is None:
                B = u.left_son
                A = u.right_son
                a = u.parent
                C = a.left_son
                self.right_zig(u, a, A, B, C)

        return u

    def insert(self, value):

        parent = None
        now_node = self
        indicator = None

        while now_node is not None:
            parent = now_node
            if value > now_node.value:
                next_node = now_node.right_son
                indicator = 'r'
            elif value < now_node.value:
                next_node = now_node.left_son
                indicator = 'l'
            else:
                root = self.splay(now_node)
                return root
            now_node = next_node

        ins_node = Node(value)
        if parent is None:
            return ins_node
        elif indicator == 'l':
            parent.left_son = ins_node
            ins_node.parent = parent
            ins_node.is_parent_left = False
            right_sum = parent.right_son.sum if parent.right_son is not None else 0
            parent.sum = ins_node.sum + right_sum + parent.value
        else:
            parent.right_son = ins_node
            ins_node.parent = parent
            ins_node.is_parent_left = True
            left_sum = parent.left_son.sum if parent.left_son is not None else 0
            parent.sum = ins_node.sum + left_sum + parent.value

        root = self.splay(ins_node)
        return root

    def split(self, key):

        now_node = self
        parent = None
        indicator = None

        while now_node is not None:
            parent = now_node
            if key < now_node.value:
                indicator = 'l'
                now_node = now_node.left_son
            elif key > now_node.value:
                indicator = 'r'
                now_node = now_node.right_son
            else:
                indicator = 'r'
                break

        root = self.splay(parent)

        if indicator == 'r':
            small_root = root
            big_root = root.right_son

            small_root.right_son = None
            left_sum = small_root.left_son.sum if small_root.left_son is not None else 0
            small_root.sum = left_sum + small_root.value

            if big_root is not None:
                big_root.parent = None

        else:
            small_root = root.left_son
            if small_root is not None:
                small_root.parent = None

            big_root = root
            big_root.left_son = None
            right_sum = big_root.right_son.sum if big_root.right_son is not None else 0
            big_root.sum = right_sum + big_root.value

        return small_root, big_root

    def merge(self, small_root, big_root):

        if small_root is None:
            return big_root
        if big_root is None:
            return small_root

        now_node = small_root
        while now_node is not None:
            if now_node.right_son is None:
                break
            now_node = now_node.right_son

        root = self.splay(now_node)

        root.right_son = big_root
        left_sum = root.left_son.sum if root.left_son is not None else 0
        root.sum = left_sum + big_root.sum + root.value

        big_root.parent = root
        big_root.is_parent_left = True

        return root

    def remove(self, value):

        parent = None
        now_node = self

        while now_node is not None:
            parent = now_node
            if value > now_node.value:
                next_node = now_node.right_son
            elif value < now_node.value:
                next_node = now_node.left_son
            else:
                break
            now_node = next_node

        if now_node is None:
            if parent is None:
                return None
            root = self.splay(parent)
            return root

        root = self.splay(now_node)

        left_root = root.left_son
        if left_root is not None:
            left_root.parent = None

        right_root = root.right_son
        if right_root is not None:
            right_root.parent = None

        root.left_son = None
        root.right_son = None

        root = self.merge(left_root, right_root)
        return root

    def search(self, key):

        res = False
        now_node = self
        parent = now_node
        while now_node is not None:
            parent = now_node
            if key < now_node.value:
                now_node = now_node.left_son
            elif key > now_node.value:
                now_node = now_node.right_son
            else:
                res = True
                break
        root = self.splay(parent)
        return root, res

def read():
    n = int(sys.stdin.readline())
    read = ['' for _ in range(n)]
    for i in range(n):
        read[i] = sys.stdin.readline().strip()
    return read


def fnc(i, s=0):
    return (i + s) % 1_000_000_001

def stpk(read):
    """
    >>> stpk(['? 1', '+ 1', '? 1', '+ 2', 's 1 2', '+ 1000000000', '? 1000000000', '- 1000000000', '? 1000000000', 's 999999999 1000000000', '- 2', '? 2', '- 0', '+ 9', 's 0 9'])
    ['Not found', 'Found', '3', 'Found', 'Not found', '1', 'Not found', '10']
    >>> stpk(['5', '? 0', '+ 0', '? 0', '- 0', '? 0'])
    ['Not found', 'Found', 'Not found']
    >>> stpk(['5', '+ 491572259', '? 491572259', '? 899375874', 's 310971296 877523306', '+ 352411209'])
    ['Found', 'Not found', '491572259']
    """
    s = 0
    root = None
    result = []
    for line in read:
        data = line.split()
        if data[0] == '+':
            i = fnc(int(data[1]), s)
            if root is None:
                root = Node(i)
            else:
                root = root.insert(i)

        elif data[0] == '-':
            if root is None:
                continue
            i = fnc(int(data[1]), s)
            root = root.remove(i)
        elif data[0] == '?':
            if root is None:
                result.append('Not found')
                continue
            i = fnc(int(data[1]), s)
            root, res = root.search(i)
            if res:
                result.append('Found')
            else:
                result.append('Not found')

        elif data[0] == 's':
            l = fnc(int(data[1]), s)
            r = fnc(int(data[2]), s)
            if root is None:
                s = 0
                result.append(str(s))
                continue
            else:
                root_1, root_2 = root.split(l-1)
                if root_2 is None:
                    s = 0
                    result.append(str(s))
                    root = root_1
                    continue
                root_2, root_3 = root_2.split(r)
                s = root_2.sum if root_2 is not None else 0
                if root_2 is not None:
                    root_2 = root_2.merge(root_2, root_3)
                else:
                    root_2 = root_3.merge(root_2, root_3)
                root = root_2.merge(root_1, root_2)
                result.append(str(s))

    return result


if __name__ == '__main__':
    doctest.testmod()
    read = read()
    result = stpk(read)
    out = '\n'.join(result)
    print(out)
