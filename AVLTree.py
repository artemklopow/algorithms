class AVLTree:

    class Node:
        """Node of AVL tree"""

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left_son = None
            self.right_son = None
            self.parent = None
            self.is_parent_left = False  # Is parent left regarding node
            self.size = 1

        def is_root(self, tree):
            return self in tree.roots

    def __init__(self):
        self.roots = []
        self.__nodes = []

    def find(self, value, root):
        """Finds value in tree. Returns Node or None."""
        result = None
        now_node = root
        while now_node is not None:
            if now_node.value == value:
                result = now_node
                break
            elif value < now_node.value:
                now_node = now_node.left_son
            else:
                now_node = now_node.right_son
        return result

    def insert(self, ins_node: Node, root=None):
        """Inserts node in tree."""

        if self.find(ins_node.value, root) is not None:
            # In value already in tree, do nothing.
            return root

        self.__nodes.append(ins_node)

        # Indicator means from which side we`re came to none reference.
        indicator = None

        parent_node = None
        now_node = root

        # Looking for None reference...
        while now_node is not None:
            parent_node = now_node
            if ins_node.value < now_node.value:
                indicator = 'l'
                now_node = now_node.left_son
            else:
                indicator = 'r'
                now_node = now_node.right_son

        # ... and suspend node instead.
        if indicator is None:
            root = ins_node
            self.roots.append(ins_node)
        elif indicator == 'l':
            parent_node.left_son = ins_node
            ins_node.parent = parent_node
            ins_node.is_parent_left = False
        else:
            parent_node.right_son = ins_node
            ins_node.parent = parent_node
            ins_node.is_parent_left = True

        self.edit_height(ins_node)
        self.edit_size(ins_node)
        root = self.node_balance(ins_node, root)

        return root

    @staticmethod
    def edit_height(node: Node):
        """Edits height from node to root"""

        now_node = node
        while now_node is not None:
            left_height = 0 if now_node.left_son is None else now_node.left_son.height
            right_height = 0 if now_node.right_son is None else now_node.right_son.height
            now_height = (max(left_height, right_height)) + 1
            now_node.height = now_height
            now_node = now_node.parent

    @staticmethod
    def edit_size(node: Node):
        """ Edits sizes from node to root"""
        now_node = node
        while now_node is not None:
            ex_size = now_node.size
            left_size = now_node.left_son.size if now_node.left_son is not None else 0
            right_size = now_node.right_son.size if now_node.right_son is not None else 0
            new_size = left_size + right_size + 1
            if ex_size > 3 and ex_size == new_size:
                break
            now_node.size = new_size
            now_node = now_node.parent

    def change(self, top_node: Node, low_node: Node, root):
        """Changes two nodes"""


        top_parent = top_node.parent
        top_is_parent_left = top_node.is_parent_left
        top_left_son = top_parent.left_son
        top_right_son = top_node.right_son
        top_size = top_node.size
        top_height = top_node.height

        low_parent = low_node.parent
        low_is_parent_left = low_node.is_parent_left
        low_left_son = low_node.left_son
        low_right_son = low_node.right_son
        low_size = low_node.size
        low_height = low_node.height

        if top_node is low_node:
            pass

        elif low_node is top_node.left_son:
            low_node.parent = top_parent
            low_node.is_parent_left = top_is_parent_left
            if low_node.parent is not None and low_node.is_parent_left:
                low_node.parent.right_son = low_node
            elif low_node.parent is not None and not low_node.is_parent_left:
                low_node.parent.left_son = low_node
            low_node.left_son = top_node
            top_node.parent = low_node
            top_node.is_parent_left = False
            top_node.left_son = low_left_son
            if top_node.left_son is not None:
                top_node.left_son.parent = top_node
            top_node.right_son = low_right_son
            if top_node.right_son is not None:
                top_node.right_son.parent = top_node
            low_node.right_son = top_right_son
            if low_node.right_son is not None:
                low_node.right_son.parent = low_node

        elif low_node is top_node.right_son:
            low_node.parent = top_parent
            low_node.is_parent_left = top_is_parent_left
            if low_node.parent is not None and low_node.is_parent_left:
                low_node.parent.right_son = low_node
            elif low_node.parent is not None and not low_node.is_parent_left:
                low_node.parent.left_son = low_node
            low_node.right_son = top_node
            top_node.parent = low_node
            top_node.is_parent_left = True
            top_node.left_son = low_left_son
            if top_node.left_son is not None:
                top_node.left_son.parent = top_node
            top_node.right_son = low_right_son
            if top_node.right_son is not None:
                top_node.right_son.parent = top_node
            low_node.left_son = top_left_son
            if low_node.left_son is not None:
                low_node.left_son.parent = low_node

        else:

            # Low_node go up.
            low_node.parent = top_parent
            low_node.is_parent_left = top_is_parent_left
            if top_is_parent_left and top_parent is not None:
                top_parent.right_son = low_node
            elif not top_is_parent_left and top_parent is not None:
                top_parent.left_son = low_node

            low_node.left_son = top_left_son
            low_node.right_son = top_right_son
            if top_left_son is not None:
                top_left_son.parent = low_node
            if top_right_son is not None:
                top_right_son.parent = low_node

            # Top node go down.
            top_node.parent = low_parent
            top_node.left_son = low_left_son
            top_node.right_son = low_right_son
            top_node.is_parent_left = low_is_parent_left
            if low_is_parent_left and low_parent is not None:
                low_parent.right_son = top_node
            elif not low_is_parent_left and low_parent is not None:
                low_parent.left_son = top_node
            if low_left_son is not None:
                low_left_son.parent = top_node
            if low_right_son is not None:
                low_right_son.parent = top_node

        top_node.height, low_node.height = low_node.height, top_node.height
        top_node.size, low_node.size = low_node.size, top_node.size

        if top_parent is None:
            if top_node in self.roots:
                self.roots.remove(top_node)
            self.roots.append(low_node)
            root = low_node

        return root

    def delete(self, del_node: Node, root, with_node_balance=True):

        # If node don`t has any sons, just remove it.
        if del_node.left_son is None and del_node.right_son is None:
            parent_node = del_node.parent
            if parent_node is not None:
                # Del_node isn`t root.
                if del_node.is_parent_left:
                    parent_node.right_son = None
                else:
                    parent_node.left_son = None
            else:
                # Del_node is root.
                if del_node in self.roots:
                    self.roots.remove(del_node)
                root = None

        # If node has two sons.
        elif del_node.left_son is not None and del_node.right_son is not None:

            # Find most right node from left subtree.
            target_node = del_node.left_son
            while target_node.right_son is not None:
                target_node = target_node.right_son

            # Change them.
            root = self.change(del_node, target_node, root)

            parent_node = del_node.parent
            if del_node.is_parent_left:
                parent_node.right_son = None
            else:
                parent_node.left_son = None

        # If node has one son only.
        else:
            son_node = del_node.left_son or del_node.right_son
            root = self.change(del_node, son_node, root)
            parent_node = del_node.parent
            if del_node.is_parent_left:
                parent_node.right_son = None
            else:
                parent_node.left_son = None

        self.__nodes.remove(del_node)
        self.edit_height(parent_node)
        self.edit_size(parent_node)
        if with_node_balance:
            root = self.node_balance(parent_node, root)

        return root

    def small_right_rotation(self, a: Node, b: Node, root):

        a_parent = a.parent
        a_is_parent_left = a.is_parent_left

        C = b.right_son
        if C is not None:
            C.parent = a
            C.is_parent_left = False
        a.left_son = C
        a.parent = b
        a.is_parent_left = True

        b.parent = a_parent
        b.is_parent_left = a_is_parent_left
        b.right_son = a

        if a_parent is not None and a_is_parent_left:
            a_parent.right_son = b
        elif a_parent is not None and not a_is_parent_left:
            a_parent.left_son = b

        if b.parent is None:
            if a in self.roots:
                self.roots.remove(a)
            self.roots.append(b)
            root = b

        self.edit_height(a)
        self.edit_size(a)

        return root

    def small_left_rotation(self, a: Node, b: Node, root):

        a_parent = a.parent
        a_is_parent_left = a.is_parent_left

        C = b.left_son
        if C is not None:
            C.parent = a
            C.is_parent_left = True
        a.right_son = C
        a.parent = b
        a.is_parent_left = False

        b.parent = a_parent
        b.is_parent_left = a_is_parent_left
        b.left_son = a

        if a_parent is not None and a_is_parent_left:
            a_parent.right_son = b
        elif a_parent is not None and not a_is_parent_left:
            a_parent.left_son = b

        if b.parent is None:
            if a in self.roots:
                self.roots.remove(a)
            self.roots.append(b)
            root = b

        self.edit_height(a)
        self.edit_size(a)

        return root

    def big_right_rotation(self, a: Node, b: Node, c: Node, root):

        a_parent = a.parent
        a_is_parent_left = a.is_parent_left

        M = c.left_son
        N = c.right_son

        if M is not None:
            M.parent = b
            M.is_parent_left = True
        if N is not None:
            N.parent = a
            N.is_parent_left = False

        b.right_son = M
        b.parent = c
        b.is_parent_left = False

        a.left_son = N
        a.parent = c
        a.is_parent_left = True

        c.left_son = b
        c.right_son = a
        c.parent = a_parent
        c.is_parent_left = a_is_parent_left

        if a_parent is not None and a_is_parent_left:
            a_parent.right_son = c
        elif a_parent is not None and not a_is_parent_left:
            a_parent.left_son = c

        if c.parent is None:
            if a in self.roots:
                self.roots.remove(a)
            self.roots.append(c)
            root = c

        self.edit_height(a)
        self.edit_height(b)
        self.edit_size(a)
        self.edit_size(b)

        return root

    def big_left_rotation(self, a:Node, b: Node, c: Node, root):

        a_parent = a.parent
        a_is_parent_left = a.is_parent_left

        M = c.left_son
        N = c.right_son

        if M is not None:
            M.parent = a
            M.is_parent_left = True
        if N is not None:
            N.parent = b
            N.is_parent_left = False

        b.left_son = N
        b.parent = c
        b.is_parent_left = True

        a.right_son = M
        a.parent = c
        a.is_parent_left = False

        c.left_son = a
        c.right_son = b
        c.parent = a_parent
        c.is_parent_left = a_is_parent_left

        if a_parent is not None and a_is_parent_left:
            a_parent.right_son = c
        elif a_parent is not None and not a_is_parent_left:
            a_parent.left_son = c

        if c.parent is None:
            if a in self.roots:
                self.roots.remove(a)
            self.roots.append(c)
            root = c

        self.edit_height(a)
        self.edit_height(b)
        self.edit_size(a)
        self.edit_size(b)

        return root

    def node_balance(self, node: Node, root):

        now_node = node
        while now_node is not None:
            next_node = now_node.parent
            a = now_node
            left_height = 0 if now_node.left_son is None else now_node.left_son.height
            right_height = 0 if now_node.right_son is None else now_node.right_son.height
            if left_height - right_height == 2:
                b = a.left_son
                b_left_height = 0 if b.left_son is None else b.left_son.height
                b_right_height = 0 if b.right_son is None else b.right_son.height
                if b_right_height <= b_left_height:
                    root = self.small_right_rotation(a, b, root)
                else:
                    c = b.right_son
                    root = self.big_right_rotation(a, b, c, root)
            elif right_height - left_height == 2:
                b = a.right_son
                b_left_height = 0 if b.left_son is None else b.left_son.height
                b_right_height = 0 if b.right_son is None else b.right_son.height
                if b_left_height <= b_right_height:
                    root = self.small_left_rotation(a, b, root)
                else:
                    c = b.left_son
                    root = self.big_left_rotation(a, b, c, root)

            now_node = next_node

        return root

    def find_by_index(self, index, root):
        """Finds value by index. Retuns value or None (if something goes wrong). INDEXES STARTS FROM 1"""
        now_node = root
        now_index = index
        while now_node is not None:
            left_size = now_node.left_son.size if now_node.left_son is not None else 0
            if now_index == left_size + 1:
                return now_node.value
            elif now_index < left_size + 1:
                now_node = now_node.left_son
            else:
                now_index = now_index - left_size - 1
                now_node = now_node.right_son
        return None  # Just in case.

    def get_max_node(self, node):
        """Returns max value node"""
        now_node = node
        while now_node.right_son is not None:
            now_node = now_node.right_son
        return now_node

    def get_min_node(self, node):
        """Returns min value node"""
        now_node = node
        while now_node.left_son is not None:
            now_node = now_node.left_son
        return now_node

    def find_right_subtree_for_merge(self, height, root):
        """Finds right subtree which equal height"""
        subtree_root = root
        while subtree_root.height - height > 1:
            subtree_root = subtree_root.right_son
        return subtree_root

    def find_left_subtree_for_merge(self, height, root):
        """Finds right subtree which equal height"""
        subtree_root = root
        while subtree_root.height - height > 1:
            subtree_root = subtree_root.left_son
        return subtree_root

    def merge_with_root(self, v1: Node, v2: Node, T: Node, merge_to_left: bool, root: Node):
        """Just change references"""
        v1_parent = v1.parent
        v1_is_parent_left = v1.is_parent_left

        T.parent = v1_parent
        T.is_parent_left = v1_is_parent_left

        if v1_parent is not None and v1_is_parent_left:
            v1_parent.right_son = T
        elif v1_parent is not None and not v1_is_parent_left:
            v1_parent.left_son = T

        v1.parent = T
        v2.parent = T
        if merge_to_left:
            T.left_son = v1
            T.right_son = v2
            v1.is_parent_left = False
            v2.is_parent_left = True
        else:
            T.left_son = v2
            T.right_son = v1
            v1.is_parent_left = True
            v2.is_parent_left = False

        self.edit_height(T)
        self.edit_size(T)
        root = self.node_balance(v1, root)
        root = self.node_balance(v2, root)
        if v2 in self.roots:
            self.roots.remove(v2)
        if T.parent is None:
            if v1 in self.roots:
                self.roots.remove(v1)
            if T not in self.roots:
                self.roots.append(T)
            root = T
        return root

    def glue_tree_(self, root_1, root_2):
        """Glue trees. root_1 contains less values!"""

        if root_2 is None:
            return root_1
        elif root_1 is None:
            return root_2
        elif root_1 is None and root_2 is None:
            return None
        elif root_1 is root_2:
            return root_1

        # If self.height >= other.height
        if root_1.height >= root_2.height:
            v1 = self.find_right_subtree_for_merge(root_2.height, root_1)
            T = self.get_max_node(v1)
            root_1 = self.delete(T, root_1, with_node_balance=False)
            self.__nodes.append(T)
            v2 = root_2
            new_root = self.merge_with_root(v1, v2, T, merge_to_left=True, root=root_1)
            return new_root

        else:
            v1 = self.find_left_subtree_for_merge(root_1.height, root_2)
            T = self.get_min_node(v1)
            self.delete(T, root_2, with_node_balance=False)
            self.__nodes.append(T)
            v2 = root_1
            new_root = self.merge_with_root(v1, v2, T, False, root=root_2)
            return new_root

    # TODO
    def split(self, key, root):
        now_node = root
        small_root = None
        big_root = None
        while now_node is not None:
            if key >= now_node.value:
                next_node = now_node.right_son
                left_root_for_merge = now_node.left_son

                if now_node.left_son is not None:
                    now_node.left_son.parent = None
                if now_node.right_son is not None:
                    now_node.right_son.parent = None
                now_node.height = 1
                now_node.left_son = None
                now_node.right_son = None
                now_node.parent = None
                now_node.is_parent_left = False
                now_node.size = 1
                self.__nodes.remove(now_node)
                if now_node in self.roots:
                    self.roots.remove(now_node)

                left_root_for_merge = self.insert(now_node, left_root_for_merge)
                small_root = self.glue_tree_(small_root, left_root_for_merge)
                now_node = next_node

            else:
                next_node = now_node.left_son
                right_root_for_merge = now_node.right_son

                if now_node.left_son is not None:
                    now_node.left_son.parent = None
                if now_node.right_son is not None:
                    now_node.right_son.parent = None
                now_node.height = 1
                now_node.left_son = None
                now_node.right_son = None
                now_node.parent = None
                now_node.is_parent_left = False
                now_node.size = 1
                self.__nodes.remove(now_node)
                if now_node in self.roots:
                    self.roots.remove(now_node)
                right_root_for_merge = self.insert(now_node, right_root_for_merge)
                big_root = self.glue_tree_(right_root_for_merge, big_root)
                now_node = next_node

        self.roots = [small_root, big_root]


