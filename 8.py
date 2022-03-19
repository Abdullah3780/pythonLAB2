from ast import Num
from math import ceil


num = int(input("Enter your no. : "))
for i in range(2, ceil(num/2)):
    if num % i == 0:
        print("No. is not prime")
        break
else:
    print("No. is prime")
