from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from pathlib import Path
from export_utils import export_to_csv, export_to_excel

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

CREDENTIALS_PATH = Path("config/credentials.json")

SPREADSHEET_ID = "PASTE_YOUR_SHEET_ID_HERE"
RANGE_NAME = "Sheet1!A1:Z1000"


def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_PATH, SCOPES
    )
    creds = flow.run_local_server(port=0)

    service = build("sheets", "v4", credentials=creds)

    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME
    ).execute()

    values = result.get("values", [])

    if not values:
        print("No data found.")
        return

    headers = values[0]
    rows = values[1:]

    formatted = [dict(zip(headers, row)) for row in rows]

    export_to_csv(formatted)
    export_to_excel(formatted)

    print("Export completed successfully.")


if __name__ == "__main__":
    main()
