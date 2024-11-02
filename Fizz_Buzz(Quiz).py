# Fizz Buzz is a children's word game that teaches division,
# It's also a classic technical interview question at countless companies. 🐝
#fizz_buzz.py
for i in range(1, 101, +1):
  if i % 3 != 0 and i % 5 != 0:
    print(i)
  elif i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")

