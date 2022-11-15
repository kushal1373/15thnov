####if the given number is divided by 3 then print "fuzz"

number=int(input("Enter the number you want to divide with"))
if number%3 and number%5==0:
    print("fuzz")
elif number%5:
    print("Hello all")
elif number%3==0:
    print("sorry 404 error")
else:
    print("out of order")


days_list=[
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'friday',
    'Saturday',


]

for day in days_list:
    print(f"the single days is: {day}")

Month_list=['January','February','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']

my_value=Month_list[3]
print(my_value)

print('banana'>'Banana')

def