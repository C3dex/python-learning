# the_cyclone🎢.py
Qa = int(input('What is your height in cm? ').strip())
Qb = int(input('How many credits do you have? ').strip())
if Qa>=137 and Qb >= 10:
  print('Enjoy the ride!')
elif Qb>=10 and Qa<137:
  print("You are not tall enough to ride.")
elif Qa>=137 and Qb<10:
  print('You dont have enough credits')
else:
  print('You have not met either requirement')
