# Will create a multiplication table based on the number you selected


print("Please enter a number", "\n")
print(">")
n = int(input())

i=1

for i in range (11):
    print (n, "x", i, "=", n*i)
    i=i+1
    