# Convert hex to base64
#
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

from base64 import b64encode
from binascii import unhexlify

HEX_STRING = ("49276d206b696c6c696e6720796f757220627261696e206c"
              "696b65206120706f69736f6e6f7573206d757368726f6f6d")

hex_array = [''.join(c) for c in zip(HEX_STRING[0::2], HEX_STRING[1::2])]

decimal_array = [int(c, 16) for c in hex_array]

character_array = [chr(int(c, 16)) for c in hex_array]

byte_array = [unhexlify(c) for c in hex_array]

base64_array = b64encode(b''.join(byte_array))

print("hex:     ", hex_array)
print("decimal: ", decimal_array)
print("chr:     ", character_array)
print("bytes:   ", byte_array)
print("b64:     ", base64_array)
