print("####Dynamic Array####")

class DynamicArray:
    def __init__(self):
        self.capacity = 3
        self.size = 0
        self.arr = [0] * self.capacity

    def _resize(self):
        new_capacity = self.capacity * 2
        new_arr = [0] * new_capacity

        for el in self.arr:
            new_arr[el] = self.arr[el]
        self.arr = new_arr
        self.capacity = new_capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = x
        self.size += 1


    def pop(self):
        if self.size == 0:
            return "ERROR empty array"

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return value

    def __str__(self):
        return str(self.arr)


da = DynamicArray()

for i in range(11):
    da.append(i)
    print(f"array{i}",da)

print("Poped", da.pop())
print("Poped", da.pop())
print("Poped", da.pop())

########################################
# LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

print("\n####Linked List Operations####\n")
ll = SinglyLinkedList()

print("insertion at begin")
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.traverse()

print("insertion at end")
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.traverse()

print("Delete")
ll.delete_by_value(3)
ll.traverse()


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after_node(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = DNode(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return True

            temp = temp.next

        return False

    def delete_at_position(self, pos):
        if pos < 0 or self.head is None:
            return False

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return True

        for _ in range(pos):
            temp = temp.next
            if temp is None:
                return False

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

        return True

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


dll = DoublyLinkedList()

print("insertion")
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

dll.traverse()

dll.insert_after_node(20, 25)
dll.traverse()

print("delete")
dll.delete_at_position(1)
dll.traverse()

dll.delete_at_position(3)
dll.traverse()


#############################
# STACK ADT
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return None

        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return None
        return self.head.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def is_empty(self):
        return self.head is None


print("\n####STACK ADT USING SINGLY LINKED LIST####\n")
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
print("peek", s.peek())
print("pop", s.pop())
s.display()

# QUEUE
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)

        if self.tail is None:  # empty queue
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue Underflow")
            return None

        removed = self.head.data
        self.head = self.head.next

        # If queue becomes empty
        if self.head is None:
            self.tail = None

        return removed

    def front(self):
        if self.head is None:
            print("Queue is empty")
            return None
        return self.head.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

print("\n#### QUEUE ####\n")
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
print(q.front())
print(q.dequeue())
q.display()

###############################
print("\n#########################\n")

def is_balanced(expr):
    stack = Stack()

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expr:
        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":
            if stack.is_empty():
                return False

            top = stack.pop()
            if pairs[ch] != top:
                return False

    return stack.is_empty()

test_cases = ["([])", "([)]", "(((", ""]

for expr in test_cases:
    result = is_balanced(expr)
    print(f"{expr!r} -> {'Balanced' if result else 'Not Balanced'}")