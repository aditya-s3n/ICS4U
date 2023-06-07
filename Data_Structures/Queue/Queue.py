'''
@author: aaronQuesnelle
2018 for ICS4U

'''


class ListNode:
    '''
    Class of listNode is a data type which holds a value and a link to the next
    node in a list. This object is used in conjunction with linked list
    '''
    
    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return self._value


    

class Queue:
    
    def __init__(self):
        '''
        Create an empty queue.
        '''
        self._length = 0
        self._head = None
        self._tail = None


    
    def empty(self):
        '''
        Determine if the queue is empty.

        Returns
        True if queue is empty, False if not.
        '''
        if self._head == None:
            return True
        else:
            return False


    
    def insert(self, value):
        '''
        Insert a value at the tail of the queue.
        Similar code to the insertNewLastNode function from LinkedLists

        Params
        value is any data type to be added to queue.
        '''
        new_node = ListNode(value)

        if self._tail == None:
            self._tail = new_node
            self._head = new_node
        else:
            previous_node = self._tail
            previous_node.newlink(new_node)
            self._tail = new_node

        self._length += 1
    


    def remove(self):
        '''
        Remove the first item from the head of the queue.
        If list is empty then return None.
        Similar to the removeFirstNode function from LinkedList

        Returns
        value at the head of the queue. If queue is empty return None.
        '''
        if self.empty():
            return None
        
        else:
            delete_node = self._head
            new_first = delete_node.link()

            self._head = new_first
            self._length -= 1

            return delete_node.value()

    
    
    def peek(self):
        '''
        Return the value of the item at the head of the queue without removing it.
        If queue is empty return None.

        Returns
        The value of the first item. If empty return None.
        '''
        if self.empty():
            return None
        else:
            return self._head.value()



    
    def __str__(self):
        '''
        Provide the string representation for the queue to appear
        as a Python List. Used with Python's built in print function.
        [item, item, item]

        Returns
        String
        '''
        list_to_print = []

        node = self._head
        for i in range(self._length):
            list_to_print.append(node.value())

            node = node.link()

        return str(list_to_print)
    

    
    
  
