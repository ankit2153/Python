dicName={}
for i in range(3):
    name=input("UID:")
    Phone=int(input("Password:"))
    dicName[name]=Phone
print(dicName)    
def Verify():
    NameV=input("UID:")
    passV=int(input("Password:"))
    if(dicName[NameV]==passV):
        print("Verified")
    else:
        print('Incorrect uid or password')    
Verify()        
