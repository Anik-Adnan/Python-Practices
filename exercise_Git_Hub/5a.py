class Input_Out_String:
    def __init__(self):
        # self.s = ''
        pass

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


str_obj = Input_Out_String()
str_obj.get_string()
str_obj.print_string()
