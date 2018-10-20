class Node:
    """Node of AVL tree"""

    def __init__(self, value):
        self.value = value
        self.height = 0
        self.left_son = None
        self.right_son = None
        self.parent = None
        self.is_parent_left = False

    def is_root(self, tree):
        return self is tree.root


class AVLTree:

    def __init__(self):
        self.root = None
        self.__nodes = []

    def find(self, value):
        """Finds value in tree. Returns value or None."""

        result = None
        now_node = self.root
        while now_node is not None:
            if now_node.value == value:
                result = value
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

        parent_node = Node
        now_node = self.root

        # Looking for None reference...
        while now_node is not None:
            now_node.height += 1
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

    @staticmethod
    def change(top_node: Node, low_node: Node):
        """Changes two nodes"""

        top_parent = top_node.parent
        top_left_son = top_node.left_son
        top_right_son = top_node.right_son
        top_is_parent_left = top_node.is_parent_left
        low_parent = low_node.parent
        low_left_son = low_node.left_son
        low_right_son = low_node.right_son
        low_is_parent_left = low_node.is_parent_left

        # Low_node go up.
        low_node.parent = top_parent
        low_node.left_son = top_left_son
        low_node.right_son = top_right_son
        low_node.is_parent_left = top_is_parent_left
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
        if low_is_parent_left and low_parent is not None:
            low_parent.right_son = top_node
        elif not low_is_parent_left and low_parent is not None:
            low_parent.left_son = top_node
        if low_left_son is not None:
            low_left_son.parent = top_node
        if low_right_son is not None:
            low_right_son.parent = top_node

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

        self.__nodes.remove(del_node)

# TODO
# ВЫСОТЫ
