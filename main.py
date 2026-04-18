from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model, evaluate_model
from src.visualization import plot_results

def main():
    print("Loading data...")
    df = load_data()

    print("Preprocessing data...")
    df = preprocess_data(df)

    print("Training model...")
    model, X_test, y_test, y_pred = train_model(df)

    print("Evaluating model...")
    evaluate_model(y_test, y_pred)

    print("Generating visualizations...")
    plot_results(y_test, y_pred)

    print("Project execution completed successfully!")

if __name__ == "__main__":
    main()