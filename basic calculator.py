# Basic calculator


a = int (input("A = "))
b = int (input("B = "))
op = input ("add/sub/mul/div: ")
if op == "add":
    c = a + b
elif op == "sub":
    c = a-b
elif op == "mul":
    c = a*b
elif op == "div":
    c = a/b
else: 
    c = "Error"
    
print("Answer = ", c)