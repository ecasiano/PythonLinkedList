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
        return f"Kink({self.tau},{self.n},{self.src},{self.dest})"

class Worldline:

    def __init__(self,n,site):
        '''Initialize worldline'''
        self.first = Kink(0,n,site,site)
        self.last = self.first

    def __repr__(self):
        '''String representation of worldline'''
        nodes = []
        curr = self.first
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '<' + ', '.join(nodes) + '>'

    def insert(self,tau_new,n_new,src_new,dest_new): 
        '''Insert a new kink at time tau_new'''
      
        # Create the kink to be inserted
        new_kink = Kink(tau_new,n_new,src_new,dest_new)

        # Get the initial/trivial kink
        first_kink = self.first

        # Get kink preceding the one to be inserted
        curr_kink = first_kink
        while (curr_kink.next is not None) and (curr_kink.next.tau < tau_new):
            curr_kink = curr_kink.next

        # Get kink following the one to be inserted
        if curr_kink.next is not None:
            next_kink = curr_kink.next
        else: next_kink = None

        # Connect new_kink to preceding kink
        new_kink.prev = curr_kink
        curr_kink.next = new_kink

        # Connect new kink to following kink
        if next_kink is not None:
            new_kink.next = next_kink
            next_kink.prev = new_kink

        # If nothing after the new kink, set it as worldline.last
        if new_kink.next is None:
            self.last = new_kink

        # CHECK for: i) inserting after trivial kink ii) middle kink
        #            iii) at the end

    def append(self,new_kink):
        '''Insert a kink at the end of the worldline'''

        # Initialize variable that will contain the last kink
        last = self.first 
  
        # new_kink will become last. Next should be None (maybe except @ T>0)
        new_kink.next = None
  
        # If empty list, make new_kink the head 
        if self.first is None: 
            new_kink.prev = None
            self.first = new_kink 
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

        return self.first

    # Get the last kink in the worldline
    def last_kink(self): 

        # Initialize last node
        last = self.first

        # Traverse worldline until last kink is reached
        while last.next is not None:
            last = last.next

        return last

    # def remove(self,tau_remove):
    #     '''Remove a kink after prev_kink'''

    #     # Initial kink
    #     kink_0 = self.head

    #     # Delete a kink at tau=tau_remove
    #     prev_kink = None
    #     curr_kink = kink_0
    #     while curr_kink.tau < tau_remove:
    #         prev_kink = curr_kink
    #         curr_kink = curr_kink.next

    #     prev_kink.next = curr_kink.next;
  
  # class Worm:

  #   def __init__(self):

  #       self.head
  #       self.tail

'-----------------------------------------------------------'

# Main

# Create a kink object
kink = Kink(0,1,0,0)

print("A kink object is represented as",kink)

# Create a wordline object
i = 0   # Worldline site
n_i = 1 # Initial number of particles on site i  
worldline = Worldline(n_i,i)

print("A worldline object is represented as",worldline)

# Insert kink at tau_new and site i
tau_new,n_new,src_new,dest_new = 0.78,2,1,0
worldline.insert(tau_new,n_new,src_new,dest_new)

print("Kink insertion:",worldline) 

# Insert a worm between the other two kinks
worldline.insert(0.15*tau_new,n_i-1,i,i)
worldline.insert(0.2*tau_new,n_i,i,i)

print("Worm insertion:",worldline)

print("worldline.head:",worldline.head.next)

# Append a kink
new_kink = Kink(0.9,1,0,1)
worldline.append(new_kink)
print("Appending kink:",worldline)

# Retrieve the first and last kinks
print("The first kink of the worldline is:",worldline.first_kink())
print("The last kink of the worldline is:",worldline.last_kink())