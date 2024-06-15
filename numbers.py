""" 1.Write a function that takes two arguments, 145 and 'o', and
uses the `format` function to return a formatted string. Print the
result. Try to identify the representation used."""

def format_string(num, char):
  formatted_string = "{num:{char}}".format(num=num, char=char)
  return formatted_string

print(format_string(145, 'o'))  # Output: 221

# Explanation:
# - The 'o' format specifier is used for octal representation (base-8).
# - The formatted string "221" represents the octal equivalent of the number 145.

"""2. In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π
r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
Water per Square Meter"""

pi = 3.14
radius = 84
pond_area = pi * radius**2

water_per_meter = 1.4
total_water = int(pond_area * water_per_meter)  # Convert to integer for whole liters

# Print the pond area and total water without decimals
print("Pond area:", pond_area, "square meters")  # Show area with two decimals
print("Total water in the pond:", total_water, "liters")


"""3. If you cross a 490meter long street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time"""

distance = 490
time_in_seconds = 7 * 60  # Convert minutes to seconds
speed = int(distance / time_in_seconds)  # Convert to integer for meters per second

print("Speed:", speed, "meters per second") # Qutput-> 1
