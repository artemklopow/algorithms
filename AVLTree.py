class AVLTree:

    class Node:
        """Node of AVL tree"""

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left_son = None
            self.right_son = None
            self.parent = None
            self.is_parent_left = False # Is parent left regarding node
            self.size = 1

        def is_root(self, tree):
            return self is tree.root

    def __init__(self):
        self.root = None
        self.__nodes = []
        self.other_root = None  # for split

    def find(self, value):
        """Finds value in tree. Returns Node or None."""

        result = None
        now_node = self.root
        while now_node is not None:
            if now_node.value == value:
                result = now_node
                break
            elif value < now_node.value:
                now_node = now_node.left_son
            else:
                now_node = now_node.right_son
        return result

    def insert(self, ins_node: Node):
        """Inserts node in tree."""

        if self.find(ins_node.value) is not None:
            # In value already in tree, do nothing.
            return

        self.__nodes.append(ins_node)

        # Indicator means from which side we`re came to none reference.
        indicator = None

        parent_node = None
        now_node = self.root

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
            self.root = ins_node
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
        self.node_balance(ins_node)

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

    def change(self, top_node: Node, low_node: Node):
        """Changes two nodes"""

        top_parent = top_node.parent
        top_left_son = top_node.left_son
        top_right_son = top_node.right_son
        top_is_parent_left = top_node.is_parent_left
        top_size = top_node.size

        low_parent = low_node.parent
        low_left_son = low_node.left_son
        low_right_son = low_node.right_son
        low_is_parent_left = low_node.is_parent_left
        low_size = low_node.size

        # Low_node go up.
        low_node.parent = top_parent
        low_node.left_son = top_left_son
        low_node.right_son = top_right_son
        low_node.is_parent_left = top_is_parent_left
        low_node.size = top_size
        if top_is_parent_left and top_parent is not None:
            top_parent.right_son = low_node
        elif not top_is_parent_left and top_parent is not None:
            top_parent.left_son = low_node
        if top_left_son is not None:
            top_left_son.parent = low_node
        if top_right_son is not None:
            top_right_son.parent = low_node

        # Top node go down.
        top_node.parent = low_parent
        top_node.left_son = low_left_son
        top_node.right_son = low_right_son
        top_node.is_parent_left = low_is_parent_left
        top_node.size = low_size
        if low_is_parent_left and low_parent is not None:
            low_parent.right_son = top_node
        elif not low_is_parent_left and low_parent is not None:
            low_parent.left_son = top_node
        if low_left_son is not None:
            low_left_son.parent = top_node
        if low_right_son is not None:
            low_right_son.parent = top_node

        top_node.height, low_node.height = low_node.height, top_node.height
        if top_node is self.root:
            self.root = low_node

    def delete(self, del_node: Node):

        # If node don`t has any sons, just remove it.
        if del_node.left_son is None and del_node.right_son is None:
            parent_node = del_node.parent
            if parent_node is not None:
                if del_node.is_parent_left:
                    parent_node.right_son = None
                else:
                    parent_node.left_son = None

        # If node has two sons.
        elif del_node.left_son is not None and del_node.right_son is not None:

            # Find most right node from left subtree.
            target_node = del_node.left_son
            while target_node.right_son is not None:
                target_node = target_node.right_son

            # Change them.
            self.change(del_node, target_node)

            parent_node = del_node.parent
            if del_node.is_parent_left:
                parent_node.right_son = None
            else:
                parent_node.left_son = None

        # If node has one son only.
        else:
            son_node = del_node.left_son or del_node.right_son
            parent_node = del_node.parent
            son_node.parent = parent_node
            if del_node.is_parent_left:
                son_node.is_parent_left = True
                parent_node.right_son = son_node
            else:
                son_node.is_parent_left = False
                parent_node.left_son = son_node

        self.edit_height(parent_node)
        self.edit_size(parent_node)
        self.node_balance(parent_node)
        self.__nodes.remove(del_node)

    def small_right_rotation(self, a: Node, b: Node):
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
            self.root = b

        self.edit_height(a)
        self.edit_size(a)

    def small_left_rotation(self, a: Node, b: Node):
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
            self.root = b

        self.edit_height(a)
        self.edit_size(a)

    def big_right_rotation(self, a: Node, b: Node, c: Node):
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
            self.root = c

        self.edit_height(a)
        self.edit_height(b)
        self.edit_size(a)
        self.edit_size(b)

    def big_left_rotation(self, a:Node, b: Node, c: Node):
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
            self.root = c

        self.edit_height(a)
        self.edit_height(b)
        self.edit_size(a)
        self.edit_size(b)

    def node_balance(self, node: Node):
        now_node = node
        while now_node is not None:
            next_node = now_node.parent
            a = now_node
            left_heigh = 0 if now_node.left_son is None else now_node.left_son.height
            right_height = 0 if now_node.right_son is None else now_node.right_son.height
            if left_heigh - right_height == 2:
                b = a.left_son
                b_left_height = 0 if b.left_son is None else b.left_son.height
                b_right_height = 0 if b.right_son is None else b.right_son.height
                if b_right_height <= b_left_height:
                    self.small_right_rotation(a, b)
                else:
                    c = b.right_son
                    self.big_right_rotation(a, b, c)
            elif right_height - left_heigh == 2:
                b = a.right_son
                b_left_height = 0 if b.left_son is None else b.left_son.height
                b_right_height = 0 if b.right_son is None else b.right_son.height
                if b_left_height <= b_right_height:
                    self.small_left_rotation(a, b)
                else:
                    c = b.left_son
                    self.big_left_rotation(a, b, c)

            now_node = next_node

    def find_by_index(self, index):
        """Finds value by index. Retuns value or None (if something goes wrong). INDEXES STARTS FROM 1"""
        now_node = self.root
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

    def find_right_subtree_for_merge(self, height):
        """Finds right subtree which equal height"""
        subtree_root = self.root
        while subtree_root.height - height > 1:
            subtree_root = subtree_root.right_son
        return subtree_root

    def find_left_subtree_for_merge(self, height):
        """Finds right subtree which equal height"""
        subtree_root = self.root
        while subtree_root.height - height > 1:
            subtree_root = subtree_root.left_son
        return subtree_root

    def merge_with_root(self, v1: Node, v2: Node, T: Node, merge_to_left: bool):
        """Just change references"""
        v1_parent = v1.parent
        v1_is_parent_left = v1.is_parent_left

        if v1_is_parent_left:
            v1_parent.right_son = T
        else:
            v1_parent.left_son = T

        T.parent = v1_parent
        T.is_parent_left = v1_is_parent_left
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
        self.node_balance(T)

    def glue_tree_(self, other):
        """Glue tree (other) which contains bigger values to tree (self) which contains less values"""

        # If self.height >= other.height
        if self.root.height >= other.root.height:
            v1 = self.find_right_subtree_for_merge(other.root.height)
            T = self.get_max_node(v1)
            self.delete(T)
            self.__nodes.append(T)
            v2 = other.root
            for node in other.__nodes:
                self.__nodes.append(node)
                other.__nodes = []
            self.merge_with_root(v1, v2, T, merge_to_left=True)
            return self

        else:
            v1 = other.find_left_subtree_for_merge(self.root.height)
            T = other.get_max_node(v1)
            other.delete(T)
            other.__nodes.append(T)
            v2 = self.root
            for node in self.__nodes:
                other.__nodes.append(node)
                self.nodes = []
            other.merge_with_root(v1, v2, T, merge_to_left=False)
            return other

    # TODO
    def split(self, key):
        now_node = self.root
        if key > now_node.value:
            now_node.left_son.parent = None





if __name__ == '__main__':
    tree = AVLTree()
    tree.insert(AVLTree.Node(10))
    tree.insert(AVLTree.Node(8))
    tree.insert(AVLTree.Node(3))
    tree.insert(AVLTree.Node(4))
    tree.insert(AVLTree.Node(5))
    tree.insert(AVLTree.Node(9))
    tree.insert(AVLTree.Node(6))
    tree.insert(AVLTree.Node(1))
    tree.insert(AVLTree.Node(2))
    tree.insert(AVLTree.Node(7))

    other = AVLTree()
    other.insert(AVLTree.Node(21))
    other.insert(AVLTree.Node(20))
    other.insert(AVLTree.Node(35))
    other.insert(AVLTree.Node(33))

    new_tree = tree.glue_tree_(other)
    print(bool(tree.root))
    print(tree.find_by_index(4))
    print(tree.find_by_index(0))
    print(tree.find_by_index(10))
    print(tree.find_by_index(1))