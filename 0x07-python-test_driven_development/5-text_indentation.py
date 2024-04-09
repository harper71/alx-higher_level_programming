#!/usr/bin/python3
"""indentation of texts"""


def text_indentation(text):
    """used to put a new line when text i

    Args:
        text (str): text to indent

    Raises:
        TypeError: text must be a string
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")

    punctuation_marks = {'.', ':', '?'}

    indented_text = ""
    for char in text:
        indented_text += char
        if char in punctuation_marks:
            indented_text += '\n\n'
    print("{}".format(indented_text))
