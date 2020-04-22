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
        prev_kink = first_kink
        while (prev_kink.next is not None) and (prev_kink.next.tau < tau_new):
            prev_kink = prev_kink.next

        # Get kink following the one to be inserted
        if prev_kink.next is not None:
            next_kink = prev_kink.next
        else: next_kink = None

        # Connect new_kink to preceding kink
        new_kink.prev = prev_kink
        prev_kink.next = new_kink

        # Connect new kink to following kink
        if next_kink is not None:
            new_kink.next = next_kink
            next_kink.prev = new_kink

        # If nothing after the new kink, set it as worldline.last
        if new_kink.next is None:
            self.last = new_kink

    def append(self,tau_new,n_new,src_new,dest_new):
        '''Insert a kink at the end of the worldline'''

        # Create the kink to be appended
        new_kink = Kink(tau_new,n_new,src_new,dest_new)

        # Get the last kink of the worldline
        last_kink = self.last

        # Connect last kink to new_kink
        last_kink.next = new_kink
        new_kink.prev = last_kink

        # Make the appended kink the last one
        new_kink.next = None
        self.last = new_kink

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

print("A kink object is represented as",kink,'\n')

# Create a wordline object
i = 0   # Worldline site
n_i = 1 # Initial number of particles on site i  
worldline = Worldline(n_i,i)

print("A worldline object is represented as",worldline,'\n')

# Insert kink after trivial kink
tau_new,n_new,src_new,dest_new = 0.78,2,1,0
worldline.insert(tau_new,n_new,src_new,dest_new)

print("Kink insertion:",worldline,'\n') 

# Insert a worm between the other two kinks
worldline.insert(0.15*tau_new,n_i-1,i,i)
worldline.insert(0.2*tau_new,n_i,i,i)
print("Worm insertion:",worldline,'\n')

# Insert kink at the end
worldline.insert(1.1*tau_new,1,0,1)
print("Insert kink at the end:",worldline,'\n')

# Append:
worldline.append(0.999999999,2,1,0)
print("Append kink:",worldline,'\n')

# Retrieve the first and last kinks
print("The first kink of the worldline is:",worldline.first)
print("The last kink of the worldline is:",worldline.last)