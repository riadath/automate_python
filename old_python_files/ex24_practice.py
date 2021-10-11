poem = """
Jony Jony\tyes papa;
eating sugar?
No papa
open your mouth
ha ha ha
"""
print("______")
print(poem)
print("______")


def multiple_returns(input_data):
    new_data_one = input_data * 500
    new_data_two = new_data_one / 1000
    new_data_three = new_data_two / 100
    return new_data_one, new_data_two, new_data_three


input_data = 10000
print("This is the input data:{}\n".format(input_data))
data_one, data_two, data_three = multiple_returns(input_data)
print("Data One:", data_one, "\nData Two:", data_two, "\nData Three:", data_three)



input_data = input_data/10
print("\nThis is the input data:{}\n".format(input_data))
all_in_one = multiple_returns(input_data)
print("Data one:{}\nData Two:{}\nData Three:{}\n".format(*all_in_one))



