# Arvid Yuen; 2020-02-17

from sys import exit
from random import randint
from textwrap import dedent

# Parent class for scenes. Includes default enter function
class Scene(object):

    def enter(self):
        print("The scene has not yet been implemented.")
        print("Subclass it and implement enter().")
        exit(1)

# Runner class to loop through the scenes until the end
# It takes an object argument that must be a Map
class Engine(object):

    def __init__(self, scene_map):
        # Initialize scene_map value from the Map argument
        self.scene_map = scene_map

    def play(self):
        # Obtain the start_scene from the Map variable,
        # assign it to current_scene
        current_scene = self.scene_map.opening_scene()
        # Set the last scene
        last_scene = self.scene_map.next_scene('finished')

        # Loop through scenes until the last scene
        while current_scene != last_scene:

            # Assign next_scene_name to the returb result of current_scene.enter()
            next_scene_name = current_scene.enter()
            # Obtain the class name of the next scene and assign it
            # to current_scene
            current_scene = self.scene_map.next_scene(next_scene_name)

        # After the while loop, enter the final scene
        current_scene.enter()

class Car(Scene):

    def enter(self):
        print(dedent("""
            You ran out of milk.  If you don’t buy some before the
            store closes, you won’t have milk for your cereal in the
            morning.  You cannot function without your morning cereal.

            You get in your car, turn the key and the engine sputters.
            It won't start!
            """))

        # Get input from user, compare to common answers
        action = input(">")
        if "jump" in action.lower():
            print(dedent("""
                With some quick thinking, you ask your neighbor to jump
                start your car. He is happy to help you. Once started, you
                head off to the grocery store.
                """))
            return 'parking_lot'
        elif "aaa" in action.lower():
            print(dedent("""
                You are prepared for such a vehicular setback with your AAA
                membership. You call them, and sure enough, a service truck
                arrives in minutes to replace your battery. Once working,
                you head off to the store.
                """))
            return 'parking_lot'
        elif "try" in action.lower():
            print(dedent("""
                A small hindrance has never held you back. You don't give up.
                You keep trying and trying the ignition. Eventually, the car
                hums, starts up, and you are on your way to the store.
                """))
            return 'parking_lot'
        elif "another car" in action.lower():
            print(dedent("""
                You decide to take another car. This one is working
                perfectly, and you drive to the store.
                """))
            return 'parking_lot'
        elif "bus" in action.lower():
            print(dedent("""
                You decide to take the bus. You get to the bus stop and wait.
                And wait. And wait. By the time the bus arrives, the store
                has closed and you lost your chance.
                """))
            return 'lost'
        elif "walk" in action.lower():
            print(dedent("""
                You decide to walk. As you're walking, you accidentally slip
                off the curb and twist your ankle. You have no choice but
                to give up.
                """))
            return 'lost'
        # If none of the common answers to included in the user input,
        # ask to try again and replay the scene
        else:
            print("Invalid input.  Please try something else.")
            return 'car'

class ParkingLot(Scene):

    def enter(self):
        print(dedent("""
        You arrive at the grocery store. It's busy.
        All parking spots are occupied. Just as a car is leaving you and
        a blue SUV signal simultaneously. This could get nasty...
        """))

        # Get input from user, compare to common answers
        action = input(">")
        if "let" in action.lower():
            print(dedent("""
                You know your manners, so you wave to let the blue SUV take
                the spot. The driver in the SUV appreciates your kindness.
                She reciprocates and lets you park.

                You enter the store.
                """))
            return 'fridge'
        elif "talk" in action.lower() or "ask" in action.lower():
            print(dedent("""
                You get out of your car to explain to the other driver that
                you can't start your day without milk and cereal. She
                understands your pain and lets you take the spot.
                """))
            return 'fridge'
        elif "wait" in action.lower():
            print(dedent("""
                Patience is a virtue. You give up the spot and wait for another.
                Sure enough, another person leaves. You are able to park and
                go inside.
                """))
            return 'fridge'
        elif "illegal" in action.lower():
            print(dedent("""
                Since it will take only a few minutes, you decide to park
                illegally. You go in the store. Just as you get inside, a
                parking agent walks up and writes a ticket. You run outside
                and apologize, but it's too late. Angry about the ticket, you
                decide to go back home.
                """))
            return 'lost'
        elif "park" in action.lower() or "race" in action.lower():
            print(dedent("""
                It's every man for himself. You slam on the gas and race
                to the spot. Your brazen decision gets you there first.

                BANG!!

                You lost sight of the parked car on the other side and smack
                into it! The car alarm goes off. Everybody is watching.
                Frozen by shame and humiliation, you are unable to go in
                the store.
                """))
            return 'lost'
        else:
            # If none of the common answers to included in the user input,
            # ask to try again and replay the scene
            print("Invalid input.  Please try something else.")
            return 'parking_lot'

