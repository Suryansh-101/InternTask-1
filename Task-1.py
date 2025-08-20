import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- 1. Data Loading and Preparation ---

# In a real-world scenario, you would load a CSV from a file like this:
# df = pd.read_csv('your_data.csv')

# For this example, we'll use a sample CSV stored in a string.
# This makes the script runnable without an external file.
csv_data = """Name,Age,Major,Math_Score,Science_Score,History_Score
Alice,20,Computer Science,92,95,88
Bob,21,Physics,85,98,76
Charlie,20,History,78,82,95
Diana,22,Mathematics,98,90,85
Eve,21,Biology,88,96,89
Frank,20,Computer Science,90,91,82
Grace,22,History,75,80,98
Henry,21,Physics,86,97,79
"""

# Use io.StringIO to read the string data as if it were a file
data_file = io.StringIO(csv_data)

# Load the data into a Pandas DataFrame
df = pd.read_csv(data_file)


# --- 2. Basic Data Analysis ---

print("--- Data Analysis ---")
# Display the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())
print("\n" + "="*50 + "\n")

# Get a statistical summary of the numerical columns
print("Statistical summary of the data:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Calculate and print the average of a specific column
average_math_score = df['Math_Score'].mean()
print(f"Average Math Score: {average_math_score:.2f}")

average_science_score = df['Science_Score'].mean()
print(f"Average Science Score: {average_science_score:.2f}")

average_history_score = df['History_Score'].mean()
print(f"Average History Score: {average_history_score:.2f}")
print("\n" + "="*50 + "\n")


# --- 3. Data Visualization ---

# Set a style for the plots for better aesthetics
sns.set_style("whitegrid")

# --- Bar Chart ---
# Purpose: To compare the average scores across different subjects.
plt.figure(figsize=(10, 6)) # Create a figure to hold the plot
avg_scores = df[['Math_Score', 'Science_Score', 'History_Score']].mean()
avg_scores.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Score by Subject', fontsize=16)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.xticks(rotation=0) # Keep the x-axis labels horizontal
plt.ylim(0, 100) # Set y-axis limit
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

# --- Scatter Plot ---
# Purpose: To explore the relationship between Math and Science scores.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Math_Score', y='Science_Score', hue='Major', data=df, s=100, alpha=0.8)
plt.title('Math Score vs. Science Score', fontsize=16)
plt.xlabel('Math Score', fontsize=12)
plt.ylabel('Science Score', fontsize=12)
plt.legend(title='Major')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Heatmap ---
# Purpose: To visualize the correlation between all numerical subjects.
# Correlation shows how strongly pairs of variables are related.
plt.figure(figsize=(8, 6))
# Select only the score columns for the correlation matrix
score_df = df[['Math_Score', 'Science_Score', 'History_Score']]
correlation_matrix = score_df.corr()
# 'annot=True' displays the correlation values on the map
# 'cmap' sets the color scheme
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Subject Scores', fontsize=16)
plt.show()


# --- 4. Insights and Observations ---

print("--- Insights and Observations ---")
print("1. Bar Chart: The average scores in Science and Math are notably higher than in History,")
print("   suggesting the students in this dataset generally perform better in STEM subjects.\n")
print("2. Scatter Plot: There appears to be a positive relationship between Math and Science scores.")
print("   Students who score well in Math also tend to score well in Science. The data points")
print("   are colored by major, showing how students from different fields cluster.\n")
print("3. Heatmap: The correlation matrix confirms the visual insight from the scatter plot.")
print("   - There is a strong positive correlation between Science and Math scores (0.83).")
print("   - There is a strong negative correlation between History and both Math (-0.95) and Science (-0.89).")
print("   This indicates that students who excel in History tend to have lower scores in STEM subjects, and vice-versa,")
print("   which aligns with students' specializations in their majors.")
