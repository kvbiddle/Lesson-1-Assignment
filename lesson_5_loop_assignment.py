
user_sentence = input('Please type a sentence: ')

user_sentence_lower = user_sentence.lower()

user_sentence_list = list(user_sentence_lower)

user_sentence_letters_list = []

for letter in user_sentence_list:
    if letter.isalpha():
        user_sentence_letters_list.append(letter)


user_sentence_string = "".join(user_sentence_letters_list)

user_sentence_letters_list.reverse()

user_sentence_letters_reverse = "".join(user_sentence_letters_list)


if user_sentence_string == user_sentence_letters_reverse:
    print('is palindrome')
else:
    print('is not palindrome')

