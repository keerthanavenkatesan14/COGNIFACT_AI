import pandas as pd
import joblib
from decision_engine import make_decision
machine_data = pd.read_csv(
    "data/cognifact_machine_dataset.csv"
)

maintenance_data = pd.read_csv(
    "data/maintenance_data.csv"
)

production_data = pd.read_csv(
    "data/production_data.csv"
)
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
model = joblib.load(
    "ml/ml_model.pkl"
)
features = factory_data[
    [
        "Temperature",
        "Vibration",
        "Power_Consumption",
        "Operating_Hours",
        "Maintenance_Days"
    ]
]
predictions = model.predict(features)

probabilities = model.predict_proba(features)[:, 1]


factory_data["Failure_Probability"] = (
    probabilities * 100
)


factory_data["Prediction"] = predictions
def get_risk_level(probability):

    if probability >= 70:
        return "HIGH"

    elif probability >= 30:
        return "MEDIUM"

    else:
        return "LOW"
def get_recommended_action(probability):

    if probability >= 70:
        return "Maintenance + Shift Production"

    elif probability >= 30:
        return "Stop + Maintenance"

    else:
        return "Continue Operating"

factory_data["Risk_Level"] = (
    factory_data["Failure_Probability"]
    .apply(get_risk_level)
)
factory_data["Recommended_Action"] = (
    factory_data["Failure_Probability"]
    .apply(get_recommended_action)
)
print("\n")
print("COGNIFACT AI")
print("FACTORY RISK MONITOR")
print(
    f"\nTotal Machine Records: "
    f"{len(factory_data)}"
)


print(
    f"Unique Machines: "
    f"{factory_data['Machine_ID'].nunique()}"
)
results = factory_data[
    [
        "Machine_ID",
        "Failure_Probability",
        "Risk_Level",
        "Recommended_Action"
    ]
].copy()


results["Failure_Probability"] = (
    results["Failure_Probability"]
    .round(2)
)


print("\nMachine Risk Status:")

print(
    results.to_string(index=False)
)
high_risk = factory_data[
    factory_data["Failure_Probability"] >= 70
]


medium_risk = factory_data[
    (factory_data["Failure_Probability"] >= 30)
    &
    (factory_data["Failure_Probability"] < 70)
]
print("\n")
print("RISK SUMMARY")

print(
    f" High Risk Records: "
    f"{len(high_risk)}"
)

print(
    f" Medium Risk Records: "
    f"{len(medium_risk)}"
)

print(
    f" Low Risk Records: "
    f"{len(factory_data) - len(high_risk) - len(medium_risk)}"
)
print("\nACTION SUMMARY")

action_counts = (
    factory_data["Recommended_Action"]
    .value_counts()
)

for action, count in action_counts.items():

    print(
        f"{action}: {count}"
    )
if len(high_risk) > 0:

    print("\n")
    print(" HIGH-RISK MACHINES")

    high_risk_display = high_risk[
        [
            "Machine_ID",
            "Temperature",
            "Vibration",
            "Power_Consumption",
            "Operating_Hours",
            "Maintenance_Days",
            "Failure_Probability",
            "Recommended_Action"
        ]
    ].copy()

    high_risk_display[
        "Failure_Probability"
    ] = high_risk_display[
        "Failure_Probability"
    ].round(2)

    print(
        high_risk_display.to_string(
            index=False
        )
    )

else:

    print("\n No high-risk machines detected.")


print("        CogniFact monitoring complete")
