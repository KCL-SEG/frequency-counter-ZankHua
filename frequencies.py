"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    frequencies = {}
    for item in items:
        # Convert the item to a string
        key = str(item)
        # Increment the count for this key in the dictionary
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
    return frequencies
