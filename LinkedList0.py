class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, n):
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n
    
    def printList(self):
        currentNode = self.first
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def addFirst(self, n):
        if self.first == None:
            self.add(n)
        else:
            n.next = self.first
            self.first = n
    
    def makeEmpty(self):
        self.first = None
        self.last = None
    
    def isEmpty(self):
        return self.first == None
        #return True if self.first == None else False
    
    def length(self):
        current = self.first
        count = 0 
        while current:
            count+= 1
            current = current.next
        return count
    
    
    def length_recursive(self, node, count=0):
        return count if node == None else self.length_recursive(node.next, count + 1)

    
    def returnAt(self, i):
        if i >= self.length():
            return "Index is out of bound."
        current = self.first
        count = 0 
        while count < i:
            count+= 1
            current = current.next
        return current.value
    

    def returnNodeAt(self, i):
        if i >= self.length():
            return "Index is out of bound."
        current = self.first
        count = 0 
        while count < i:
            count+= 1
            current = current.next
        return current
    

    def insertAt(self, node, x):
        if x == 0:
            self.addFirst(node)
            
        elif x >= self.length():
            self.add(node)
        
        else:
            count = 0
            current_node = self.first
            while current_node:
                if count == x - 1:
                    node.next = current_node.next
                    current_node.next = node
                    return
                current_node = current_node.next
                count += 1


    def sort_list(self):
        counter = 0
        length = self.length()
        for i in range(length):
            minimum_index = i
            for j in range(i+1, length):
                counter += 1
                print(str(self.returnAt(minimum_index)) + ">" + str(self.returnAt(j)))
                if self.returnAt(minimum_index) > self.returnAt(j):
                    print("yes")
                    minimum_index = j
            node1 = self.returnNodeAt(minimum_index)
            node2 = self.returnNodeAt(i)
            node1.value, node2.value = node2.value, node1.value
