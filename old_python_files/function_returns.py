def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def square(n1):
    return n1*n1

def factorial_of(n):
    fact = 1
    while n >0:
        fact = fact*n
        n -= 1
    return fact

age = add(16,2) #18
weight = sub(68,2) #66
height = multiply(34,2) #68
iq = div(200,2) #100

print(f"Your age is {age},weight is {weight},height is {height},iq is {iq}")
print(f"The square of 5 is {square(5)}")
merged = add(age,sub(height,multiply(weight,div(iq,2))))
print(merged)

print(factorial_of(4))
