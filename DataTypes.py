########################################################
#                                                      #
#                   Stephen Bridgett                   #
#             Ordered Collection Data Types            #
#                                                      #
########################################################

#helper "Node" class
class Node:
    def __init__(self,idata):
        self.data = idata
        self.next = None
        self.back = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getBack(self):
        return self.back

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setBack(self,newback):
        self.back = newbext        


#Linked List and Doubly-Linked List
class Linked__Doubly_List(object):
    def __init__(self):
        self.head = None

#Appends item to end of the list
    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.back = None
            self.head = newNode
        else:
            newNode = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.back = cur
            newNode.next = None

#adding something to front of list
    def add(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.back = None 
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.back = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.back = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
       
#removes item from list      
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current is not None:
            if current.getData() == item:
                break
            else:
                previous = current
                current = current.getNext()

        if previous == None:
           self.head = current.getNext()
        else:
           previous.setNext(current.getNext())
           
#searches for item in list and return boolean
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found            
#checks to see if list is empty, return boolean
    def isEmpty(self):
        return self.head == None
#returns the number of items in list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
#adds a new item to the end of the list
    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)
#returns position of item in the list
    def index(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.position
            else:
                current = current.next
        #error if item isnt in the list
        print ("item not present in list")        

#adds a new item to the list at a specific position
    def insert(self,item):
        if position == 0:
            self.add(item)
        elif position > self.size():
            print("position index out of range")
        elif position == self.size():
            self.AppendNode(item)
        else:
            temp = Node(item, position)
            current = self.head
            previous = None
            while current.position != position:
                previous = current
                current = current.next
            previous.next = temp
            temp.next = current
            temp.back = previous
            current.back = temp
            current = self.head
            self.index_correct(current)

#removes and returns last item in list
    def pop(self):
        if self.size == 0:
            print("list empty")
        else:
           return self.linkedlist.pop()
#removes and returns the item at a position   
    def pop(self, position):
        if self.size < position:
            print("list too short")
        else:
            return self.linkedlist.pop(position)
#prints the linked list
    def print(self):
        print("[ ", end='')
        node = self.head
        while(node != None):
            print(str(node.getData())+ " ", end='')
            node = node.getNext()
        print("]")    

mylist = Linked__Doubly_List() #creates a doubly-linked list

mylist.add(41)
mylist.append(1)
mylist.append(2)
mylist.append(32)
mylist.append(5)
mylist.append(34)
mylist.append(9)
mylist.append(132)
mylist.append(142)
mylist.append(612)
mylist.append(21)
mylist.add(15)

mylist.add(41)
mylist.add(67)
mylist.add(27)
mylist.add(83)
mylist.add(36)
mylist.add(64)

mylist.print()
print()

print("Print the size of the above list:")
print(mylist.size())
print()
print("Is 67 in the above list?")      
print(mylist.search(67))
print()
print("Is 100 in the above list?")
print(mylist.search(100))
print()
print("Is 83 in the above list?")
print(mylist.search(83))
print()

mylist.add(100)
mylist.print()
print()
print("Is 100 in the above list?")
print(mylist.search(100))
print()
print("Print the size of the above list:")
print(mylist.size())
print()

print("Remove 36 from the above list.")
mylist.remove(36)
print()
mylist.print()
print()
print("Print the new size of the list:")
print(mylist.size())
print()
print("Remove 64 from the above list.")
mylist.remove(64)
print()
mylist.print()
print()
print("Print the new size of the list:")
print(mylist.size())
print()
print("Remove 9 from above the list.")
mylist.remove(9)
print()
mylist.print()
print()
print("Print the new size of the list:")
print(mylist.size())
print()
print("Is 27 still in the above list?")
print(mylist.search(27))
print()
print("----------------------------------------")
print()

#############################################################
# The Linked List and Doubly-linked list methods run rather #
# fast. Their methods can be seen being completed in either #
# linear or constant time.                                  #
#############################################################


########################### 3 #################################
#                                                             #
#   It is believed Python's internal representation of a      #
#   list is represented by a doubly-linked list. This is      #
#   assumed because they are more effiencent to work          #
#   with when working with lists and large amounts of         #
#   data since they work backwards and fowards.               #
#                                                             #
###############################################################


############################ 4 ################################

#stack class that creates a new empty stack
class Stack:
    def __init__(self):
        self.stacklist = []
#ckecks to see if stack is empty
    def isEmpty(self):
        if len(self.stacklist)==0:
            return True
        else:
            return False
#removes top item from stack
    def pop(self):
        item = self.stacklist[-1]
        del self.stacklist[-1]
        return item

#adds new item to top of stack
    def push(self, item):
        self.stacklist.append(item)

#returns top item of stack but doesn't remove it
    def peek(self):
        return self.stacklist[0]

#returns number of items on stack
    def size(self):
        count = 0

        for item in self.stacklist:
            count += 1

        return count

##############################################################
# The stack methods run rather fast. Their methods can       #
# be seen being completed in either linear or constant time. #
##############################################################

############################ 5 ################################

#queue class that creates a new empty queue    
class Queue():
   def __init__(queue):
       self.queuelist = []

#adds new item to rear of queue
   def enqueue(self, item):
       self.queuelist.enqueue(item)

#removes the front item from queue
   def dequeue(self):
       self.queuelist.pop(0)
       return self.queuelist(0)

#tests to see whether queue is empty
   def isEmpty(self):
       if not self.stacklist:
          return True
       else:
          return False

#returns number of items in queue
   def size(self):
        return len(self.stacklist)

##############################################################
# The queue methods run rather fast. Their methods can       #
# be seen being completed in either linear or constant time. #
##############################################################

############################ 6 ################################

#deque class that creates new empty deque
class Deque:
   def __init__(self):
        self.deque = []

#adds new item to front	
   def addFront(self, item):
        self.deque.append(item)

#adds new item to rear
   def addRear(self, item):
        self.deque.insert(0,item)

#removes item from front
   def removeFront(self):
       return self.deque.pop()

#removes item from rear
   def removeRear(self):
       return self.deque.pop(0)

#test to see whether it's empty	    
   def isEmpty(self):
        if not self.deque:
            return True
        else:
            return False
    
#returns number of items in deque
   def size(self):
       return len(self.deque)

##############################################################
# The deque methods run rather fast. Their methods can       #
# be seen being completed in either linear or constant time. #
##############################################################

############################ 7 ################################

#function that solves equations based in Reverse Polish Notation
##the function manipulates stacks and its methods to solve these equations

def rpn_eval(input_string):
    input_list = input_string.split(' ')
    rpn_stack = Stack()
    for item in input_list:
        if item == "+":
            n1 = rpn_stack.pop()
            n2 = rpn_stack.pop()
            rpn_stack.push(n2+n1)
        elif item == "-":
            n1 = rpn_stack.pop()
            n2 = rpn_stack.pop()
            rpn_stack.push(n2-n1)
        elif item == "*":
            n1 = rpn_stack.pop()
            n2 = rpn_stack.pop()
            rpn_stack.push(n2*n1)
        elif item == "/":
            n1 = rpn_stack.pop()
            n2 = rpn_stack.pop()
            rpn_stack.push(n2/n1)                
        else:
            rpn_stack.push(int(item))
    ans = rpn_stack.pop()       
    return ans
print("Reverse Polish Notation:")
print()
print("What is the answer of (8 2 4 + -)?")
print(rpn_eval("8 2 4 + -"))
print()
print("What is the answer of (1 2 +)?")
print(rpn_eval("1 2 +"))
print()
print("What is the answer of (1000 990 1 2 + * +)?")
print(rpn_eval("1000 990 1 2 + * +"))
print()
print("What is the answer of (400 50 1 1 + / -)?")
print(rpn_eval("400 50 1 1 + / -"))         
