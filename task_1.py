#takes basic product information
product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product :"))
Quantity = input("Enter the quantity of the product :")
manufacturer = input("Enter the manufacturer of the product :") 

print("==============================")
print("Product Name:", product_name)
print("Price:", price)
print("Quantity:", Quantity)            
print("Manufacturer:", manufacturer)
print("==============================")

# takes a student's marks in 5 subjects (out of 100) and calculates their percentage and grade (A: ≥90%, B: ≥80%, C: ≥70%, D: ≥60%, F: <60%). 

subject1 = input("Enter the subject1 marks :")
subject2 = input("Enter the subject2 marks :")
subject3 = input("Enter the subject3 marks :")
subject4 = input("Enter the subject4 marks :")
subject5= input("Enter the subject5 marks :")

print("percentage ",(int(subject1) + int(subject2) + int(subject3) + int(subject4) + int(subject5)) / 5)

if((int(subject1) + int(subject2) + int(subject3) + int(subject4) + int(subject5)) / 5) >= 90 :
    print("garde A")
elif((int(subject1) + int(subject2) + int(subject3) + int(subject4) + int(subject5)) / 5) >= 80 :
    print("garde B")
elif((int(subject1) + int(subject2) + int(subject3) + int(subject4) + int(subject5)) / 5) >= 70 :
    print("grade c")
elif((int(subject1) + int(subject2) + int(subject3) + int(subject4) + int(subject5)) / 5) >= 60 :
    print("grade D")
else:
    print("grade F")




