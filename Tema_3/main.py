#1.
def list_operations(a, b):
    result = []
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    result.append(intersection)
    result.append(union)
    result.append(a_minus_b)
    result.append(b_minus_a)
    return result

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
result = list_operations(list_a, list_b)
print(f"Ex. 1:\n{result}\n")


#2.
def character_count(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

result = character_count("Ana has apples.")
print(f"Ex. 2:\n{result}\n")


#3.
def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False
    if isinstance(dict1, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        for key in dict1.keys():
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        return True
    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False
        for i in range(len(dict1)):
            if not compare_dicts(dict1[i], dict2[i]):
                return False
        return True
    else:
        return dict1 == dict2

# Example usage
dict1 = {'a': [1, 2, {'x': 3}], 'b': {'c': 4}}
dict2 = {'a': [1, 2, {'x': 3}], 'b': {'c': 4}}
result = compare_dicts(dict1, dict2)
print(f"Ex. 3:\n{result}\n")


#4.
def build_xml_element(tag, content, **attributes):
    attribute_string = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    return f'<{tag} {attribute_string}>{content}</{tag}>'

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(f"Ex. 4:\n{result}\n")


#5.
def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix):
            return False
        if middle not in value[1:-1]:
            return False
        if not value.endswith(suffix):
            return False
    return True

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {
    "key1": "come inside, it's too cold out",
    "key2": "start with winter and end with winter",
    "key3": "this is not valid"
}
result = validate_dict(rules, d)
print(f"Ex. 5:\n{result}\n")


#6.
def count_unique_duplicates(input_list):
    unique_elements = set(input_list)
    num_unique = len(unique_elements)
    num_duplicates = len(input_list) - num_unique
    return (num_unique, num_duplicates)

my_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 7]
result = count_unique_duplicates(my_list)
print(f"Ex. 6:\n{result}\n")


#7.
def set_operations(*args):
    operations = {
        "|": lambda a, b: a.union(b),
        "&": lambda a, b: a.intersection(b),
        "-": lambda a, b: a.difference(b),
    }
    result = {}
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            set1 = args[i]
            set2 = args[j]
            for op, operation in operations.items():
                key = f"{set1} {op} {set2}"
                result[key] = operation(set1, set2)
    return result

set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}

result = set_operations(set1, set2, set3)
print("Ex. 7:")
for key, value in result.items():
    print(f"{key}: {value}")
print("\n")


#10.
def loop(mapping):
    visited = set()
    current_key = mapping["start"]
    result = []
    while current_key not in visited:
        result.append(current_key)
        visited.add(current_key)
        current_key = mapping[current_key]
    return result

result = loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
print(f"Ex. 10:\n{result}\n")


#11.
def my_function(*args, **args2):
    args_set = set(args)
    matching_count = sum(1 for arg in args_set if arg in args2.values())
    return matching_count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(f"Ex. 11:\n{result}")

