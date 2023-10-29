#elif means else if
age= int(input("Enter age :"))
if age==0 or age<0:
    print("You cann't watch")
elif 0<age<=3:
    print("Ticket price : free")
elif 3<age<=10:
    print("Ticket price :150tk")
elif 10<age<=60:
    print("Ticket price : 250tk")
else :
    print("Ticket price : 200tk")

