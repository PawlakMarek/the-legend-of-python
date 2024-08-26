"""
Instructions:
We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
- 🇨🇴 Colombian pesos
- 🇵🇪 Peruvian soles
- 🇧🇷 Brazilian reais

Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!

The output of the program should look like this:
```
What do you have left in pesos? 5600
What do you have left in soles? 105
What do you have left in reais? 280
413.0
```

Cha-ching! Now you have the total in USD. 💰

Once you are done, post a screenshot of your code to Twitter by clicking the icon below, and then head over to #CodedexCurrency and review another learner's work. Be supportive of your fellow learners! :)
"""

COP_USD_RATE = 0.0002
PEN_USR_RATE = 0.2674
BRL_USD_RATE = 0.1944

cop = input("What do you have left in pesos? ")
pen = input("What do you have left in soles? ")
brl = input("What do you have left in reais? ")
print(
    f"Total in USD: {float(cop) * COP_USD_RATE + float(pen) * PEN_USR_RATE + float(brl) * BRL_USD_RATE}"
)
