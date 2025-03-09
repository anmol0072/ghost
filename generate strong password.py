# Import the `random` module to generate random numbers
import random

# Define a function to generate a random password
def generate_password(length):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
  password = "".join(random.choice(characters) for _ in range(length))
  return password

# Define a function to check if a password is strong
def is_strong_password(password):
  if len(password) < 12:
    return False
  if not any(char.isdigit() for char in password):
    return False
  if not any(char.isupper() for char in password):
    return False
  if not any(char.islower() for char in password):
    return False
  return True

# Define a function to get user input and validate it
def get_user_input(prompt):
  while True:
    user_input = get_user_input(prompt)
    if is_strong_password(user_input):
      return user_input
    else:
      print("Password is not strong enough. Try again!")

# Main program
print("Welcome to the Password Generator!")

# Ask the user for their name
name = input("What is your name? ")

# Generate a random password for the user
password = generate_password(12)

# Print out the generated password
print("Here is a strong password for you, " + name + ": " + password)

# Ask the user to enter their own password
user_password = get_user_input("Enter your own password: ")

# Print out a message if the user's password is strong
if is_strong_password(user_password):
  print("Your password is strong!")
else:
  print("Your password is not strong enough. Try again!")

# Create a dictionary to store user data
user_data = {"name": name, "password": password}

# Print out the user data
print("User Data:")
for key, value in user_data.items():
  print(key + ": " + value)