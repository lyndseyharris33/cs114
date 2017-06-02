
# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful',
#     'Maybe someday',
#     'Can you speak up?'
#     'Im not sure you would like my answer',
#      'Do you really want to ask that?' ]


import random
print("What is your question?")
question = input()

print(messages[0])
print(messages[random.randint(0,8)])
print(messages[random.randint(0, len(messages) - 1)])

if len(question) 8> )])
  ['It is decidedly so',
  'Yes definitely',
  'Reply hazy try again']
elif:
  len(question) 9< )])
 ['Ask again later',
 'Concentrate and ask again',
 'My reply is no',
 'Outlook not so good',
 'Very doubtful']
elif:
   len(question) 20< )])
  ['Maybe someday',
  'Can you speak up?'
  'Im not sure you would like my answer',
   'Do you really want to ask that?' ]


#
# else def prompt_for_question():
#     """if question is 8 letters or less, provide these responses."""
#
# def prompt_for_question():
#     """if question is 9 letters or more, provide these responses."""
#
# def prompt_for_question():
#     """if question is 25 letters or more, provide these responses."""


# message_num = input print("What do you want to know?)
# if len(message_num) >7:


# def prompt_for_question():
#
#     return int(input('What would yo like to know?: '))
#
#
# def question():
#     return num // 10
#
#
# def get_ones_digit(num):
#     """Return the ones digit of a number."""
#     return num % 10
#
#
# def tens_digit_to_word(tens_digit):
#     """From the tens digit, return the word representing that."""
#     if tens_digit == 9:
#         tens_word = 'ninety'
#     elif tens_digit == 8:
#         tens_word = 'eighty'
#     elif tens_digit == 7:
#         tens_word = 'seventy'
#     elif tens_digit == 6:
#         tens_word = 'sixty'
#     elif tens_digit == 5:
#         tens_word = 'fifty'
#     elif tens_digit == 4:
#         tens_word = 'forty'
#     elif tens_digit == 3:
#         tens_word = 'thirty'
#     elif tens_digit == 2:
#         tens_word = 'twenty'
#     else:
#         tens_word = ''
#     return tens_word
