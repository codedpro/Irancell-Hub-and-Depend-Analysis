from cleanDep import clean
from analysehub import analyze
from merger import merge_columns
from depadd import add_col_from_file


clean('DepCount-MTNi.xlsx', 'cleaned_file.xlsx')
analyze('cleaned_file.xlsx')
merge_columns("output.xlsx", "cleaned_file.xlsx")
add_col_from_file("updated_file1.xlsx", "DepCount-MTNi.xlsx", "Analyzed DepCount-MTNi.xlsx")
