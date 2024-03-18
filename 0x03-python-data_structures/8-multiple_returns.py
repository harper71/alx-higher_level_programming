#!/usr/bin/python3
def multiple_returns(sentence):
    string = tuple(sentence)
    amount = len(sentence)
    first_char = sentence[0]
    return amount, first_char
