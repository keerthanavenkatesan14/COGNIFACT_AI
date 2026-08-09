import joblib
import pandas as pd

from decision_engine import make_decision

model = joblib.load("ml/ml_model.pkl")

machine_id = "M003"

machine = pd.DataFrame([{
    "Temperature": 88,
    "Vibration": 7.2,
    "Power_Consumption": 5.1,
    "Operating_Hours": 2300,
    "Maintenance_Days": 90
}])

prediction = model.predict(machine)[0]

probability = model.predict_proba(machine)[0][1]

failure_probability = probability * 100

print("\n CogniFact AI Prediction")
print(f"Machine: {machine_id}")

print(f"Failure Probability: {failure_probability:.2f}%")

if failure_probability >= 70:
    risk = "HIGH"
elif failure_probability >= 30:
    risk = "MEDIUM"
else:
    risk = "LOW"

print(f"Risk Level: {risk}")

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

print("\n===== AI Feature Importance =====")

for _, row in importance_df.iterrows():
    print(
        f"{row['Feature']}: "
        f"{row['Importance'] * 100:.2f}%"
    )

print("\nAI Recommendation")

recommended_action = make_decision(
    failure_probability
)

print(
    f"Recommended Action: {recommended_action}"
)
make_decision(machine_id, failure_probability)

