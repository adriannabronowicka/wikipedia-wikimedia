import pandas as pd

df6 = pd.read_csv("../csv_files/6-polskie_artykuly_w_top_1000_monthly.csv")

# Create full date from year and month columns / Tworzenie pełnej daty na podstawie roku i miesiąca
df6["Data"] = pd.to_datetime(
    df6["year"].astype(str) + "-" + df6["month"].astype(str) + "-01"
).dt.date

# Rename columns / Zmiana nazw kolumn
df6["Rok"] = df6["year"]
df6["Miesiąc"] = df6["month"]
df6["Pozycja w Rankingu"] = df6["rank"]
df6["Tytuł Artykułu"] = df6["title"]
df6["Liczba Wyświetleń"] = df6["views"]
df6["ID Strony"] = df6["page_id"].fillna(-1).astype("int64")

# Select columns / Wybór kolumn
df6_clean = df6[
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
df6_clean["Liczba Wyświetleń"] = df6_clean["Liczba Wyświetleń"].astype("int64")
df6_clean["Pozycja w Rankingu"] = df6_clean["Pozycja w Rankingu"].astype("int64")

# Export clean dataset to CSV / Zapis do CSV
df6_clean.to_csv("../csv_files_clean/6-polskie_artykuly_w_top_1000_clean.csv", index=False, encoding="utf-8")