#!/usr/bin/env python

import sys
from mastermindlib import generate_code,check_guess

level = { 'easy': 1, 'medium': 2, 'hard': 3 }

code = generate_code( level['easy'] )

rounds = 1
print "[Round %d]: " % rounds,
guess = sys.stdin.readline().rstrip('\n').split(' ')
results = check_guess(code,guess)

while (4,4) != results:
    print "\tcorrect location %d, total %d" % results
    rounds += 1

    print "[Round %d]: " % rounds,
    guess = sys.stdin.readline().rstrip('\n').split(' ')
    results = check_guess(code,guess)

print "\tYou Win!"
