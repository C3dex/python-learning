# Write code below 💖
EW = float(0) #Earth Weight
MeW = float(0) #Mercury Weight
VeW = float(0) #Venus Weight
MaW = float(0) #Mars Weight
JuW = float(0) #Jupiter Weight
SaW = float(0) #Saturn Weight
UrW = float(0) #Uranus Weight
NeW = float(0) #Neptune Weight
EW = float(input('Enter your earth weight in kg: '))
print('Choose one of the following planet destinations(1,7):')
print('1 - Mercury')
print('2 - Venus')
print('3 - Mars')
print('4 - Jupiter')
print('5 - Saturn')
print('6 - Uranus')
print('7 - Neptune')
while True:
  DE = int(input('Your destination: '))
  try:
    if DE in (1, 2, 3, 4, 5, 6, 7):
      if DE == 1:
        MeW = EW*0.38 #Conversion rate 
        print(MW)
      elif DE == 2:
        VeW = EW*0.91 
        print(VW)
      elif DE == 3:
        MaW = EW*0.38 
        print(MaW)
      elif DE == 4:
        JuW = EW*2.53
        print(JuW)
      elif DE == 5:
        SaW = EW*1.07
        print(SaW)
      elif DE == 6:
        UrW = EW*0.89
        print(UrW)
      elif DE == 7:
        NeW = EW*1.14
        print(NeW)
      break
    else:
      print('Invalid planet number')
  except ValueError:
    print('Invalid planet number')
