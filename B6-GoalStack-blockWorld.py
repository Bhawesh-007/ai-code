# Goal Stack Planning Example for Blocks World
initial_state = {
    "ONTABLE(A)",
    "ONTABLE(B)",
    "CLEAR(A)",
    "CLEAR(B)",
    "ARMEMPTY"
}

goal_state = ["ON(A,B)"]
plan = []

print("Initial State:")
print(initial_state)

if "ON(A,B)" not in initial_state:
    if "ONTABLE(A)" in initial_state and "CLEAR(A)" in initial_state and "ARMEMPTY" in initial_state:
        plan.append("PICKUP(A)")
        initial_state.remove("ONTABLE(A)")
        initial_state.remove("CLEAR(A)")
        initial_state.remove("ARMEMPTY")
        initial_state.add("HOLDING(A)")

    if "HOLDING(A)" in initial_state and "CLEAR(B)" in initial_state:
        plan.append("STACK(A,B)")
        initial_state.remove("HOLDING(A)")
        initial_state.remove("CLEAR(B)")
        initial_state.add("ON(A,B)")
        initial_state.add("CLEAR(A)")
        initial_state.add("ARMEMPTY")

print("\nPlan:")
for step in plan:
    print(step)

print("\nFinal State:")
print(initial_state)