""" 1.Create a variable named pi and store the value 22/7 in it, then check its data type"""
pi = 22/7

print("The value of pi is: ",pi) #print the value of pi
print("The data type of pi is:", type(pi))  # Check the data type

# Output:
# The value of pi is: 3.142857142857143
# The data type of pi is: <class 'float'>

""" 2. Create a variable called 'for' and assign it a value 4.
  See what happens and explain the reason."""


#for = 4   This will raise a SyntaxError
# what happen-> This will give SyntaxError.
# Why->'for' is a reserved keyword used for loop statements. Using it as a variable name will cause a SyntaxError.

""" 3. Calculate Simple Interest """
principal = 10000  # Desired principal amount
rate = 5  # Desired interest rate
time = 3  # Desired time period (years)

simple_interest = principal * rate * time / 100
print("The simple interest for", principal,"at", rate, "% for", time, "years is:", simple_interest)

# Output (assuming principal=10000, rate=5, time=3):
# The simple interest for 10000 at 5% for 3 years is: 1500.0
