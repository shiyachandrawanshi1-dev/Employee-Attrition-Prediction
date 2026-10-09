# Employee Attrition Prediction

> Predicting employee attrition using Machine Learning to help organizations identify employees who may be at risk of leaving.

[🚀 Live Streamlit App](https://employee-attrition-ui.onrender.com) · [💻 GitHub Repository](https://github.com/shiyachandrawanshi1-dev/Employee-Attrition-Prediction)

---

## 🎯 Business Problem

Employee attrition can increase recruitment and training costs, disrupt teams, and result in the loss of valuable experience.

This project uses Machine Learning to predict whether an employee is likely to leave a company based on factors such as age, monthly income, job satisfaction, work-life balance, and years at the company.

**Goal:** Help HR teams identify potential attrition risks and make more informed employee-retention decisions.

**Target audience:** HR teams, people analytics teams, and business managers.

---

## 📊 Dataset

* **Source:** IBM HR Analytics Employee Attrition Dataset
* **Dataset file:** `IBM.csv`
* **Target variable:** `Attrition`
* **Prediction classes:** Yes / No
* **Data processing:** Data cleaning, feature engineering, and categorical-variable encoding

The dataset contains employee information used to explore patterns associated with employees leaving an organization.

---

## 🔍 Exploratory Data Analysis (EDA)

The project explores relationships between employee attrition and several factors, including:

* 💰 Monthly income and compensation
* 🧑 Age and career stage
* 📍 Distance from home
* 😔 Job and environmental satisfaction
* 🏢 Years at the company and previous companies worked
* 💍 Marital status
* 🏬 Department and education field
* ⚖️ Class imbalance between employees who stayed and employees who left

Visualizations help identify patterns and compare attrition rates across employee groups.

---

## ⚙️ Feature Engineering

Two additional features were created to capture potentially useful relationships in the data.

**1. IncomePerYear**

`IncomePerYear = MonthlyIncome / Age`

This feature represents monthly income relative to age. It is an engineered ratio, not a direct measure of employee dissatisfaction.

**2. SatisfactionScore**

`SatisfactionScore = (JobSatisfaction + EnvironmentSatisfaction + WorkLifeBalance) / 3`

This feature combines three employee-experience indicators into one average score.

These features are used alongside the original employee attributes during prediction.

---

## 🤖 Machine Learning Model

The project uses **Logistic Regression** to predict employee attrition as a binary classification problem.

### Why Logistic Regression?

* Suitable for binary classification.
* Estimates the probability of an employee leaving.
* Relatively efficient to train and evaluate.
* Provides a useful baseline for comparing classification models.

The model uses employee features to estimate attrition risk and generate a prediction.

### Model Evaluation

Model performance should be evaluated using metrics suited to the imbalanced target variable:

* **Recall:** How many employees who actually left were identified.
* **Precision:** How many employees flagged as at risk actually left.
* **F1-score:** A balance between precision and recall.
* **Accuracy:** The proportion of all predictions that were correct.

Recall is particularly relevant when missing an employee at risk of leaving is considered costly. However, a high recall can also generate more false positives, so the threshold should be chosen based on the organization's needs.

*See the project notebook for the actual evaluation results and model comparisons.*

---

## 🚀 Live Application

Try the deployed application:

### [Open Employee Attrition Prediction App](https://employee-attrition-ui.onrender.com)

The application provides an interface to:

* Enter employee details.
* Generate an attrition prediction.
* View the model's estimated prediction probability.
* Explore potential attrition risk based on the supplied details.

**Note:** Predictions are estimates from a machine learning model and should support—not replace—human judgment in HR decisions.

---

## 🛠️ Tech Stack

| Category             | Technologies                      |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| Data Analysis        | Pandas, NumPy                     |
| Machine Learning     | Scikit-learn, Logistic Regression |
| Data Visualization   | Matplotlib, Seaborn               |
| Model Serialization  | Joblib                            |
| API Development      | Flask                             |
| Web Interface        | Streamlit                         |
| Deployment           | Render                            |
| Version Control      | Git, GitHub                       |

---

## 📂 Project Structure

```text
Employee-Attrition-Prediction/
│
├── IBM.csv
├── IBM_Attrition_prediction.ipynb
├── final_model.pkl
├── README.md
├── .gitignore
│
└── Employee_Attrition_API/
    ├── app.py
    ├── final_model.pkl
    └── requirements.txt
```

---

## 💻 Run the Project Locally

**1. Clone the repository**

```bash
git clone https://github.com/shiyachandrawanshi1-dev/Employee-Attrition-Prediction.git
```

**2. Navigate to the application folder**

```bash
cd Employee-Attrition-Prediction/Employee_Attrition_API
```

**3. Create and activate a virtual environment**

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

**4. Install the dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the Streamlit application**

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

* Add SHAP-based explanations for individual predictions.
* Compare additional models, such as Random Forest and XGBoost.
* Improve performance on the minority attrition class.
* Build a department-level attrition analytics dashboard.
* Add model monitoring and periodic retraining.
* Improve threshold selection based on business costs.

---

## 💡 Key Learnings

1. Exploratory Data Analysis helps uncover patterns in employee data.
2. Feature engineering can introduce additional signals for a predictive model.
3. Accuracy alone can be misleading when the target classes are imbalanced.
4. Recall and precision help evaluate the trade-offs in attrition prediction.
5. Model and library versions must be compatible when deploying saved machine learning models.
6. Deploying with Flask and Streamlit provides experience with APIs and interactive machine learning applications.

---

## 👩‍💻 Author

**Shiya Chandrawanshi**

B.Tech Computer Science and Engineering

[GitHub](https://github.com/shiyachandrawanshi1-dev)

---

⭐ If you find this project useful, consider giving the repository a star!
