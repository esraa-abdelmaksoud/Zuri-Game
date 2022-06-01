import random

opts = ["R", "P", "S"]

def play(opts):

    while True:
        player = input("Please choose any of [R/P/S].\n").upper()

        try:
            if player in opts:
                break
        except ValueError:
            ("Please choose a valid option [R/P/S]\n")

    cpu = random.choice(opts)

    play_dict = {"R":"Rock", "P":"Paper", "S":"Scissors"}

    print("Player ({}) : CPU ({})".format(play_dict[player], play_dict[cpu]))

    return player, cpu


player, cpu = play(opts)

while player == cpu:
    print("It's a tie!")
    player, cpu = play(opts)

if (player == "R" and cpu == "S") or (
    player == "P" and cpu == "R") or (
    player == "S" and cpu == "P"):
    print("Player Wins!")

else:
    print("CPU Wins!")