text = "  Hello, World! Welcome to Python.  "

print("Original :", repr(text))
print()

# 1. upper() — converts all characters to uppercase
print("upper()  :", text.upper())

# 2. lower() — converts all characters to lowercase
print("lower()  :", text.lower())

# 3. strip() — removes leading and trailing whitespace
print("strip()  :", text.strip())

# 4. split() — splits string into a list by delimiter (default: whitespace)
words = stripped.split()
print("split()  :", words)

csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(",")
print("split(','):", fruits)

# 5. join() — joins a list into a string using a separator
joined = " | ".join(fruits)
print("join()   :", joined)

rejoined = " ".join(words)
print("join(' '):", rejoined)

# 6. replace() — replaces occurrences of a substring
replaced = stripped.replace("World", "Python")
print("replace():", replaced)

# 7. find() — returns index of first occurrence (-1 if not found)
index = stripped.find("World")
print("find()   :", index, f"→ '{stripped[index:index+5]}'")

