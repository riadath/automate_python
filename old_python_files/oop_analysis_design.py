# Making a simple game engine
# Gothons from planet Percal #25

from sys import exit
from textwrap import dedent
from random import randint


class Scene(object):
    def enter(self):
        print("Scene not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):
    def __int__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "You died.You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a looser",
        "I have a puppy that's better at this.",
        "You're worse than your dad's joke."
    ]

    def enter(self):
        print(Death.quips[0, len(self.quips) - 1])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of planet percel 25 have invaded your
        shit and destroyed your entire crew. You are the
        last survivor nigga.Your mission is to get the 
        neutron destruct bomb from the weapons armory and
        put it in the bridge and blow the ship after you 
        are in the escape pod.
        
        Your are running down the central corridor to the
        weapons armory when a gothon jumps out.He has blocked the
        door to the weapons armory and is about to shoot you"""))
        action = input(">>>")
        if action == "shoot":
            print(dedent("""
            You shoot the gothon but miss him by a bit and ruin 
            his brand new costume. He got fucking angry and beats 
            the fuck outta you until you are dead af!!"""))
            return 'death'
        elif action == 'dodge':
            print(dedent("""
            You dodge it like Muhammad Ali but slip and fall
            on the floor and the gothon beats the fuck 
            outta you until you are so fucking dead!"""))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
            Lucky for you the made you learn gothon insults
            back in the academy.Your tell the joke'dfj sle fje
            fjljd eoe eleo nrnje' and he starts laughing like
            a 9 year old and you blast his head off"""))
            return 'laser_weapon_armory'
        else:
            print("Does not compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You do a dive roll into the weapon armory, crouch
        and scan room for more gothons that might be hiding.
        In the corner you find the neutron bomb in a safe.It
        has a three digit password. You have to get it right
        within ten guesses."""))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("KEYPAD>>")
        guesses = 0
        while guess


class TheBridge(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self, starting_scene):
        self.starting_scene = starting_scene

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
