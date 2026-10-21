#sum of two numbers
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
sum=num1+num2
print("Sum of two numbers:",sum)

#odd or even
if(sum%2==0):
    print("It is even")
else:
    print("It is Odd")

#factorial    
n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial of ",n,"is ",factorial)

#fibonacci
z=7
a=0
b=1
print(a)
print(b)
for i in range(z-2):
    nextnum=a+b
    print(nextnum)
    a=b
    b=nextnum

#string reverse
text=input("Enter a string to reverse:")
reverse=text[::-1]
print("Reversed text:",reverse)

#palindrome check
if text==reverse:
    print("It is palindrome")
else:
    print("It is not a palindrome")

#leap year check
year=int(input("Enter the year check if its leap year or not:"))
if(year%4==0 and year%100!=0) or(year%400==0):
    print(year," is leap year")
else:
    print(year," is not a leap year")


#Armstrong number
numtext=input("Enter the number:")
digitcount=len(numtext)
total=0
for digit in numtext:
    number = int(digit)
    total= total+ (number ** digitcount)
if total == int(numtext):
    print("It is an Armstrong number!")
else:
    print("It is NOT an Armstrong number.")













