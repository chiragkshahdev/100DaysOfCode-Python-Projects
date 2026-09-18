# Day 009 - Blind Auction Project

This is Day 9 of 100 Days of Python Bootcamp.

### Concept Covered
- Python Dictionaries
- Nesting & Looping through Dictionary
- Functions with return

### How it Works
1. Program asks for bidder name and bid amount.
2. Stores data in Dictionary: '{"Mubeen": 150, "Aman": 200}'
3. Asks "Any other bidders?"
4. If 'Yes' -> Screen clears (so next bidder can't see previous bid) - This is the "Blind" Part.
5. If 'No' -> Loop through Dictionary and find highest bid.

### Key Logic
'''python
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder