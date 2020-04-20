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

    def first_kink():

        return 0


    def last_kink(): 

        return 0

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
    def insert(self, prev_kink, new_kink): 
      
            # 1. check if the given prev_node is NULL 
            if prev_kink is None: 
                return
      
            # 4. Make next of new node as next of prev_node 
            new_kink.next = prev_kink.next
      
            # 5. Make the next of prev_node as new_node  
            prev_kink.next = new_kink 
      
            # 6. Make prev_node as previous of new_node 
            new_kink.prev = prev_kink
      
            # 7. Change previous of new_node's next node */ 
            if new_kink.next is not None: 
                new_kink.next.prev = new_kink 
  
#  This code is contributed by jatinreaper

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

print("After kink insertion:",worldline) 

# Insert a worm between the other two kinks
worldline.insert(worldline.head,Kink(0.3,1,0,0)) # worm tail
worldline.insert(worldline.head,Kink(0.2,0,0,0)) # worm head

print("After worm insertion:",worldline)

print("worldline.head:",worldline.head.next)
