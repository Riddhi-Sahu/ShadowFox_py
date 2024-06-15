"""1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row"""

import random

# Number of times to roll the die
num_rolls = 20

# Count for each roll value and consecutive sixes
sixes_count = 0
ones_count = 0
consecutive_sixes = 0

for _ in range(num_rolls):
  # Roll the die (1-6)
  roll = random.randint(1, 6)

  # Count rolls of 1 and 6
  if roll == 6:
    sixes_count += 1
    consecutive_sixes += 1
  elif roll == 1:
    ones_count += 1
    consecutive_sixes = 0  # Reset consecutive sixes if not consecutive
  else:
    consecutive_sixes = 0  # Reset consecutive sixes if not consecutive

# Print statistics
print("Number of times you rolled a 6: ", sixes_count)
print("Number of times you rolled a 1: ", ones_count)
print("Number of times you rolled two 6s in a row: ", consecutive_sixes)


"""2. Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of
jumping jacks."
For example, if you did only 30 jumping jacks and answered "yes," the program
will break and print, "You completed a total of 30 jumping jacks."
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you complete all 100 jumping jacks, it should print, "Congratulations! You
completed the workout," and stop the program"""

total_jumping_jacks = 0
remaining_jumping_jacks = 100

while remaining_jumping_jacks > 0:
  # Perform 10 jumping jacks
  total_jumping_jacks += 10
  remaining_jumping_jacks -= 10

  print("You completed", total_jumping_jacks, "jumping jacks.", remaining_jumping_jacks, "remaining.")
  is_tired = input("Are you tired? (yes/no) ").lower()  # Convert to lowercase

  if is_tired in ("yes", "y"):
    skip_remaining = input("Do you want to skip the remaining sets? (yes/no) ").lower()
    if skip_remaining in ("yes", "y"):
      break  # Exit the loop if user wants to skip
    else:
      continue  # Continue if user wants to keep going

# Print results based on completion status
if total_jumping_jacks == 100:
  print("Congratulations! You completed the workout.")
else:
  print("You completed a total of", total_jumping_jacks, "jumping jacks.")
