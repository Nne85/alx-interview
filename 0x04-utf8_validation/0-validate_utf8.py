#!/usr/bin/python3
"""This module contains a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, False otherwise.
    """

    num_bytes_remaining = 0
    index = 0

    while index < len(data):
        first_byte = data[index]

        if num_bytes_remaining == 0:
            if (first_byte >> 7) == 0:
                num_bytes_remaining = 0
            elif (first_byte >> 5) == 0b110:
                num_bytes_remaining = 1
            elif (first_byte >> 4) == 0b1110:
                num_bytes_remaining = 2
            elif (first_byte >> 3) == 0b11110:
                num_bytes_remaining = 3
            else:
                return False
        else:
            if (first_byte >> 6) != 0b10:
                return False
            num_bytes_remaining -= 1

        index += 1
    return num_bytes_remaining == 0
