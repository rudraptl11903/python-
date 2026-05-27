# basic 
s = {10, 50, 20}
print(s)
print(type(s))

# type casting 
s = set(["a", "b", "c"])
print(s)

# add element 
s.add("d")
print(s)

# method for set

# 1. add
s = {"a", "b", "c"}
s.add("d")
print(s)

# 2. Union 

a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# 3. intersection 

a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

#4.  Difference of Sets: 
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

#5 Clearing a Set

s = {1, 2, 3}
s.clear()
print(s)
