#Creating a Dictionary
a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)

#Accessing Dictionary

d = {"name": "rudra", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()

#Add and update

d = {"name": "rudra"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "patel"   # Updating an existing value
print(d)

#  Removing Dictionary Items

# 1. del()
d = {"a": 1, "b": 2}
del d["a"]
print(d)

#2 pop()
d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)

# 3.  popitem()
d = {"a": 1, "b": 2}
print(d.popitem())

# 4. clear()
d = {"a": 1, "b": 2}
d.clear()
print(d)
