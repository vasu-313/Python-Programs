class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next 

            temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" --> ")     
            temp = temp.next

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None 
            return 

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return            
        
        prev.next = temp.next
        temp = None

l = SLL()
l.insert(10)                   
l.insert(20)                   
l.insert(30)                   
l.insert(40)   
# l.display()
l.delete(30) 
l.display()


