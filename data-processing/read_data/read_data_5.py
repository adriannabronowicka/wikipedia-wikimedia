import pandas as pd

df5 = pd.read_csv("../csv_files/5-top_1000_artykulow_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df5.shape)

print("\n--- TYPY I BRAKI ---")
print(df5.info())

print("\n--- PRÓBKA DANYCH ---")
print(df5.head())

# Filtrowanie wierszy, gdzie page_id jest puste (NaN)
null_rows = df5[df5["page_id"].isna()]

# Wyświetlenie pierwszych kilku brakujących wierszy
print(f"Liczba wierszy bez ID: {len(null_rows)}")
print(null_rows.head())


