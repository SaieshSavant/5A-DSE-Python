n=int(input("Enter the no:\n"))
a=n
length=len(str(n))
sum=0
while n!=0:
    digit=n%10
    sum+=digit**length
    n=n//10
if a==sum:
    print("It is an armstrong no")
else:
    print("It is not armstrong no")   