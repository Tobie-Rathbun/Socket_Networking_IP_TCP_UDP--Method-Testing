import requests

# Set the base URL of the server
BASE_URL = "https://tobie.games"

# Start a new game by requesting a new random number from the server
response = requests.get(BASE_URL)
number = response.json()["number"]

# Keep guessing until the correct number is guessed
while True:
    # Get a guess from the user
    guess = int(input("Enter a guess: "))
    # Send the guess to the server
    data = {"guess": guess}
    response = requests.post(BASE_URL, json=data)
    result = response.json()["result"]
    # Print the result from the server
    if result == "Correct":
        print("You guessed the correct number!")
        break
    else:
        print(result)

