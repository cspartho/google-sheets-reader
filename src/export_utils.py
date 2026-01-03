import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def export_to_csv(data, filename="output.csv"):
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_DIR / filename, index=False)

def export_to_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(OUTPUT_DIR / filename, index=False)
