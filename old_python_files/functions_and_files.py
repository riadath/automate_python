from sys import argv
script,filename = argv

def print_all(f):
    print("||Printing everything||")
    print(f.read())
    print("\n\n")

def rewind(f):
    f.seek(0)

def print_single_line(line_no,f):
    print("Printing line:",line_no,"\n",f.readline())
    print("\n\n")

input_file = open(filename)
print_all(input_file)

rewind(input_file)

line_count = 1

print_single_line(line_count,input_file)
line_count += 1
print_single_line(line_count,input_file)
line_count += 1
print_single_line(line_count,input_file)