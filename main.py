import sys
from stats import  count_words, count_characters, sort_characters

def get_book_text(path_to_file):
	with open(path_to_file) as f:
	    file_contents = f.read()
	return(file_contents)

def main():
	
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")

    text = get_book_text(path)
    word_total = count_words(text)
    char_counts = count_characters(text)

    sorted_characters = sort_characters(char_counts)
    # print(char_counts)

    print("--------- Character Count -------")
    for item in sorted_characters:
        	print(f"{item['char']}: {item['num']}")
    print("============ END ============")

main()	
