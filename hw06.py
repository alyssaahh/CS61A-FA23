from re import L


passphrase = 'slinky'

def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    '083405e24afb7fe627c935f5c078cd7273590b80c691569b86d6bc03'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        #keep track of product name and price
        #initialize stock to 0
        #initialize funds to 0 
        self.product = product
        self.price = price
        self.stock = 0
        self.funds = 0

    
    def vend(self):
        #checks if there is stock 
        #if none, print "nothing left to vend..."
        #if sufficient stock and insufficient funds --> return "please add X more funds"
            #if change, return rest of funds (reset funds)
        if self.stock == 0:
            return f"Nothing left to vend. Please restock."
        else:
            if self.funds < self.price:
                difference = self.price - self.funds
                return f"Please add ${difference} more funds." 
            else:
                self.stock -= 1
                change = self.funds - self.price
                self.funds = 0
                if change == 0:
                    return f"Here is your {self.product}."
                else:
                    return f"Here is your {self.product} and ${change} change."
            
    def add_funds(self, funds):
        #check stock
        #if no stock, don't take any funds
       
        if self.stock == 0:
            return f"Nothing left to vend. Please restock. Here is your ${funds}."
        else:
            self.funds +=funds
            return f"Current balance: ${self.funds}"


    def restock(self,stock):
        #update stock variable
        #return current stock 
        self.stock += stock
        return f"Current {self.product} stock: {self.stock}"


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    
    #Do not use any string manipulation functions like str and reversed.

    if n == 0:
        return Link(0)
    else:
       new_list= Link.empty
       while n > 0:
            new_list = Link(n%10, new_list)
            n = n//10
        
    return new_list



       


def deep_map_mut(func, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    #Hint: The built-in isinstance function may be useful.
    #s = Link(1, Link(2, Link(3, Link(4))))
    # >>> isinstance(s, Link)
    #True
    #>>> isinstance(s, int)
    #False

    #isinstance returns whether rest is link 
    #recurison!! 

    if lnk is Link.empty:
        return
    elif isinstance(lnk.first, Link): #is lnk.first instance of Link?
        deep_map_mut(func,lnk.first)  #apply func to lnk.first
    else:
        lnk.first = func(lnk.first) #so lnk.first is not a link --> call func on lnk.first to replace it 
    
    deep_map_mut (func, lnk.rest) #recursively call so we can look at the rest of the link 
    




def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
    #once reach base case  (empty list)
        #


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

