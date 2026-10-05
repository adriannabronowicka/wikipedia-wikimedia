import pandas as pd

df8 = pd.read_csv("../csv_files/8-edycje_uzytkownikow_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df8.shape)

print("\n--- TYPY I BRAKI ---")
print(df8.info())

print("\n--- PRÓBKA DANYCH ---")
print(df8.head())