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
    remaining_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if remaining_bytes > 0:
            # Check if the current byte starts with '10'
            if (byte & 0b11000000) == 0b10000000:
                remaining_bytes -= 1
            else:
                return False
        else:
            # Checks number of leading '1' bits to determine the len of char
            if (byte & 0b10000000) == 0:
                # 1-byte character
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                # 2-byte character
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                # 3-byte character
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                # 4-byte character
                remaining_bytes = 3
            else:
                return False

    # Check if all characters have been fully processed
    return remaining_bytes == 0
