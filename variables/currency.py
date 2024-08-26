COP_USD_RATE = 0.0002
PEN_USR_RATE = 0.2674
BRL_USD_RATE = 0.1944

cop = input("What do you have left in pesos? ")
pen = input("What do you have left in soles? ")
brl = input("What do you have left in reais? ")
print(
    f"Total in USD: {float(cop) * COP_USD_RATE + float(pen) * PEN_USR_RATE + float(brl) * BRL_USD_RATE}"
)
