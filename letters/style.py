import os


class Style:
    
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def replace(list_name:list, base:str, change:str):
        list_name = [word.replace(base, change) for word in list_name]

        return list_name


    def center(centervar:str, space:int=None):
        if not space:
            space=(os.get_terminal_size().columns - len(centervar.splitlines()[int(len(centervar.splitlines())/2)])) /2

        for centervar in centervar.splitlines():
            return ''.join(f"{(' ' * int(space)) + centervar}\n")

            return result


    def width(taille:int, text:str):
        result = ''

        for character in text:
            if character == '\n':
                result += '\n'.join(character)

            else:
                result += ''.join(character*taille)
            
        return result


    def length(taille:int, text:str):
        result = ''

        for w in text.splitlines():
            if w == '\n':
                result += w
            result += (w+'\n')*taille

        return result


    def big(tailleg:int, taillea:int, text:str):
        result = Style.grossir(tailleg, text)
        result = Style.agrandir(taillea, text)

        return result