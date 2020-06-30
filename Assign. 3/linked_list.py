# Author:      Jacob Hendry
# Date:        05/05/2020
# Description: This is a python file called linked_list.py. It will include Part 1: implement
#              the deque and bag ADT with a Linked List and Part 2: implement the deque ADT
#              with a CircularlyDoubly-Linked List

"""
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
"""


class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # If the index is less than 0, raise an Exception to indicate index out of range
        if index < 0:
            raise Exception('Index is out of range')

        # If index is 0, insert it into the front of the list
        if index == 0:
            new_link.next = self.head.next
            self.head.next = new_link
            return

        # If the list is empty, insert the value into the list in the beginning
        if self.head.next == self.tail:
            new_link.next = self.tail
            self.head.next = new_link
            return

        # Initialize the current node
        curr = self.head
        previous = None

        # Iterate through the list to find the index
        for values in range(index + 1):
            # If the current node becomes the tail, raise an Exception to indicate out of range
            if curr == self.tail:
                raise Exception('Index is out of range')
            previous = curr
            curr = curr.next
            new_link.next = curr
        # Add the new_link data into next of the previous node
        previous.next = new_link
        return

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            index: The index of the node that will be removed
        """
        # Initialize the the current and previous nodes
        curr = self.head
        previous = None

        # If the index is less than 0, raise Exception indicating out of range
        if index < 0:
            raise Exception('Index is out of range')

        # If the index is 0, remove the only index in the list
        if index == 0:
            self.head.next = curr.next

        # For loop through the list to find the indicated index to remove
        for value in range(index + 1):
            # If the current node is beyond the list, raise Exception to indicate out of range
            if curr == self.tail:
                raise Exception('Index is out of range')
            previous = curr
            curr = curr.next
        # Removes the indicated index and replaces it with the next current node
        previous.next = curr.next

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # Set the new_link data next as the head next
        new_link.next = self.head.next

        # Now new_link is add at the front of the list
        self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # Set variable curr as the head
        curr = self.head
        previous = None

        # Loop through the linked list to find the back node
        while curr != self.tail:
            previous = curr
            curr = curr.next
            new_link.next = curr
        previous.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        if self.head.next == self.tail:
            return None
        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        if self.head.next == self.tail:
            return None
        curr = self.head
        previous = None

        # Loop through the list to find the back node
        while curr != self.tail:
            previous = curr
            curr = curr.next
        # Return the last data in the list
        return previous.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """
        if self.head.next == self.tail:
            return False
        curr = self.head.next
        self.head.next = curr.next  # The front has been replaced now
        return True

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        curr = self.head
        previous = None

        # Loop through the list to find the last data in the list
        while curr.next != self.tail:
            previous = curr
            curr = curr.next
        previous.next = self.tail  # The back has been replaced now
        return

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.head.next == self.tail:
            return True
        return False  # Only returns false if list has data

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        curr = self.head

        # Loop through the list to find the indicated value in the list
        while curr != self.tail:
            # Returns true if value is present
            if curr.data == value:
                return True
            curr = curr.next
        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        curr = self.head
        previous = None

        # Loop through the list to find the indicated value to remove
        while curr != self.tail:
            # If the value is present in the list, remove it
            if curr.data == value:
                previous.next = curr.next
                return
            previous = curr
            curr = curr.next
        return


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''


class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # If the index is less than 0, raise an Exception to indicate index is out of range
        if index < 0:
            raise Exception('Index is out of range')

        # If the index is 0, insert the node in the beginning
        if index == 0:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link
            return

        # If the index is larger than 0, add link where indicated by index
        curr = self.sentinel.next

        # Loop through the list to find the index
        for value in range(index):
            curr = curr.next
            # If the current node is equal to the sentinel, raise an Exception
            if curr == self.sentinel:
                raise Exception('Index is out of range')

        new_link.prev = curr.prev
        curr.prev.next = new_link
        new_link.next = curr
        curr.prev = new_link
        return

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            index: The index of the node that will be removed
        """
        # If there is no links, return false
        if self.sentinel.next == self.sentinel:
            return False

        # If the index is less than 0, raise an Exception
        if index < 0:
            raise Exception('Index is out of range')

        # Initialize the current node
        curr = self.sentinel.next

        # Loop through the list to find the indicated index
        for value in range(index):
            curr = curr.next

        # If the list has only one node
        if curr.prev == self.sentinel and curr.next == self.sentinel:
            self.sentinel.prev = self.sentinel
            self.sentinel.next = self.sentinel

            # If the node is not linked to the sentinel
        if curr.prev != self.sentinel and curr.next != self.sentinel:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next

            # If the node is at the front of the list
        if curr.prev == self.sentinel and curr.next != self.sentinel:
            curr.next.prev = self.sentinel
            self.sentinel.next = curr.next

            # If the node is at the back of the list
        if curr.prev != self.sentinel and curr.next == self.sentinel:
            curr.prev.next = self.sentinel
            self.sentinel.prev = curr.prev

        # Return true to indicate the node has been add
        return True

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # Need to set the next and prev on the sentinel for an empty list
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link
            return

        # Need to add the data to the front for a non-empty list
        new_link.prev = self.sentinel
        new_link.next = self.sentinel.next
        self.sentinel.next.prev = new_link
        self.sentinel.next = new_link
        return

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # Need to set net and prev on the sentinel for an empty list
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link
            return

        # Need to set next on the sentinel for an non-empty list
        new_link.prev = self.sentinel.prev
        new_link.next = self.sentinel
        self.sentinel.prev.next = new_link
        self.sentinel.prev = new_link
        return

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        return self.sentinel.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        return self.sentinel.prev.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """
        # If the list is empty
        if self.sentinel.next == self.sentinel:
            return False

        # Else remove the front node
        self.sentinel.next.next.prev = self.sentinel
        self.sentinel.next = self.sentinel.next.next
        return True

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        # If the list is empty
        if self.sentinel.prev == self.sentinel:
            return False

        # Else remove the last node
        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev
        return True

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.sentinel.next == self.sentinel:
            return True
        return False  # Return false if the list is not empty

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        # If the list is empty
        if self.sentinel.next == self.sentinel:
            return False
        curr = self.sentinel.next

        # Loop through the list to find the indicated value
        while curr != self.sentinel:

            # if the value is in the list return True
            if curr.data == value:
                return True
            curr = curr.next

        # Return false if the value isn't present
        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        # Initialize the current node
        curr = self.sentinel.next

        # Loop through the list to find the value to remove
        while curr != self.sentinel:

            # If the value is in the list, find where it is is now
            if curr.data == value:

                # If the value is at the beginning of the list
                if curr.prev == self.sentinel and curr.next != self.sentinel:
                    self.sentinel.next = curr.next
                    curr.next.prev = self.sentinel

                # If the value is at the end of the list
                if curr.prev != self.sentinel and curr.next == self.sentinel:
                    self.sentinel.prev = curr.prev
                    curr.prev.next = self.sentinel

                # If the value is somewhere between the front and end of the list
                if curr.prev != self.sentinel and curr.next != self.sentinel:
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next

                # Returns true to indicate the value has been removed
                return True
            curr = curr.next
        # Returns false if the value doesn't exist
        return False

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """
        curr = self.sentinel.next
        temp_node = curr.next

        # Loop through the list to start reversing the list
        while curr != self.sentinel:
            curr.next = curr.prev
            curr.prev = temp_node
            curr = temp_node
            temp_node = curr.next

        # Reverse the prev and next nodes
        new_temp = curr.prev
        curr.prev = curr.next
        curr.next = new_temp
        return
