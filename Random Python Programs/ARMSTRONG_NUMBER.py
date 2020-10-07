#Write a program to check an Armstrong number of n digits
#num = 1634
# Changed num variable to string,
# and calculated the length (number of digits)
num=int(input("Enter a No:"))
order = len(str(num))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
# display the result
if num == sum:
   print(num,"is an a number")
else:
   print(num,"is not an a number")
