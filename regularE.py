#import re
#txt = "Use pf pyhton in Machine Learning"
#x = re.search("^Use.*Learning$", txt)
#if (x):
    #print("YES! We have a match!")
#else:
    #print("No match")
#import re
#txt = "Use  of python in Machine Learing"
#x = re.findall("e" , txt)
#print(x)
import re
txt = "Pyhton is one of the most popular langauge"
searchobj = re.search("\s",txt)
print("The first white-space character is located")