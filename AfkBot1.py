# -*- coding: utf-8 -*-

import json
import os
import time
import random

import psutil
import pyautogui
from pyautogui import typewrite, keyDown, keyUp
pubg_url = 'steam://rungameid/578080'

PROCNAME = "TslGame.exe"
CRASH_PROCNAME = "BroCrashReporter.exe"
debug_directory = "debug_screenshots"
start_state = "HELLO"
play_state = "PLAYING"
play_timer_max = 60 * 3
matching_state = "MATCHING"
matching_timer_max = 60 * 3
loading_state = "LOADING"
loading_timer_max = 60 * 3
gameloading_state = "GAME IS LOADING"
gameloading_timer_max = 60 * 3

state = start_state
takeScrenshot = True
timer = 0.0

threehundredws = []
for _ in range(300):
    threehundredws.append('w')


def getConfig():
    with open('config.json', encoding='UTF-8') as data_file:
        data = json.load(data_file)
    return data

def getpixel(x, y):
    return pyautogui.screenshot().getpixel((x, y))

def pixelMatchesColor(x, y, expectedRGBColor, tolerance=0):
    pix = getpixel(x,y)
    if len(pix) == 3 or len(expectedRGBColor) == 3:  # RGB mode
        r, g, b = pix[:3]
        exR, exG, exB = expectedRGBColor[:3]
        return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance)
    elif len(pix) == 4 and len(expectedRGBColor) == 4:  # RGBA mode
        r, g, b, a = pix
        exR, exG, exB, exA = expectedRGBColor
        return (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance) and (
            abs(a - exA) <= tolerance)
    else:
        assert False, 'Color mode was expected to be length 3 (RGB) or 4 (RGBA), but pixel is length %s and expectedRGBColor is length %s' % (
            len(pix), len(expectedRGBColor))


def printScreen(message):
    if takeScrenshot:
        if not os.path.exists(debug_directory):
            os.makedirs(debug_directory)
        pyautogui.screenshot('{}/{}{}.png'.format(debug_directory, time.strftime("%m.%d %H.%M.%S", time.gmtime()), message))


def changeState(value):
    global state, timer
    state = value
    timer = 0


def killGame():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

def matchesButton(position):
    if pixelMatchesColor(position[0], position[1], white_button,
                      tolerance=color_tolerance) or pixelMatchesColor(position[0],
                                                                      position[1],
                                                                      gray_button,
                                                                      tolerance=color_tolerance) \
    or pixelMatchesColor(position[0],
                         position[1],
                         super_white_button,
                         tolerance=color_tolerance) or pixelMatchesColor(
        position[0], position[1], golden_button, tolerance=color_tolerance):
        return True
    return False

def isGameRunning():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            return True
        else:
            return False

def checkTimer():
    global state
    if state == loading_state and timer > loading_timer_max:
        printScreen('Timeout')
        print('Timeout. Restarting the game')
        changeState(start_state)
    elif state == matching_state and timer > matching_timer_max:
        printScreen('Timeout')
        print('Timeout. Restarting the game')
        changeState(start_state)
    elif state == play_state and timer > play_timer_max:
        printScreen('Timeout')
        print('Timeout. Restarting the game')
        changeState(start_state)
    elif state == gameloading_state and timer > gameloading_timer_max:
        printScreen('Timeout')
        print('Timeout. Restarting the game')
        changeState(start_state)


config = getConfig()

# Menu
print('By using this software you agree with license! You can find it in code.')
print('Choose a server:')
number = 1
for server in config['servers']:
    print('{}. {}'.format(number, server['title']))
    number += 1
inp = int(input('Type number: '))
inp -= 1
server_position = (config['servers'][inp]['x'], config['servers'][inp]['y'], config['servers'][inp]['title'])
print('Choose a mod:')
number = 1
for server in config['modes']:
    print('{}. {}'.format(number, server['title']))
    number += 1
inp = int(input('Type number: '))
inp -= 1

