#!/usr/bin/env python

"""Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge1 import HEX_LUT, hex_to_bytes

def bytes_to_hex(bytes):
    """Converts an array of bytes into a hex string"""
    hex = ''
    for b in bytes:
        high_nibble = (b >> 4) & 15
        low_nibble = b & 15
        hex += HEX_LUT[high_nibble]
        hex += HEX_LUT[low_nibble]
    return hex

def hex_xor(first_hex, second_hex):
    """Take two equal-length hex strings and return their XOR product"""
    first_raw = hex_to_bytes(first_hex)
    second_raw = hex_to_bytes(second_hex)
    bytes = bytearray()
    for b in range(0, len(first_raw)):
        bytes.append(first_raw[b] ^ second_raw[b])
    return bytes_to_hex(bytes)

def main():
    FIRST_HEX = '1c0111001f010100061a024b53535009181c'
    SECOND_HEX = '686974207468652062756c6c277320657965'
    print(hex_xor(FIRST_HEX, SECOND_HEX))

if __name__ == '__main__':
    main()
