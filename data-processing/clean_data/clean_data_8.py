import pandas as pd

df8 = pd.read_csv("../csv_files/8-edycje_uzytkownikow_monthly.csv")

# Clean up the date string by replacing incorrect hyphens and removing  zeros / Usunięcie zbędnych myślników i zer
clean_str = (
    df8["month"]
    .str.replace("-1-0-", "-10-", regex=False)
    .str.replace("-1-1-", "-11-", regex=False)
    .str.replace("-1-2-", "-12-", regex=False)
    .str.replace("-0-", "-", regex=False)
)

# Extract year and month components / Wyciągnięcie rok i miesiąca
extracted = clean_str.str.extract(r"(\d{4}).*?(\d{1,2})")

# Construct standardized date string / Tworzenie pełnej daty
data_str = extracted[0] + "-" + extracted[1].str.zfill(2) + "-01"

# Create clean date and numeric time dimension columns / Stworzenie kolumny z datą oraz numerycznymi składowymi czasu
df8["Data"] = pd.to_datetime(data_str).dt.date
df8["Rok"] = extracted[0].astype("int64")
df8["Miesiąc"] = extracted[1].astype("int64")

# Map editor types / Tłumaczenie typu edytorów
editor = {
    "anonymous": "Anonimowy",
    "user": "Zarejestrowany użytkownik",
    "group-bot": "Bot (Oficjalny)",
    "name-bot": "Bot (Wg nazwy)",
}
df8["Typ Edytora"] = df8["editor_type"].map(editor).fillna(df8["editor_type"])

# Fill missing values with zeros and convert to int64 / Konwersja na typ int64 int64 oraz uzupełnienie braków zerami
df8["Edycje Artykułów"] = df8["total.content"].fillna(0).astype("int64")
df8["Edycje Pozaartykułowe"] = df8["total.non-content"].fillna(0).astype("int64")

# Select columns / Wybór kolumn
df8_clean = df8[
    [
        "Data",
        "Rok",
        "Miesiąc",
        "Typ Edytora",
        "Edycje Artykułów",
        "Edycje Pozaartykułowe",
    ]
].copy()

# Export clean dataset to CSV / Zapis do CSV
df8_clean.to_csv("../csv_files_clean/8_edycje_uzytkownikow_clean.csv", index=False, encoding="utf-8")