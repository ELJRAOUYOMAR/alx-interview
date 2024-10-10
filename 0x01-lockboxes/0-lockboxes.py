#!/usr/bin/python3
""" docs """


def canUnlockAll(boxes):
    """
    -Start with the first box (index 0) already unlocked.
    -Use the keys inside the opened boxes to 
    unlock other boxes.
    -Keep track of the unlocked boxes in a set
    to avoid reprocessing the same box multiple times.
    -If all boxes are unlocked at the end, 
    return True; otherwise, return False.
    """
    unlocked = {0}
    keys = [0]
    
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)

