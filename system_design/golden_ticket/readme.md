# Golden Ticket Chocolates Candy Shop
## Step 1: Exchange money for chocolate
There is a candy shop that sells chocolate so fancy, they are sold in golden wrappers.

Write a function that calculates how many chocolates you are able to eat, based on a given price per choclate and how much money you have.

#1: $15, $3/chocolate = 5 chocolates
#2: $10, $3/chocolate = 3 chocolates

## Step 2: Add wrapper exchange for more chocolates
Because of fancy gold wrappers, the store now takes empty wrappers in exchange for more chocolate. But customers eat the chocolates in the store and exchange immediately instead.

Given a number of wrappers per chocolate, update the function to include chocolates for exchange wrappers.

#1 $20, $3/chocolate, 5 wrappers/chocolate
// Buy 6 initially, exchange 5 -> 1  = 6 + 1
= 7

#2 $16, $2/chocolate, 2 wrappers/chocolate
// Buy 8 initially, exchange 8 -> 4, exchange 2 -> 1 = 8 + 4 + 2 + 1
= 15

#4 $15, $1/chocolate, 3 wrappers/chocolate
// Buy 15 initially, exchange 15 -> 5, exchange 5 -> 1 (2 remain), exchange 2 + 1 ->  = 15 + 5 + 1 + 1
= 22

## Part 3: Test Cases
What test should be added to ensure correctness? Candidate should come up with some of these on their own.
- not enough money (money < price)
- wrapper cost < 2 (x == 1 is infinite loop)
- Minimum wrapper exchange rate
- $0/chocolate
- divide by 0 (0 wrapper / chocolate)
- no wrapper exchange ($2, $1/chocolate, 5 wrappers/chocolate)
- negative or zero price
- no money
- not enough wrappers
- infinite money

## Internal Questions
### Part 1
- Did they ask for price?
- Did they hardcode price, or have a param?
- Did they add a test?

### Part 2
- Did they encode wrapper exchange rate?
- Loop or recursion? Did they explain why?
- Are they guarding against bad values? Justifying their reasons?