x = int(input("Enter the number : "))
k = x
count = 0
while (x != 0):
    x = x//10
    count = count+1
sum, dig = 0, 0
num = k
while (k != 0):
    dig = k % 10
    sum = sum+(dig**count)
    k = k//10
#print(sum)
if (sum == num):
    print(num,"is an Armstrong number.")
else:
    print(num,"is Not an Armstrong number.")
