# 🏠 Bengaluru House Price Analytics using Machine Learning

> **An end-to-end Machine Learning project that predicts residential property prices in Bengaluru using a Linear Regression model implemented completely from scratch with NumPy.**

This project demonstrates the complete machine learning workflow—from raw data preprocessing and feature engineering to model training, evaluation, and accurate house price prediction—without relying on machine learning libraries for the learning algorithm.

# 🎯 Project Objective

Real estate prices depend on several factors such as location, total area, number of bedrooms, and amenities. Determining a fair market price manually is difficult due to the large number of influencing factors.

The objective of this project is to build a machine learning system capable of estimating house prices accurately by learning patterns from historical housing data.

The project focuses on understanding the mathematics behind Linear Regression by implementing Gradient Descent from scratch using NumPy instead of using Scikit-learn's built-in Linear Regression.

# 🌍 Real-World Applications

This solution can be useful for:

* 🏠 Home buyers to estimate fair property prices
* 🏢 Real estate companies for automated valuation
* 💰 Banks during home loan approval
* 📈 Property investment analysis
* 🏗️ Real estate websites to recommend competitive pricing
* 📊 Market trend analysis and decision making

# 📌 Project Highlights

✔ Complete data preprocessing pipeline

✔ Feature engineering for improved prediction accuracy

✔ Linear Regression implemented from scratch using NumPy

✔ Gradient Descent optimization

✔ Mean Squared Error (MSE) loss function

✔ Model evaluation using R² Score and RMSE

✔ Data visualization and exploratory analysis

✔ Clean, modular, and well-documented code

# 📂 Project Structure

```text
Bengaluru-House-Price-Analytics/

│
├── Bengaluru_House_Data.csv
├── Preprocessing_EDA.ipynb
├── Linear_Reg_Logistic_Reg.ipynb
├── requirements.txt
└── README.md
```

# 📊 Dataset Overview

The project uses the **Bengaluru House Price Dataset** containing over **13,000 residential property listings**.

### Features

| Feature      | Description                        |
| ------------ | ---------------------------------- |
| area_type    | Property type                      |
| availability | Ready-to-move or possession status |
| location     | House location                     |
| size         | Number of bedrooms                 |
| total_sqft   | Total area in square feet          |
| bath         | Number of bathrooms                |
| balcony      | Number of balconies                |
| price        | Target variable (Price in Lakhs)   |

# ⚙ Data Preprocessing

The raw dataset contains missing values, inconsistent formats, and outliers.

The preprocessing pipeline includes:

* Removing unnecessary columns
* Handling missing values
* Extracting BHK values
* Converting area ranges into numeric values
* Removing duplicate records
* Detecting and removing outliers
* Standardizing numerical features

The resulting dataset is cleaner, more consistent, and better suited for machine learning.

# 🧠 Feature Engineering

To improve predictive performance, several meaningful features were created.

* Price per Square Foot
* Average Price by Location
* Location Premium Index
* Square Feet per Bedroom (BHK)

These engineered features enable the model to capture relationships that are not directly available in the original dataset.

# 🤖 Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Handling
      │
      ▼
Feature Engineering
      │
      ▼
Outlier Removal
      │
      ▼
Feature Standardization
      │
      ▼
Train-Test Split
      │
      ▼
Linear Regression (NumPy)
      │
      ▼
Gradient Descent Optimization
      │
      ▼
Model Evaluation
      │
      ▼
House Price Prediction
```

# 📈 Model Implementation

The Linear Regression model was developed **entirely from scratch** using **NumPy**, providing a deeper understanding of the underlying mathematical concepts.

### Implemented Components

* Cost Function (Mean Squared Error)
* Gradient Descent
* Weight Initialization
* Bias Optimization
* Feature Normalization
* Prediction Function
* Model Evaluation
  
# 📊 Model Performance

| Metric           | Result               |
| ---------------- | -------------------- |
| Algorithm        | Linear Regression    |
| Implementation   | NumPy (From Scratch) |
| Optimizer        | Gradient Descent     |
| Loss Function    | Mean Squared Error   |
| Training Epochs  | 5000                 |
| Learning Rate    | 0.001                |
| Train/Test Split | 80/20                |
| R² Score         | ~0.70+               |
| RMSE             | ~₹60–90 Lakhs        |

# 📉 Exploratory Data Analysis

Several visualizations were created to understand the dataset, including:

* Price Distribution
* Correlation Heatmap
* BHK Distribution
* Location-wise Price Analysis
* Price vs Total Square Feet
* Bathroom vs Price
* Outlier Detection
* Feature Correlation Analysis

These insights helped identify important trends and improve model performance.

# 🛠 Technologies Used

| Category            | Technologies       |
| ------------------- | ------------------ |
| Programming         | Python             |
| Numerical Computing | NumPy              |
| Data Analysis       | Pandas             |
| Visualization       | Matplotlib, Plotly |
| Notebook            | Jupyter Notebook   |

# 🚀 Key Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning fundamentals
* Linear Regression mathematics
* Gradient Descent optimization
* Feature Engineering
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Model Evaluation
* Building machine learning models without external ML libraries

# 🔮 Future Enhancements

Potential improvements include:

* Implementing Ridge and Lasso Regression
* Comparing multiple regression algorithms
* Hyperparameter optimization
* Advanced feature engineering
* Cross-validation
* Model deployment using a web application
* Support for multiple city datasets

# 💡 Why This Project?

Most house price prediction projects rely entirely on Scikit-learn.

This project intentionally builds the Linear Regression algorithm from scratch to demonstrate a solid understanding of:

* The mathematics behind machine learning
* Optimization using Gradient Descent
* Model training without high-level ML libraries
* End-to-end machine learning workflow

It highlights not just the ability to use machine learning tools, but also the ability to understand and implement the underlying algorithms.

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you have ideas to enhance the project, feel free to fork the repository, submit issues, or create pull requests.

# ⭐ If You Found This Project Helpful

If you enjoyed exploring this project or found it useful, consider giving it a ⭐ on GitHub. It motivates me to continue building and sharing more machine learning projects.
