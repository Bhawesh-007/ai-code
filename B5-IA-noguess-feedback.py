low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    guess = (low + high) // 2
    print(f"My guess is: {guess}")
    feedback = input("Enter Higher, Lower, or Correct: ").lower().strip()
    
    if feedback == "correct":
        print(f"I guessed your number: {guess}")
        break
    elif feedback == "higher":
        low = guess + 1
    elif feedback == "lower":
        high = guess - 1
    else:
        print("Invalid input. Please enter Higher, Lower, or Correct.")