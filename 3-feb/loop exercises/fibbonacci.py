terms = int(input("enter number of terms: "))

n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence:")
while count < terms:
    print(n1, end="  ")
    temp = n1 + n2
    # update values
    n1 = n2
    n2 = temp
    count += 1


#Output :
#enter number of terms: 15
#Fibonacci sequence:
#0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
