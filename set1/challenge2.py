#!/usr/bin/env python

"""Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179

@TODO: Use own binary array to hex method instead of hexlify
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

from challenge1 import hex_to_array, hex_to_bytes
from codecs import encode

def hex_xor(first_hex, second_hex):
    first_raw = hex_to_bytes(first_hex)
    second_raw = hex_to_bytes(second_hex)
    bytes = bytearray()
    for b in range(0, len(first_raw)):
        bytes.append(first_raw[b] ^ second_raw[b])
    return encode(bytes, 'hex_codec')

if __name__ == "__main__":
    first_hex = '1c0111001f010100061a024b53535009181c'
    second_hex = '686974207468652062756c6c277320657965'
    print(hex_xor(first_hex, second_hex))
