def width(taille:int, text:str) -> str:
    result = ''

    for character in text:
        if character == '\n':
            result += '\n'.join(character)

        else:
            result += ''.join(character*taille)
        
    return result

def length(taille:int, text:str) -> str:
    result = ''

    for w in text.splitlines():
        if w == '\n':
            result += w
        result += (w+'\n')*taille

    return result

def big(tailleg:int, taillea:int, text:str) -> str:
    result = Style.grossir(tailleg, text)
    result = Style.agrandir(taillea, text)

    return result