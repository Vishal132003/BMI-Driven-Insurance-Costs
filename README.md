# 🏥 Insurance Charges Prediction Project

## 📌 Overview

This project predicts medical insurance charges based on personal attributes using Machine Learning. It helps estimate healthcare costs for individuals and supports better decision-making for insurance providers.

---

## 🔗 Live Demo

👉 [Click Here to Use the App](https://bmi-driven-insurance-costs-ztmfaldvvrtp9ey6rrz7jp.streamlit.app/)

---

## 📊 Dataset

The dataset used is **insurance.csv**, which contains the following features:

* **age**
* **sex**
* **bmi**
* **children**
* **smoker**
* **region**
* **charges**

### ⚙️ Preprocessing

* Handled outliers in the **bmi** column
* Applied **One-Hot Encoding** to categorical features

---

## 🎯 Features Used

### Independent Variables (Input):

* age
* bmi
* children
* smoker_yes

### Target Variable (Output):

* charges

---

## 🤖 Model

* Algorithm: **Linear Regression**
* Train-Test Split: **80% Training, 20% Testing**
* Tested multiple `random_state` values for better performance

---

## 📈 Results

* Achieved **R² Score ≈ 0.82**
* Shows good model performance and prediction capability

---

## ⚙️ Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## ▶️ Usage

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Add Dataset

Place **insurance.csv** in the project directory

### 3. Run Project

* Open: `insurance_prediction.ipynb`
  OR
* Run: `app.py` (for Streamlit app)

---

## 📁 Project Structure

```
app.py                      # Streamlit application
insurance.csv               # Dataset
insurance_prediction.ipynb  # Model training & analysis
model_pickle.pkl            # Trained model
requirements.txt            # Dependencies
README.md                   # Project documentation
```

---

## 🧠 Conclusion

This project demonstrates how Machine Learning can predict insurance costs effectively using basic user data. The model performs well and can be improved further with advanced techniques.

---

## 🚀 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Add more features for better accuracy
* Improve UI with graphs and dashboards
* Deploy with authentication system

---
