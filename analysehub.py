import pandas as pd
from tqdm import tqdm
import openpyxl

def get_highest_row(sheet, site, progress_bar=None):
    site_rows = (sheet.iloc[:, 1:] == site).any(axis=1)
    if site_rows.any():
        highest_row = site_rows[::-1].idxmax()
        if progress_bar:
            progress_bar.update(1)
        return highest_row
    return -1

def analyze(input_file : str):
    wb = openpyxl.load_workbook(input_file)
    with pd.ExcelWriter('output.xlsx') as writer:
        for sheet_name in wb.sheetnames:
            sheet = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

            output_data = {'Site': [], 'Hub': []}
            processed_sites = set()

            total_iterations = sum(len(sheet[col].dropna().unique()) for col in range(1, len(sheet.columns)))
            progress_bar = tqdm(total=total_iterations, desc=f"Processing {sheet_name}")

            unique_first_column = sheet.iloc[:, 0].drop_duplicates()

            for cell in unique_first_column:
                highest_row = get_highest_row(sheet, cell, progress_bar)
                if highest_row != -1:
                    hub_site = sheet.iloc[highest_row, 0]
                    if cell.strip() and hub_site.strip() and cell != hub_site:
                        output_data['Site'].append(cell)
                        output_data['Hub'].append(hub_site)
                    processed_sites.add(cell)

            for cell in unique_first_column:
                if cell not in processed_sites:
                    output_data['Site'].append(cell)
                    output_data['Hub'].append("-")

            output_df = pd.DataFrame(output_data)
            output_df.to_excel(writer, sheet_name=sheet_name, index=False)

            progress_bar.close()
