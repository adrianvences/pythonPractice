import random

computersHandInt = random.randint(1,3)
hand =  {
  1: "paper",
  2: "scissors",
  3: "rock"
}

computersHand = hand.get(computersHandInt)


def rockPaperScissor(input):
  if input == "rock" and computersHand == "paper":
    print("You lose!")
  if input == "paper" and computersHand == "scissors":
    print ("you lose!")
  if input == "scissors" and computersHand == "rock":
    print ("you lose!")
  if input == "scissors" and computersHand == "paper":
    print ("you win!")
  if input == "rock" and computersHand == "scissors":
    print ("you win!")
  if input == "paper" and computersHand == "rock":
    print ("you win!")
  if input == computersHand :
    print("its a tie")

print(computersHand)
print(rockPaperScissor("rock"))