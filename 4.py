num = int(input("Enter your no. : "))
fact = 1
for i in range(1, num+1):
    fact = i*fact
print(str(i)+"! = "+str(fact))
