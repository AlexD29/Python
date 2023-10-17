import math

#1.
def gcd(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd
def get_input():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number ('q' to quit): ")
            if user_input.lower() == 'q':
                break
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter only numbers.")
    return numbers
print("Ex. 1:")
numbers = get_input()
if numbers:
    gcd = gcd(numbers)
    print("GCD = " + str(gcd) + "\n")
else:
    print("No numbers entered.\n")


#2.
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for c in input_string:
        if c in vowels:
            count += 1
    return count

nr = count_vowels("Ana are mere.")
print("Ex. 2:\nNumber of vowels: " + str(nr) + "\n")


#3.
def get_occurrences(first, second):
    count = 0
    i = 0
    while i < len(second):
        i = second.find(first, i)
        if i == -1:
            break
        count += 1
        i += len(first)
    return count

first = "ac"
second = "acest accent este foarte ciudat."
occurrences = get_occurrences(first, second)
print("Ex. 3:\nNumber of occurrences: " + str(occurrences) + "\n")


#4.
def UpperCamelCase_into_lowercase_with_underscores(string):
    output = ""
    for c in string:
        if c.isupper():
            output += '_' + c.lower()
        else:
            output += c
    if output.startswith('_'):
        output = output[1:]
    print("Ex. 4:\n" + output + "\n")

upper_camel_case_string = "UpperCamelCaseString"
UpperCamelCase_into_lowercase_with_underscores(upper_camel_case_string)


#5.
def spiral_traverse(matrix):
    result = ""
    while matrix:
        result += matrix[0]
        matrix = matrix[1:]

        if matrix and matrix[0]:
            result += "".join(row[-1] for row in matrix)
            matrix = [row[:-1] for row in matrix]

        if matrix:
            result += matrix[-1][::-1]
            matrix = matrix[:-1]

        if matrix and matrix[0]:
            result += "".join(row[0] for row in matrix[::-1])
            matrix = [row[1:] for row in matrix]
    return result

matrix = [
    "firs",
    "n_lt",
    "oba_",
    "htyp"
]

result = spiral_traverse(matrix)
print("Ex. 5:\n" + result + "\n")


#6.
def is_palindrome(x):
    aux = str(x)
    return aux == aux[::-1]

result = is_palindrome(12321)
print("Ex. 6:\n" + str(result) + "\n")


#7.
def extract_number(text):
    number = ""
    for c in text:
        if c.isdigit():
            number += c
        elif number:
            break
    if number:
        return int(number)
    else:
        return None

result1 = extract_number("An apple is 123 USD")
result2 = extract_number("abc123abc2")
print("Ex. 7:\n" + str(result1))
print(str(result2) + "\n")


#8.
def count_number_of_one_bits(x):
    count = 0
    while x:
        binary_x = bin(x)[2:]
        last_bit = binary_x[-1]
        if last_bit == '1':
            count = count + 1
        x = x // 2
    return count

result = count_number_of_one_bits(24)
print("Ex. 8:\nNumber of 1 bits: " + str(result) + "\n")


#9.
def most_common_letter(text):
    text = text.lower()
    max_count = 0
    most_common = None

    for c in text:
        if c.isalpha():
            count = text.count(c)
            if count > max_count:
                max_count = count
                most_common = c

    return (most_common,max_count)

result = most_common_letter("an apple is not a tomato")
print("Ex. 9:\n" + str(result) + "\n")


#10.
def count_words(text):
    words = text.split()
    return len(words)

result = count_words("I have Python exam tomorrow.")
print("Ex. 10:\nThe text has " + str(result) + " words.")
