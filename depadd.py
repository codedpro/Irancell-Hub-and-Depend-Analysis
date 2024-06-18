import pandas as pd
import re

def add_col_from_file(file1_path, file2_path, output_file_path):
    sheets_dict1 = pd.read_excel(file1_path, sheet_name=None)
    sheets_dict2 = pd.read_excel(file2_path, sheet_name=None)
    
    writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

    for sheet_name in sheets_dict1.keys():
        if sheet_name in sheets_dict2:
            df1 = sheets_dict1[sheet_name]
            df2 = sheets_dict2[sheet_name]
            
            site_column_index = 0
            col1_column_index = 0

            new_col = []
            for site1 in df1.iloc[:, site_column_index]:
                site1_escaped = re.escape(str(site1))
                
                pattern = f'.*{site1_escaped}.*'

                matching_row = df2[df2.iloc[:, col1_column_index].str.contains(pattern, na=False, case=False, regex=True)]

                if not matching_row.empty:
                    col2_value = matching_row.iloc[0, 1]
                else:
                    col2_value = None

                new_col.append(col2_value)

            df1['Number of Depends'] = new_col
            df1.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            print(f"Sheet {sheet_name} not found in {file2_path}")

    writer._save()

