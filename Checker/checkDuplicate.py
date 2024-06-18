import pandas as pd

def find_duplicates(df):
    """
    Find duplicates in the first column of a DataFrame.
    """
    duplicates = df[df.duplicated(df.columns[0])]
    return duplicates

def check_duplicates_in_excel(file_path):
    """
    Check for duplicates in the first column of each sheet in an Excel file.
    """
    xls = pd.ExcelFile(file_path)
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        duplicates = find_duplicates(df)
        
        if not duplicates.empty:
            print(f"Duplicates found in sheet '{sheet_name}':")
            print(duplicates)
            print()

check_duplicates_in_excel('updated_file1.xlsx')
