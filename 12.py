num = int(input("Enter your num : "))
for i in range(1, num+1):
    for j in range(1, num*2):
        if j < num and j >= num+1-i:
            print(num+1-j, end=' ')
        elif j == num:
            print(1, end=' ')
        elif j > num and (j < num+i):
            print(j-num+1, end=' ')
        else:
            print(" ", end=' ')
    print()
