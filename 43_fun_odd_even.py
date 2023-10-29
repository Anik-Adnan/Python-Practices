#test number is even or odd
def odd_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     return "Odd"

# def odd_even(num):
#     if num%2==0:
#         return True
#     return False

# def is_even(num):
#         return num%2==0 #ture

n=int(input("Enter number :"))
print(f"number is : {odd_even(n)}")