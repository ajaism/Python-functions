#funaddition4.py
def addop():
     #taking input
     m,n=float(input("Enter first value: ")),float(input("Enter Second Value: "))
     #process
     k=m+n
     #return the result
     return m,n,k
#Main Program
m,n,k=addop()
print("sum({},{})={}".format(m,n,k))



