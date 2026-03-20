import streamlit as st
import pandas as pd
import pickle

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="🏥",
    layout="centered"
)

# ---------------- Load Model ----------------
try:
    model = pickle.load(open("model_pickle.pkl", "rb"))
except Exception as e:
    st.error(f"❌ Model load error: {e}")
    st.stop()

# ---------------- Title ----------------
st.title("🏥 Insurance Charges Predictor")
st.write("Predict insurance charges based on user details")

st.markdown("---")

# ---------------- Inputs ----------------
age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI", 15.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["No", "Yes"])

st.markdown("---")

# ---------------- Prediction ----------------
if st.button("Predict Charges"):

    try:
        # Convert input
        smoker_yes = 1 if smoker == "Yes" else 0

        # DataFrame (IMPORTANT: order must match training)
        input_data = pd.DataFrame(
            [[age, bmi, children, smoker_yes]],
            columns=['age', 'bmi', 'children', 'smoker_yes']
        )

        prediction = model.predict(input_data)[0]

        # ---------------- Output ----------------
        st.subheader("💰 Predicted Charges")
        st.success(f"${prediction:,.2f}")

        # ---------------- Simple Analysis ----------------
        if smoker == "Yes":
            st.warning("⚠️ Smoking increases cost")
        else:
            st.info("✅ Non-smoker → lower cost")

        if bmi > 30:
            st.warning("⚠️ High BMI increases cost")

        if age > 50:
            st.warning("⚠️ Higher age → higher charges")

    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
