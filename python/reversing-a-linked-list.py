'''
Task
Reverse a linked list: Write a function that takes the head of a linked list and returns the reversed linked list.
'''

# I'll assume a single linked list

NODE_LIST_LENGTH = 10
node_array = []

class Node:

    def __init__(self, id: int):

        # stores the pointer to the next node in the list
        self.next = None

        # dummy ID
        self.id = id


def reverse_node_list(node_list: list) -> list:
    """Returns a reversed list of nodes.

    Args:
        node_list (list): List of node objects to reverse.

    Returns:
        list: The reversed list.
    """

    new_list = []
    for i in range(len(node_list)):
        new_list.append(node_list[-i - 1])

    return new_list

# buld the node array
for i in range(NODE_LIST_LENGTH):
    node_array.append(Node(i))

reversed_node_list = reverse_node_list(node_array)

for i in range(NODE_LIST_LENGTH):
    print(reversed_node_list[i].id)