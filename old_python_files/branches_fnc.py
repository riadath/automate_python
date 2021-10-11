from sys import exit


def dead(reason):
    print(reason)
    exit(0)


def start():
    print("""You are in a dark room.\nThere're two rooms.
Choose left or right.""")
    choice = input('>>>')
    if 'left' in choice:
        bear_room()
    elif 'right' in choice:
        devil_room()
    else:
        dead('You die of hunger.')


def gold_room():
    print('There is unlimited amount of gold in this room.', end=' ')
    print('How much do you want to take?')
    choice = input('>>')
    if '0' in choice or '1' in choice or \
            '2' in choice or '3' in choice or '4' in choice or \
            '5' in choice or '6' in choice or '7' in choice or \
            '8' in choice or '9' in choice:
        how_much = int(choice)
        if how_much <= 50:
            print('You are not a greedy man. You win')
            exit(0)
        else:
            dead('you are greedy af')
    else:
        print('Learn to type a number.')
        gold_room()


def bear_room():
    print("There's a bear sleeping in the room with some honey.")
    print("Theres a door right behind him")
    print('What do you do?')
    bear_moved = False
    while True:
        print("1.take honey\n2.taunt bear")
        choice = input('>>>')
        if 'take honey' in choice:
            dead('You got some balls.You are dead btw')
        elif 'taunt bear' in choice and not bear_moved:
            bear_moved = True
            print('Your are in front of the door.What do you do now?')
        elif choice == 'open door' and bear_moved:
            gold_room()
        elif choice == 'taunt bear' and bear_moved:
            dead('You just died.')
        else:
            dead('Wrong move bro. The bear is awake and you are dead.')


def devil_room():
    print('There is a devil in the room. What do you do?')
    choice = input('>>>')
    if 'flee' in choice:
        start()
    elif 'sell my soul' in choice:
        dead('You are a demon now')
    else:
        devil_room()


start()
