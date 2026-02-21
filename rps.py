import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# User choice
choice = int(input("Escolha 0 para PEDRA, 1 para PAPEL e 2 para TESOURA: "))
if choice < 0 or choice > 2:
    print("Você colocou um valor invalido")


else:
    print(game[choice])

    # Random choice
    bot = random.randint(0, 2)
    print(game[bot])

    # Conditions
    if (choice == 0 and bot == 0) or (choice == 1 and bot == 1) or (choice == 2 and bot == 2):
        print("Empate")
    if (choice == 0 and bot == 1) or (choice == 1 and bot == 2) or (choice == 2 and bot == 0):
        print("VOCÊ PERDEU!")
    if (choice == 0 and bot == 2) or (choice == 1 and bot == 0) or (choice == 2 and bot == 1):
        print("VOCÊ VENCEU!")
