import pygame

from pygame.locals import * 

def GenerateJoyObj(setup_location):
    joysetup_path = setup_location
    joyfile = open(joysetup_path ,"r")
    joyids = joyfile.readlines() 
    joyfile.close()

    joybuttons = {
        0 : {"id" : 0, "name" : "a", "type" : "button", "is" : False, "variants": []},
        1 : {"id" : 0, "name" : "b", "type" : "button", "is" : False, "variants": []},
        2 : {"id" : 0, "name" : "y", "type" : "button", "is" : False, "variants": []},
        3 : {"id" : 0, "name" : "x", "type" : "button", "is" : False, "variants": []},
        4 : {"id" : 0, "name" : "r1", "type" : "button", "is" : False, "variants": []},
        5 : {"id" : 0, "name" : "l1", "type" : "button", "is" : False, "variants": []},
        6 : {"id" : 0, "name" : "select", "type" : "button", "is" : False, "variants": []},
        7 : {"id" : 0, "name" : "start", "type" : "button", "is" : False, "variants": []},
        8 : {"id" : 0, "name" : "LEFT", "type" : "joystick", "is" : False},
        9 : {"id" : 0, "name" : "RIGHT", "type" : "joystick", "is" : False},
        10 : {"id" : 0, "name" : "LEFT", "type" : "pad", "is" : False},
        11 : {"id" : 0, "name" : "RIGHT", "type" : "pad", "is" : False},
        12 : {"id" : 0, "name" : "UP", "type" : "pad", "is" : False},
        13 : {"id" : 0, "name" : "DOWN", "type" : "pad", "is" : False},
        14 : {"id" : 0, "name" : "r2", "type" : "joystick", "is" : False},
        15 : {"id" : 0, "name" : "l2", "type" : "joystick", "is" : False},
        16 : {"id" : 0, "name" : "UP", "type" : "joystick", "is" : False},
        17 : {"id" : 0, "name" : "DOWN", "type" : "joystick", "is" : False},
    }
    for index, id in enumerate(joyids):
        if joybuttons[index]["type"] == "button" or joybuttons[index]["type"] == "pad":  
            joybuttons[index]["id"] = int(id[0])

    return joybuttons

def Event(event, joysticks, joybuttons, joydirectV, joydirectH):
    added, removed = False, False
    
    if event.type == pygame.JOYDEVICEADDED:
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        added = True

    if event.type == pygame.JOYDEVICEREMOVED:
        joysticks.pop(-1)
        removed = True

    if event.type == JOYHATMOTION:
        button_id = -1
        if event.value[0] < 0:
            button_id = 0
        if event.value[0] > 0:
            button_id = 1

        if event.value[1] < 0:
            button_id = 2
        if event.value[1] > 0:
            button_id = 3
        
        for key in joybuttons:
            if joybuttons[key]["id"] == button_id and joybuttons[key]["type"] == "pad": 
                joybuttons[key]["is"] = True

    if event.type == JOYBUTTONDOWN:
        for key in joybuttons:
            if joybuttons[key]["id"] == event.button and joybuttons[key]["type"] == "button": 
                joybuttons[key]["is"] = True
                if not event.instance_id in joybuttons[key]["variants"]:
                    joybuttons[key]["variants"].append(event.instance_id)

    if event.type == JOYAXISMOTION:
        if event.axis == 0:
            joydirectH = event.value

        if event.axis == 1:
            joydirectV = event.value
        else: 
            joydirectV = 0

        if event.axis == 5:
            joybuttons[14]["is"] = True
    else:
        for key in joybuttons:
            if joybuttons[key]["type"] == "joystick":  
                joybuttons[key]["is"] = False
    
    return joysticks, joybuttons, joydirectV, joydirectH, added, removed
