#!/usr/bin/python3
def text_indentation(text):
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    
    punctuation_marks = {'.', ':', '?'}

    indented_text = ""
    for char in text:
        indented_text += char
        if char in punctuation_marks:
            indented_text += '\n\n'
    print("{}".format(indented_text))