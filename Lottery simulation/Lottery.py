import random
import matplotlib.pyplot as plt 
account = 0

x = []
y = []
for i in range(7):
    x.append(i+1)
    # Take user's bet
    print("No of Bet: ",i+1)
    bet = int(input("Your bet from 1 to 10: "))
    # Generate lucky draw number
    lucky_draw = random.randint(1, 10)
    # Show the lucky number (for checking)
    print("Bet: ", bet)
    print("Lucky draw:", lucky_draw)
    # Start account balance

    # Check win/loss condition
    if bet == lucky_draw:
        account = account + 900 - 100   # win: +900 but subtract 100 for bet
    else:
        account = account - 100   
    y.append(account)    # lose: subtract bet
    # Show final account balance
    print("Your account balance:", account)
plt.plot(x, y)
plt.xlabel('Days')
plt.ylabel('Account Balance')
plt.show()