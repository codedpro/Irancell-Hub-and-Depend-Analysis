import pandas as pd

def check_columns_equal(input_file):
    df = pd.read_excel(input_file, header=None)
    
    for index, row in df.iterrows():
        if row[0] == row[1]:
            print(f"Row {index + 1}: col1 == col2 -> {row[0]}")

input_file = "updated_file1.xlsx"

check_columns_equal(input_file)
