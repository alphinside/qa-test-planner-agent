from google.auth import default
import gspread

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds, _ = default(scopes=scopes)
client = gspread.authorize(creds)
spreadsheet = client.open("test")
