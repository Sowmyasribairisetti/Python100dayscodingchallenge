'''The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)
Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the highest bid and prints it.
 Hint 1 
 Hint 2 
Flowchart
If you want to see my flowchart, you can download it here.'''


from art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
