from sys import argv  
from os.path import exists

script, file_from,file_to = argv

print(f"Will be copied form {file_from} to {file_to}.\n")
in_file = open(file_from)
in_data = in_file.read()
print(f"The input file is {len(in_data)} bytes long")

file_exits = exists(file_to)
if(file_exits):
    print("The file exists.\n")
else :
    print("The file doesn't exist.\n")
    
out_file = open(file_to,'w')
out_file.write(in_data)

print("Aright aright aright")
out_file.close()
in_file.close()