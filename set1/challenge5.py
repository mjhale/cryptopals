#!/usr/bin/env python

"""Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge2 import bytes_to_hex

def repeating_key_xor_encode(plaintext, key):
    """Encrypts plaintext using repeating-key XOR and returns hex result"""
    bytes = bytearray()
    for i in range(len(plaintext)):
        # Plaintext character at position i
        c = ord(plaintext[i])
        # Key character cycling between positions 0-len(key)
        k = ord(key[i % len(key)])
        bytes.append(c ^ k)
    return bytes_to_hex(bytes)

def main():
    PLAINTEXT = "Burning 'em, if you ain't quick and nimble\n"
    PLAINTEXT += "I go crazy when I hear a cymbal"
    KEY = 'ICE'
    print(repeating_key_xor_encode(PLAINTEXT, KEY))

if __name__ == '__main__':
    main()
