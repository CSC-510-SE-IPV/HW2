"""
This module contains a function for shuffling an array by replacing
each element with a randomly generated number using the `shuf` command.
"""

import subprocess

def random_array(arr):
    """
    Shuffle an array by replacing each element with a random number.

    Args:
        arr (list): List of integers.

    Returns:
        list: The shuffled list with random numbers.
    """
    for i, _ in enumerate(arr):
        # Using `check=True` to raise an exception if the command fails
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
