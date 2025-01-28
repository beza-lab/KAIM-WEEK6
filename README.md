Credit Scoring Model
Task 2 - Exploratory Data Analysis (EDA)
Overview of the Data:
Understand the structure of the dataset, including the number of rows, columns, and data types.
Summary Statistics
Understand the central tendency, dispersion, and shape of the dataset’s distribution.
Distribution of Numerical Features
Visualize the distribution of numerical features to identify patterns, skewness, and potential outliers.
Distribution of Categorical Features
Analyzing the distribution of categorical features provides insights into the frequency and variability of categories.
Correlation Analysis
Understanding the relationship between numerical features.
Identifying Missing Values
Identify missing values to determine missing data and decide on appropriate imputation strategies.
Outlier Detection
Use box plots to identify outliers.

Task 3 - Feature Engineering
Create Aggregate Features
	Example:
Total Transaction Amount: Sum of all transaction amounts for each customer.
Average Transaction Amount: Average transaction amount per customer.
Transaction Count: Number of transactions per customer.
Standard Deviation of Transaction Amounts: Variability of transaction amounts per customer.
Extract Features
	Example:
Transaction Hour: The hour of the day when the transaction occurred.
Transaction Day: The day of the month when the transaction occurred.
Transaction Month: The month when the transaction occurred.
Transaction Year: The year when the transaction occurred.
Encode Categorical Variables
Convert categorical variables into numerical format by using:
One-Hot Encoding: Converts categorical values into binary vectors.
Label Encoding: Assigns a unique integer to each category.
Handle Missing Values
	Use imputation or Removal to handle missing values
Imputation: Filling missing values with mean, median, mode, or using more methods like KNN imputation.
Removal: Removing rows or columns with missing values if they are few.
Normalize/Standardize Numerical Features
Normalization and standardization are scaling techniques used to bring all numerical features onto a similar scale.
Normalization: Scales the data to a range of [0, 1].
Standardization: Scales the data to have a mean of 0 and a standard deviation of 1.

Task 4 - Default estimator and WoE binning 

The purpose of any credit scoring system is to classify users as high risk or low-risk. High-risk groups are those with high likelihood of default - those who do not pay the loan principal and interest in the specified time frame. 

To simplify the process, here we want to construct a variable based on RFMS formalism that classifies users into good (high RFMS score) and bad (low RFMS score). 
Construct a default estimator (proxy)
By visualizing all transactions in the RFMS space, establish a boundary where users are classified as high and low RFMS scores.
Assign all users the good and bad label
Perform Weight of Evidence (WoE) binning 

Task 5 - Modelling

Model Selection and Training
Split the Data
Splitting the data into training and testing sets helps evaluate the model’s performance on unseen data.
Choose Models
		Choose at least two models  from the following:
Logistic Regression
Decision Trees
Random Forest
Gradient Boosting Machines (GBM)
Train the Models
Train the models on the training data
Hyperparameter Tunning
Improve model performance using hyperparameter tuning, use techniques like:
Grid Search
Random Search
Model Evaluation
Assess model performance using the following metrics
Accuracy: The ratio of correctly predicted observations to the total observations.
Precision: The ratio of correctly predicted positive observations to the total predicted positives.
Recall (Sensitivity): The ratio of correctly predicted positive observations to all observations in the actual class.
F1 Score: The weighted average of Precision and Recall.
ROC-AUC: Area Under the Receiver Operating Characteristic Curve, which measures the ability of the model to distinguish between classes.

Task 6 - Model Serving API Call

Create a REST API to serve the trained machine-learning models for real-time predictions.
Choose a framework:
Select a suitable framework for building REST APIs (e.g., Flask, FastAPI, Django REST framework).
Load the model:
Use the model from Task 4 to load the trained machine-learning model.
Define API endpoints:
Create API endpoints that accept input data and return predictions.
Handle requests:
Implement logic to receive input data, preprocess it, and make predictions using the loaded model.
Return predictions:
Format the predictions and return them as a response to the API call.
Deployment:
Deploy the API to a web server or cloud platform.