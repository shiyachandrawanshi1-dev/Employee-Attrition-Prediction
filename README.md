# IBM Employee Attrition Prediction

## 📌 Project Overview

Employee attrition refers to employees leaving an organization. High employee attrition can increase recruitment costs, reduce productivity, and affect overall business performance.

This project uses Machine Learning to predict whether an employee is likely to leave an organization based on employee-related information.

The goal is to help organizations understand attrition patterns and support data-driven HR decisions.

## 🎯 Project Objectives

* Analyze employee data to understand attrition patterns.
* Prepare and process data for Machine Learning.
* Train and use a Machine Learning model for attrition prediction.
* Provide predictions through a Python application.
* Explore how data analytics and predictive modeling can support HR decision-making.

## 🛠️ Technologies Used

* **Python** – Core programming language
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine Learning model development
* **Joblib** – Saving and loading the trained model
* **Flask** – API development
* **Streamlit** – Interactive user interface
* **Jupyter Notebook** – Data analysis and model experimentation

## 📂 Project Structure

```text
Employee-Attrition-Prediction/
│
├── Employee_Attrition_API/
│   ├── app.py
│   ├── final_model.pkl
│   └── requirements.txt
│
├── IBM_Attrition_prediction.ipynb
├── IBM.csv
├── final_model.pkl
├── .gitignore
└── README.md
```

## 📊 Dataset

The project uses an IBM employee dataset containing employee-related attributes that can be analyzed to identify patterns associated with attrition.

The dataset is used for data exploration, preprocessing, and Machine Learning.

## ⚙️ Project Workflow

1. **Data Collection:** Load the employee dataset.
2. **Exploratory Data Analysis:** Explore the dataset and identify patterns related to attrition.
3. **Data Preprocessing:** Prepare the data for model training.
4. **Model Training:** Train a Machine Learning model using the processed data.
5. **Model Saving:** Save the trained model for later use.
6. **Prediction:** Use employee information to generate attrition predictions.
7. **Application:** Provide an interface and API using the application's Flask and Streamlit components.

## 🚀 Getting Started

### Prerequisites

Make sure Python and Git are installed on your computer.

### 1. Clone the repository

```bash
git clone https://github.com/shiyachandrawanshi1-dev/Employee-Attrition-Prediction.git
```

### 2. Navigate to the application folder

```bash
cd Employee-Attrition-Prediction/Employee_Attrition_API
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

The application entry point is `app.py`. Run it using the command appropriate to the current Flask and Streamlit setup.

For a Streamlit entry point, the typical command is:

```bash
streamlit run app.py
```

Make sure the Flask API is started and configured as required by the application code.

## 💡 Expected Outcome

The application is intended to predict employee attrition based on the information provided and demonstrate how Machine Learning can be applied to HR analytics.

Predictions are estimates and should not be treated as definitive judgments about individual employees.

## 🔮 Future Improvements

* Improve model performance through feature engineering and model evaluation.
* Add more interactive visualizations.
* Deploy the application online.
* Improve API integration and error handling.
* Add further insights into employee attrition patterns.

## 👩‍💻 Author

**Shiya Chandrawanshi**

GitHub: [shiyachandrawanshi1-dev](https://github.com/shiyachandrawanshi1-dev)

---

⭐ If you find this project interesting, feel free to explore the repository!
