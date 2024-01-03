
def highestBid(biddingRecord):
  highestBid  = 0 
  winner = ''
  for bidder in biddingRecord:
    bidAmount = biddingRecord[bidder]
    if bidAmount > highestBid:
      highestBid = bidAmount
      winner = bidder
  print(f'the winner is {winner} with a bid of ${highestBid}')




def secret_auction():
  flag = False
  bidders = {}
  while flag == False:
    
    name = input('what is your name? : ')
    bid = int(input('what is your bid? : '))

    bidders[name] = bid
    print(bidders)
    

    proceed = input('is there someone else bidding? Type "yes" or "no" : ')

    if proceed == 'yes':
      flag = False 
    else:
      flag = True
      highestBid(bidders)
    

secret_auction()