def get_num_words(text):
	words = text.split()
	return len(words)

def count_chars(text):
	lower = text.lower()
	dict = {}

	for char in lower:
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1

	return dict

def chars_sorter(e):
	return e['num']

def get_chars_list(dict):
	chars = []

	for char in dict:
		chars.append({ "char": char, "num": dict[char]})

	chars.sort(reverse=True, key=chars_sorter)

	return chars