s=input("Enter a String: ")
rev=""
for i in s:
    rev=rev+i
if s==rev:
    print("Palindrome")
else:
    print("NOT palindrome")    