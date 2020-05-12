

# ! Create a class "Node" that keeps track of the value of our node and the pointer to the next node in our list
class Node:
    # * set next to have a default value of none so that the linked list can have one value to begin
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # * method that allows us to get the value of the node we are on
    def get_value(self):
        return self.value

    # * method that allows us to get the value of the node we are pointing to
    def get_next_node(self):
        return self.next

    # * method that allows us to set the next node in the list
    def set_next_node(self, next_node):
        self.next = next_node


# ! create a classed called "LinkedList" that will hold the info of our list and build methods to manage it
class LinkedList:
    # * initalize linked list -> default value is set to none
    def __init__(self, value=None):
        # * our head node is the first node in the list
        self.head_node = Node(value)

    # * create a method to return the head node
    def get_head_node(self):
        return self.head_node

    # * create a method to insert a new node to the beginning of the linked list
    # * our new_value is the value we are passing into node
    def insert_beginning(self, new_value):
        # * new_node is the creation of our new node in our linked list and new_value is what we are passing in
        new_node = Node(new_value)
        # ? currently our old head node will be orphaned so we need to point our new node at our old head node
        # * newly created node is setting the next node to equal the current head node
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # create a method to insert a new node to the end of the linked list

    def insert_end(self, new_value):
        new_node = Node(new_value)
        # what node do we want to add the new node to?
        # the last node in the list
        # we can get to the last node in the list by traversing it
        current = self.head_node
        while current.get_next_node() is not None:
            current = current.get_next_node()
            # we're at the end of the linked list
        current.set_next_node(new_node)

    def delete_end(self):
        if self.head_node is None:
            return None
        current_node = self.get_head_node()
        previous_node = current_node
        while current_node.get_next_node() is not None:
            previous_node = current_node
            current_node = current_node.get_next_node()
        previous_node.set_next_node(None)
        return current_node.value

    def delete_head(self):

        deleted = self.head_node.get_value()
        # print('deleted ' + deleted)
        self.head_node = self.head_node.get_next_node()

        # print('new head node ', self.head_node.value)
        return deleted

    def print_list(self):
        current_node = self.get_head_node()
        while True:
            if current_node is None:
                break
            print(current_node.value)
            current_node = current_node.get_next_node()


third = LinkedList('first')
third.insert_beginning('new first')
third.insert_end('end')
third.delete_end()
third.insert_end('new end')
third.delete_head()

# print(third.head_node.value)

print(third.print_list())
