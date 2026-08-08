machine_id = "M003"
maintenance_cost = 12000
production_loss_if_stopped = 20000
potential_failure_loss = 80000
shift_production_cost = 5000
option1_cost = potential_failure_loss
option2_cost = maintenance_cost + production_loss_if_stopped
option3_cost = maintenance_cost + shift_production_cost
print("\n===== CogniFact AI Decision Engine =====")
print(f"Machine: {machine_id}")

print("\nPossible Actions:")

print("\nOption 1: Continue Operating")
print(f"Estimated Impact: ₹{option1_cost:,}")

print("\nOption 2: Stop + Maintenance")
print(f"Maintenance Cost: ₹{maintenance_cost:,}")
print(f"Production Loss: ₹{production_loss_if_stopped:,}")
print(f"Total Impact: ₹{option2_cost:,}")

print("\nOption 3: Maintenance + Shift Production")
print(f"Maintenance Cost: ₹{maintenance_cost:,}")
print(f"Production Shift Cost: ₹{shift_production_cost:,}")
print(f"Total Impact: ₹{option3_cost:,}")
options = {
    "Continue Operating": option1_cost,
    "Stop + Maintenance": option2_cost,
    "Maintenance + Shift Production": option3_cost
}

best_action = min(options, key=options.get)
best_cost = options[best_action]


print("\n")
print("RECOMMENDED ACTION")
print(f"Action: {best_action}")
print(f"Estimated Impact: ₹{best_cost:,}")