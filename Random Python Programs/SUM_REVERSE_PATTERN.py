ip = input("Enter a no.\t")
length = len(ip) - 1
sum = 0
print("The reverse of  ur no. is ", end = '')
while length >= 0:
    print(ip[length], end = '')
    sum += int(ip[length])
    length -= 1
print("\nThe sum of the digits is: ", sum)

print()


#PATTERN
rows = int(input("Enter the no. of rows for pattern: "))
for i in range(1, rows+1):
    print('#'*i)
