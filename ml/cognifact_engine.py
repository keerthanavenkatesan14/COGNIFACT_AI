import pandas as pd
import joblib
machine_data = pd.read_csv("data/cognifact_machine_dataset.csv")
maintenance_data = pd.read_csv("data/maintenance_data.csv")
production_data = pd.read_csv("data/production_data.csv")
factory_data = machine_data.merge(
    maintenance_data,
    on="Machine_ID",
    how="left"
)

factory_data = factory_data.merge(
    production_data,
    on="Machine_ID",
    how="left"
)
model = joblib.load("ml/ml_model.pkl")
machine_id = "M003"

machine = factory_data[
    factory_data["Machine_ID"] == machine_id
].iloc[0]
features = pd.DataFrame([{
    "Temperature": machine["Temperature"],
    "Vibration": machine["Vibration"],
    "Power_Consumption": machine["Power_Consumption"],
    "Operating_Hours": machine["Operating_Hours"],
    "Maintenance_Days": machine["Maintenance_Days"]
}])
prediction = model.predict(features)[0]

probability = model.predict_proba(features)[0][1]

failure_probability = probability * 100
if failure_probability >= 70:
    risk_level = "HIGH "

elif failure_probability >= 30:
    risk_level = "MEDIUM "

else:
    risk_level = "LOW "
feature_names = [
    "Temperature",
    "Vibration",
    "Power_Consumption",
    "Operating_Hours",
    "Maintenance_Days"
]

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

maintenance_cost = machine["Maintenance_Cost"]

production_value_per_hour = machine[
    "Production_Value_Per_Hour"
]

production_loss = production_value_per_hour * 4

failure_loss = production_value_per_hour * 10
shift_cost = production_value_per_hour * 2
continue_cost = failure_loss
maintenance_only_cost = (
    maintenance_cost + production_loss
)

maintenance_shift_cost = (
    maintenance_cost + shift_cost
)


options = {
    "Continue Production": continue_cost,
    "Stop + Maintenance": maintenance_only_cost,
    "Maintenance + Shift Production": maintenance_shift_cost
}


best_action = min(
    options,
    key=options.get
)

best_cost = options[best_action]
print("\n")
print("          COGNIFACT AI")

print(f"\nMachine: {machine_id}")

print(
    f"Temperature: {machine['Temperature']} °C"
)

print(
    f"Vibration: {machine['Vibration']}"
)

print(
    f"Power Consumption: "
    f"{machine['Power_Consumption']} kW"
)

print(
    f"Operating Hours: "
    f"{machine['Operating_Hours']}"
)

print(
    f"Maintenance Days: "
    f"{machine['Maintenance_Days']}"
)
print("AI PREDICTION")

print(
    f"Failure Probability: "
    f"{failure_probability:.2f}%"
)

print(f"Risk Level: {risk_level}")
print("\n")
print("TOP RISK FACTORS")

for _, row in importance_df.head(3).iterrows():

    print(
        f"{row['Feature']}: "
        f"{row['Importance'] * 100:.2f}%"
    )
print("\n")
print("WHAT-IF ANALYSIS")

print(
    f"Continue Production: "
    f"₹{continue_cost:,.0f}"
)

print(
    f"Stop + Maintenance: "
    f"₹{maintenance_only_cost:,.0f}"
)

print(
    f"Maintenance + Shift Production: "
    f"₹{maintenance_shift_cost:,.0f}"
)
print("\n")
print("RECOMMENDATION")

if failure_probability >= 70:

    print(
        f"Recommended Action: "
        f"{best_action}"
    )

    print(
        f"Estimated Impact: "
        f"₹{best_cost:,.0f}"
    )

    print(
        " Immediate attention recommended."
    )

elif failure_probability >= 30:

    print(
        " Inspect the machine soon."
    )

else:

    print(
        " Continue normal operation."
    )
