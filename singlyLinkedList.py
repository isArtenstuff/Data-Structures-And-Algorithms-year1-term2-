"""Singly liked List"""
class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        new_node = DataNode(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self.count += 1

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
            return
        cur = self.head
        output = cur.data
        while cur.next is not None:
            cur = cur.next
            output += " -> " + cur.data
        print(output)

    def insert_front(self, data):
        new_node = DataNode(data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        if self.head.data == node:
            new_node = DataNode(data)
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return

        cur = self.head
        while cur.next is not None and cur.next.data != node:
            cur = cur.next
        if cur.next is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        new_node = DataNode(data)
        new_node.next = cur.next
        cur.next = new_node
        self.count += 1

    def delete(self, data):
        if self.head is None:
            print("Cannot delete, " + data + " does not exist.")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        
        cur = self.head
        while cur.next is not None and cur.next.data != data:
            cur = cur.next
        if cur.next is None:
            print("Cannot delete, " + data + " does not exist.")
            return
        if cur.next.next is None:
            cur.next = None
            self.count -= 1
            return
        cur.next = cur.next.next
        self.count -= 1
        



def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
       mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()

main()