import pandas as pd

df5 = pd.read_csv("../csv_files/5-top_1000_artykulow_monthly.csv")

# Create full date from year and month columns / Tworzenie pełnej daty na podstawie roku i miesiąca
df5["Data"] = pd.to_datetime(
    df5["year"].astype(str) + "-" + df5["month"].astype(str) + "-01"
).dt.date

# Handle missing page IDs (fill NaN with -1 and convert to int64) / Obsługa ID strony (uzupełnienie NaN jako -1 i konwersja na int64)
df5["ID Strony"] = df5["page_id"].fillna(-1).astype("int64")

# Rename columns / Zmiana nazw kolumn
df5["Rok"] = df5["year"]
df5["Miesiąc"] = df5["month"]
df5["Pozycja w Rankingu"] = df5["rank"]
df5["Tytuł Artykułu"] = df5["title"]
df5["Liczba Wyświetleń"] = df5["views"]

# Select columns / Wybór kolumn
df5_clean = df5[
    [
        "Data",
        "Rok",
        "Miesiąc",
        "Pozycja w Rankingu",
        "Tytuł Artykułu",
        "Liczba Wyświetleń",
        "ID Strony",
    ]
].copy()

# Ensure numeric data types / Upewnienie się o typach liczbowych
df5_clean["Liczba Wyświetleń"] = df5_clean["Liczba Wyświetleń"].astype("int64")
df5_clean["Pozycja w Rankingu"] = df5_clean["Pozycja w Rankingu"].astype("int64")

# Export clean dataset to CSV / Zapis do CSV
df5_clean.to_csv("../csv_files_clean/5_top_1000_artykulow_clean.csv", index=False, encoding="utf-8")