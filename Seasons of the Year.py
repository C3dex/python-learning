# 🗓️ Seasons of the Year
month = 0
while True:
  month = int(input('Please enter the month in integer form: '))
  try:
    if month in (1,2,3,4,5,6,7,8,9,10,11,12):
      if month in (1,2,3):
        print('Winter 🌨️')
      elif month in (4,5,6):
        print('Spring 🌱')
      elif month in (7,8,9):
        print('Summer 🌻')
      elif month in (10,11,12):
        print('Autumn 🍂')
      break
    else:
      print('Invalid')
      print('Please try inputting a month in integer form: ')
  except:
    print('Invalid input, try again. ')
