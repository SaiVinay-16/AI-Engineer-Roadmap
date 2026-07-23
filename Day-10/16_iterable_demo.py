# Examples of different iterable objects

# 1. List
my_list = [10, 20, 30, 40]
print("List elements:")
for item in my_list:
    print(item)

# 2. Tuple
my_tuple = ("apple", "banana", "cherry")
print("\nTuple elements:")
for item in my_tuple:
    print(item)

# 3. String
my_string = "Hello"
print("\nString characters:")
for char in my_string:
    print(char)

# 4. Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "Hyderabad"}
print("\nDictionary elements (key -> value):")
for key in my_dict:
    print(key, "->", my_dict[key])

# 5. Set
my_set = {1, 2, 3, 4, 5}
print("\nSet elements:")
for item in my_set:
    print(item)
