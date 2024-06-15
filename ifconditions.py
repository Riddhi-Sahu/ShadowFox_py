""" 1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
"""
def calculate_bmi(weight, height):
  bmi = weight / (height**2)
  if bmi >= 30:
    return "Obesity"
  elif bmi >= 25:
    return "Overweight"
  elif bmi >= 18.5:
    return "Normal"
  else:
    return "Underweight"

# Get user input for height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI and determine category
bmi_category = calculate_bmi(weight, height)

# Print the result
print("Your BMI category is:", bmi_category)


""" 2. Write a program to determine which country a city belongs to.
Given list of cities per country:
Australia = ["Sydney","Melbourne","Brisbane","Perth"]

UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"]

Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
"""

countries = {
  "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Get user input for city name
city = input("Enter a city name: ")

# Find the country based on the city (if it exists)
country = None
for country_name, cities in countries.items():
  if city.lower() in [city.lower() for city in cities]:  # Check case-insensitively
    country = country_name
    break

# Print the result
if country:
  print(city, "is in", country)
else:
  print("City", city, "not found in the listed countries.")


"""3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"

Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
"""

countries = {
  "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def get_city_country(city, countries):
  """Finds the country a city belongs to, handling case-insensitive search and returning None if not found.

  Args:
      city: The city name to search for (string).
      countries: The dictionary mapping countries to their city lists.

  Returns:
      The country name (string) if the city is found, otherwise None.
  """
  for country_name, cities in countries.items():
    if city.lower() in [city.lower() for city in cities]:  # Check case-insensitively
      return country_name
  return None

# Get user input for both cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Find the countries for each city (handle potential None if not found)
country1 = get_city_country(city1, countries)
country2 = get_city_country(city2, countries)

# Print the result based on the countries found
if country1 and country2 == country1:
  print("Both cities are in", country1)
elif country1 and country2:
  print("They don't belong to the same country")
else:
  # Handle cases where at least one city is not found in the list
  if not country1:
    print("City", city1, "not found in the listed countries.")
  if not country2 and country1:
    print("City", city2, "not found in the listed countries.")
