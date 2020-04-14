# Definition of Linked List Class
# Reference: https://dbader.org/blog/python-linked-list

'-------------------------------------------------------------------------'

class DListNode:
	"""
	A node in a doubly-linked list.
	"""
	def __init__(self, data=None, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next

	def __repr__(self):
		return repr(self.data)
	
class DoublyLinkedList:
	def __init__(self):
		"""
		Create a new doubly linked list.
		Takes O(1) time.
		"""
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

	def prepend_node(self, data):
		"""
		Insert a new element at the beginning of the list.
		Takes O(1) time.
		"""
		new_head = DListNode(data=data, next=self.head)
		if self.head:
			self.head.prev = new_head
		self.head = new_head

	def append_node(self, data):
		"""
		Insert a new element at the end of the list.
		Takes O(n) time.
		"""
		if not self.head:
			self.head = DListNode(data=data)
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = DListNode(data=data, prev=curr)

	def find_node(self, key):
		"""
		Search for the first element with `data` matching
		`key`. Return the element or `None` if not found.
		Takes O(n) time.
		"""
		curr = self.head
		while curr and curr.data != key:
			curr = curr.next
		return curr  # Will be None if not found

	def remove_node(self, node):
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

	def remove(self, key):
		"""
		Remove the first occurrence of `key` in the list.
		Takes O(n) time.
		"""
		elem = self.find(key)
		if not elem:
			return
		self.remove_elem(elem)

	def reverse(self):
		"""
		Reverse the list in-place.
		Takes O(n) time.
		"""
		curr = self.head
		prev_node = None
		while curr:
			prev_node = curr.prev
			curr.prev = curr.next
			curr.next = prev_node
			curr = curr.prev
		self.head = prev_node.prev

	# Given a node as prev_node, insert 
	# a new node after the given node 
	# https://www.geeksforgeeks.org/doubly-linked-list/  
	def insert_node(self, prev_node, new_data): 
	  
	        # 1. check if the given prev_node is NULL 
	        if prev_node is None: 
	            print("This node doesn't exist in DLL") 
	            return
	  
	        #2. allocate node  & 3. put in the data 
	        new_node = Node(data = new_data) 
	  
	        # 4. Make next of new node as next of prev_node 
	        new_node.next = prev_node.next
	  
	        # 5. Make the next of prev_node as new_node  
	        prev_node.next = new_node 
	  
	        # 6. Make prev_node as previous of new_node 
	        new_node.prev = prev_node 
	  
	        # 7. Change previous of new_node's next node */ 
	        if new_node.next is not None: 
	            new_node.next.prev = new_node 
	  
	#  This code is contributed by jatinreaper
		
'-------------------------------------------------------------------------'  
  
# Code execution starts here 
if __name__=='__main__': 
  
	# Initialize that will contain worldline configurations
	data_struct = [] # A list for the two types of particles

	L = 2
	for i in range(L):
		initial_kink = DoublyLinkedList()
		initial_kink.prepend_node([0,1,(i,i)])
		data_struct.append([initial_kink,initial_kink])

	print(data_struct)


	# Insert a kink from site i to j for a species 0 OR 1.
	i,j = 1,0
	n_i,n_j = 0,2
	species = 1
	print('\n',data_struct[i][species],'\n')
	data_struct[i][species].append_node([0.3,n_i,(i,j)])
	data_struct[j][species].append_node([0.3,n_j,(i,j)])

	print('\n',data_struct[i][species])
	print('',data_struct[j][species])

	# Insert a worm end on site i for species 0 OR 1.
	i = 0
	n_i = 0
	species = 0
	worm_head_kink = [0.2,0,(i,i)]
	worm_head_kink = DoublyLinkedList().prepend_node(worm_head_kink)
	data_struct[i][species].insert_node(data_struct[i][species].find_node[initial_kink])

	# i = 2
	# print(data_struct[i])