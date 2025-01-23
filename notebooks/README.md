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
