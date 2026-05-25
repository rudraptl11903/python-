#tuple basic

#using String
tup = ("rudra" , "patel")
print(tup)

# Using List
li = [1,2,3,4,5]
print(tuple(li))

# Using Built-in Function
tup = tuple('rudra')
print(tup)

#Creating a Tuple with Mixed Datatypes
tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)


tup = tuple('Rudrapatel')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])
