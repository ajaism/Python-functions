#varlengthparamex5.py
def findsumavg(sname,*n,city="Hyd"):
     print("-----------------------------------------")
     print("Name of the student={}".format(sname))
     print("Student Lives: {}".format(city))
     s=0
     for val in n:
         s=s+val
         print("\t\t{}".format(val))
     else:
          print("-----------------------------------------")
          print("\tsum={}".format(s))
          print("\tAvg={}".format(s/len(n)))
         # print("------------------------------------------")
#main program
findsumavg("Ram",10,20)
findsumavg("Ram Krishna",10,20,34.56)
findsumavg("Rossum",10.2,-20,34.2,3.4,5.6)
findsumavg("Rajinush",10,-10,20,-20,city="Ameerpet")
