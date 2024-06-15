justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate number of members
num_members = len(justice_league)
print("Number of members:", num_members)  # Output: Number of members: 6

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)  # Output: ... (including Batgirl and Nightwing)

# 3. Move Wonder Woman to the beginning
wonder_woman_index = justice_league.index("Wonder Woman")
justice_league.insert(0, justice_league.pop(wonder_woman_index))
print("Wonder Woman as leader:", justice_league)  

# 4. Separate Aquaman and Flash (using Green Lantern)
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
green_lantern_index = justice_league.index("Green Lantern")

justice_league.insert(flash_index + 1, justice_league.pop(green_lantern_index))
print("Aquaman and Flash separated:", justice_league)  

# 5. Replace team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)  

# 6. Sort alphabetically and print leader
justice_league.sort()
print("Sorted Justice League:", justice_league)  # Output: Sorted Justice League: ... (alphabetically sorted)

# BONUS: Predicting the new leader (assuming sorting is case-sensitive)
print("New leader (predicted):", justice_league[0])  # Output: New leader (predicted): Cyborg
