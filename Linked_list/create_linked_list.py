class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None :
            self.head = new_node
        
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node
            
    def dispaly(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
            
l = SLL()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.dispaly()