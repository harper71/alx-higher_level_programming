#!/usr/bin/python3
def multiple_returns(sentence):
    amount = len(sentence)
    first_character = sentence[0] if amount > 0 else "None"
    return amount, first_character
