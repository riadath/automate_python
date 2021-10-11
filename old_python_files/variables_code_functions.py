#defining a funciton in python

def print_two_arguments(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1} arg2:{arg2}")

#theres one more way of doing the same thing
def print_two_arg_onecMore(arg1,arg2):
    print(f"arg1:{arg1} arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_no_shit():
    print("I dont have antything")

print_two_arguments("Riadath","Akib")
print_two_arg_onecMore("Riadath","Akib")
print_one("Akib")
print_no_shit()