#varlengthparamex3.py
def disp(sname,*k):  # here k is holding varaible number
      print("-----------------------------------------")
      print("Name of student:{}".format(sname))
      for val in k:
            print("\t{}".format(val),end="")
            print()
           # print("------------------------------------")
#main program
disp("RS",10) #function call
disp("JG",10,20) #function call
disp("DR,10,20,30")#function call
disp("Travis","Java","Python","OS")#function call
disp("tim") 