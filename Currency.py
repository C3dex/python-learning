# Currency.py
a = int(input('What do you have left in pesos? '))
b = int(input('What do you have left in soles? '))
c = int(input('What do you have left in reais? '))
PinUSD = (a*0.00023)
SinUSD = (b*0.265)
RinUSD = (c*0.1727)
T = (PinUSD+SinUSD+RinUSD)
print(T)
