# Simple Reflex Agent for Vacuum Cleaner World
def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

# Initial Environment
environment = {
    "A": "Dirty",
    "B": "Clean"
}
location = "A"

print("Initial Environment:", environment)

for i in range(4):
    print("\nStep", i + 1)
    print("Location:", location)
    print("Status:", environment[location])
    action = reflex_agent(location, environment[location])
    print("Action:", action)
    
    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

print("\nFinal Environment:", environment)