"""
The player's AI code
    Functions here are called by clock.py to run the AI code
"""

import math
import random

from clientLogic import clientData, commands
from clientLogic.logging import logPrint

#from msvcrt import getch
import keyboard
auto_fire = True

def onConnect():
    """
    Called when the player initially connects to the server but before the tank first spawns
    """
    commands.setInfo("Python player instance running the example AI.\n" +
                     "Fork me at https://github.com/JoelEager/pyTanks.Player")

def onSpawn():
    """
    Called when the tank spawns in a new game
    """
    pass

def onTick(elapsedTime):
    """
    Called once every frame while the tank is alive
    :param elapsedTime: The time elapsed, in seconds, since the last frame
    """
    global auto_fire

    gs = clientData.gameState

    if not keyboard.is_pressed('w'):
        commands.stop()

    if keyboard.is_pressed('a'):
        logPrint('Turned left', 2)
        commands.turn(gs.myTank.heading + 0.1)
    if keyboard.is_pressed('d'):
        logPrint('Turned right', 2)
        commands.turn(gs.myTank.heading - 0.1)

    if keyboard.is_pressed('w'):
        logPrint('Moving forward!', 2)
        commands.go()

    if keyboard.is_pressed('k'):
        if auto_fire:
            auto_fire = False
        else:
            auto_fire = True


    if keyboard.is_pressed('f'):
        logPrint('Fire!', 2)
        commands.fire(gs.myTank.heading)
        auto_fire = False


    # # Collided so try to get moving again
    # if not gs.myTank.moving:
    #     commands.turn((math.pi / 4) * random.randint(0, 7))
    #     commands.go()
    #     logPrint("Turned and starting moving", 2)
    #


    # Shooting logic
    if gs.myTank.canShoot and random.randint(0, 4) == 0 and auto_fire == True:
        # Select a target
        random.shuffle(gs.tanks)
        for target in gs.tanks:
            if target.alive:
                # Do the math
                deltaX = abs(gs.myTank.x - target.x)
                if deltaX == 0: return
                deltaY = gs.myTank.y - target.y
                angle = math.atan(deltaY / deltaX)

                if target.x < gs.myTank.x:
                    angle = math.pi - angle

                commands.fire(angle)
                logPrint("Fired", 2)

                break
