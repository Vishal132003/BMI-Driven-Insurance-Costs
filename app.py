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
@st.cache_resource
def load_model():
    try:
        with open('model_pickle.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

model = load_model()

# ---------------- UI Design ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(120deg, #1e3c72, #2a5298);
    color: white;
}
.stButton>button {
    background-color: #00c6ff;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🏥 Insurance Charges Predictor")
st.write("Predict medical insurance cost based on user details")

st.markdown("---")

# ---------------- Input Section ----------------
st.subheader("🧾 Enter Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)
    children = st.slider("Children", 0, 5, 0)

with col2:
    bmi = st.number_input("BMI", 15.0, 50.0, 25.0)
    smoker = st.selectbox("Smoker", ["No", "Yes"])

st.markdown("---")

# ---------------- Prediction ----------------
if st.button("🚀 Predict Charges"):

    if model is None:
        st.error("Model file not found!")
    else:
        smoker_yes = 1 if smoker == "Yes" else 0

        input_data = pd.DataFrame(
            [[age, bmi, children, smoker_yes]],
            columns=['age', 'bmi', 'children', 'smoker_yes']
        )

        prediction = model.predict(input_data)[0]

        # ---------------- Output Section ----------------
        st.subheader("💰 Result")

        st.success(f"Estimated Charges: ${prediction:,.2f}")

        # ---------------- Analysis ----------------
        st.subheader("📊 Quick Analysis")

        if smoker == "Yes":
            st.warning("Smoking significantly increases insurance cost.")
        else:
            st.info("Non-smoker → lower risk → lower charges")

        if bmi > 30:
            st.warning("High BMI may increase medical expenses.")
        elif bmi < 18.5:
            st.warning("Low BMI may indicate health risks.")
        else:
            st.success("BMI is in healthy range.")

        if age > 50:
            st.warning("Higher age → higher insurance cost.")
        else:
            st.info("Younger age → relatively lower cost.")

        st.markdown("---")
        st.caption("⚠️ This is a predicted value based on ML model.")
