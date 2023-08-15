
import pandas as pd
class Formatter:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def create_df(self):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(self.csv_filename)

            # Perform any necessary formatting operations on the DataFrame
            # For example, you can remove leading/trailing spaces from column names
            df.columns = df.columns.str.strip()
            numeric_columns = ['Revenue', 'Profit', 'Cost', 'Expense', 'Income', 'Price', 'Salary', 'Investment']
            for col in numeric_columns:
                df[col] = df[col].str.replace('$', '')
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # Group by 'Master' and 'ID', then calculate sum for all numeric columns
            grouped_data = df.groupby(['Master', 'ID']).sum()

            # Return the formatted DataFrame and Grouped
            return df,grouped_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


# Usage
if __name__ == "__main__":
    Formatter_obj = Formatter("sample.csv")
    df,grouped = Formatter_obj.create_df()

    if df is not None:
        print("Formatted DataFrame:")
        print(df)
        print("Grouped :")
        print(grouped)