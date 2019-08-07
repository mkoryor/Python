import sys
import os
from sys import exit
import time
import itertools
import webbrowser


class TheMaze(object):
    """This is the actions you take when you enter the grievers hole"""

    def escape(self):

        print("Year's have passed now and now your losing all hope, and food is diminishing")
        print("However, the time has come and you've finally have the huevos to go far into the maze")

        chances = 5
        while chances > 0:
            answers = [1348, 4123, 1341, 1242]
            passcode = int(input("put the code in to enter the door: "))
            remaining_time = 10

            if passcode in answers:
                print("Access Granted!")
                print("PROCEED!")
                WickedComplex().scene()

            elif passcode not in answers:
                chances -= 1
                print('you have ' + str(chances) + ' chances left')

        print("You have ran out of time, the Grievers shred you to pieces")
        print("LONG LIVE THE MAZE RUNNER")
        print("_ - _ _ _ _ _ _ - _" * 1)
        print("  +             +")
        print("- _ - - - - - - _ -" * 1)
        print(" ")
        print(" \_______________/ ")
        print("  \_____________/ ")


class TheBox(object):
    """This is the first stage of 'The Maze' trial"""

    def move(self):  # define act as self.act here to assign it to a usable variable
        print("You've awoken from your unconcious sleep")
        print("Your being thrust from the bottom of the earth")
        print("Suddenly you arrived to a place called the Glades\n")
        act = input("> what do you want to do? (survive?/run?) ")

        if act == "survive":
            TheGlade().survival()
        if act == "run":
            Walls().grievers()


class TheGlade(object):
    def _init__(self, choice):
        self.choice = choice

    def survival(self):
        # while True: #You have while True here and no way to exit this block? it just runs forever, thats a problem, so i just took it out, its not used
        # if you define a self.guide, make sure you have guide used in the innit
        # i also changed your initial guide to a normal print statement and changed self.guide to self.choice here, for clarity
        print(
            """This is the scene when of how lived in the glades and what you did to survive"""
            """Your choices are:
            build yourself a house to live in, (enter: 'build')
            hunt for food to eat, (enter: 'hunt')
            starve to death (enter: 'starve')
            run towards the maze tunnel trying to escape (enter: 'run')""")
        choice = input("> where to start ")
        if choice.lower() == "build":
            time.sleep(2)
            print("You started to build a small home? ")
            print("[            ]")
            print(" \/\/\/\/\/\/")
            print("|  []   []   |")
            print("|____________|")
            print("took you a while, but you've created a master piece house")
            TheGlade().survival()

        elif choice.lower() == "hunt":
            print("You went out to hunt for food int he grass ")
            time.sleep(2)
            print(" ")
            print("SWOOOPP!!!!")
            print("------------>>          <^:()>")
            print("Nice you killed a rodent now feast!!! ")
            TheGlade().survival()
        elif choice.lower() == "starve":
            Walls().grievers()
        elif choice.lower() == "run":
            TheMaze().escape()

        # you didnt define what happens if they run so i added one above, also leading to death.


class WickedComplex(TheMaze):
    """This is the place the everything started and the answers you've been looking for"""

    def scene(self):
        print("You've slide down a tunnel after getting past grievers and arrived to a  mysterious location")
        action = input("> What would you like to do? (walk/watch): ")

        if action == "walk":
            print("An infected person came out of nowhere and tries to stab you, you've died.")
            GameOver()

        if action == "watch":
            print(watch_video("https://www.youtube.com/watch?v=cWjm9iPSDFw"))


class Walls(TheMaze):
    def grievers(self):
        print("grievers are coming boii")
        print("you got lucky and accidentally found an exit!")
        WickedComplex().scene()


def GameOver():
    print("You failed the mission, LOSER!")
    run_again = input("> Wanna play again? ")
    if run_again.lower() != "no":
        TheBox().move()
    else:
        print("THANKS FOR PLAYING SUCKA!!")


def watch_video(url):
    webbrowser.open(url)


TheBox().move()
