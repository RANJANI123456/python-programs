n=int(input("Enter a number: "))
sum = 0
if(n <= 0):
    print("enter a whole positive numbers:")
else:
    sum=sum+n
    n=n-1
    print("The sum of first n natural numbers is",sum)
