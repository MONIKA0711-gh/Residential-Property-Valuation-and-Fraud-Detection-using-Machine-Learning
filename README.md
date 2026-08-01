# 🏠 AI-Powered Residential Property Valuation and Fraud Detection System

> **An end-to-end Machine Learning system that predicts fair residential property prices and detects suspicious property listings using Linear Regression and Logistic Regression implemented completely from scratch with NumPy.**

This project goes beyond traditional house price prediction by combining **property valuation**, **fraud probability estimation**, **risk assessment**, and an **Explainable Fraud Engine** into a single intelligent property analysis system.

---

# 📌 Project Overview

Buying a property is one of the biggest financial decisions an individual makes. However, buyers often rely solely on the seller's quoted price without knowing whether it truly reflects the property's market value.

This project addresses that challenge by developing an AI-powered decision support system that:

- Predicts the fair market value of a property.
- Identifies suspicious property pricing.
- Estimates fraud probability.
- Calculates a risk score and assigns a risk level.
- Explains why a property is considered suspicious.
- Suggests a fair market price range.

---

# 🎯 Project Objectives

- Predict accurate house prices using Linear Regression implemented from scratch.
- Detect suspicious property pricing using Logistic Regression implemented from scratch.
- Build a custom fraud detection dataset from an existing house price dataset.
- Generate explainable fraud analysis for better decision-making.
- Assist buyers in evaluating whether a property's quoted price is reasonable.

---

# 🌍 Real-World Applications

This project can be used by:

- 🏠 Home Buyers for fair price estimation before purchasing.
- 🏢 Real Estate Companies for automated property valuation.
- 🏦 Banks during home loan property valuation.
- 📈 Property Investors to compare investment opportunities.
- 🌐 Real Estate Platforms for intelligent pricing insights.
- 📊 Market Analysts for studying pricing patterns.

---

# 📂 Dataset

**Dataset:** Bengaluru House Price Dataset

The original dataset contains over **13,000 residential property listings**.

### Original Features

- Area Type
- Availability
- Location
- Size
- Total Square Feet
- Bathrooms
- Balconies
- Price

> **Note:** The original dataset does **not** contain fraud labels or suspicious property information.

---

# ⚙ Data Preprocessing

The preprocessing pipeline includes:

- Removing unnecessary columns
- Handling missing values
- Extracting BHK values
- Converting area ranges into numeric values
- Removing duplicate records
- Handling rare locations
- Detecting and removing outliers
- Standardizing numerical features

---

# 🧠 Feature Engineering

To improve prediction performance, additional meaningful features were engineered.

### Price Prediction Features

- Price per Square Foot
- Square Feet per BHK
- Location Average Price
- Location Premium Index

### Fraud Detection Features

- Quoted Price
- Inflation Ratio
- Difference Percentage
- Area Value Index
- Price Rank
- Risk Score

These engineered features were used to create a custom fraud detection dataset and improve model performance.

---

# 🤖 Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Linear Regression (From Scratch)
      │
      ▼
Predicted Market Price
      │
      ▼
Custom Fraud Dataset Generation
      │
      ▼
Fraud Feature Engineering
      │
      ▼
Logistic Regression (From Scratch)
      │
      ▼
Fraud Probability Prediction
      │
      ▼
Risk Score Generation
      │
      ▼
Explainable Fraud Engine
      │
      ▼
Final Property Analysis Report
```

---

# 🧮 Model 1 — Linear Regression (From Scratch)

Implemented completely from scratch using **NumPy**.

### Implemented Components

- Weight Initialization
- Bias Initialization
- Feature Standardization
- Mean Squared Error (MSE)
- Gradient Descent
- Weight Updates
- Prediction Function

### Purpose

Predict the fair market value of a property based on:

- Location
- Total Square Feet
- BHK
- Bathrooms

---

# 🚨 Custom Fraud Detection Pipeline

Since the original dataset did not contain fraud labels, a custom fraud detection pipeline was designed.

### Steps

- Generate seller quoted prices
- Compare quoted price with predicted market price
- Generate fraud labels using rule-based logic
- Engineer fraud-related features
- Train Logistic Regression model

This transformed a standard regression dataset into a supervised fraud detection dataset.

---

# 🧠 Model 2 — Logistic Regression (From Scratch)

Implemented completely from scratch using **NumPy**.

### Implemented Components

- Sigmoid Function
- Binary Cross Entropy Loss
- Gradient Descent
- Weight Updates
- Probability Prediction
- Binary Classification

### Purpose

Estimate the probability that a property's quoted price is suspicious.

---

# 📊 Model Performance

## Linear Regression

| Metric | Value |
|---------|-------|
| Algorithm | Linear Regression |
| Implementation | NumPy (From Scratch) |
| Optimizer | Gradient Descent |
| Loss Function | Mean Squared Error |
| Epochs | 5000 |
| Learning Rate | 0.001 |

---

## Logistic Regression

| Metric | Value |
|---------|-------|
| Algorithm | Logistic Regression |
| Implementation | NumPy (From Scratch) |
| Classification Accuracy | **97.74%** |
| Precision | **(Add Your Value)** |
| Recall | **(Add Your Value)** |
| F1-Score | **(Add Your Value)** |

---

# 🔍 Explainable Fraud Engine

Instead of simply classifying a property as suspicious, the system provides human-readable explanations.

Example outputs:

- Property appears moderately overpriced.
- Large positive deviation from predicted market price.
- Property price is close to estimated market value.
- Property is significantly below estimated market value (possible bargain).

---

# ⚠ Risk Assessment Module

The project also generates:

- Fraud Probability
- Risk Score
- Risk Level

Risk Levels:

- Low
- Moderate
- High
- Critical

---

# 📋 Final Property Analysis Report

The final system generates:

- Predicted Market Price
- Quoted Price
- Price Difference
- Fraud Probability
- Risk Score
- Risk Level
- Explainable Reasons
- Suggested Fair Price Range

---

# 💻 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Numerical Computing | NumPy |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Notebook | Google Colab |
| Machine Learning | Linear Regression, Logistic Regression |

---

# 📚 Key Learning Outcomes

Through this project I gained practical experience in:

- Machine Learning Fundamentals
- Linear Regression Mathematics
- Logistic Regression Mathematics
- Gradient Descent Optimization
- Feature Engineering
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Custom Fraud Dataset Generation
- Explainable AI
- Model Evaluation

---

# 🚀 Future Enhancements

- Streamlit Web Application
- Interactive Dashboard
- Real-Time Property API Integration
- Multi-city Property Analysis
- Advanced Explainable AI
- Deep Learning Models
- Cloud Deployment

---

# ⭐ Why This Project?

Most house price prediction projects stop after predicting the property's price.

This project extends beyond traditional prediction by:

- Implementing both Linear Regression and Logistic Regression completely from scratch.
- Designing a custom fraud detection pipeline.
- Engineering fraud-related features.
- Providing fraud probability estimation.
- Generating explainable fraud analysis.
- Producing a complete property analysis report.

It demonstrates not only machine learning implementation but also problem-solving, feature engineering, explainability, and end-to-end system design.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository, open issues, or submit pull requests.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
