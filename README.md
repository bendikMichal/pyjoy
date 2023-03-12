# pyjoy
Pygame handling inputs from joystick for you + basic joystick keybind setup

# Documentation
- To set bindings run `setup.py`

## Project 
- Basic project examlpe

```python
# import modules
import pygame
import joystickHandler

# init modules
from pygame.locals import *
pygame.init()
pygame.joystick.init()

# set variables
setup_location = "data/setup/gamepad.txt"                   # Location of file generated / edited by setup.py
joybuttons = joystickHandler.GenerateJoyObj(setup_location) # Dictionary, contains buttons, their type and their state
joysticks = []                                              # List of connected joysticks
joydirectV, joydirectH = 0, 0                               # Rotation of joystick stick

while 1:
    # reset old inputs
    for key in joybuttons:
        if joybuttons[key]["type"] == "button":
            joybuttons[key]["is"] = False
            joybuttons[key]["variants"] = []

    # get new inputs
    for event in pygame.event.get():
        joysticks, joybuttons, joydirectV, joydirectH, added, removed = joystickHandler.Event(event, joysticks, joybuttons, joydirectV, joydirectH)
    
    # checking input
    if joybuttons[0]["is"]: # a
        print("Player pressed a...")
    
    # checking from multiple gamepads for input (NOTE: Not all buttons have multiple gamepad support)
    if 0 in joybuttons[0]["variants"]:
        print("Player 0 pressed a...")
    if 1 in joybuttons[0]["variants"]:
        print("Player 1 pressed a...")
    


```
