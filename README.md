# 🔧 AI-Powered Predictive Maintenance System

## 📌 Overview

This project simulates an AI-based predictive maintenance system that detects potential failures using machine learning and operational data.

It includes a complete pipeline:

* Data preprocessing
* Feature engineering
* Machine learning model
* Real-time prediction dashboard using Streamlit

---

## 🎯 Problem Statement

Industries face unexpected machine failures that lead to downtime and financial loss.
This project predicts potential failures in advance using data-driven techniques.

---

## 🏭 Industry Relevance

* Manufacturing plants
* Automotive systems
* IoT-based monitoring systems
* Energy and power plants

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 📊 Dataset

Walmart dataset used to simulate real-world operational conditions.
Failure is defined based on low performance (proxy-based labeling).

---

## 🧠 Model

* Algorithm: Random Forest Classifier
* Handled:

  * Data leakage
  * Class imbalance
* Achieved:

  * ~70% accuracy
  * Improved failure detection recall

---

## 🏗️ Architecture

Data → Preprocessing → Feature Engineering → Model → Prediction → Dashboard

---

## 🚀 How to Run

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd AI-Predictive-Maintenance-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Model

```bash
python main.py
```

### 4. Run Dashboard

```bash
streamlit run app.py
```

---

## 📸 Results

### Dashboard

![Dashboard](images/dashboard_home.png)

### Normal Prediction

![Normal](images/normal_prediction.png)

### Failure Detection

![Failure](images/failure_prediction.png)

### Confusion Matrix

![Confusion](images/confusion_matrix.png)

### Feature Importance

![Feature](images/feature_importance.png)

---

## 💡 Key Learnings

* Handling real-world data issues (missing values, encoding)
* Avoiding data leakage
* Handling imbalanced datasets
* Building end-to-end ML systems
* Deploying ML using Streamlit

---

## 📌 Future Improvements

* Real IoT sensor integration
* Deep learning models (LSTM)
* Real-time streaming data
* Cloud deployment

---

## 👨‍💻 Author

Varda Kunde