import openpyxl
import re

def clean(filename, output_filename):
    wb = openpyxl.load_workbook(filename)
    cleaned_wb = openpyxl.Workbook()

    pattern = re.compile(r'[a-zA-Z]\d{4}')
    
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        cleaned_sheet = cleaned_wb.create_sheet(title=sheet_name)

        for row in sheet.iter_rows():
            cleaned_row = []
            for cell in row:
                cell_value = str(cell.value)
                match = pattern.search(cell_value)
                if match:
                    index = match.start()
                    cleaned_value = cell_value[index:index+5]
                    cleaned_row.append(cleaned_value)
            cleaned_sheet.append(cleaned_row)

    default_sheet = cleaned_wb.active
    cleaned_wb.remove(default_sheet)

    cleaned_wb.save(output_filename)