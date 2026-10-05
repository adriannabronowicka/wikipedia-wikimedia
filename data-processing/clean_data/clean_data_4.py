import pandas as pd

df4 = pd.read_csv("../csv_files/4-aktywni_edytorzy_monthly.csv")

# Convert date format and extract date components / Zmiana formatu daty, utworzenie nowych kolumn
dt_series = pd.to_datetime(df4["month"])
df4["Data"] = dt_series.dt.date
df4["Rok"] = dt_series.dt.year
df4["Miesiąc"] = dt_series.dt.month

# Rename value column / Zmiana nazwy kolumny z wartościami
df4["Liczba Aktywnych Edytorów"] = df4["total.total"]

# Select columns / Wybór kolumn
df4_clean = df4[
    ["Data", "Rok", "Miesiąc", "Liczba Aktywnych Edytorów"]
].copy()

# Fill missing values with zeros and convert to int64 / Konwersja na typ int64 int64 oraz uzupełnienie braków zerami
df4_clean["Liczba Aktywnych Edytorów"] = (
    df4_clean["Liczba Aktywnych Edytorów"].fillna(0).astype("int64")
)

# Export clean dataset to CSV / Zapis do pliku CSV
df4_clean.to_csv("../csv_files_clean/4_aktywni_edytorzy_clean.csv", index=False, encoding="utf-8")