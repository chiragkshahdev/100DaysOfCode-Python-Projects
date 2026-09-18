# Day 011 - Blackjack Game

First Capstone Project of 100 Days.

### Rules
- Goal is to get as close to 21 as possible.
- J, Q, K = 10, Ace = 11 or 1
- If you get Ace + 10, it's Blackjack = Auto Win
- If your score > 21, you bust
- Computer must hit until score >= 17

### Concepts Used
- `deal_card()` - random card
- `calculate_score()` - Ace logic (11 to 1 conversion) + Blackjack check
- `compare()` - Win/Lose logic
- While loops + Recursion for replay

### Ace Logic (Main Trick)
```python
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)