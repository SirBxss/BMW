import pandas as pd


def list_sheet_names(input_file):
    """
    Lists all sheet names in the given XLSM file.

    :param input_file: Path to the input XLSM file
    :return: List of sheet names
    """
    try:
        xls = pd.ExcelFile(input_file, engine='openpyxl')
        print("Available sheets:", xls.sheet_names)
        return xls.sheet_names
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def convert_xlsm_to_csv(input_file, output_file, sheet_name=None, keep_columns=None):
    """
    Converts a specified sheet (or the first sheet by default) from an XLSM file to a CSV file.
    Keeps only the specified columns if `keep_columns` is provided.

    :param input_file: Path to the input XLSM file
    :param output_file: Path to the output CSV file
    :param sheet_name: Name of the sheet to convert. Defaults to the first sheet if not provided.
    :param keep_columns: List of column indices to keep (0-indexed). Defaults to None (keep all columns).
    """
    try:
        # List all sheets in the file
        xls = pd.ExcelFile(input_file, engine='openpyxl')
        available_sheets = xls.sheet_names

        # Use the specified sheet or the first sheet if not provided
        if sheet_name is None:
            sheet_name = available_sheets[0]
            print(f"No sheet name provided. Defaulting to the first sheet: '{sheet_name}'")
        elif sheet_name not in available_sheets:
            raise ValueError(f"Sheet '{sheet_name}' not found in the file. Available sheets: {available_sheets}")

        # Read the specified sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Keep only the specified columns
        if keep_columns is not None:
            df = df.iloc[:, keep_columns]

        # Write the DataFrame to a CSV file
        df.to_csv(output_file, index=False)
        print(f"Sheet '{sheet_name}' has been successfully converted to '{output_file}'.")
        print(f"Kept columns: {keep_columns}")

    except Exception as e:
        print(f"Error: {e}")


# Example Usage
if __name__ == "__main__":
    input_xlsm = '/Users/amin/PycharmProject/BMW/Data/I20_RL/Inhalt_I20RL.xlsm'  # Replace with your XLSM file path
    output_csv = '/Users/amin/PycharmProject/BMW/Data/I20_RL/output.csv'  # Replace with your desired CSV output path

    # Step 1: List available sheets
    print("Listing available sheets...")
    available_sheets = list_sheet_names(input_xlsm)

    # Step 2: Convert the desired sheet to CSV
    if available_sheets:
        sheet_to_convert = input("Enter the sheet name to convert (or press Enter to use the first sheet): ").strip()
        sheet_to_convert = sheet_to_convert if sheet_to_convert else None  # Default to None if empty

        # Specify columns to keep (0 to 11 = first 12 columns)
        keep_columns = list(range(12))  # Adjust the range as needed
        convert_xlsm_to_csv(input_xlsm, output_csv, sheet_to_convert, keep_columns)
