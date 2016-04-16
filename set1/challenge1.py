#!/usr/bin/env python

"""Convert hex to base64

The string:
49276d206b696c6c696e6720796f757220627261696e206c
696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

BASE64_LUT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
HEX_LUT = '0123456789abcdef'

def hex_to_dec(hex):
    """Converts a single hex value to decimal"""
    if len(hex) != 1:
        return None
    return HEX_LUT.index(hex)

def hex_to_array(hex):
    """Converts a hex value to a byte-sized array"""
    # Add padding if odd length
    if len(hex) % 2 == 1:
        hex = '0' + hex
    return [''.join(n) for n in zip(*[iter(hex)] * 2)]

def hex_to_bytes(hex):
    """Converts a hex value to bytes"""
    bytes = bytearray()
    for high_hex, low_hex in hex_to_array(hex):
        high_nibble = hex_to_dec(high_hex)
        low_nibble = hex_to_dec(low_hex)
        # Combine nibbles into a byte
        bytes.append(high_nibble << 4 | low_nibble)
    return bytes

def dec_to_base64(dec):
    """Converts a single decimal value to base64"""
    if (dec < 0) or (dec > 64):
        return None
    return BASE64_LUT[dec]

def bytes_to_base64(bytes):
    """Converts an array of bytes into a base64 string

             1         2
    123456789012345678901234
    010011010110000101101110 Bit pattern
    000000001111111122222222 8-bit position
    000000111111222222333333 6-bit position
    | 19 || 22 ||  5 || 46 | Index

    Output is padded to always be a multiple of four

    @TODO: Apply padding to base64 string
    """
    base64 = ''
    # 24 is LCM of 6 and 8, therefore process in three 8-bit chunks
    for b0, b1, b2 in zip(*[iter(bytes)] * 3):
        # First 6 bits of b0
        base64 += dec_to_base64((b0 >> 2) & 63)
        # Last 2 bits of b0, first 4 bits of b1
        base64 += dec_to_base64(((b0 << 4) & 48) | ((b1 >> 4) & 15))
        # Last 4 bits of b1, first 2 bits of b2
        base64 += dec_to_base64(((b1 << 2) & 60) | ((b2 >> 6) & 3))
        # Last 6 bits of b2
        base64 += dec_to_base64(b2 & 63);
    if len(bytes) % 3 == 2:
        # Take last two bytes
        b0, b1 = bytes[-2:]
        # First 6 bits of b0
        base64 += dec_to_base64((b0 >> 2) & 63)
        # Last 2 bits of b0, first 4 bits of b1
        base64 += dec_to_base64(((b0 << 4) & 48) | ((b1 >> 4) & 15))
        # Last 4 bits of b1
        base64 += dec_to_base64(((b1 << 2) & 60))
        base64 += '='
    if len(bytes) % 3 == 1:
        # Take last byte
        b = bytes[-1]
        # First 6 bits of b0
        base64 += dec_to_base64((b >> 2) & 63)
        # Last 2 bits of b0
        base64 += dec_to_base64(((b << 4) & 48))
        base64 += '=='
    return base64

def hex_to_base64(hex):
    """Converts a hex value into a base64 string"""
    bytes = hex_to_bytes(hex)
    return bytes_to_base64(bytes)

def main():
    INPUT_HEX = ('49276d206b696c6c696e6720796f757220627261696e206c'
                 '696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print(hex_to_base64(INPUT_HEX))

if __name__ == '__main__':
    main()
