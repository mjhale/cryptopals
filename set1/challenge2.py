#!/usr/bin/env python
# Fixed XOR
#
# Write a function that takes two equal-length buffers and produces their XOR combination.
#
# If your function works properly, then when you feed it the string:
#
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
#
# 686974207468652062756c6c277320657965
# ... should produce:
#
# 746865206b696420646f6e277420706c6179

from challenge1 import hex_to_byte_array
from binascii import hexlify

def hex_xor(first_hex, second_hex):
    first_raw = b''.join(hex_to_byte_array(first_hex))
    second_raw = b''.join(hex_to_byte_array(second_hex))
    raw = []

    for b in range(0, len(first_raw)):
        raw.append(first_raw[b] ^ second_raw[b])

    raw = bytes(raw)

    return hexlify(raw)

if __name__ == "__main__":
    first_hex = "1c0111001f010100061a024b53535009181c"
    second_hex = "686974207468652062756c6c277320657965"
    print(hex_xor(first_hex, second_hex))
