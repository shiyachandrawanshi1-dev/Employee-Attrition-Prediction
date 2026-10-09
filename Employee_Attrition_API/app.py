import joblib
import pandas as pd
import streamlit as st
from flask import Flask,request,jsonify

# 1. flask app and model
app = Flask(__name__)
model = joblib.load('final_model.pkl')


# 2. Prepare input data
def Prepare_input(data):
    df = pd.DataFrame([data])

    # Marital status encoding
    marital_mapping = {
        "Divorced": 0,
        "Married": 1,
        "Single": 2

    }

    df["MaritalStatus"] = df["MaritalStatus"].map(
        marital_mapping
    )
    
    # Feature Engineering
    df["IncomePerYear"] = df["MonthlyIncome"] / df["Age"]

    df["SatisfactionScore"] = (
        df["EnvironmentSatisfaction"]
        + df["JobSatisfaction"]
        + df["WorkLifeBalance"]
    ) / 3

    # department encoding
    df["Department_Research & Development"] =(
        df["Department"] == "Research & Development"
    ).astype(int)


    df["Department_Sales"] = (
        df["Department"] == "Sales"
    ).astype(int)

    # Education Field Encoding
    df["EducationField_Life Sciences"] = (
        df["EducationField"] == "Life Sciences"
    ).astype(int)

    df["EducationField_Marketing"] = (
        df["EducationField"] == "Marketing"
    ).astype(int)

    df["EducationField_Medical"] = (
        df["EducationField"] == "Medical"
    ).astype(int)

    df["EducationField_Other"] = (
        df["EducationField"] == "Other"
    ).astype(int)

    df["EducationField_Technical Degree"] = (
        df["EducationField"] == "Technical Degree"
    ).astype(int)

    # Remove original categorical columns
    df = df.drop(
        ["Department", "EducationField"],
        axis=1
    )

    # keep the exact feature order used during training 
    columns = [
        "Age",
        "DistanceFromHome",
        "Education",
        "EnvironmentSatisfaction",
        "JobSatisfaction",
        "MaritalStatus",
        "MonthlyIncome",
        "NumCompaniesWorked",
        "WorkLifeBalance",
        "YearsAtCompany",
        "IncomePerYear",
        "SatisfactionScore",
        "Department_Research & Development",
        "Department_Sales",
        "EducationField_Life Sciences",
        "EducationField_Marketing",
        "EducationField_Medical",
        "EducationField_Other",
        "EducationField_Technical Degree"
    ]

    return df[columns]

# 3. Flask API
@app.route("/")
def home():
    return "Employee Attrition Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Please provide employee data as JSON"
            }), 400

        # Prepare input data
        input_data = Prepare_input(data)

        # Calculate prediction
        prediction = int(model.predict(input_data)[0])

        # Calculate probability
        probability = float(
            model.predict_proba(input_data)[0][1]
        )

        # Convert prediction into readable result
        if prediction == 1:
            result = "Likely to Leave"
        else:
            result = "Likely to Stay"

        return jsonify({
            "prediction": prediction,
            "result": result,
            "probability_of_leaving": round(probability, 4)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

# 4. Streamlit user interface

def run_streamlit():
    st.set_page_config(
        page_title="Employee Attrition Prediction",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Employee Attrition Prediction")

    st.write(
        "Enter employee details to estimate the likelihood "
        "of employee attrition."
    )

    st.info(
        "This is a model-based estimate, not a guarantee "
        "of an employee's future decision."
    )
    with st.form("employee_form"):
        st.subheader("Employee Details")

        col1,col2,col3 = st.columns(3)

        with col1:
            age = st.number_input(
                "Age", min_value=18, max_value=100, value=28
            )

            distance = st.number_input(
                "Distance From Home",
                min_value=1, max_value=100, value=5
            )

            education = st.selectbox(
                "Education Level", [1, 2, 3, 4, 5], index=1
            )

            marital_status = st.selectbox(
                "Marital Status",
                ["Single", "Married", "Divorced"]
            )
        with col2:  
            monthly_income = st.number_input(
                "Monthly Income",
                min_value=1, max_value=1000000, value=5000
            )

            num_companies = st.number_input(
                "Number of Companies Worked",
                min_value=0, max_value=50, value=2
            )

            years_at_company = st.number_input(
                "Years At Company",
                min_value=0, max_value=80, value=3
            )

            department = st.selectbox(
                "Department",
                [
                    "Research & Development",
                    "Sales",
                    "Human Resources"
                ]
            )
        with col3:
            environment_satisfaction = st.selectbox(
                "Environment Satisfaction (1–4)",
                [1, 2, 3, 4]
            )

            job_satisfaction = st.selectbox(
                "Job Satisfaction (1–4)",
                [1, 2, 3, 4]
            )

            work_life_balance = st.selectbox(
                "Work-Life Balance (1–4)",
                [1, 2, 3, 4]
            )

            education_field = st.selectbox(
                "Education Field",
                [
                    "Life Sciences",
                    "Marketing",
                    "Medical",
                    "Other",
                    "Technical Degree",
                    "Human Resources"
                ]
            )
        submitted = st.form_submit_button(
            "Predict Attrition",
            type="primary",
            use_container_width=True
        )
    if submitted:
        employee_data = {
            "Age": age,
            "DistanceFromHome": distance,
            "Education": education,
            "EnvironmentSatisfaction": environment_satisfaction,
            "JobSatisfaction": job_satisfaction,
            "MaritalStatus": marital_status,
            "MonthlyIncome": monthly_income,
            "NumCompaniesWorked": num_companies,
            "WorkLifeBalance": work_life_balance,
            "YearsAtCompany": years_at_company,
            "Department": department,
            "EducationField": education_field
        }
        try:
            input_data =Prepare_input(employee_data)
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
            
            st.divider()
            st.subheader("Prediction Result")

            if prediction == 1:
                st.error("⚠️ Likely to Leave")
            else:
                st.success("✅ Likely to Stay")

            st.metric(
                "Model-estimated probability of leaving",
                f"{probability * 100:.2f}%"
            )

            st.progress(float(probability))

            with st.expander("View processed input features"):
                st.dataframe(
                    input_data,
                    use_container_width=True
                )

        except Exception as e:
            st.error(f"Prediction failed: {e}")
        

# 5. Launch the application

if __name__ == "__main__":
    # When launched with Streamlit, display the UI.
    # Otherwise, start the Flask API.
    try:
        from streamlit.runtime.scriptrunner import(
            get_script_run_ctx
        )

        streamlit_context = get_script_run_ctx()

    except ImportError:
        streamlit_context = None

    if streamlit_context is not None:
        run_streamlit()
    else:
        app.run(
            host="127.0.0.1",
            port=5000,
            debug=False
        )            



            




