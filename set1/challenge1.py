#!/usr/bin/env python
# Convert hex to base64
#
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# TODO Stop using strings for hex representation

from base64 import b64encode
from binascii import unhexlify

def hex_array(hex):
    return [''.join(c) for c in zip(hex[0::2], hex[1::2])]

def hex_to_byte_array(hex):
    byte_array = [unhexlify(c) for c in hex_array(hex)]
    return byte_array

if __name__ == "__main__":
    HEX_STRING = ("49276d206b696c6c696e6720796f757220627261696e206c"
                  "696b65206120706f69736f6e6f7573206d757368726f6f6d")

    print("hex:     ", hex_array(HEX_STRING))
    print("decimal: ", [int(c, 16) for c in hex_array(HEX_STRING)])
    print("chr:     ", [chr(int(c, 16)) for c in hex_array(HEX_STRING)])
    print("b64:     ", b64encode(b''.join(hex_to_byte_array(HEX_STRING))))
