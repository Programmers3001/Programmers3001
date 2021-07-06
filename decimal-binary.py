print ('enter d() to convert binary to decimal and b() to convert decimal to binary')
def b():
     n = int(input("Enter Decimal:"))
     L = [] 
     final_value = 0
     while n != 0 :
          temp = n%2
          L.append(temp)
          n=n//2

     remove = ','
     L.reverse()
     dug=len(L)
     if dug==4:
          print (L[0], L[1], L[2], L[3])
     elif dug==5:
          print (L[0], L[1], L[2], L[3], L[4])
     elif dug==6:
          print (L[0], L[1], L[2], L[3], L[4], L[5])
     elif dug==7:
          print (L[0], L[1], L[2], L[3], L[4], L[5], L[6])
def d():
     num = int(input("Enter Binary:"))
     suma= 0
     i=0
     while num!=0:
          rem = num%10
          suma= suma+rem*pow(2,i)
          num=int(num/10)
          i=i+1
     print (suma)
