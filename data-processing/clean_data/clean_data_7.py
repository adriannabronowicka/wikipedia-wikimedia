import pandas as pd

df7 = pd.read_csv("../csv_files/7-top_100_najczesciej_edytowanych_artykulow_monthly.csv")

# Create full date from year and month columns / Tworzenie pełnej daty na podstawie roku i miesiąca
df7["Data"] = pd.to_datetime(
    df7["year"].astype(str) + "-" + df7["month"].astype(str) + "-01"
).dt.date

# Handle missing page IDs (fill NaN with -1 and convert to int64) / Obsługa ID strony (uzupełnienie NaN jako -1 i konwersja na int64)
df7["ID Strony"] = df7["page_id"].fillna(-1).astype("int64")

# Rename columns / Zmiana nazw kolumn
df7["Rok"] = df7["year"]
df7["Miesiąc"] = df7["month"]
df7["Pozycja w Rankingu"] = df7["rank"]
df7["Tytuł Artykułu"] = df7["title"]
df7["Liczba Edycji"] = df7["edits"]

# Select columns / Wybór kolumn
df7_clean = df7[
    [
        "Data",
        "Rok",
        "Miesiąc",
        "Pozycja w Rankingu",
        "Tytuł Artykułu",
        "Liczba Edycji",
        "ID Strony",
    ]
].copy()

# Ensure numeric data types / Upewnienie się o typach liczbowych
df7_clean["Liczba Edycji"] = df7_clean["Liczba Edycji"].fillna(0).astype("int64")
df7_clean["Pozycja w Rankingu"] = df7_clean["Pozycja w Rankingu"].astype("int64")

# Export clean dataset to CSV / Zapis do CSV
df7_clean.to_csv(
    "../csv_files_clean/7_top_100_najczesciej_edytowanych_clean.csv", index=False, encoding="utf-8"
)