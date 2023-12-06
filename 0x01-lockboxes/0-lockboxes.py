#!/usr/bin/python3
""" LockBoxes Module"""


def canUnlockAll(boxes):
    """ Function to track keys """
    unlocked_boxes = set()

    # Start with the first box, which is already unlocked
    unlocked_boxes.add(0)

    # Create a stack to keep track of the boxes to explore
    stack = [0]

    # While there are boxes to explore
    while stack:
        # Pop a box from the stack
        current_box = stack.pop()

        # Check the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and it's not already unlocked
            if 0 <= key < len(boxes) and key not in unlocked_boxes:
                # Unlock the new box
                unlocked_boxes.add(key)
                # Add the new box to the stack for further exploration
                stack.append(key)

    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)
