def count_words(text):
        words = text.split()     # Splits the string into words at whitespace
        count = len(words)       # Count how many words
        print(f"Found {count} total words")


def count_characters(text):
    text = text.lower()    # Convert all characters to lower case
    counts = {}            # initialize counts dictionary to store counts for each character

    for char in text:            # loop through each character in the string
        if char in counts:       # if the character is in the dictionary, increment its count
            counts[char] += 1
        else:                    # if the character is not in the dictionary, add it with a starting count of 1
            counts[char] = 1

    return counts                # return the dictionary with all the character counts

def sort_characters(char_dict):
    sorted_list = []

    # Transform the dictionary into a list of {'char': ..., 'num': ...}
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})

    # Sort the list in-place by 'num', from greatest to least
    sorted_list.sort(key=lambda item: item["num"], reverse=True)

    return sorted_list

