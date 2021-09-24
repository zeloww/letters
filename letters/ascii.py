class Ascii:

	lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	hexdigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
	octdigits = ['0', '1', '2', '3', '4', '5', '6', '7']
	punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
	whitespace = [' ', '\t', '\v', '\n', '\r', '\f']

	upper_case = list(map(str.upper, lower_case))
	letters = lower_case + upper_case
	printable = digits + letters + punctuation + whitespace

	yes = ['y', 'yes', 'Y', 'Yes', 'YES']
	no = ['n', 'no', 'N', 'No', 'NO']