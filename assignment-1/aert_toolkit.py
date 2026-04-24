import sys
sys.setrecursionlimit(10000)

# part a

class StackADT:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def __repr__(self):
        return f"Stack ({self.data})"

print("\n=== Stack ===")
stack = StackADT()
s = StackADT()
for val in [10, 20, 30]:
    s.push(val)
print(f"After pushing 10, 20, 30  →  {s}")
print(f"peek()  = {s.peek()}")
print(f"pop()   = {s.pop()}")
print(f"size()  = {s.size()}")
print(f"Stack now: {s}")
print(f"is_empty() = {s.is_empty()}")

# part b
def factorial(n):
    if n < 0:
        return "Not possible"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\n==factorial")
for n in [0, 1, 5, 10]:
    print(f"  factorial({n:2d}) = {factorial(n)}")

# --------------
naive_calls = 0
memo_calls = 0

def fib_nav(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_nav(n - 1) + fib_nav(n - 2)

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}
    if n <= 1:
        return n

    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print("\n== fib_nav & fib_memo =")

print(f"  {'n':>3}  {'Result':>12}  {'Naive calls':>12}  {'Memo calls':>11}")
print(f"  {'-' * 3}  {'-' * 12}  {'-' * 12}  {'-' * 11}")
for n in [5, 10, 20, 30]:

    naive_calls = 0
    result_n = fib_nav(n)
    memo_calls = 0
    result_m = fib_memo(n)
    print(f"  {n:>3}  {result_n:>12}  {naive_calls:>12}  {memo_calls:>11}")

#part c
hanoi_moves = StackADT()

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        hanoi_moves.push(move)
        return
    hanoi(n - 1, source, auxiliary, destination)
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    hanoi_moves.push(move)
    hanoi(n - 1, auxiliary, source, destination)

print("\n=== hanoi ===")
hanoi(3, 'A', 'B', 'C')
print(f"\n  Total moves stored in StackADT: {hanoi_moves.size()}")
print(f"  (Expected: 2^3 - 1 = 7 moves)")

# part d

mid_stack = StackADT()

def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    mid_stack.push(mid)

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


print("\n=== binary_search ===")
arr = [1, 3, 5, 7, 9, 11, 13]
print(f"  Array: {arr}\n")

for key in [7, 1, 13, 2]:
    mid_stack.data.clear()
    idx = binary_search(arr, key, 0, len(arr) - 1)
    mids = list(mid_stack.data)
    if idx != -1:
        print(f"  Search {key:>2} → Found at index {idx}  | mids visited: {mids}")
    else:
        print(f"  Search {key:>2} → NOT FOUND (-1)       | mids visited: {mids}")

