dataword=[]
codeword=[]
divisor=[]
datalen=int(input("Enter the length of dataword\n"))
codelen=int(input("enter the length of codeword\n"))

print("enter the data word in binary format");
for i in range(0,datalen):
    b=int(input())
    if (b==0) or (b==1):
        dataword.append(b)
    else:
        print("invalid input")
append=codelen-datalen
for i in range(0,append):
    dataword.append(0)

print("enter the divisor in binary format");
for i in range(0,datalen):
    b=int(input())
    if (b==0) or (b==1):
        divisor.append(b)
    else:
        print("invalid input")

print("dataword",dataword)
print("length of codeword",codelen)
print("divisor",divisor)
datalen=len(dataword)
print("new length of dataword",datalen)
divisorlen=len(divisor)
print("length if divisor",divisorlen)

j=0
res=[]
for i in range(0,4):
    res.append(dataword[i])
print("new res",res)
def xor(divisor,res):
    print("divisor in xor",divisor);
    print("res in xor",res);
    result = []  
    for i in range(0,divisorlen): 
        if divisor[i] == res[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return (result) 
   


for i in range(0,divisorlen):
    if (res[0]==1):
        res=xor(divisor,res)
        res= [int(i) for i in res]

        print("res after xor",res)
        res.append(0)
        res.pop(0)
        print("res in if",res)
    else:
        res.append(0)
        res.pop(0)
        print("res in else",res)


print(res)
for i in range(0,divisorlen):
    codeword.append(dataword[i])
for i in range(0,3):
    codeword.append(res[i])

print("codeword is",codeword)
                
      

        
    
