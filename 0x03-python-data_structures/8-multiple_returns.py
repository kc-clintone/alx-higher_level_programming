#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        result = (0, None)
        return result
    else:
        response = (l, sentence[0:1])
        return response
