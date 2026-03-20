# Insurance Charges Prediction Project

## Overview

This project focuses on predicting insurance charges based on personal attributes. The goal is to build a machine learning model that estimates medical costs accurately, helping individuals and insurance providers make better decisions.

---

## Dataset

The dataset used is **insurance.csv**, which includes:

* age
* sex
* bmi
* children
* smoker
* region
* charges

### Preprocessing:

* Handled outliers in the **bmi** column
* Applied **one-hot encoding** for categorical features

---

## Features Used

Independent variables:

* age
* bmi
* children
* smoker_yes

Target variable:

* charges

---

## Model

* Algorithm: **Linear Regression**
* Train-Test Split: **80% training, 20% testing**
* Multiple random states tested to achieve best performance

---

## Results

* Achieved **R² score ≈ 0.82**
* Indicates strong predictive performance and good model fit

---

## Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Usage

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

2. Ensure `insurance.csv` is in the project directory

3. Run:

* Jupyter Notebook: `insurance_prediction.ipynb`
* OR Python script (if available)

---

## Project Structure

* `insurance.csv` → Dataset
* `insurance_prediction.ipynb` → Model building & analysis
* `model_pickle.pkl` → Saved trained model
* `requirements.txt` → Dependencies

---

## Conclusion

This project demonstrates how machine learning can effectively predict insurance costs using basic personal data. The model shows strong performance and can be further improved with advanced techniques.
