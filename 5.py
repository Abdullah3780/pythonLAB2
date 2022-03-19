import string


num = str(input("Enter your 5 Digit Number"))
a = ''
for i in range(1, len(num)+1):
    a += num[len(num)-i]
print(a)