print('Can I take screenshots if something wrong happens? (y/N)')
if input().lower() == 'y':
    print('Thanks')
else:
    print("Well, if something will go wrong, then I can't help you")
    takeScrenshot = False

# Position init
mode_position = (config['modes'][inp]['x'], config['modes'][inp]['y'], config['modes'][inp]['title'])
mode_tick_position = (config['modes'][inp]['tick']['x'], config['modes'][inp]['tick']['y'])
play_button_position = (config['play_button']['x'], config['play_button']['y'])
play_state_position = (config['play_state']['x'], config['play_state']['y'])
text_position = (config['text']['x'], config['text']['y'])
exit_position = (config['exit_to_lobby']['x'], config['exit_to_lobby']['y'])
error_position_check = (config['error_position']['x'], config['error_position']['y'])
error_ok_position = (config['error_ok_position']['x'], config['error_ok_position']['y'])
game_message_position = (config['game_message_position']['x'], config['game_message_position']['y'])
exit_button_position = (config['exit_button_position']['x'], config['exit_button_position']['y'])
reconnect_button_position = (config['reconnect_button_position']['x'], config['reconnect_button_position']['y'])

# Reading timings
refresh_rate = config["timers"]["refresh_rate"]
wait_after_killing_a_game = config["timers"]["wait_after_killing_a_game"]
start_delay = config["timers"]["start_delay"]
animation_delay = config["timers"]["animation_delay"]
wait_for_players = config["timers"]["wait_for_players"]
wait_for_plain = config["timers"]["wait_for_plain"]
exit_animation_delay = config["timers"]["exit_animation_delay"]
loading_delay = config["timers"]["loading_delay"]

# Colors
def getColor(config, name):
    return (config["colors"][name]["r"], config["colors"][name]["g"], config["colors"][name]["b"])


color_tolerance = config["color_tolerance"]
dark_play_color = getColor(config, "dark_play_color")
play_color = getColor(config, "play_color")
matching_color = getColor(config, "matching_color")
matching_tick_color = getColor(config, "matching_tick_color")
text_start_color = getColor(config, "text_start_color")
white_button = getColor(config, "white_button")
gray_button = getColor(config, "gray_button")
golden_button = getColor(config, "golden_button")
super_white_button = getColor(config, "super_white_button")
windows_background = getColor(config, "windows_background")
exit_button_color = getColor(config, "exit_button_color")
reconnect_button_color = getColor(config, "reconnect_button_color")

# Game info
print('Server: {}. Mode: {}'.format(server_position[2], mode_position[2]))

