#Find prime numbers in a given range
a = int(input('Enter the starting range: '))
b = int(input('Enter the ending range: '))

for i in range(a, b+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


#Output
#Enter the starting range: 5
#Enter the ending range: 23
#5
#7
#11
#13
#17
#19
#23
