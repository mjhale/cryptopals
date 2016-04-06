#!/usr/bin/env python

"""Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
Evaluate each output and choose the one with the best score.
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge1 import HEX_LUT, hex_to_bytes
from challenge2 import hex_xor
from collections import defaultdict

# Normalized to have a total probability of ~1
LETTER_FREQUENCY = {
    'A': .0812,
    'B': .0149,
    'C': .0271,
    'D': .0432,
    'E': .1202,
    'F': .0230,
    'G': .0203,
    'H': .0592,
    'I': .0731,
    'J': .0010,
    'K': .0069,
    'L': .0398,
    'M': .0261,
    'N': .0695,
    'O': .0768,
    'P': .0182,
    'Q': .0011,
    'R': .0602,
    'S': .0628,
    'T': .0910,
    'U': .0288,
    'V': .0111,
    'W': .0209,
    'X': .0017,
    'Y': .0211,
    'Z': .0007
    }

def hex_decode(hex):
    plain = ''
    for b in hex_to_bytes(hex):
        plain += chr(b)
    return plain

def score(message):
    score = 0
    for c in message:
        score += LETTER_FREQUENCY.get(c.upper())
    return score

def decrypt_message(hex):
    message = 0
    candidates = defaultdict(list)
    for b in hex_to_bytes(hex):

def main():
    INPUT_HEX = ('1b37373331363f78151b7f2b783431333d'
                 '78397828372d363c78373e783a393b3736')
    decrypt_message(INPUT_HEX)
    print(hex_decode(INPUT_HEX))
    #print(score('hello'))

if __name__ == '__main__':
    main()
