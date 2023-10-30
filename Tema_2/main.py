#1.
def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list

result = fibonacci(10)
print(f"Ex. 1:\n{result}\n")

#2.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num + 1 // 2):
        if num % i == 0:
            return False
    return True
def get_primes(numbers):
    list = []
    for num in numbers:
        if is_prime(num):
            list.append(num)
    return list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = get_primes(numbers)
print(f"Ex. 2:\n{prime_numbers}\n")


#3.
def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
result = list_operations(list_a, list_b)
print("Ex. 3:\nIntersection:", result[0])
print("Union:", result[1])
print("A - B:", result[2])
print("B - A:", result[3], "\n")


#4.
def compose(notes, moves, start_position):
    song = [notes[start_position]]
    current_position = start_position
    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])
    return song

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
composed_song = compose(notes, moves, start_position)
print(f"Ex. 4:\n{composed_song}\n")


#5.
def replace_below_principal_diagonal(matrix):
    result = matrix
    for i in range(len(result)):
        for j in range(len(result[i])):
            if j < i:
                result[i][j] = 0
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = replace_below_principal_diagonal(matrix)
print("Ex. 5:")
for row in new_matrix:
    print(row)
print("\n")


#6.
def find_items_appearing_x_times(x, *args):
    combined_list = []
    for lst in args:
        combined_list.extend(lst)
    count_dict = {}
    for item in combined_list:
        count_dict[item] = count_dict.get(item, 0) + 1
    result = []
    for item, count in count_dict.items():
        if count == x:
            result.append(item)
    return result

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2

result = find_items_appearing_x_times(x, list1, list2, list3, list4)
print(f"Ex. 6:\n{result}\n")


#7.
def is_palindrome(x):
    return str(x) == str(x)[::-1]

def find_palindromes(numbers):
    palindromes = []
    for num in numbers:
        if is_palindrome(num):
            palindromes.append(num)
    if not palindromes:
        return (0, None)
    max_palindrome = max(palindromes)
    return (len(palindromes), max_palindrome)

numbers = [121, 123, 1331, 454, 567]
result = find_palindromes(numbers)
print(f"Ex. 7:\n{result}\n")


#8.
def generate_ascii_lists(x=1, strings=[], flag=True):
    result_lists = []
    for string in strings:
        char_list = []
        if flag:
            for c in string:
                if ord(c) % x == 0:
                    char_list.append(c)
        else:
            for c in string:
                if ord(c) % x != 0:
                    char_list.append(c)
        result_lists.append(char_list)

    return result_lists

x = 2
strings = ["test", "hello", "lab002"]
flag = False

result = generate_ascii_lists(x, strings, flag)
print(f"Ex. 8:\n{result}\n")


#9.
def find_bad_seats(matrix):
    bad_seats = []
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[i])-1, -1, -1):
            height = matrix[i][j]
            for k in range(i - 1, -1, -1):
                if matrix[k][j] >= height:
                    bad_seats.append((i, j))
                    break

    return bad_seats


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

bad_seats = find_bad_seats(matrix)
print(f"Ex. 9:\n{bad_seats}\n")


#10.
def combine_lists(*args):
    max_length = max(len(lst) for lst in args)
    result = []
    for i in range(max_length):
        tuples = tuple(lst[i] if i < len(lst) else None for lst in args)
        result.append(tuples)
    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = combine_lists(list1, list2, list3)
print(f"Ex. 10:\n{result}\n")


#11.
def get_character(tuple_element):
    return tuple_element[1][2]
def order_tuples(lst):
    return sorted(lst, key=get_character)

tuples = [('abc', 'bcd'), ('abc', 'zza')]

result = order_tuples(tuples)
print(f"Ex. 11:\n{result}\n")


#12.
def group_by_rhyme(words):
    rhyme_dict = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme not in rhyme_dict:
            rhyme_dict[rhyme] = [word]
        else:
            rhyme_dict[rhyme].append(word)
    return list(rhyme_dict.values())

words = ['ana', 'banana', 'carte', 'arme', 'parte']

result = group_by_rhyme(words)
print(f"Ex. 12:\n{result}")
