import random
options = ("piedra", "papel", "tijera")


def choose_options():
  user_option = input("piedra, papel o tijera => ")
  comp_option = random.choice(options)
  user_option=user_option.lower()
  if not user_option in options:
    print("opcion invalida")
    return None, None
  print('user option', user_option)
  print('comp_option', comp_option)
  return user_option, comp_option

def check_rules(user_option, comp_option, user_wins, computer_wins):
  if user_option == comp_option:
    print("Empate!")
  elif user_option == "piedra":
    if comp_option == "tijera":
      print("piedra gana a tijera")
      print("user gano!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("comp gano!")
      computer_wins += 1
  elif user_option == "papel":
    if comp_option == "piedra":
      print("papel gana a piedra")
      print("user gano!")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("comp gano!")
      computer_wins += 1
  elif user_option == "tijera":
    if comp_option == "papel":
      print("tijera gana a papel")
      print("user gano!")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("comp gano!")
      computer_wins +=1
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 2:
    print("El ganador es la computadora")
  if user_wins == 2:
    print('el ganador es el usuario')
    return True
  return False

def run_game():
  rounds=1
  user_wins = 0
  computer_wins = 0
  
  while user_wins < 2 and computer_wins < 2:
    print(f'Round {rounds}:')
    user_option, comp_option = choose_options()
  
    if user_option is None or comp_option is None:
        continue  # Skip to the next round if invalid option
  
    user_wins, computer_wins = check_rules(user_option, comp_option, user_wins, computer_wins)
  
    print(f'User wins: {user_wins} | Computer wins: {computer_wins}')
  
    if check_winner(user_wins, computer_wins):
        break

    rounds += 1
run_game()