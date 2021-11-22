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


    black_to_white = ["m;m;m"]
    black_to_red = ["m;0;0"]
    black_to_green = ["0;m;0"]
    black_to_blue = ["0;0;m"]

    white_to_black = ["n;n;n"]
    white_to_red = ["255;n;n"]
    white_to_green = ["n;255;n"]
    white_to_blue = ["n;n;255"]

    red_to_black = ["n;0;0"]
    red_to_white = ["255;m;m"]
    red_to_yellow = ["255;m;0"]
    red_to_purple = ["255;0;m"]

    green_to_black = ["0;n;0"]
    green_to_white = ["m;255;m"]
    green_to_yellow = ["m;255;0"]
    green_to_cyan = ["0;255;m"]

    blue_to_black = ["0;0;n"]
    blue_to_white = ["m;m;255"]
    blue_to_cyan = ["0;m;255"]
    blue_to_purple = ["m;0;255"]

    yellow_to_red = ["255;n;0"]
    yellow_to_green = ["n;255;0"]

    purple_to_red = ["255;0;n"]
    purple_to_blue = ["n;0;255"]

    cyan_to_green = ["0;255;n"]
    cyan_to_blue = ["0;n;255"]

    gradients_list = [
        black_to_white, black_to_red, black_to_green, black_to_blue,
        white_to_black, white_to_red, white_to_green, white_to_blue,

        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,
        
        yellow_to_red, yellow_to_green,
        purple_to_red, purple_to_blue,
        cyan_to_green, cyan_to_blue
    ]

for gradients in Colors.gradients_list:
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

for gradient in Colors.gradients_list:
    grad = []
    for graded in gradient:
        grad.append(graded)
    for grad in grad:
        gradient.append(grad)