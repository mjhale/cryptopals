#!/usr/bin/env python

"""Break repeating-key XOR

There's a file here (challenge6.txt). It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

@TODO Implement base64 decode.
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from base64 import b64decode

def dec_to_bin(string):
    """Returns the binary representation of a string"""
    bits = [bin(c)[2:].zfill(8) for c in bytearray(string, 'utf8')]
    return ''.join(bits)

def hamming_distance(first, second):
    """Calculates the edit distance between two strings"""
    assert len(first) == len(second)
    first = dec_to_bin(first)
    second = dec_to_bin(second)
    return sum(b0 != b1 for b0, b1 in zip(first, second))

def decrypt_vigenere(cipher, keysize_min, keysize_max):
    for key_length in range(keysize_min, keysize_max):
        b0 = cipher[:key_length]
        print(b0)
    return None

def main():
    FIRST = 'this is a test'
    SECOND = 'wokka wokka!!!'
    in_file = open('challenge6.txt', 'r')
    base64 = in_file.read()
    decrypt_vigenere(b64decode(base64), 2, 40)

if __name__ == '__main__':
    main()
