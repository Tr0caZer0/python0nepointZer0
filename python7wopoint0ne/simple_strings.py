def first_last(s):       #  Returns the first and last character in the string s
     return s[0]+" " +s[-1]
# First and last in "May the Force be with you!":
 
def char_types(s):       #  Returns the number of vowels and consonants in string s
    vowels = set("aeiouy")
    consonants = set("bcdfghjklmnpqrstvwxz")
    s = s.lower()
    
    count_consonants = 0
    count_vowels = 0
    
    for i in s:
        if i in consonants:
            count_consonants += 1
        elif i in vowels:
            count_vowels += 1
            
    return f"In that sentence, the number of vowels is {count_vowels} and the number of consonants is {count_consonants}"
            
            
    
def char_symbol_number(s):  #  Returns the number of characters, symbols (including spaces) and numbers in string s
    letters = set("abcdefghijklmnopqrstuvwxyz")
    integers = set("0123456789")
    s = s.lower()
    
    letter_count = 0
    integer_count = 0
    symbol_count = 0
    
    for i in s: 
        if i in letters:
            letter_count += 1
        elif i in integers:
            integer_count += 1
        else:
            symbol_count += 1
    return_string = f'In the sentence "{s}" the number of letters is {letter_count}, symbols is {symbol_count} and numbers is {integer_count}'    
    return return_string

sentence_1 = "May the Force be with you!"
sentence_2 = "I am 1 with the Force, not 2..."

print(f'First and last in "{sentence_1}" is : {first_last(sentence_1)}')
print(char_types(sentence_1))
print(char_symbol_number(sentence_2))