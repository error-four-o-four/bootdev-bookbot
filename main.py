from stats import get_num_words, count_chars, get_chars_list

import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path):
	with open(path) as f:
		contents = f.read()
		return contents

def pretty_print(path, num_words, list_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")

	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	print("--------- Character Count -------")
	for item in list_chars:
		if item["char"].isalpha() == True:
			print(f"{item["char"]}: {item["num"]}")

	print("============= END ===============")

def main():
	path = sys.argv[1]
	text = get_book_text(path)
	num_words = get_num_words(text)
	dict_chars = count_chars(text)
	list_chars = get_chars_list(dict_chars)

	pretty_print(path, num_words, list_chars)

main()