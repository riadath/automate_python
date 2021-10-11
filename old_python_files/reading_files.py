from sys import argv #adds argument variable

script, filename = argv #takes filename as input from the argument
txt = open(filename) #opens the text file

print(f"Heres your file {filename}:")
print(txt.read()) #prints whatever that is written on the file

print("Type the filename again:")
file_again = input('>>>') #takes the name of the file as input

txt_again = open(file_again) #opens the file
print(txt_again.read()) #prints whatever is on the file
