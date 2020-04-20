# A complete working Python program to demonstrate all 
# insertion methods 
# References: https://www.geeksforgeeks.org/doubly-linked-list/,
#              https://dbader.org/blog/python-linked-list
  
# A linked list node 
class Kink: 
  
    def __init__(self,tau,n,src,dest): 
        '''Kink constructor'''
        self.tau = tau
        self.n = n
        self.src = src
        self.dest = dest
        self.next = None
        self.prev = None

    def __repr__(self):
        '''Return string representation of kink'''
        return "Kink(%s,%s,%s,%s)"%(self.tau,self.n,\
            self.src,self.dest)

class Worldline:

    def __init__(self):
        '''Initialize worldline'''
        self.head = None


    def __repr__(self):
        '''String representation of worldline'''
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '<' + ', '.join(nodes) + '>'

    # Given a reference to the head of a list and an 
    # kink data, inserts a new node on the front of list 
    def push(self,new_kink):  
  
        # Prepended kink needs to point to originally 1st node
        new_kink.next = self.head 
  
        # Prev of what is now the 2nd kink, needs to point to 1st kink
        if self.head is not None: # Cannot change prev of 2nd if empty list
            self.head.prev = new_kink 
  
        # Direct the head pointer to the prepended kink
        self.head = new_kink 

    # Given a node as prev_node, insert 
    # a new node after the given node 
    def insert(self,prev_kink,new_kink): 
      
        # Check if prev_kink exists 
        if prev_kink is None: 
            return
  
        # Make new_kink's next pointer same as prev_kink's next ptr 
        new_kink.next = prev_kink.next
  
        # Next of prev_kink should now point to the new_kink  
        prev_kink.next = new_kink 
  
        # New_kink's prev needs to point to prev_kink
        new_kink.prev = prev_kink
  
        # prev of Next kink to new_kink should now point to new_kink
        if new_kink.next is not None: 
            new_kink.next.prev = new_kink 

    # Attach a kink at the end of the doubly linked list
    def append(self,new_kink):

        # Initialize variable that will contain the last kink
        last = self.head 
  
        # new_kink will become last. Next should be None (maybe except @ T>0)
        new_kink.next = None
  
        # If empty list, make new_kink the head 
        if self.head is None: 
            new_kink.prev = None
            self.head = new_kink 
            return
  
        # Otherwise, traverse until last node and assign it to last 
        while (last.next is not None): 
            last = last.next
  
        # Last node should now point to the new_kink 
        last.next = new_kink 

        # New kink's prev should point to original last kink
        new_kink.prev = last

    # Get the first kink in the wordline
    def first_kink(self):

        return self.head

    # Get the last kink in the worldline
    def last_kink(self): 

        # Initialize last node
        last = self.head

        # Traverse worldline until last kink is reached
        while last.next is not None:
            last = last.next

        return last
  
'-----------------------------------------------------------'

# Main

# Create a kink object
kink = Kink(0,1,0,0)

print("A kink object is represented as",kink)

# Create a wordline object
worldline = Worldline()

# Push a kink to the worldline
worldline.push(kink)

print("A worldline object is represented as",worldline)

# Insert kink
new_kink = Kink(0.5,2,1,0)
worldline.insert(kink,new_kink)

print("Kink insertion:",worldline) 

# Insert a worm between the other two kinks
worldline.insert(worldline.head,Kink(0.3,1,0,0)) # worm tail
worldline.insert(worldline.head,Kink(0.2,0,0,0)) # worm head

print("Worm insertion:",worldline)

print("worldline.head:",worldline.head.next)

# Append a kink
new_kink = Kink(0.9,1,0,1)
worldline.append(new_kink)
print("Appending kink:",worldline)

# Retrieve the first and last kinks
print("The first kink of the worldline is:",worldline.first_kink())
print("The last kink of the worldline is:",worldline.last_kink())