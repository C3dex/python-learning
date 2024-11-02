# The storing hat quiz 
G = 0 #🦁 Gryffindor
R = 0 #🦅 Ravenclaw
H = 0 #🦡 Hufflepuff
S = 0 #🐍 Slytherin
#Q1 Loop:
while True:
  print('Q1) Do you like Dawn or Dusk?');
  print('    1) Dawn');
  print('    2) Dusk');
  try:
    Q1 = int(input());
    if Q1 == 1:
      G += 1
      R += 1
      break 
    elif Q1 == 2:
      H += 1
      S += 1
      break
    else:
      print('Wrong input, Please enter 1 or 2.')
  except ValueError:
    print('Invalid input, Please enter a number (1 or 2).')
#Q2 Loop
while True:
  print('Q2) When I’m dead, I want people to remember me as:');
  print('    1) The Good');
  print('    2) The Great');
  print('    3) The Wise');
  print('    4) The Bold');
  try:
    Q2 = int(input());
    if Q2 == 1:
      H += 2
      break
    elif Q2 == 2:
      S += 2
      break
    elif Q2 == 3:
      R += 2
      break
    elif Q2 == 4:
      G += 2
      break
    else:
      print('Wrong input, please choose (1,4)')
  except ValueError:
    print('Invalid input, please choose (1,4)')
#Q3 Loop
while True:
  print('Q3) Which kind of instrument most pleases your ear?');
  print('    1) The violin');
  print('    2) The trumpet');
  print('    3) The piano');
  print('    4) The drum');
  try:
    Q3 = int(input());
    if Q3 == 1:
      S += 4
      break
    elif Q3 == 2:
      H += 4
      break
    elif Q3 == 3:
      R += 4
      break
    elif Q3 == 4:
      G += 4
      break
    else:
      print('Wrong input, please choose (1,4)')
  except ValueError:
    print('Invalid input, please choose (1,4)')
#Result Conditions
if G > R and G > H and G > S:  
    print('Congratulations! You are a 🦁 Gryffindor')  
elif R > G and R > H and R > S:  
    print('Congratulations! You are a 🦅 Ravenclaw')  
elif H > G and H > R and H > S:  
    print('Congratulations! You are a 🦡 Hufflepuff')  
elif S > G and S > R and S > H:  
    print('Congratulations! You are a 🐍 Slytherin')
