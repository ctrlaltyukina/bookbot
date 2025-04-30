from stats import get_book_text, count_words, count_characters, chars_dict_to_sorted_list
import sys


num_args = len(sys.argv)
if num_args == 2:
    path = sys.argv[1] # define the path variable once
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


text = get_book_text(path)       # Read the book text
num_words = count_words(text)    # Count the words

# Count the characters
num_characters = count_characters(text)

# Use the correct variable name here
sorted_chars = chars_dict_to_sorted_list(num_characters)


print("============ BOOKBOT ============")
print(f"*** YOU ASKED TO ANALYZE: {path}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")  # Use num_words instead of word_count
print("--------- Character Count -------")

# Print each character and its count
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["num"]
    
    # Skip non-alphabetical characters
    if char.isalpha():
        print(f"{char}: {count}")

# Print the footer
print("============= END ===============")



