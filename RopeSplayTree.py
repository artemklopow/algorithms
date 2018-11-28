class Node:

    def __init__(self, char):
        self.char = char
        self.parent = None
        self.is_parent_left = False
        self.left_son = None
        self.right_son = None
        self.sum = 1

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

        b.sum = C_sum + D_sum + 1
        a.sum = B_sum + b.sum + 1
        u.sum = A_sum + a.sum + 1

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

        b.sum = C_sum + D_sum + 1
        a.sum = B_sum + b.sum + 1
        u.sum = A_sum + a.sum + 1

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

        b.sum = C_sum + D_sum + 1
        a.sum = A_sum + B_sum + 1
        u.sum = a.sum + b.sum + 1

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

        b.sum = C_sum + D_sum + 1
        a.sum = A_sum + B_sum + 1
        u.sum = a.sum + b.sum + 1

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

        a.sum = B_sum + C_sum + 1
        u.sum = a.sum + A_sum + 1

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

        a.sum = B_sum + C_sum + 1
        u.sum = a.sum + A_sum + 1

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

    def split(self, index, left_cut):

        root = self.search(index)

        if root is None:
            return self, None

        if left_cut:
            small_root = root
            big_root = root.right_son

            small_root.right_son = None
            small_left_sum = small_root.left_son.sum if small_root.left_son is not None else 0
            small_root.sum = small_left_sum + 1

            if big_root is not None:
                big_root.parent = None

        else:
            small_root = root.left_son
            big_root = root

            big_root.left_son = None
            big_right_sum = big_root.right_son.sum if big_root.right_son is not None else 0
            big_root.sum = big_right_sum + 1

            if small_root is not None:
                small_root.parent = None

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
        root.sum = left_sum + big_root.sum + 1

        big_root.parent = root
        big_root.is_parent_left = True

        return root

    def search(self, index):

        now_node = self
        search_index = index
        if index > now_node.sum:
            return None
        while now_node is not None:
            left_sum = now_node.left_son.sum if now_node.left_son is not None else 0
            if search_index == left_sum + 1:
                root = self.splay(now_node)
                return root
            if search_index > left_sum + 1:
                search_index = search_index - left_sum - 1
                now_node = now_node.right_son
            else:
                now_node = now_node.left_son

        return None


if __name__ == '__main__':
    root = None
    string = 'hlelowrold'
    for char in string:
        if root is None:
            root = Node(char)
        else:
            root = root.merge(root, Node(char))

    print(root)