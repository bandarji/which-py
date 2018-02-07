#!/usr/bin/env python

try:
    import random
    import sys
    import time
except ImportError as e_msg:
    raise SystemExit('Error: ' + str(e_msg))

def random_message():
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
