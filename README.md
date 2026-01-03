# Google Sheets Reader (No Browser)

Read Google Sheets data on Windows without opening Google Sheets in a browser.
Exports data to CSV and Excel using the Google Sheets API.

## Features
- Read-only access
- No Google Sheets UI
- Works on Windows
- Export to CSV and XLSX
- GitHub-ready structure

## Requirements
- Python 3.9+
- Google Cloud project
- Google Sheets API enabled

## Setup
Create Google API credentials (one-time setup)

- You must do this once in a browser (no way around this).
- Go to Google Cloud Console
- Create a project
- Enable Google Sheets API
- Create OAuth Client ID

Download credentials.json and place it to config folder

## Configuration (.env)
Copy the example file:
```bash
cp .env.example .env 
```
Edit .env:
```
SPREADSHEET_ID=your_sheet_id
RANGE_NAME=Sheet1!A1:D500
GOOGLE_CREDENTIALS_PATH=config/credentials.json
```
## Run the script
```
python src/fetch_sheet.py
```

## Clone repo
```bash
git clone https://github.com/cspartho/google-sheets-reader.git
cd google-sheets-reader
```
