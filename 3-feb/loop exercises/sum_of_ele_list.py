#Sum of all elements in a list

n = int(input('Enter number of elements in the list: '))
lst = []
for i in range(n):
    num = int(input("Enter the number: "))
    lst.append(num)

sum = 0
j = 0

while(j < len(lst)):
    sum += lst[j]
    j += 1

print("Sum of all elements in the list: ",sum)


#Output
#Enter the number: 26
#Enter the number: 52
#Enter the number: 45
#Enter the number: 75
#Enter the number: 23
#Sum of all elements in the list:  221
