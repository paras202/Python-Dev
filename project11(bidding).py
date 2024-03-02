import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
bidding = False
def highest_bidding(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding:
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or No.\n").lower()
    if should_continue == "no":
        bidding = True
        highest_bidding(bids)
    elif should_continue == "yes":
        os.system('cls')
