# Convert string to camel case
"""
Description
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    #your code here 
    if text == '':
        return ''
    if '-' in text:
        text = text.replace('-', '_')
    if '_' in text:
        words_arr = text.split('_')
    
    first_word = words_arr[0]
    words_arr = [word.capitalize() for word in words_arr]
    words_arr[0] = first_word

    return ''.join(words_arr)
