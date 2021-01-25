import gspread
import pandas as pd

class GoogleSheetManager:
    gc = gspread.service_account("google_api_key.json")
    gsheet_filename = ""
    worksheet = None
    csv_data = None

    def __init__(self, gsheet_filename, csv_data):
        self.gsheet_filename = gsheet_filename
        self.csv_data = csv_data
        self._open_worksheet(gsheet_filename)

    def _open_worksheet(self, gsheet_filename):
        self.worksheet = self.gc.open(gsheet_filename).sheet1

    # Create Methods

    def add_data(self):
        self.worksheet.update([self.csv_data.columns.values.tolist()] + self.csv_data.values.tolist())