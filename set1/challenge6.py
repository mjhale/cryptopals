#!/usr/bin/env python

"""Break repeating-key XOR

There's a file here (challenge6.txt). It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits.

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to do this.

8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
"""

__author__ = 'michael@michaelhale.org (Michael Hale)'

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

def main():
    FIRST = 'this is a test'
    SECOND = 'wokka wokka!!!'
    print(hamming_distance(FIRST, SECOND))

if __name__ == '__main__':
    main()
