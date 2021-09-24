class Colors:

    black = '30'
    red = '31'
    green = '32'
    yellow = '33'
    blue = '34'
    magenta = '35'
    cyan = '36'
    white = '37'

    bright_black = '90'
    bright_red = '91'
    bright_green = '92'
    bright_yellow = '93'
    bright_blue = '94'
    bright_magenta = '95'
    bright_cyan = '96'
    bright_white = '97'

    bg_black = '40'
    bg_red = '41'
    bg_green = '42'
    bg_yellow = '43'
    bg_blue = '44'
    bg_magenta = '45'
    bg_cyan = '46'
    bg_white = '47'

    bg_bright_black = '100'
    bg_bright_red = '101'
    bg_bright_green = '102'
    bg_bright_yellow = '103'
    bg_bright_blue = '104'
    bg_bright_magenta = '105'
    bg_bright_cyan = '106'
    bg_bright_white = '107'

    italic = '3'
    souligné  ='4'
    barree = '9'
    encercle = '52'
    surligné = '53'


    vertical = ['vertical', 'Vertical', 'v', 'V']
    horizontal = ['horizontal', 'Horizontal', 'h', 'H']
    diagonal = ['diagonal', 'Diagonal', 'd', 'D']


    black_to_white = ['m;m;m']
    white_to_black = ['n;n;n']

    red_to_yellow = ['255;m;0']
    red_to_pink = ['255;0;m']

    green_to_yellow = ['m;255;0']
    green_to_lightblue = ['0;255;m']

    darkblue_to_lightblue = ['0;m;255']
    darkblue_to_purple = ['m;0;255']

    red_to_yellow_reversed = ['255;n;0']
    red_to_pink_reversed = ['255;0;n']

    green_to_yellow_reversed = ['n;255;0']
    green_to_lightblue_reversed = ['0;255;n']

    darkblue_to_lightblue_reversed = ['0;n;255']
    darkblue_to_purple_reversed = ['n;0;255']

    #Thanks to @billythegoat326 for that :p
    gradients_list = [black_to_white, white_to_black, red_to_yellow, red_to_pink, green_to_yellow, green_to_lightblue, darkblue_to_lightblue, darkblue_to_purple, red_to_yellow_reversed, red_to_pink_reversed, green_to_yellow_reversed, green_to_lightblue_reversed, darkblue_to_lightblue_reversed, darkblue_to_purple_reversed]

    for gradients in gradients_list:
        gradient = 20
        reversed_gradient = 220

        dbl_gradient = 20
        dbl_reversed_gradient = 220

        content = gradients[0]
        gradients.pop(0)
        
        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(gradient))
                gradients.append(result)
            
            elif 'n' in content:
                result = content.replace('n', str(reversed_gradient))
                gradients.append(result)

            gradient += 20
            reversed_gradient -= 20

        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(dbl_reversed_gradient))
                gradients.append(result)
            
            elif 'n' in content:
                result = content.replace('n', str(dbl_gradient))    
                gradients.append(result)

            dbl_gradient += 20
            dbl_reversed_gradient -= 20

    for gradient in gradients_list:
        grad = []
        for graded in gradient:
            grad.append(graded)
        for grad in grad:
            gradient.append(grad)