class Fridge(Scene):

    def enter(self):
        print(dedent("""
        You arrive at the milk section. There is one carton left.
        You reach for it at the same time as an old lady. As mature adults,
        the two of you agree to play rock-paper-scissors for it. It's best
        two out of three.
        """))

        # Initialize rock/paper/scissors wins counters
        your_wins = 0
        lady_wins = 0

        # Loop through the rock/paper/scissors game until someone
        # gets 3 wins
        while your_wins < 2 and lady_wins < 2:
            lady_move_int = randint(1,3)
            if lady_move_int == 1:
                lady_move = "rock"
            elif lady_move_int == 2:
                lady_move = "paper"
            elif lady_move_int == 3:
                lady_move = "scissors"
            else:
                lady_move = "rock"
            while True:
                your_move_in = input("Rock/Paper/Scissors?>")
                if "skip" in your_move_in:
                    return 'cashier'
                if "rock" in your_move_in:
                    your_move = "rock"
                    break
                elif "paper" in your_move_in:
                    your_move = "paper"
                    break
                elif "scissor" in your_move_in:
                    your_move = "scissors"
                    break
                else:
                    # If input does not match a valid entry, ask to try again
                    print("Invalid Input.  Please enter 'rock', 'paper' or 'scissors'.")
            # Increment wins for someone when they win a round
            if lady_move == your_move:
                text = "It's a draw."
            elif lady_move == "rock":
                if your_move == "paper":
                    your_wins += 1
                    text = "You win."
                else:
                    lady_wins += 1
                    text = "Lady wins."
            elif lady_move == "paper":
                if your_move == "rock":
                    lady_wins += 1
                    text = "Lady wins."
                else:
                    your_wins += 1
                    text = "You win."
            elif lady_move == "scissors":
                if your_move == "rock":
                    your_wins += 1
                    text = "You win."
                else:
                    lady_wins += 1
                    text = "Lady wins."
            else:
                text = "It's a draw."
            # Print the results of the round
            print(f"\nThe lady used {lady_move}, you used {your_move}. {text}")
            print(f"Lady: {lady_wins}   You: {your_wins}")

        # Outcome if you reach 2 wins before the old lady
        if your_wins == 2:
            print(dedent("""
                Incredibly, you won the match of rock/paper/scissors!
                You happily pick up the last carton of milk, and head to
                the cashier.
                """))
            return 'cashier'
        # Outcome if the old lady reaches 2 wins before you
        else:
            print(dedent("""
                Unfortunately, you were no match for the old lady.
                Try again?
                """))
            # Give the player a chance to try the scene again
            action = input(">")
            if "y" in action:
                return 'fridge'
            else:
                print("The old lady cheerfully takes the milk. You go home empty handed.")
                return 'lost'

class Cashier(Scene):

    def enter(self):
        print(dedent("""
            You get in line at the cashier. You notice something is
            dripping. The milk carton has a hole in it. You must act
            quickly or the entire carton will end up on the floor.
            """))

        # Get input from user, compare to common answers
        action = input(">")
        if "tape" in action.lower():
            print(dedent("""
            You rush to the hardware aisle and grab tape. You apply some tape
            to the hole. It's not pretty, but the leak has stopped. Crisis averted.
            You pay for your goods and head home. Success!
            """))
            return 'finished'
        elif "bag" in action.lower():
            print(dedent("""
            You ask the cashier for a plastic bag. You put the carton in the
            bag and tie it up. Some milk is dripping into the bag, but at
            least it's contained. Your resourcefulness has proven worthy.
            """))
            return 'finished'
        elif "tilt" in action.lower() or "flip" in action.lower():
            print(dedent("""
            You calmly tilt the carton up vertically so that the hole is
            facing upwards. Nothing to worry about. A bit of care on the way
            home and you've got your milk!
            """))
            return 'finished'
        elif "drink" in action.lower() or "chug" in action.lower():
            print(dedent("""
            You decide to drink the milk. After some effort, you've finished!
            However, now you have no milk for tomorrow...
            """))
            return 'lost'
        # If none of the common answers to included in the user input,
        # the game is over
        else:
            print(dedent("""
            You fumble around trying keep the milk in the leaking carton.
            Panic sets in and you struggle to keep your hands from shaking.
            The carton falls from to the ground and explodes - milk everywhere!
            Everybody is watching as you fight back tears and run out of the
            store.
            """))
            return 'lost'

class Lost(Scene):

    # List of print statements for game over to be played randomly
    quips = [
        "You lost. Maybe this is too hard for you",
        "You couldn't even buy milk. Where did it all go wrong?",
        "You failed to get milk. It's time to pack it all up live in the woods.",
        "Milk eludes you. You wonder if you'll ever see milk again.",
        "No milk for you. What did you do to deserve this?"
    ]

    # Prints a random quip plus GAME OVER
    def enter(self):
        print(Lost.quips[randint(0, len(self.quips) - 1)],"\n\nGAME OVER")
        exit(1)

class Finished(Scene):

    # Victory print statement
    def enter(self):
        print(dedent("""
            You have successfully bought milk. Good job!
            """))
        exit(0)

# Map class to navigate between scenes
class Map(object):

    # Scenes dictionary by return string to class name
    scenes = {
        'car': Car(),
        'parking_lot': ParkingLot(),
        'fridge': Fridge(),
        'cashier': Cashier(),
        'lost': Lost(),
        'finished': Finished()
    }

    # Init method initializes the start_scene String
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Obtain the next_scene Class name from the return String entered
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # Get the opening scene by Class name
    def opening_scene(self):
        return self.next_scene(self.start_scene)
