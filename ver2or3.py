#!/usr/bin/env python

"""
Answers the question, "Should I use Python version 2 or 3 for my project?"
Sean Jain Ellis <sellis@bandarji.com> @bandarji
"""

try:
    import random
    import sys
    import time
except ImportError as e_msg:
    raise SystemExit('Error: ' + str(e_msg))

def random_message():
    """
    Returns a random message, to "show" the computer figuring out how to answer
    the query
    """
    return random.choice([
        'Thinking',
        'Considering',
        'Weighing options',
        'Consulting with a religious leader',
        'Rolling some dice',
        'Rolling the bones',
        'Shaking Magic Eight Ball',
        'Phoning a friend',
        'Reading daily horoscope',
        'Basing decision on your social media interests'
    ])

def main():
    """
    Main function
    """
    message = random_message() + '...'
    sys.stdout.write(message)
    sys.stdout.flush()
    time.sleep(2)
    message = 'done\nUse Python v3 unless forced to use v2'
    if sys.version_info.major >= 3:
        print(message)
    elif sys.version_info.major < 3:
        raise SystemExit(message)
    return 0

if __name__ == '__main__':
    sys.exit(main())
