num=int(input("enter the number:"))
x=num
binary='' 
if num<0:
    num = abs(num)
    sign='-'
else:
    sign=''
while num>0:
    binary=str(num%2)+binary
    num=num//2
print("binaryform of",x,"is:",sign+binary)
