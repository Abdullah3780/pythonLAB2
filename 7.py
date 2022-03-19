num1 = int(input("Enter your first No. : "))
num2 = int(input("Enter your Second No. : "))
gcd = 1
divisorsOfNum1 = []
divisorsOfNum2 = []
commonDivisors = []

for i in range(1, num1+1):
    if num1 % i == 0:
        divisorsOfNum1.append(i)

for i in range(1, num2+1):
    if num2 % i == 0:
        divisorsOfNum2.append(i)
for i in range(0, len(divisorsOfNum1)):
    for j in range(0, len(divisorsOfNum2)):
        print(i, j)
        if divisorsOfNum1[i] == divisorsOfNum2[j]:
            gdc = divisorsOfNum1[i]
            continue

print(divisorsOfNum1)
print(divisorsOfNum2)
print(gdc)
