import pandas as pd
import numpy as np

def preprocess_data(df):
    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    # Fix missing values (UPDATED FOR PANDAS 2.x)
    df = df.ffill()
    df = df.bfill()

    # Check if Weekly_Sales exists
    if 'Weekly_Sales' not in df.columns:
        raise ValueError("Weekly_Sales column not found! Use train.csv instead of test.csv")

    # Simulate FAILURE LABEL
    threshold = df['Weekly_Sales'].quantile(0.25)
    df['Failure'] = np.where(df['Weekly_Sales'] < threshold, 1, 0)

    # Drop unnecessary columns
    df = df.drop(['Date'], axis=1)

    print("Preprocessing Completed!")
    return df