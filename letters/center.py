from os import get_terminal_size

class Center:
	def horizontal(text:str, spaces:int=None, force_horizontal:bool=False, end:str='') -> str:
		if not force_horizontal and not spaces:
			spaces = int((get_terminal_size().columns - len(text.splitlines()[0])) / 2)

		result = ''
		for lines in text.splitlines():

			if force_horizontal:
				spaces = int((get_terminal_size().columns - len(lines)) / 2)

			result += '\n' + ' ' * spaces + lines

		result += end
		return result

	def vertical(text:str, lines:int=None, force_vertical:bool=True) -> str:
		if force_vertical:
			lines = int((get_terminal_size().lines - len(text.splitlines())) / 2)

		elif not lines:
			lines = int(get_terminal_size().lines / 2)

		return '\n' * lines + '\n'.join(text.splitlines())

	def center(text:str, spaces:int=None, lines:int=None, force_vertical:bool=True, force_horizontal:bool=False, force_center:bool=False, end='\n') -> str:
		if not spaces and not force_horizontal and not force_center:
			spaces = int((get_terminal_size().columns - len(text.splitlines()[0])) / 2)

		horizontal_result = ''
		for line in text.splitlines():

			if force_horizontal or force_center:
				spaces = int((get_terminal_size().columns - len(line)) / 2)

			horizontal_result += '\n' + ' ' * spaces + line

		horizontal_result += end

		if force_vertical or force_center:
			lines = int((get_terminal_size().lines - len(text.splitlines())) / 2)

		elif not lines:
			lines = int(get_terminal_size().lines / 2)

		result = '\n' * lines + '\n'.join(horizontal_result.splitlines())
		return result

	def border(text:str, lenght:str="=", width:str="|", distance:int=1, center=True):
	    longest_line_lenght = max([len(line) for line in text.splitlines()])
	    result = lenght * (longest_line_lenght + 2 + distance * 2) + "\n"

	    for line in text.splitlines():
	        if center:
	            distance_lenght = distance + (longest_line_lenght - len(line)) / 2
	            distance_lenght2 = distance + (longest_line_lenght - len(line)) / 2

	            if int(distance_lenght) != distance_lenght:
	                distance_lenght2 += 1

	            result += width + " " * int(distance_lenght) + line + " " * int(distance_lenght2) + width + "\n"

	        else:
	            result += width + " " * distance + line + " " * int(distance + longest_line_lenght - len(line)) + width + "\n"

	    result += lenght * (longest_line_lenght + 2 + distance * 2) + "\n"
	    return result
	    
	def logo(text:str, icon:str, spaces:int=5) -> str:
		line = 0
		result = ''

		if len(text.splitlines()) < len(icon.splitlines()):
			text += '\n' * (len(icon.splitlines()) - len(text.splitlines()) + 1)

		elif len(text.splitlines()) > len(icon.splitlines()):
			icon += '\n' * (len(text.splitlines()) - len(icon.splitlines()) + 1)

		longest_line = max(list(text.splitlines()), key=len)

		for lines in text.splitlines():
			result += lines + (' ' * (spaces + (len(longest_line) - len(lines)))) + icon.splitlines()[line] + '\n'
			line += 1

		return result