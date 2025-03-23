


# class Person:
#     legs = "Twenty"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

# p = Person("Alice", 30)
# m = Person("John Doe", 20)

# # print(p.__dict__)  # {'name': 'Alice', 'age': 30}
# # print(m.__dict__)  # {'name': 'Alice', 'age': 30}
# # print(Person.__dict__)  # {'name': 'Alice', 'age': 30}

# print(setattr(m, 'degree', 'Bachelor'))
# print(getattr(m, 'name', None))
# print(m.degree)

my_dict = {'a': 1, 'b': 2}

# Using get() with "" as default
result1 = my_dict.get('q')
print(result1)  # Output: ""

# Using get() with '' as default
result2 = my_dict.get('q')
print(result2)  # Output: ''