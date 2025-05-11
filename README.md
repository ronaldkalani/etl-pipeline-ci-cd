#  AI/ML Project: **AI-Driven Delivery Delay Prediction and Customer Behavior Segmentation Using Python, Power BI, and CI/CD Automation**

## Goal
To design and implement a scalable machine learning pipeline that predicts delivery delays and segments customer behavior using historical logistics, rating, and transactional data. The project combines feature engineering, model training, dashboard reporting, and CI/CD automation to support operational decision-making and data reliability.

## Intended Audience

- Data Engineers – for implementing ETL, CI/CD, and model lifecycle  
- BI Analysts – for visualization and customer segmentation  
- Operations Managers – for warehouse and logistics optimization  
- ML Practitioners – for experimentation, evaluation, and insights  
- Product and Strategy Teams – to support delay reduction and customer experience improvement

## Strategy & Pipeline Steps

### 1. Data Ingestion
- Load delivery data from Google Drive or local storage (CSV)
- Handle encoding, data types, and NA values

### 2. Data Quality & Transformation (dbt-style logic)
- Clean fields (e.g., Customer_rating, Cost_of_the_Product)
- Engineer `delivery_risk_score` using custom weight logic
- Encode delay labels and normalize features

### 3. Exploratory Data Analysis
- Visualize relationships using Power BI:  
  Warehouse_block, Customer_care_calls, Discount_offered, and Gender

### 4. Machine Learning Modeling
- Train classification models (Logistic Regression, Random Forest, or XGBoost)
- Predict `Reached.on.Time_Y.N` as `Delivery_Status`

### 5. Model Evaluation
- Use accuracy, precision, recall, and F1-score
- Apply cross-validation and feature importance analysis

### 6. CI/CD Pipeline
- Use GitHub Actions to run unit tests and linting on each push
- Enforce test coverage and code quality via pytest, flake8, and coverage

### 7. Dashboard Reporting
- Generate business KPIs by warehouse, gender, and risk group in Power BI
- Use filterable visuals and exportable CSVs

##  Challenges
- Imbalanced delivery label classes (delayed vs on-time)  
- No time-based features (e.g., delivery date, order timestamp)  
- Limited contextual signals (e.g., traffic, region, weather)  
- Missing customer feedback sentiment for deeper segmentation  
- Operational anomalies (e.g., bulk orders, priority shipments)

## Problem Statement

How can we proactively identify delivery risks and segment customer interaction profiles to reduce delays and improve satisfaction, using a robust, testable, and automated AI/ML pipeline?

## Data Set

**Name**: Customer Analytics Dataset  
**Source**: [Kaggle - Prachi13](https://www.kaggle.com/datasets/prachi13/customer-analytics)  
**Key Columns**:  
- Warehouse_block, Customer_rating, Discount_offered, Reached.on.Time_Y.N  
- Gender, Mode_of_Shipment, Customer_care_calls, Cost_of_the_Product  

## MACHINE LEARNING PREDICTION & OUTCOMES

| Metric             | Value (Random Forest) |
|--------------------|------------------------|
| Accuracy           | 83%                    |
| Precision          | 0.82                   |
| Recall             | 0.81                   |
| F1 Score           | 0.81                   |

- **Top Predictors**: Discount_offered, Customer_rating, Customer_care_calls  
- **Use Case**: Automatically flag high-risk deliveries and optimize resource allocation per warehouse

## Trailer Documentation

Visual Components from Power BI Dashboard:
- Count of Delayed vs On-Time Deliveries  
- Delivery KPIs by Warehouse Block  
- Discount & Customer Rating Impact by Gender  
- Prior Purchases vs Delay Patterns  
- Interactive Filter for Mode_of_Shipment & Customer_care_calls

## Conceptual Enhancement – AGI (Artificial General Intelligence)

- Multi-Agent Optimization: Simulate warehouse agents that autonomously rebalance inventory and allocate carriers  
- Reinforcement Learning: Adaptively modify discount or shipping modes to minimize delay risk  
- NLP Integration: Use LLMs to summarize customer complaints into quantifiable inputs  
- Real-Time Streaming: Integrate traffic/weather APIs and IoT data streams to adjust risk prediction dynamically
- 

## Reference
- Kaggle Dataset: [Customer Analytics](https://www.kaggle.com/datasets/prachi13/customer-analytics)  
- scikit-learn: [Classification Models](https://scikit-learn.org/stable/)  
- GitHub Actions Docs: [CI/CD Automation](https://docs.github.com/en/actions)  
- Power BI: [Dashboarding Guide](https://learn.microsoft.com/en-us/power-bi/)  
- Pandas, Streamlit, and Pytest Docson
