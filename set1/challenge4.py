#!/usr/bin/env python

"""Detect single-character XOR

One of the 60-character strings in this file (challenge4.txt) has been encrypted
by single-character XOR. Find it.

(Your code from #3 should help.)
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge3 import decode_single_byte_xor

def decode_single_character_xor(file):
    candidates = []
    with open(file) as f:
        for line in f:
            candidates.append(decode_single_byte_xor(line.rstrip()))
    return min(candidates, key=lambda x: x[1])

def main():
    print(decode_single_character_xor('challenge4.txt'))

if __name__ == '__main__':
    main()
