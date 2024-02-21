from art import logo
from replit import clear

print(logo)
Bidders = {}
OtherPlayer = True
while OtherPlayer:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  Bidders[name] = bid
  MorePlayers = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if MorePlayers == "no":
    OtherPlayer = False
  clear()
#HINT: You can call clear() to clear the output in the console.
BidderName = ""
HighestBider = 0
for Person in Bidders:
  if Bidders[Person] > HighestBider:
        HighestBider = Bidders[Person]
        BidderName = Person
print(f"The winner is {BidderName} with a bid of ${HighestBider}")