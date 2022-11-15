print("Hello {}, your balance is {}.".format("kushal",1000000),end="") 
print("hello {}, your servicing due date is {}.".format("kushal","27nov"))

print(f"{0.1:.60f}")
print(f"{0.2:.60f}")
print(f"{0.1+0.2:.2f}")
print(f"{0.3:.60f}")

a=123
b=complex(a)
print(b)

num1= int(input("Enter first number : "))
num2= int(input("Enter Second number: "))
res=num1 - num2
print("Sum of "+str(num1)+" and "+str(num2), " is "+str(res))

import pdb
bike1= "yamaha"
bike1_price = 25000

bike2 ="honda"
bike2_price =50000

pdb.set_trace()
name = input("Enter your name: ")
choose = int(input("press 1 for yamaha and 2 for honda: "))
print(f"hello{name}")

if choose==1:
    print(f"{bike1} will cost u {bike1_price}")
elif choose==2:
    print(f"{bike2}will cost you {bike2_price+2000}")
else:
    print("press only 1 or 2") 

savings=int(input("Enter your pocket money"))
if savings>3000:
    print("Dating with sita")
elif savings>2000:
    print("Dating with rita")
else:
    print("go out")



