print("Welcome to the secret auction program")
auction={}
otherBiders=True

while otherBiders:
    name = input("What is your name ?: ")
    bid = int(input("What is your bid ?: "))
    auction[name]=bid
    answer = input("Other bidder ? (Yes/No)")
    if answer!="Yes":
        otherBiders=False
maxBid=0
winner=""
for bidder in auction:
    bid = auction[bidder]
    if maxBid<bid:
        maxBid=bid
        winner=bidder
print(f"{winner} win the auction with a bid at {maxBid}")
