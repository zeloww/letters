<h1 align="center">Letters</h1>
<br>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.1-blue.svg?cacheSeconds=2592000" />
  
  <a href="https://github.com/zeloww/letters/blob/main/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-blue.svg" />
  </a>
  
  <a href="https://github.com/zeloww/letters" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/maintained-yes-blue.svg" />
  </a>
  
  <a href="https://github.com/zeloww/letters/blob/main/LICENSE" target="_blank">
    <img alt="License: EPL-2.0" src="https://img.shields.io/github/license/zeloww/letters?color=blue"/>
  </a>
  
  <a href="https://pepy.tech/project/letters" target="_blank">
    <img alt="Downloads" src="https://static.pepy.tech/personalized-badge/letters?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads" />
  </a>
</p>

> **Letters** is a python library to make very beautiful TUI designs, ASCII arts, fonts and more.
> <br>
> <br>
> Developped by [Zelow](https://github.com/Zeloww)

## Install

To install with PIP, do the following command:

```shell
# Linux/macOS
python3 -m pip install -U letters

# Windows
py -3 -m pip install -U letters
```

To install the development version, do the following command:

```shell
$ git clone https://github.com/zeloww/letters
$ cd letters
```

## Fade

> Color your texts easily

Finir d'écrire:
> statics color:str, text:str, fond:str='1',style:str='1'
> all_statics text="Exemple"

> gradient gradient:str, text:str, mode_type:str='vertical', speed:int=1
> all_gradients text:str='Example', mode_type:str='vertical', speed:str=1

> fade(gradient:str, text:str, mode_type:str='vertical', stop:str="", time:float=None, interval:float=0.05, max_speed:int=10)

### Colors list

> List of the ANSI Escape Codes

```python
from letters.colors import Colors

Colors.black, Colors.red, Colors.green, Colors.yellow, Colors.blue, Colors.magenta, Colors.cyan, Colors.white
Colors.bg_black, Colors.bg_red, Colors.bg_green, Colors.bg_yellow, Colors.bg_blue, Colors.bg_magenta, Colors.bg_cyan, Colors.bg_white

Colors.bg_bright_black, Colors.bg_bright_red, Colors.bg_bright_green, Colors.bg_bright_yellow, Colors.bg_bright_blue, Colors.bg_bright_magenta, Colors.bg_bright_cyan, bg_bright_white
    
Colors.black_to_white, Colors.black_to_red, Colors.black_to_green, Colors.black_to_blue,
Colors.white_to_black, Colors.white_to_red, Colors.white_to_green, Colors.white_to_blue,

Colors.red_to_black, Colors.red_to_white, Colors.red_to_yellow, Colors.red_to_purple,
Colors.green_to_black, Colors.green_to_white, Colors.green_to_yellow, Colors.green_to_cyan,
Colors.blue_to_black, Colors.blue_to_white, Colors.blue_to_cyan, Colors.blue_to_purple,

Colors.yellow_to_red, Colors.yellow_to_green,
Colors.purple_to_red, Colors.Colors.purple_to_blue,
Colors.cyan_to_green, Colors.cyan_to_blue
```

#Center
> Center your text in many ways

> Make a logo with text

```python
>>> from letters.center import Center
>>> i="""
...
...          wWWWw               wWWWw
...    vVVVv (___) wWWWw         (___)  vVVVv
...    (___)  ~Y~  (___)  vVVVv   ~Y~   (___)
...     ~Y~   \|    ~Y~   (___)    |/    ~Y~
...     \|   \ |/   \| /  \~Y~/   \|    \ |/
...    \\|// \\|// \\|/// \\|//  \\|// \\\|///
... ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
... """
>>> print(Center.logo("hello\nUse Letters !", i))
hello
Use Letters ! 
                                wWWWw               wWWWw
                          vVVVv (___) wWWWw         (___)  vVVVv
                          (___)  ~Y~  (___)  vVVVv   ~Y~   (___)
                           ~Y~   \|    ~Y~   (___)    |/    ~Y~
                           \|   \ |/   \| /  \~Y~/   \|    \ |/
                          \\|// \\|// \\|/// \\|//  \\|// \\\|///
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

> Center text in a terminal horizontally, vertically or both directly!

```python
from letters.center import Center

"""
 |  border(text: str, lenght: str = '=', width: str = '|', distance: int = 1, center=True)
 |
 |  center(text: str, spaces: int = None, lines: int = None, force_vertical: bool = True, force_horizontal: bool = False, force_center: bool = False, end='\n') -> str
 |
 |  horizontal(text: str, spaces: int = None, force_horizontal: bool = False, end: str = '') -> str
 |
 |  logo(text: str, icon: str, spaces: int = 5) -> str
 |
 |  vertical(text: str, lines: int = None, force_vertical: bool = True) -> str
"""

Center.horizontal("Use letters!") #center horizontally
Center.vertical("Made with <3") #center vertically
Center.center("By github.com/Zeloww") #center horizontally and vertically
```

from letters.center import Center
Center.logo, border, horizontal, vertical, center

## ASCII

> list of all ASCII character types

```python
from letters.ascii import Ascii

Ascii.lower_case #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Ascii.digits #['1', '2', '3', '4', '5', '6', '7', '8', '9']
Ascii.hexdigits #['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
Ascii.octdigits #['0', '1', '2', '3', '4', '5', '6', '7']
Ascii.punctuation #['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
Ascii.whitespace #[' ', '\t', '\v', '\n', '\r', '\f']

Ascii.upper_case #list(map(str.upper, lower_case))
Ascii.letters #lower_case + upper_case
Ascii.printable #digits + letters + punctuation + whitespace

Ascii.yes #['y', 'yes', 'Y', 'Yes', 'YES']
Ascii.no #['n', 'no', 'N', 'No', 'NO']
```

## Fonts

> Customize any texts with fonts!

**All font names are available [Here](https://pastebin.com/r1taHnrZ)**

### Fonts list

> List of all fonts

```python
from letters.asciiart import all_fonts

def get_fontslist():
  return all_fonts

get_fontslist()
```

Returns a list of all fonts

input:
```python
from letters.asciiart import fonts_list
fonts_list(text="Zelow")
```

Output:<br>
Show all fonts with the text `Zelow`

## ASCII Art

> Returns the chosen image in ASCII art

### Gray levels

```python
# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
complexGrayScale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

# 10 levels of gray by default
easyGrayScale = '@%#*+=-:. '
```

### Exemple

input:
```python
from letters.asciiart import img2ascii

img2ascii("path/to/dir/image.jpg", scale=0.25, moreLevels=None, reverseLight=False)
```

output:
<img src=https://i.imgur.com/C57mNoo.png>

## Text size
> Change the size of any of your texts
  
```py
>>> from letters.style import width, length, big
>>>
>>> box = """
... |--------|
... |        |
... |--------|
... """

>>> print(width(2, box))
"""
||----------------||
||                ||
||----------------||
"""

>>> print(length(2, box))
"""
|--------|
|--------|
|        |
|        |
|--------|
|--------|
"""

>>> print(big(2, 2, box))
"""
||----------------||
||----------------||
||                ||
||                ||
||----------------||
||----------------||
"""
```

## Others
> Other useful functions

```python
from letters.system import Title, Clear, Print, Input, Replace #or from letters.system import *

Title("New program title") #Change the program title
Clear() #Delete the text already present in the terminal

Print("My text", speed=0.5) #Print all characters in `My text`waiting `0.5` seconds between each characters 
Input("My text", speed=1) #Input the text by printing all characters in `My text` waiting `1` seconds between each characters 
Replace(list_name, base, change) #Replace `base` by `change` for all elements in `list_name`
```

## 👤 Authors

👤 GitHub: [@**Zeloww**](https://github.com/zeloww)<br>

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/zeloww/letters/issues).

## ❤ Show your support

Give a ⭐️ if this project helped you!
