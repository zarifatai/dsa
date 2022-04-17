class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = next


class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds!") 

        if index == 0:
            insert_at_beginning(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1


    def remove_at(self):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds!") 
        
        if index == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_after, self.head.next)        
            return


        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


class DoubleLinkedList(LinkedList):
    def __init__(self):
        super(DoubleLinkedList, self).__init__()


    def print_forward(self):
        self.print()

    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty!")

        itr = get_last_node()
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.prev else str(itr.data)
            itr = itr.prev


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)

        itr = self.head
        while itr.next
            itr = itr.next

        itr.next = Node(data, None, itr)


    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds!") 

        if index == 0:
            insert_at_beginning(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node =  Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    
    def remove_at(self):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds!") 
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev        
                    break


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    