# Author:      Jacob Hendry
# Date:        05/21/2020
# Description: This is a python file named bst.py.
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================


class Student:

    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        # return value is less than the given node
        return self.grade < kq.grade

    def __gt__(self, kq):
        # return value is greater than the given node
        return self.grade > kq.grade

    def __eq__(self, kq):
        # return value is equal to the given node
        return self.grade == kq.grade

    def __str__(self):
        if self.grade is not None:
            # If there is a grade, return the name of the student and grade
            return str(self.name) + ": " + str(self.grade) + "%"


class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:

    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None
        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.
        Args:
            val: Item to be stored in the new node
        """
        newNode = TreeNode(val)

        parent = None
        currentNode = self.root
        while currentNode is not None:
            parent = currentNode
            if newNode.val < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if parent is None:
            self.root = newNode
        elif newNode.val < parent.val:
            parent.left = newNode
        else:
            parent.right = newNode

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
        """
    Perform in-order traversal of the tree and return a list of visited nodes
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node

            visited = []
            self.in_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack

        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree

        self.in_order_traversal(cur_node.left, visited)
        visited.append(cur_node.val)
        self.in_order_traversal(cur_node.right, visited)
        return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes
        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node

            visited = []
            self.pre_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for pre_order traversal:
        # store current node value, visit left subtree, visit right subtree, return container

        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes
        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node

            visited = []
            self.post_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for post_order traversal:
        # visit left subtree, visit right subtree, store current node value, return container

        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.
        Args:
            kq: query key
        Returns:
            True if kq is in the tree, otherwise False
        """
        currentNode = self.root

        # while the root node has a value, determine if the node is in the bst(binary search tree)
        while currentNode is not None:
            if currentNode.val == kq:
                # if the value is in the tree return true
                return True
            elif kq < currentNode.val:
                # if the value is less than the current node value move to the left subtree
                currentNode = currentNode.left
            else:
                # if the value is more than the current node value move to the right subtree
                currentNode = currentNode.right

        # Return false if the value is not found
        return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns the left-most node of the given subtree
        """
        if self.root is None:
            return None
        currentNode = node

        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.
        Args:
            kq: key of node to remove
        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        newNode = TreeNode(kq)

        if self.root.val == newNode:
            # if the node is the root of the tree, call the remove first method, which will return true when removed
            self.remove_first()
            return

        if self.contains(kq):
            # if the tree contains the node, set root as the current node
            currentNode = self.root
            while currentNode.val != newNode:
                if newNode < currentNode.val:
                    # if the current node is less than kq node set it to the left else set it the right subtree
                    currentNode = currentNode.left
                currentNode = currentNode.right
        else:
            return False

        # find the kq parent node by calling the get_nodeParent method
        kqParent = self.get_nodeParent(currentNode)

        if currentNode.left is None and currentNode.right is None:
            # if the tree has no children, compare current node vale to kq parent and remove
            if currentNode.val < kqParent.val:
                kqParent.left = None
            kqParent.right = None
        else:
            if currentNode.right is None:
                # the node successor is now the current node on the leftmost subtree
                nodeSuccessor = currentNode.left
                if currentNode.val < kqParent.val:
                    # replace the node successor to the kq parent node on the left side
                    kqParent.left = nodeSuccessor
                # else replace the node successor to the kq parent node on the right side
                kqParent.right = nodeSuccessor

                # Replace the empty nodes as None
                currentNode.left = None
                currentNode.right = None
                return True

            # else the current node.left is None
            nodeSuccessor = self.left_child(currentNode.right)

            nodeSuccessorParent = self.get_nodeParent(nodeSuccessor)
            # find the node successor parent node by calling the get_nodeParent method
            nodeSuccessor.left = currentNode.left

            if nodeSuccessor is not currentNode.right:
                # now set the left node successor parent as the node successor on the right
                nodeSuccessorParent.left = nodeSuccessor.right
                nodeSuccessor.right = currentNode.right

            if currentNode.val < kqParent.val:
                # Replace the left parent node as the node successor now
                kqParent.left = nodeSuccessor
            # else replace the right parent node as the node successor now
            kqParent.right = nodeSuccessor

        # Replace the empty nodes as None
        currentNode.left = None
        currentNode.right = None
        return True

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.
        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root is None:
            # if the root value is None, there is no value and return none
            return None
        # else return the value that is at the root of the tree
        return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.
        Returns:
            True if the root was removed, otherwise False
        """
        if self.root is None:
            # returns false if there is nothing in the tree
            return False

        elif self.root.left is None and self.root.right is None:
            # If the root has no children, remove the root and return true
            self.root = None
            return True

        elif self.root.right is None:
            # the root doesn't have a right subtree child, now left becomes the root
            self.root = self.root.left
            return True
        else:
            # the in order successor node is set the leftmost node in the right subtree
            nodeSuccessor = self.left_child(self.root.right)

            # set the node successor parent by finding the nodes parent
            nodeSuccessorParent = self.get_nodeParent(nodeSuccessor)

            # If the node successor parent is the root, remove the leftmost node and move it to the root node
            if nodeSuccessorParent == self.root:
                nodeSuccessor.left = self.root.left
                self.root = nodeSuccessor
                return True

            # if the node successor parent is not the root, replace the leftmost node with move nodes around
            nodeSuccessor.left = self.root.left
            nodeSuccessorParent.left = nodeSuccessor.right
            nodeSuccessor.right = self.root.right
            self.root = nodeSuccessor
            return True

    def get_nodeParent(self, node):
        """
        Returns the passed child node's parent
        Returns:
            the parent of the child node passed
        """
        if node is self.root:
            # if the passed node is the root, there is no parents, return None
            return None

        # Set the current node to the root
        currentNode = self.root

        # while the current node isn't the passed node, continue, else return false
        while currentNode is not node:

            if node.val < currentNode.val:
                # find the parent node on the left subtree
                if currentNode.left.val == node.val:
                    return currentNode
                currentNode = currentNode.left
            else:
                # find the parent node on the right subtree
                if currentNode.right.val == node.val:
                    return currentNode
                currentNode = currentNode.right
        return False
