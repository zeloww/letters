import random

class Fade:
    
    def static(color:str, text:str, fond:str='1',style:str='1'):
        if color.lowercase() in ['random', 'r']:
            color = random.choice(range(38))

        os.system('')
        result = f'\033[{color};{fond};{style}m{text}\033[0m'

        return result


    def all_statics(text:str='Example'):
        os.system('')
        result = ''

        for color in range(108):
             result += f'\033[{color}m{text}\033[0m\n'

        return result


    def gradient(gradient:str, text:str, types:str='vertical', speed:int=1):
        os.system('')

        result = ''
        gradient_n = 0

        if gradient == 'random':
            gradient = random.choice(Colors.gradients_list)

        for line in text.splitlines():
            characters = list(line)

            if types in Colors.horizontal:
                gradient_n = 0

            if types in Colors.vertical:
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

    def all_gradients(text:str='Example', types:str='vertical', speed:str=1):
        os.system('')
        result = ''

        for gradient in Colors.gradients_list:
            result_one = ''
            gradient_n = 0

            for line in text.splitlines():
                characters = list(line)

                if types in Colors.horizontal:
                    gradient_n = 0

                if types in Colors.vertical:
                    for character in characters:
                        result_one += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                    if line == '':
                        pass

                    elif gradient_n + speed < len(gradient):
                        gradient_n += speed

                    else:
                        gradient_n = gradient in Colors.horizontal

                    result_one += '\n'

                else:
                    for character in characters:
                        result_one += f'\033[38;2;{gradient[gradient_n]}m{character}\033[38;2;255;255;255m'

                        if line == '':
                            pass

                        elif gradient_n + speed < len(gradient):
                            gradient_n += speed

                        else:
                            gradient_n = gradient in Colors.horizontal

                    result_one += '\n'

            result += result_one + '\n' 

            Style.clear()
            print(result_one)
            input()

        return result