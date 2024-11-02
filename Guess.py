# Write code below 💖
guess = 0
tries = 0
int(input('Guess the number: '))
while guess !=6:
  guess = int(input("Guess the number again! "))
  tries += 1
  if tries == 5:
    print('You have reached the maximum amount of tries...')
    break
if guess == 6:
  print("You got it!")
