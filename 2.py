list1=()
list2=()
list3=()

class temperature:
    f=0.0
    c=0.0

    def f_to_c(self):
        self.f=float(input("Enter Value in Fahrenheit : "))
        self.c=5*(self.f-32)/9
        print(round(self.c,4))

    def c_to_f(self):
        self.c=float(input("Enter Value in Celsius : "))
        self.f=1.8*self.c+32
        print(self.f)

from_t=("||",)

temp=temperature()
temp.f_to_c()
from_t=from_t+("Converted from F : ",temp.f,"To C : ",temp.c," || ")
print(from_t)
temp.c_to_f()
from_t=from_t+("Converted from C : ",temp.c,"To F : ",temp.f," || ")
print(from_t)