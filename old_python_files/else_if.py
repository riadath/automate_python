print('''
Lets make a game nobody will ever play except me!!!

 ____________   
|    The     |
|    Shit    |
|    Game    |
|            |
|____________|

''')


def prime_check(n):
    for i in range(2,(int(n/2)+1)):
        if n%i == 0:
            return False
    return True


print('Select a number')
n1 = int(input('>>>'))
if 1 <= n1 <= 100:
    print('Select a another number:')
    n2 = int(input('>>>'))
    if prime_check(n2):
        print('How much did you think before putting that number?')
        print('''
        1.A Lot
        2.Not at all
        3.Somewhat
        ''')
        n3 = input('>>>')
        if "2" in n3 or "3" in n3:
            print("""Did you know that it's prime number?
                1.Yes
                2.No
            """)
            n4 = int(input('>>>'))
            if n4 == 1:
                print('You are a man of maths!!')
            elif n4 == 2:
                print('Okay, have a nice day')
        if n3 == 1:
            print("""Did you know that it's prime number?
                1.Yes
                2.No
            """)
            n4 = int(input('>>>'))
            if n4 == 1:
                print('You have to be smarter and faster!!')
            elif n4 == 2:
                print('Okay, have a nice day')

    elif 1000 <= n2 <= 100:
        print('You have opened your mind somewhat :D ')
    else:
        print('you need to open up your mind more often!!')
else:
    print("You are man of numbers, aren't you?")

