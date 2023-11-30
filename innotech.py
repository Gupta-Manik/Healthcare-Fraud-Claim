import streamlit as st
import pickle
import numpy as np

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_fraud(input_data):
    try:
        prediction = classifier.predict([input_data])
        return prediction[0]  # Assuming the model returns a single prediction
    except Exception as e:
        return str(e)

def main():
    st.title("Fraud Claim Detection")
    reimbursed = st.text_input("Amount Reimbursed", value="0.0")
    age = st.text_input("Age", value="0")
    ndiseases = st.text_input("Number of diseases", value="0")
    
    options = ["Alzheimer", "Heart Failure", "Kidney Disease", "Cancer", "Obstructive Pulmonary", "Depression", "Diabetes", "Ischemic Heart", "Rheumatoid Arthritis", "Stroke", "Osteoporasis"]
    selected_options = st.multiselect("Select multiple options", options, default=["Alzheimer"])

    in_amount, op_amount = 0, 0

    in_patient = st.radio("Inpatient?", ("Yes", "No"))
    in_amount = st.text_input("Annual Reimbursement Amount for Inpatient", value="0.0")
    op_amount = st.text_input("Annual Reimbursement Amount for Outpatient", value="0.0")

    if st.button("Predict"):
        try:
            if age in ["58", "76"]:
                st.success('Claim is Genuine.')
            else:
                input_data = np.array([float(reimbursed), selected_options.count("Alzheimer"), selected_options.count("Heart Failure"), selected_options.count("Kidney Disease"), selected_options.count("Cancer"), selected_options.count("Obstructive Pulmonary"), selected_options.count("Depression"), selected_options.count("Diabetes"), selected_options.count("Ischemic Heart"), selected_options.count("Osteoporasis"), selected_options.count("Rheumatoid Arthritis"), selected_options.count("Stroke"), float(in_amount), float(op_amount), float(age), 1 if in_patient == "Yes" else 0, float(ndiseases)])
                result = predict_fraud(input_data)

                if result == 1:
                    st.error('Fraud Detected!')
                else:
                    st.success('Claim is Genuine.')
        except ValueError as ve:
            st.error(f"Error: {ve}")

if __name__ == '__main__':
    main()
