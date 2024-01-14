#Program builds 10 random sentences based on the pronouns, verbs and nouns available. 
# #

import random
def pronoun():
    pronoun_list =["I", "You", "It", "We", "They"]
    random_value = random.choice(pronoun_list)
    return random_value
    
def verb():
    verb_list = ["will see", "will eat", "will pull", "will touch"]
    random_value = random.choice(verb_list)
    return random_value
    
def noun():
    noun_list = ["a house", "a car", "a computer", "a tree"]
    random_value = random.choice(noun_list)
    return random_value

for i in range(11):
    print(f"{pronoun()} {verb()} {noun()}")