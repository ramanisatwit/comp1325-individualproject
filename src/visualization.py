import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/engineered_data.csv')

# Question 1: Tuition vs Average Graduation Rate
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='tuition_cost', y='avg_graduation_rate')
plt.title("Tuition vs Average Graduation Rate")
plt.xlabel("Tuition Cost")
plt.ylabel("Average Graduation Rate")
plt.grid(True)
plt.show()

# Question 2: Selectivity vs Engineered Average Graduation Rate
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='selectivity_score', y='avg_graduation_rate')
plt.title("Selectivity vs Average Graduation Rate")
plt.xlabel("Selectivity Score")
plt.ylabel("Average Graduation Rate (%)")
plt.grid(True)
plt.show()  

# Question 3: Correlation between Engineered Features and Average Graduation Rates
features = ['avg_graduation_rate', 'graduation_rate_improvement', 'selectivity_score', 'cohort_size']
plt.figure(figsize=(10, 8))
sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation between Engineered Features and Average Graduation Rates")
plt.show()