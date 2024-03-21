class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index: int, data):
        if index<0 or index> self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        if index== self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
    
    def find_index(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            count+=1
            itr=itr.next
        raise Exception("Data not found in the Linked List")

    def remove_by_value(self, data):
        index = self.find_index(data)
        self.remove_at(index)

    def __repr__(self) -> str:
        if self.head is None:
            return "Linked List is empty"
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        return llstr
    
    def get_length(self)-> int:
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self, index: int)-> None:
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count+= 1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange","figs"])
    print(ll)
    ll.insert_after_value("mango","apple") # insert apple after mango
    print(ll)
    ll.remove_by_value("orange") # remove orange from linked list
    print(ll)
    ll.remove_by_value("figs")
    print(ll)
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print(ll)
