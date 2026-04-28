from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        return root

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True
        elif data < root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.data)
            self._inorder(root.right, result)

    def delete(self, key):
        return self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self._min_value(root.right)
            root.data = successor.data
            root.right = self._delete(root.right, successor.data)
        return root

    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current




bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)


print("Insertion\n", bst.inorder())

print("\nSearch 20:", bst.search(20))
print("Search 70:", bst.search(70))

print("\nAfter Deleting (20)")
bst.delete(20)
print(bst.inorder())

print("\nAfter Deleting (30)")
bst.delete(30)
print(bst.inorder())

print("\nAfter Deleting (50)")
bst.delete(50)
print(bst.inorder())



class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.labels = ["A", "B", "C", "D", "E", "F"]

    def add_edge(self, u, v, w):
        self.graph[u].append([v, w])

    def print_graph(self):
        print("Adjacency List")
        for i in range(self.V):
            edge = " -> ".join([f"{self.labels[nbr]}({wt})" for nbr, wt in self.graph[i]])
            print(f"{self.labels[i]} -> {edge}")

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque([start])

        print("\nBFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            if not visited[node]:
                print(self.labels[node], end=" ")
                visited[node] = True

                for neighbor, _ in self.graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = [False] * self.V
        print("\nDFS Traversal:", end=" ")
        self._dfs_recursive(start, visited)
        print()

    def _dfs_recursive(self, node, visited):
        if not visited[node]:
            print(self.labels[node], end=" ")
            visited[node] = True

            for neighbor, _ in self.graph[node]:
                self._dfs_recursive(neighbor, visited)

g = Graph(6)

edges = [
    (0, 1, 2), (0, 2, 4),
    (1, 3, 7), (1, 4, 3),
    (2, 4, 1), (2, 5, 8),
    (3, 5, 5),
    (4, 3, 2), (4, 5, 6)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

g.print_graph()

g.bfs(0)
g.dfs(0)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def print_table(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

ht = HashTable(5)

keys = [10, 15, 20, 7, 12]

for k in keys:
    ht.insert(k, f"Value{k}")

ht.print_table()

print(ht.get(10))
print(ht.get(7))
print(ht.get(12))

ht.delete(15)
ht.print_table()