while (1):
    try:
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == CRASH_PROCNAME:
                print('Fucking bugs in PUBG. Trying to avoid them!')
                proc.kill()
                killGame()
                time.sleep(wait_after_killing_a_game)
                changeState(start_state)
    except Exception as ex:
        print('Something went wrong while killing bug reporter... Error message: {}'.format(ex))
    if state == start_state:
        if pixelMatchesColor(error_position_check[0], error_position_check[1], windows_background,
                             tolerance=color_tolerance):
            pyautogui.press('enter')
            pyautogui.click(error_ok_position[0], error_ok_position[1])
        killGame()
        time.sleep(wait_after_killing_a_game)
        try:
            os.startfile(pubg_url)
            changeState(loading_state)
            time.sleep(start_delay)
            print('Loading PUBG')
        except Exception as ex:
            print('Something went wrong while starating PUBG... Error message: {}'.format(ex))

    elif state == loading_state:
        if pixelMatchesColor(play_state_position[0], play_state_position[1], play_color,
                             tolerance=color_tolerance) or pixelMatchesColor(play_state_position[0],
                                                                             play_state_position[1],
                                                                             dark_play_color,
                                                                             tolerance=color_tolerance):
            pyautogui.moveTo(play_button_position[0], play_button_position[1])
            time.sleep(animation_delay)
            # Pick a server
            pyautogui.click(server_position[0], server_position[1])
            time.sleep(animation_delay)
            pyautogui.click(mode_position[0], mode_position[1])
            time.sleep(animation_delay)
            if pixelMatchesColor(mode_tick_position[0], mode_tick_position[1], matching_tick_color,
                                 tolerance=color_tolerance):
                pyautogui.click(mode_tick_position[0], mode_tick_position[1])
            pyautogui.click(play_button_position[0], play_button_position[1])
            changeState(matching_state)
            time.sleep(loading_delay)
            print('Starting matchmaking...')
        elif pixelMatchesColor(text_position[0], text_position[1], text_start_color, tolerance=color_tolerance):
            print('I see text, so the game is probably ready...')
            changeState(play_state)
        elif pixelMatchesColor(reconnect_button_position[0], reconnect_button_position[1], reconnect_button_color, tolerance=color_tolerance):
            print('Nice orange button? I\'ll press it!')
            pyautogui.click(reconnect_button_position[0], reconnect_button_position[1])
            time.sleep(animation_delay)
        elif matchesButton(game_message_position):
            print("Game's message was denied")
            pyautogui.click(game_message_position[0], game_message_position[1])
        elif not pixelMatchesColor(exit_button_position[0], exit_button_position[1], exit_button_color, tolerance=color_tolerance) \
            and not pixelMatchesColor(exit_button_position[0], exit_button_position[1], matching_tick_color, tolerance=color_tolerance)\
            and timer > 30 and isGameRunning():
            print('I can\'t see exit button, so the game is probably ready...')
            time.sleep(wait_for_players)
            changeState(play_state)

    elif state == matching_state:
        if pixelMatchesColor(play_state_position[0], play_state_position[1], play_color,
                             tolerance=color_tolerance) or pixelMatchesColor(play_state_position[0],
                                                                             play_state_position[1],
                                                                             dark_play_color,
                                                                             tolerance=color_tolerance):
            changeState(loading_state)
            time.sleep(loading_delay)
        if not pixelMatchesColor(play_state_position[0], play_state_position[1], matching_color,
                                 tolerance=color_tolerance):
            if pixelMatchesColor(play_state_position[0], play_state_position[1], matching_tick_color,
                                 tolerance=color_tolerance):
                changeState(gameloading_state)
                time.sleep(loading_delay)
                print('Session is loading')
    elif state == gameloading_state:
        if not pixelMatchesColor(play_state_position[0], play_state_position[1], matching_tick_color,
                                 tolerance=color_tolerance):
            print('Loading is complete')
            time.sleep(wait_for_players)
            changeState(play_state)
    elif state == play_state:
        # print(text_position[0], text_position[1])
        if not pixelMatchesColor(text_position[0], text_position[1], text_start_color, tolerance=color_tolerance):
            wait_for_plane = random.randint(50, 53)
            print('Time selected was {} seconds'.format(wait_for_plane))
            time.sleep(wait_for_plane)
            pyautogui.press('f')
            print('F was hit')
            timeout = time.time() + 60
            print("should be holding w down")
            pyautogui.keyDown('w')
            while True:
                if time.time() < timeout:
                    print('Pressing W')

                else:
                    print('Dont drown and lay it down')
                    pyautogui.keyUp('w')
                    pyautogui.keyDown('space')
                    time.sleep(2)
                    pyautogui.keyUp('space')
                    time.sleep(1.2)
                    pyautogui.press('z') 
                    print('Waiting to pass afk timer')
                    break
            time.sleep(135)
            pyautogui.press('esc')
            time.sleep(animation_delay)
            pyautogui.click(exit_position[0], exit_position[1])
            time.sleep(exit_animation_delay)
            pyautogui.click(exit_position[0], exit_position[1])
            changeState(loading_state)
            print('Going in menu. Loading again')
            time.sleep(10)

    time.sleep(refresh_rate)
    timer += refresh_rate
    checkTimer()
