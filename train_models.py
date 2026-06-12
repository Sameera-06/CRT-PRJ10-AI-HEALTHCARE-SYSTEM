from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

print("Training Disease Prediction Model...")

# ==========================================
# DISEASE PREDICTION MODEL
# ==========================================

X_disease, y_disease = make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=4,
    n_redundant=0,
    n_classes=2,
    random_state=42
)

disease_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

disease_model.fit(
    X_disease,
    y_disease
)

joblib.dump(
    disease_model,
    "models/disease_model.pkl"
)

print("Disease Model Saved")

# ==========================================
# OUTCOME PREDICTION MODEL
# ==========================================

print("Training Outcome Prediction Model...")

X_outcome, y_outcome = make_classification(
    n_samples=1000,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    random_state=42
)

outcome_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

outcome_model.fit(
    X_outcome,
    y_outcome
)

joblib.dump(
    outcome_model,
    "models/outcome_model.pkl"
)

print("Outcome Model Saved")

print("\n================================")
print("ALL MODELS GENERATED SUCCESSFULLY")
print("================================")