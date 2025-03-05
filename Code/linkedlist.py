#!python


class Node:
    def __init__(self, data, count=1):  # Add count parameter
        """Initialize this node with data and an optional count (default = 1)."""
        self.data = data
        self.count = count  # Track frequency of words
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data}, count={self.count})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)
                
    def replace(self, old_item, new_item):
        """Replace the given old_item with new_item in the linked list.
        Best case: O(1) if old_item is at the head.
        Worst case: O(n) if old_item is at the tail or not in the list."""
        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return True  # Indicate replacement was successful
            node = node.next

        return False  # Indicate replacement failed

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list.
        Running time: O(1) because we maintain a size counter."""
        return self.size

    def append(self, data, count=1):
        """Append a new node with data and count."""
        if self.head is None:
            self.head = Node(data, count)  # Initialize first node
            self.tail = self.head
        else:
            self.tail.next = Node(data, count)  # Append new node
            self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we directly update head."""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def find(self, matcher):
        """Find and return the node where matcher(node) is True."""
        current = self.head
        while current:
            if matcher(current):  # Pass the full node to matcher function
                return current  # Return the full Node object
            current = current.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case: O(1) if deleting the head.
        Worst case: O(n) if deleting the tail or a middle node."""
        if self.is_empty():
            raise ValueError(f'Item not found: {item}')

        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                if previous is None:  # Deleting the head
                    self.head = current.next
                    if self.head is None:  # If the list becomes empty
                        self.tail = None
                else:
                    previous.next = current.next
                    if current.next is None:  # Deleting the tail
                        self.tail = previous

                self.size -= 1
                return

            previous = current
            current = current.next

        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
