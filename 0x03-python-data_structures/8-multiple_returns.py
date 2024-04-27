#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        chr = sentence[0]
    else:
        chr = None
    return (len(sentence), chr)
