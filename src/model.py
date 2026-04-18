from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd


def train_model(df):
    X = df.drop(['Failure', 'Weekly_Sales', 'Dept', 'Store'], axis=1)  # ✅ FIX HERE
    y = df['Failure']

    # Encode categorical
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        X[col] = X[col].astype('category').cat.codes

    print("\nChecking data types:\n", X.dtypes)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
    )

    print("Fitting model...")
    model.fit(X_train, y_train)
    print("Model fit complete!")

    import joblib

    print("Saving model...")
    joblib.dump(model, "models/predictive_model.pkl")
    print("Model saved successfully!")

    # 🔥 FEATURE IMPORTANCE (ADD HERE)
    import matplotlib.pyplot as plt
    feature_importances = model.feature_importances_
    features = X.columns

    plt.figure()
    plt.barh(features, feature_importances)
    plt.title("Feature Importance")
    plt.savefig("outputs/feature_importance.png")
    plt.show()

    y_pred = model.predict(X_test)

    print("Model Training Completed!")

    return model, X_test, y_test, y_pred

def evaluate_model(y_test, y_pred):
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))