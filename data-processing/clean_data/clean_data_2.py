import pandas as pd

df2 = pd.read_csv("../csv_files/2-nowe_artykuly_monthly.csv")

# Convert date format and extract date components / Zmiana formatu daty, utworzenie nowych kolumn
dt_series = pd.to_datetime(df2["month"])
df2["Data"] = dt_series.dt.date
df2["Rok"] = dt_series.dt.year
df2["Miesiąc"] = dt_series.dt.month

# Rename value column / Zmiana nazwy kolumny z wartościami
df2["Liczba Nowych Artykułów"] = df2["total.content"]

# Select columns / Wybór kolumn
df2_clean = df2[
    ["Data", "Rok", "Miesiąc", "Liczba Nowych Artykułów"]
].copy()

# Fill missing values with zeros and convert to int64 / Konwersja na typ int64 int64 oraz uzupełnienie braków zerami
df2_clean["Liczba Nowych Artykułów"] = (
    df2_clean["Liczba Nowych Artykułów"].fillna(0).astype("int64")
)

# Export clean dataset to CSV / Zapis do pliku CSV
df2_clean.to_csv("../csv_files_clean/2_nowe_artykuly_clean.csv", index=False, encoding="utf-8")