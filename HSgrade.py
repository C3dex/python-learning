# Highschool american grade survey🚌💨
grade = 0
while True:
  try:
    grade = int(input('Enter your Highschool grade: '))
    if grade in (9, 10, 11, 12):
      if grade == 9:
        print('Freshman')
      elif grade == 10:
        print('Sophomore')
      elif grade == 11:
        print('Junior')
      elif grade == 12:
        print('Senior')
      else:
        print('TBD')
      break
  except ValueError:
    print('Invalid input, please try again: ')
      

