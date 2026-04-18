import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def plot_results(y_test, y_pred):
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    disp.plot()
    plt.title("Failure Prediction Confusion Matrix")
    plt.savefig("outputs/confusion_matrix.png")
    plt.show()

    # Prediction comparison
    plt.figure()
    plt.plot(y_test.values[:100], label="Actual")
    plt.plot(y_pred[:100], label="Predicted")
    plt.legend()
    plt.title("Actual vs Predicted Failure")
    plt.savefig("outputs/prediction_plot.png")
    plt.show()


    