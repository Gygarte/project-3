import pandas as pd

def write_to_excell(file_path, data_frame, sheet_name):
    with pd.ExcelWriter(file_path, mode='a') as f:
        data_frame.to_excel(f, sheet_name=sheet_name)
