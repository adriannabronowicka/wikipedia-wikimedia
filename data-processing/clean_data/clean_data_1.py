import pandas as pd

df1 = pd.read_csv("../csv_files/1-ogladalnosc_monthly.csv")

# Convert date format and extract date components / Zmiana formatu daty, utworzenie nowych kolumn
dt_series = pd.to_datetime(df1["month"])
df1["Data"] = dt_series.dt.date
df1["Rok"] = dt_series.dt.year
df1["Miesiąc"] = dt_series.dt.month

# Fill missing values with zeros / Wypełnienie braków zerami
df1["total.mobile-app"] = df1["total.mobile-app"].fillna(0)

# Unpivot
df1_transformed = df1.melt(
    id_vars=["Data", "Rok", "Miesiąc", "agent"],
    value_vars=["total.mobile-app", "total.desktop", "total.mobile-web"],
    var_name="Urządzenie",
    value_name="Liczba Wyświetleń",
)

# Value mapping (English to Polish) / Tłumaczenie wartości
device_dictionary = {
    "total.mobile-app": "Aplikacja Mobilna",
    "total.desktop": "Komputer (Desktop)",
    "total.mobile-web": "Przeglądarka Mobilna",
}

agent_dictionary = {
    "user": "Użytkownik (Człowiek)",
    "spider": "Bot Wyszukiwarki",
    "automated": "Skrypt Automatyczny",
}

df1_transformed["Urządzenie"] = df1_transformed["Urządzenie"].map(
    device_dictionary
)
df1_transformed["Typ Użytkownika"] = df1_transformed["agent"].map(
    agent_dictionary
)

# Select columns / Wybór kolumn
df1_clean = df1_transformed[
    [
        "Data",
        "Rok",
        "Miesiąc",
        "Typ Użytkownika",
        "Urządzenie",
        "Liczba Wyświetleń",
    ]
].copy()

df1_clean["Liczba Wyświetleń"] = df1_clean["Liczba Wyświetleń"].astype("int64")

# Export clean dataset to CSV / Zapis do CSV
df1_clean.to_csv("../csv_files_clean/1_ogladalnosc_monthly_clean.csv", index=False, encoding="utf-8")