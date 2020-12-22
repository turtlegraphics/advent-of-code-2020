#
# Advent of Code 2020
# Bryan Clair
#
# Day 22
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

totgames = 0
totrounds = 0
maxdepth = 0

def show_progress():
    if args.verbose > 1:
        print totgames,'games with',
        print totrounds,'rounds.',
        print 'Maximum recursion depth of',maxdepth

def subdecks(c0,c1,decks):
    return [decks[0][1:c0+1],decks[1][1:c1+1]]

def game(decks,depth=1):
    global totgames, totrounds, maxdepth
    totgames += 1
    maxdepth = max(depth,maxdepth)

    if totgames % 2000 == 0:
        show_progress()

    seen = {}

    while decks[0] and decks[1]:
        totrounds += 1

        # check for repeated round
        h = str(decks)
        if h in seen:
            winner = 0  # player 1 wins
            break
        seen[h] = True

        # round starts
        # deal top cards
        c0,c1 = decks[0][0],decks[1][0]

        if part == 2 and len(decks[0]) > c0 and len(decks[1]) > c1:
            # recurse
            winner = game(subdecks(c0,c1,decks),depth+1)
        else:
            winner = 0 if c0 > c1 else 1

        decks[0] = decks[0][1:]
        decks[1] = decks[1][1:]

        if winner == 0:
            decks[0].append(c0)
            decks[0].append(c1)
        else:
            decks[1].append(c1)
            decks[1].append(c0)

    if decks[0]:
        return 0
    else:
        return 1

def score(deck):
    m = len(deck)
    s = 0
    for c in deck:
        s += m * c
        m -= 1
    return s

player_str = open(args.file).read().split('\n\n')

for part in [1,2]:
    decks = []
    for ps in player_str:
        deck = ps.strip().split('\n')
        decks.append([int(x) for x in deck[1:]])

    winner = game(decks)
    show_progress()
    print 'part %d:' % part,
    print score(decks[winner])
