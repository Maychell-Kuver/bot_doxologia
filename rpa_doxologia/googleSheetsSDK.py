import gspread
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1kPwmEZc7dP589Vc962i1VMXiNiGbsbPpcRo3l3uK338/export?format=csv'
df = pd.read_csv(url)
print(df.head())

class googleSheetsSDK:
    def __init__(self):
        self.sheet_url = "https://docs.google.com/spreadsheets/d/1kPwmEZc7dP589Vc962i1VMXiNiGbsbPpcRo3l3uK338/export?format=csv"
        
    def read_sheet(self):
        df = pd.read_csv(self.sheet_url)