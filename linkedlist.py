class Class:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_class = Class(data)
        if not self.head:
            self.head = new_class
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_class
   
    def insert_at_start(self, data):
        new_class = Class(data)
        new_class.next = self.head
        self.head = new_class

    def insert_at_index(self, index, data):
        if index < 0:
            print("Cant be Negative.")
            return
        new_class = Class(data)
        if index == 0:
            new_class.next = self.head
            self.head = new_class
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                print("Out of range.")
                return
            current = current.next
        if not current:
            print("Out of range.")
            return
        new_class.next = current.next
        current.next = new_class

    def delete_at_index(self, index):
        if not self.head:
            print("Empty.")
            return
        if index < 0:
            print("Cant be negative.")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                print("Out of range.")
                return
            current = current.next
        if not current or not current.next:
            print("Out of range.")
            return
        current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        if not self.head:
            print("Empty.")
            return
        current = self.head
        while current:
            print(current.data, end=",")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.insert_at_index(1, 15)
    ll.display()  # 5,15,10,20,None
    print("Index of 10:", ll.search(10))  #2
    ll.delete_at_index(1)
    ll.display()  # 5,10,20,None
    print("Index of 10:", ll.search(10))#1