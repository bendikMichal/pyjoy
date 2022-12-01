import pygame, sys
sys.path.insert(1, "data/scripts")
import text
from saver import*
from pygame.locals import*

pygame.init()
pygame.joystick.init()

width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gamepad setup")

joysetup_path = str(input("enter path to setup (d for default): "))
if joysetup_path == "d":
    joysetup_path = "data/setup/"

joysetup_file = str(input("enter name of setup (d for default): "))
if joysetup_file == "d":
    joysetup_file = "gamepad.txt"


binds = [0, 1, 2, 3, 4, 5, 6, 7, "joy", "joy", 0, 1, 2, 3, "joy", "joy"]
suggestions = [
    "press a",
    "press b",
    "press y",
    "press x",
    "press rb",
    "press lb",
    "press select",
    "press start",
    "",
    "",
    "press left",
    "press right",
    "press up",
    "press down",
    "",
    ""
]
index = 0

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

Main = True
while Main:
    if binds[index] ==  "joy":
        index += 1
    if index >= len(binds):
        Main = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Main = False
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
            
            if button_id != -1:
                binds[index] = button_id
                index += 1

            
        if event.type == JOYBUTTONDOWN:
            binds[index] = event.button
            index += 1
        
    win.fill((0, 0, 0))
    text.renderText(
        win, 
        40, 
        [0, 0], 
        (255, 255, 255), 
        suggestions[index], 
        text_type="sys", 
        shadow=True, 
        shadow_amp=0.05 * 40
    )
    pygame.display.update()

pygame.joystick.quit()
pygame.quit()

for i in range(len(binds)):
    binds[i] = str(binds[i]) + "\n" * int(i < len(binds) - 1)

file = open(joysetup_path + joysetup_file, "w")
file.writelines(binds)
file.close()

sys.exit()
