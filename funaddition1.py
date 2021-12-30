#funaddition1.py
#this program computes addition of two values by using function
def addop(a,b):
        c=a+b
        return c
#main program
k= float(input("Enter First Value:"))
v= float(input("Enter Second Value:"))
res=addop(k,v)
print("sum={}".format(res))