import pandas as pd

# Load the dataset
file_path = '/Users/amin/PycharmProjec/BMW/Data/I20/output.csv'
data = pd.read_csv(file_path)

# Step 1: Set new column headers from the second row (index 1)
data.columns = data.iloc[1]
data_cleaned = data[2:].reset_index(drop=True)

# Step 2: Drop rows with all NaN values
data_cleaned = data_cleaned.dropna(how='all')

# Step 3: Standardize column names (strip whitespace and replace line breaks or special characters)
data_cleaned.columns = [str(col).strip().replace("\n", " ").replace("\\n", " ") for col in data_cleaned.columns]

# Step 4: Fill empty cells in the "Benennung Teil (TAISS)" column with the previous value
column_name = "Benennung Teil (TAISS)"
data_cleaned[column_name] = data_cleaned[column_name].fillna(method='ffill')

# Step 5: Add a new "Title" column as column 0 and assign unique numbers (no "ID" prefix)
data_cleaned.insert(0, "Title", [str(i + 1) for i in range(len(data_cleaned))])

# Step 6: Remove rows where the "Kommentar" column is empty
data_cleaned = data_cleaned.dropna(subset=["Kommentar"])

# Step 7: Remove specified columns (1, 2, 3, 5, and 8 by index after insertion of "Title")
columns_to_remove = [1, 2, 3, 5, 8]  # Adjust indices after adding the "Title" column
data_cleaned = data_cleaned.drop(data_cleaned.columns[columns_to_remove], axis=1)

# Step 8: Rename the columns to match the new headers
new_headers = [
    "Title_1",
    "BenennungTeil_1",
    "Programmnummer_1",
    "Laufzeit_1",
    "Kommentar_1",
    "Sachnummer_1",
    "ZI_1",
    "AI_1"
]
data_cleaned.columns = new_headers

# Step 9: Save the cleaned and updated dataset to a new CSV file
output_path = '/Users/amin/PycharmProjec/BMW/Data/I20/cleaned.csv'
data_cleaned.to_csv(output_path, index=False)

# Display a preview of the cleaned dataset
print(data_cleaned.head())
