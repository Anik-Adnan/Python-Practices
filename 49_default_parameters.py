#default parameter
# def user_info(first_name,last_name,age):
#     print(f"your name is {first_name}")
#     print(f"your name is {last_name}")
#     print(f"your name is {age}")
# user_info("anik","adnan",20)

# def user_info(first_name,last_name,age=None):
#     print(f"your name is {first_name}")
#     print(f"your name is {last_name}")
#     print(f"your name is {age}")
# user_info("anik","adnan")

def user_info(first_name,last_name='unknown',age=None):
    print(f"your name is {first_name}")
    print(f"your name is {last_name}")
    print(f"your name is {age}")
user_info("anik")


