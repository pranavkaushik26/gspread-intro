import pandas as pd

from google_sheet import GoogleSheetManager

googlesheet_name = "gspread sample"
data = pd.read_csv("datasheet.csv")

manager = GoogleSheetManager(googlesheet_name, data)

manager.add_data()