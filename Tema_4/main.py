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
        self.matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            self.matrix.append(row)

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transposed_matrix = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(self.matrix[j][i])
            transposed_matrix.append(row)
        self.matrix = transposed_matrix
        self.n, self.m = self.m, self.n

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Number of columns must be equal to the number of rows")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result

    def apply_transformation(self, transform):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = transform(self.matrix[i][j])

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'
        return result


print(f"Ex. 3:")
matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)
print("matrix:")
print(matrix)

print(f"matrix[1][2]: {matrix.get(1, 2)}")

matrix.transpose()
print("\nTransposed Matrix:")
print(matrix)

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 10)
matrix2.set(0, 1, 11)
matrix2.set(1, 0, 13)
matrix2.set(1, 1, 14)
matrix2.set(2, 0, 13)
matrix2.set(2, 1, 14)

matrix.transpose()
result_matrix = matrix.multiply(matrix2)
print("\nmatrix1 x matrix2:")
print(result_matrix)

matrix.apply_transformation(lambda x: x * 2)
print("\nMatrix after multiplying by 2:")
print(matrix)

