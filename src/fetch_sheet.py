import os
from pathlib import Path
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from export_utils import export_to_csv, export_to_excel

# Load environment variables
load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = os.getenv("RANGE_NAME")
CREDENTIALS_PATH = Path(os.getenv("GOOGLE_CREDENTIALS_PATH", ""))


def validate_env():
    missing = []
    if not SPREADSHEET_ID:
        missing.append("SPREADSHEET_ID")
    if not RANGE_NAME:
        missing.append("RANGE_NAME")
    if not CREDENTIALS_PATH.exists():
        missing.append("GOOGLE_CREDENTIALS_PATH")

    if missing:
        raise RuntimeError(
            f"Missing or invalid environment variables: {', '.join(missing)}"
        )


def main():
    validate_env()

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

    formatted = [
        dict(zip(headers, row + [""] * (len(headers) - len(row))))
        for row in rows
    ]

    export_to_csv(formatted)
    export_to_excel(formatted)

    print("✅ Export completed successfully.")


if __name__ == "__main__":
    main()
