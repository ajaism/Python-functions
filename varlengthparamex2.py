#varlengthparam3x2.py
def disp(*k): #Here k is holding number of values o <class'tuple'>
   #print("-------------------------------------------------------")
   for val in k:
        print("\t{}".format(val),end="")
   print()
   #print("----------------------------------------------")
# Main Program
disp(10)# function call
disp(10,20)#function call
disp(10,20,30)#function call
disp("java","Python","DS")#function call
disp()