import pandas as pd

# Load the processed file
input_file = '/Users/amin/PycharmProjec/BMW/Data/I20/cleaned.csv'
output_file = '/Users/amin/PycharmProjec/BMW/Data/I20/cleaned_no_quotes.csv'

# Read the CSV file as a plain text file
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Remove surrounding quotes and replace escaped quotes (double quotes within fields)
cleaned_lines = [line.strip().strip('"').replace('""', '"') for line in lines]

# Save the cleaned content to a new CSV file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("\n".join(cleaned_lines))

print(f"Cleaned CSV file saved to {output_file}")
