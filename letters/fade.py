from os import system
from time import sleep
from random import choice
from threading import Thread, currentThread

from . import colors
from .system import Clear

def static(color:str, text:str, fond:str='1',style:str='1') -> str:
    if color.lower() in ['random', 'r']:
        color = choice(range(38))

    system('')
    result = f'\033[{color};{fond};{style}m{text}\033[0m'

    return result

def all_statics(text:str='Example') -> str:
    system('')
    result = ''

    for color in range(108):
         result += f'\033[{color}m{text}\033[0m\n'

    return result

def gradient(gradient:str, text:str, mode_type:str='vertical', speed:int=1) -> str:
    system('')

    result = ''
    gradient_n = 0

    if gradient == 'random':
        gradient = choice(Colors.gradients_list)

    for line in text.splitlines():
        characters = list(line)

        if mode_type in Colors.horizontal:
            gradient_n = 0

        if mode_type in Colors.vertical:
            for character in characters:
                result += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

            if line == '':
                pass

            elif gradient_n + speed < len(gradient):
                gradient_n += speed

            else:
                gradient_n = gradient in Colors.horizontal

        else:
            for character in characters:
                result += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                if line == '':
                    pass

                elif gradient_n + speed < len(gradient):
                    gradient_n += speed

                else:
                    gradient_n = gradient in Colors.horizontal

        result += '\n'

    return result

def all_gradients(text:str='Example', mode_type:str='vertical', speed:str=1) -> str:
    system('')
    result = ''

    for gradient in gradients_list:
        result_one = ''
        gradient_n = 0

        for line in text.splitlines():
            characters = list(line)

            if mode_type in horizontal:
                gradient_n = 0

            if mode_type in vertical:
                for character in characters:
                    result_one += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                if line == '':
                    pass

                elif gradient_n + speed < len(gradient):
                    gradient_n += speed

                else:
                    gradient_n = gradient in horizontal

                result_one += '\n'

            else:
                for character in characters:
                    result_one += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                    if line == '':
                        pass

                    elif gradient_n + speed < len(gradient):
                        gradient_n += speed

                    else:
                        gradient_n = gradient in horizontal

                result_one += '\n'

        result += result_one + '\n' 

        clear()
        print(result_one)
        input()

    return result

def on_input(stop:str, accept:bool):
    while True:
        press = input()

        if press == stop:
            if accept:
                global ok
                ok = False

            break

def on_sleep(time:int | float, accept:bool):
    sleep(time)

    if accept:
        global ok
        ok = True

def fade(gradient:str, text:str, mode_type:str='vertical', stop:str="", time:int | float=None, interval:int | float=0.05, max_speed:int=10) -> None:
    system('')
    speed = 0

    global ok
    ok = True

    if stop is not False:
        if time:
            accept = False

        else:
            accept = True

        thread1 = Thread(target=on_input, args=(stop, accept))
        thread1.start()

    if time:
        if stop is not False:
            accept =  False

        else:
            accept = True

        thread2 = Thread(target=on_sleep, args=(time, accept))
        thread2.start()

    while ok:
        if stop is not False and time:
            if not thread1.is_alive() and not thread2.is_alive():
                ok = False

        Clear()
        speed += 1

        if speed >= max_speed:
            speed = 1

        result = ''
        gradient_n = 0

        if gradient == 'random':
            gradient = choice(Colors.gradients_list)

        for line in text.splitlines():
            characters = list(line)

            if mode_type in Colors.horizontal:
                gradient_n = 0

            if mode_type in Colors.vertical:
                for character in characters:
                    result += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                if line == '':
                    pass

                elif gradient_n + speed < len(gradient):
                    gradient_n += speed

                else:
                    gradient_n = gradient in Colors.horizontal

            else:
                for character in characters:
                    result += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                    if line == '':
                        pass

                    elif gradient_n + speed < len(gradient):
                        gradient_n += speed

                    else:
                        gradient_n = gradient in horizontal

            result += '\n'

        print(result)
        sleep(interval)