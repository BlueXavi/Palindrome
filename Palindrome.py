def is_palindrome(word):
    # Remove any spaces and convert the word to lowercase for uniformity
    cleaned_word = word.replace(" ", "").lower()
    
    # Check if the cleaned word reads the same forward and backward
    return cleaned_word == cleaned_word[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
