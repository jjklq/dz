import random


random_numbers = [random.randint(1, 100) for _ in range(26)]


for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write(str(random_numbers[i]))

with open("summary.txt", "w") as summary_file:
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        summary_file.write(f"{letter}.txt: {random_numbers[i]}\n")

print("Файлы созданы и данные записаны.")



with open("first_file.txt", "w") as file:
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    file.write(content)


with open("second_file.txt", "w") as second_file:
    with open("first_file.txt", "r") as first_file:
        content = first_file.read().upper()
        second_file.write(content)

import random
import csv


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]


game_results = []
for _ in range(100):
    for player in players:
        score = random.randint(0, 1000)
        game_results.append((player, score))


with open("game_scores.csv", "w", newline="") as csvfile:
    fieldnames = ["Player name", "Score"]
    writer = csv.writer(csvfile)
    
    
    writer.writerow(fieldnames)
    
   
    writer.writerows(game_results)
