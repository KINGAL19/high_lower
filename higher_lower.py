
from art import logo
from art import vs
from game_data import data
import random 
from replit import clear
def trans(dict):
  list_trans = []
  list_trans.append(dict["name"])
  list_trans.append(dict["follower_count"])
  list_trans.append(dict["description"])
  list_trans.append(dict["country"])
  return list_trans

def ans(a, b):
  if a[1] > b[1]:
    return "a"
  elif a[1] < b[1]:
    return "b"

print(logo)

a_b = []
score = 0
for _ in range(2):
  a_b.append(random.choice(data))

is_game_over = False
while not is_game_over:
  a = trans(a_b[0])
  b = trans(a_b[1])
  print(f"Compare A:{a[0]}, a {a[2]}, from {a[3]}, pssst{a[1]}.")
  print(vs)
  print(f"Compare B:{b[0]}, a {b[2]}, from {b[3]}, pssst{b[1]}.")
  guess = input("Who has more followers? Type 'A' or 'B':").lower()
  answer = ans(a, b)
  clear()
  if guess == answer:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    is_game_over = True
    print(f"Sorry, that's wrong. Final score: {score}")
  a_b.remove(a_b[0])
  a_b.append(random.choice(data))