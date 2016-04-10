#!/usr/bin/env python

"""Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.

Evaluate each output and choose the one with the best score.

@TODO: Find a new way to penalize or exclude non-ascii chars.
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge1 import hex_to_bytes
from challenge2 import bytes_to_hex, hex_xor
from collections import defaultdict

# Normalized frequency table which has a total probability of ~1
LETTER_FREQUENCY = {
    'a': .0812,
    'b': .0149,
    'c': .0271,
    'd': .0432,
    'e': .1202,
    'f': .0230,
    'g': .0203,
    'h': .0592,
    'i': .0731,
    'j': .0010,
    'k': .0069,
    'l': .0398,
    'm': .0261,
    'n': .0695,
    'o': .0768,
    'p': .0182,
    'q': .0011,
    'r': .0602,
    's': .0628,
    't': .0910,
    'u': .0288,
    'v': .0111,
    'w': .0209,
    'x': .0017,
    'y': .0211,
    'z': .0007
    }

def hex_decode(hex):
    """Converts hex string to ASCII string."""
    plain = ''
    for b in hex_to_bytes(hex):
        plain += chr(b)
    return plain

def decode_single_byte_xor(hex):
    """Decodes a single-byte XOR cipher using a chi-squared test."""
    candidates = defaultdict(list)
    # Iterate through each possible key
    for i in range(256):
        candidate_hex = hex_xor(hex, bytes_to_hex(bytes([i] * len(hex))))
        candidate_plain = hex_decode(candidate_hex)
        score = 0.0
        # Iterate through every letter of the english alphabet
        for c in candidate_plain:
            if c in LETTER_FREQUENCY:
                c_count = candidate_plain.lower().count(c)
                c_expected = LETTER_FREQUENCY[c] * len(candidate_plain)
                # Chi-squared calculation
                score += ((c_count - c_expected)**2) / c_expected
            elif not c.isspace():
                # Penalize non-space and non-[a-z] chars
                score += len(candidate_plain) / 4
        candidates[i].append([score, candidate_hex, candidate_plain])
    # Find candidate with lowest score. Retrieve candidate_plain ([1][0][2])
    message = min(candidates.items(), key=lambda x: x[1])
    return message

def main():
    INPUT_HEX = ('1b37373331363f78151b7f2b783431333d'
                 '78397828372d363c78373e783a393b3736')
    print(decode_single_byte_xor(INPUT_HEX))

if __name__ == '__main__':
    main()
