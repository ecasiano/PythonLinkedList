# A complete working Python program to demonstrate all 
# insertion methods 
# References: https://www.geeksforgeeks.org/doubly-linked-list/,
#              https://dbader.org/blog/python-linked-list
  
# A linked list node 
class Kink: 
  
    # Constructor to create a new node 
    def __init__(self,tau,n,src,dest): 
        self.tau = tau
        self.n = n
        self.src = src
        self.dest = dest
        self.next = None
        self.prev = None

#     def __repr__(self):
#         return repr(self.)

'-----------------------------------------------------------'
  
# Class to create a Doubly Linked List 
class DoublyLinkedList: 
  
    # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '<' + ', '.join(nodes) + '>'

  
    # Given a reference to the head of a list and an 
    # integer, inserts a new node on the front of list 
    def push(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put the data in it 
        new_node = Node(new_data) 
  
        # 3. Make next of new node as head and 
        # previous as None (already None) 
        new_node.next = self.head 
  
        # 4. change prev of head node to new_node 
        if self.head is not None: 
            self.head.prev = new_node 
  
        # 5. move the head to point to the new node 
        self.head = new_node 

  
    # Given a node as prev_node, insert a new node after 
    # the given node 
    def insertAfter(self, prev_node, new_data): 
  
        # 1. Check if the given prev_node is None 
        if prev_node is None: 
            print("the given previous node cannot be NULL")
            return 
  
        # 2. allocate new node 
        # 3. put in the data 
        new_node = Node(new_data) 
  
        # 4. Make net of new node as next of prev node 
        new_node.next = prev_node.next
  
        # 5. Make prev_node as previous of new_node 
        prev_node.next = new_node 
  
        # 6. Make prev_node ass previous of new_node 
        new_node.prev = prev_node 
  
        # 7. Change previous of new_nodes's next node 
        if new_node.next is not None: 
            new_node.next.prev = new_node 

  
    # Given a reference to the head of DLL and integer, 
    # appends a new node at the end 
    def append(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put in the data 
        new_node = Node(new_data) 
  
        # 3. This new node is going to be the last node, 
        # so make next of it as None 
        new_node.next = None
  
        # 4. If the Linked List is empty, then make the 
        # new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
  
        # 5. Else traverse till the last node 
        last = self.head 
        while(last.next is not None): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next = new_node 
  
        # 7. Make last node as previous of new node 
        new_node.prev = last 
  
        return


    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found


    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None


    # This function prints contents of linked list 
    # starting from the given node 
    def printList(self, node): 
  
        print("\nTraversal in forward direction")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
  
        print("\nTraversal in reverse direction")
        while(last is not None): 
            print(" % d" %(last.data))
            last = last.prev 
  
'-----------------------------------------------------------'

# Main
  
# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
llist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next.next, 8) 
  
print("Created DLL is: ") 
llist.printList(llist.head) 

print("Doubly Linked list representation is: ")
print(llist)

# Try to delete an element from the list
num = 7
elem = llist.find(8)
llist.remove_elem(elem)
print("After removing %d using remove_elem(): "%num)
print(llist)
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 