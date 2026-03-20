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
    except Exception as e:
        return None

model = load_model()

# ---------------- UI Styling ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg,#1e3c72,#2a5298);
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
st.write("Predict medical insurance cost using Machine Learning")

st.markdown("---")

# ---------------- Input Section ----------------
st.subheader("🧾 Enter Client Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)
    children = st.slider("Children", 0, 5, 0)

with col2:
    bmi = float(st.number_input("BMI", 15.0, 50.0, 25.0))
    smoker = st.selectbox("Smoker", ["No", "Yes"])

st.markdown("---")

# ---------------- Prediction ----------------
if st.button("🚀 Predict Charges"):

    if model is None:
        st.error("❌ Model file not found. Upload model_pickle.pkl")
    else:
        try:
            smoker_yes = 1 if smoker == "Yes" else 0

            input_data = pd.DataFrame(
                [[age, bmi, children, smoker_yes]],
                columns=['age', 'bmi', 'children', 'smoker_yes']
            )

            prediction = model.predict(input_data)[0]

            # ---------------- Result ----------------
            st.subheader("💰 Predicted Charges")
            st.success(f"Estimated Charges: ${prediction:,.2f}")

            # ---------------- Analysis ----------------
            st.subheader("📊 Health Analysis")

            if smoker == "Yes":
                st.warning("⚠️ Smoking increases insurance cost significantly")
            else:
                st.info("✅ Non-smoker → Lower insurance cost")

            if bmi > 30:
                st.warning("⚠️ High BMI → Higher health risk")
            elif bmi < 18.5:
                st.warning("⚠️ Low BMI → Possible health issues")
            else:
                st.success("✅ BMI is in healthy range")

            if age > 50:
                st.warning("⚠️ Higher age → Higher charges")
            else:
                st.info("✅ Lower age → Lower charges")

            st.markdown("---")
            st.caption("⚠️ This is an ML-based prediction, actual charges may vary.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
