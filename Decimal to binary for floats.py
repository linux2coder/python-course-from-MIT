p=0
while((2**p)*x)%1!=0:
    
     p+=1
num = int(x*(2**p))
binary = ''
if num ==0:
    binary ='0'
while num > 0:
    binary = str(num%2)+binary
    num = num//2
for i in range(p-len(binary)):
    binary = '0'+ binary
binary = binary[0:-p]+'.'+binary[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(binary))
