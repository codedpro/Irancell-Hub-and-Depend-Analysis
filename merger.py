import pandas as pd

def merge_columns(output: str, cleaned: str):
    df1 = pd.read_excel(output, sheet_name=None)
    df2 = pd.read_excel(cleaned, sheet_name=None)

    all_sites_in_df1 = set()

    for df1_sheet in df1.values():
        all_sites_in_df1.update(df1_sheet['Site'])

    updated_data = {}

    for sheet_name, df2_sheet in df2.items():
        sites_in_file2 = df2_sheet.iloc[:, 0].tolist()

        new_sites = []

        for site in sites_in_file2:
            if site not in all_sites_in_df1:
                new_sites.append(site)
                all_sites_in_df1.add(site)

        new_sites_df = pd.DataFrame(new_sites, columns=['Site'])
        new_sites_df['Hub'] = '-'

        if sheet_name in df1:
            updated_data[sheet_name] = pd.concat([df1[sheet_name], new_sites_df], ignore_index=True)
        else:
            updated_data[sheet_name] = new_sites_df

    with pd.ExcelWriter('updated_file1.xlsx') as writer:
        for sheet_name, df in updated_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
