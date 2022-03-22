
users_word = input('please type in a word ')

letters_in_word = list(users_word)

letters_in_word.reverse()

string_from_list = "".join(letters_in_word)

is_palindrome = string_from_list == users_word

print(is_palindrome)

