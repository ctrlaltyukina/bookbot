def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
        
    return char_counts
    
def chars_dict_to_sorted_list(char_dict):
    # Create an empty list to store our new dictionaries
    result_list = []
    
    # For each character and its count in the original dictionary
    for char, count in char_dict.items():
        # Create a new dictionary and add it to our list
        result_list.append({"char": char, "num": count})
    
    # Define how to sort the list (by the "num" value)
    def sort_on(dict):
        return dict["num"]
    
    # Sort the list in descending order (reverse=True)
    result_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return result_list