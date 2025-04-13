from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Ensure app directory exists
os.makedirs("app", exist_ok=True)

# Save model
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to app/model.pkl")
