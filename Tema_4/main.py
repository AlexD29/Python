# 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Ex. 1:")
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print("\n")


# 2
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Ex. 2:")
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print("\n")


# 3
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get_element(self, i, j):
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.m)]
        aux = self.n
        self.n = self.m
        self.m = aux

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second "
                             "matrix")

        result = Matrix(self.n, other.m)

        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result

    def apply_transformation(self, transformation):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = transformation(self.matrix[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


print(f"Ex. 3:")
matrix = Matrix(3, 3)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 2)
matrix.set_element(0, 2, 3)
matrix.set_element(1, 0, 4)
matrix.set_element(1, 1, 5)
matrix.set_element(1, 2, 6)
matrix.set_element(2, 0, 7)
matrix.set_element(2, 1, 8)
matrix.set_element(2, 2, 9)
print("Matrix:")
print(matrix)

print(f"Element at (1, 2): {matrix.get_element(1, 2)}")

matrix.transpose()
print("\nTransposed Matrix:")
print(matrix)

matrix2 = Matrix(3, 3)
matrix2.set_element(0, 0, 10)
matrix2.set_element(0, 1, 11)
matrix2.set_element(0, 2, 12)
matrix2.set_element(1, 0, 13)
matrix2.set_element(1, 1, 14)
matrix2.set_element(1, 2, 15)
matrix2.set_element(2, 0, 16)
matrix2.set_element(2, 1, 17)
matrix2.set_element(2, 2, 18)

matrix.transpose()
result_matrix = matrix.multiply(matrix2)
print("\nResult of Matrix Multiplication:")
print(result_matrix)

matrix.apply_transformation(lambda x: x * 2)
print("\nMatrix after applying transformation (multiply by 2):")
print(matrix)