if __name__ == '__main__':
    tree = AVLTree()
    root_1 = tree.insert(AVLTree.Node(10))
    root_1 = tree.insert(AVLTree.Node(8), root_1)
    root_1 = tree.insert(AVLTree.Node(3), root_1)
    root_1 = tree.insert(AVLTree.Node(4), root_1)
    root_1 = tree.insert(AVLTree.Node(5), root_1)
    """
    root_1 = tree.insert(AVLTree.Node(9), root_1)
    root_1 = tree.insert(AVLTree.Node(6), root_1)
    root_1 = tree.insert(AVLTree.Node(1), root_1)
    root_1 = tree.insert(AVLTree.Node(2), root_1)
    root_1 = tree.insert(AVLTree.Node(7), root_1)
    """
    print(tree.roots)


    root_2 = tree.insert(AVLTree.Node(21))
    root_2 = tree.insert(AVLTree.Node(20), root_2)
    root_2 = tree.insert(AVLTree.Node(35), root_2)
    root_2 = tree.insert(AVLTree.Node(33), root_2)
    root_2 = tree.insert(AVLTree.Node(40), root_2)
    root_2 = tree.insert(AVLTree.Node(50), root_2)
    root_2 = tree.insert(AVLTree.Node(60), root_2)
    root_2 = tree.insert(AVLTree.Node(55), root_2)
    print(tree.roots)

    new_root = tree.glue_tree_(root_1, root_2)
    tree.split(20, new_root)
    print(*tree.roots)
    print(tree.find_by_index(4, new_root))
    print(tree.find_by_index(0, new_root))
    print(tree.find_by_index(10, new_root))
    print(tree.find_by_index(1, new_root))
