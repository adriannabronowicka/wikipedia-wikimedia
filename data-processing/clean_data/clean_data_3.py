import pandas as pd


df3 = pd.read_csv("../csv_files/3-nowe_rejestracje_monthly.csv")

# Convert date format and extract date components / Zmiana formatu daty, utworzenie nowych kolumn
dt_series = pd.to_datetime(df3["month"])
df3["Data"] = dt_series.dt.date
df3["Rok"] = dt_series.dt.year
df3["Miesiąc"] = dt_series.dt.month

# Rename value column / Zmiana nazwy kolumny z wartościami
df3["Liczba Nowych Rejestracji"] = df3["total.total"]

# Select columns / Wybór kolumn
df3_clean = df3[
    ["Data", "Rok", "Miesiąc", "Liczba Nowych Rejestracji"]
].copy()

# Fill missing values with zeros and convert to int64 / Konwersja na typ int64 oraz uzupełnienie braków zerami
df3_clean["Liczba Nowych Rejestracji"] = (
    df3_clean["Liczba Nowych Rejestracji"].fillna(0).astype("int64")
)

# Export clean dataset to CSV / Zapis do pliku CSV
df3_clean.to_csv("../csv_files_clean/3_nowe_rejestracje_clean.csv", index=False, encoding="utf-8")