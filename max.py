a=[]
n=int(input("No. of Numbers"))
for i in range(n):
    Number=int(input("Enter Number_{}:".format(i+1)))
    a.append(Number)
print("Numbers are:",a)
max=a[0]
for i in range(n):
    if(a[i]>max):
        max=a[i]      
print("Max",":",max)
      



            
                
            


        
        

            
