from os import system, name
from time import sleep

def Title(title:str) -> None:
    if name == 'nt':
        system(f'title {title}')

def Clear() -> None:
    if name == 'nt':
        system('cls')

    else:
        system('clear')

def Print(text:str, speed:int=0.5) -> str:
    for character in text:
        print(character, end='')
        sleep(speed)

def Input(text:str, speed:int=0.5) -> str:
    for character in text:
        print(character, end='')
        sleep(speed)

    input(' ')

def Replace(list_name:list, base:str, change:str) -> list:
    list_name = [word.replace(base, change) for word in list_name]

    return list_name
