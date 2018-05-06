"""square root of number"""

x=int(input("enter the number you want to find square root:"))
e=float(input("enter the error:"))
high =x
low =1
ans = (high+low)/2
steps =0
while abs(ans**2-x)>e:
    steps+=1
    if ans**2-x<0:
        low = ans
    else:
        high = ans
    ans=(high+low)/2
print("the square root of",x,"with error ",e,"is",ans ,"with",steps,"number of steps")
