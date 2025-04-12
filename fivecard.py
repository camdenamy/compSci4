import itertools
from collections import Counter

# Ranks and suits
RANKS = "23456789TJQKA"
SUITS = "CDHS"

# Build a deck
deck = [r + s for r in RANKS for s in SUITS]

def rank_counts(hand):
    return Counter(card[0] for card in hand)

def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_straight(ranks):
    i_ranks = [RANKS.index(r) for r in ranks]
    i_ranks.sort()
    return i_ranks == list(range(i_ranks[0], i_ranks[0] + 5)) or i_ranks == [0, 1, 2, 3, 12]  # Handle A-2-3-4-5

def classify(hand):
    ranks = sorted([card[0] for card in hand], key=RANKS.index)
    counts = Counter(ranks).values()
    flush = is_flush(hand)
    straight = is_straight(ranks)
    
    if flush and straight and 'A' in ranks and 'T' in ranks:
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if 4 in counts:
        return "Four of a Kind"
    if 3 in counts and 2 in counts:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if 3 in counts:
        return "Three of a Kind"
    if list(counts).count(2) == 2:
        return "Two Pair"
    if 2 in counts:
        return "One Pair"
    return "High Card"

# Tally results
hand_counts = Counter()
total_hands = 0

for hand in itertools.combinations(deck, 5):
    category = classify(hand)
    hand_counts[category] += 1
    total_hands += 1

# Display probabilities
print("Poker Hand Probabilities:\n")
for hand in [
    "Royal Flush", "Straight Flush", "Four of a Kind", "Full House",
    "Flush", "Straight", "Three of a Kind", "Two Pair", "One Pair", "High Card"
]:
    count = hand_counts[hand]
    probability = count / total_hands
    print(f"{hand:20}: {count:10} ({probability:.8%})")
