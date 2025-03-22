import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define API scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from JSON key file
creds = ServiceAccountCredentials.from_json_keyfile_name("your_project.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
spreadsheet = client.open("nubtk lookup")  # Change to your sheet name
sheet = spreadsheet.sheet1  # Select the first sheet

# Read all data from the Google Sheet
names = sheet.col_values(2)  # names are in column B
print("Names in Google Sheet:", names)

# Write a test entry in Column B (Profiles)
sheet.update_cell(2, 2, "https://linkedin.com/in/test-profile")  # (Row 2, Column B)
print("Profile link added!")
