
student = ["Rudra", 101, 20, "CE", "A"]

print("Original List:", student)

student.append("Pass")
print("After Append:", student)

student.insert(2, "Ganpat University")
print("After Insert:", student)

student.extend(["Python", "Java"])
print("After Extend:", student)

student[0] = "Rudra Patel"
print("After Update:", student)

student.remove("A")
print("After Remove:", student)