import pandas as pd

df3 = pd.read_csv("../csv_files/3-nowe_rejestracje_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df3.shape)

print("\n--- TYPY I BRAKI ---")
print(df3.info())

print("\n--- PRÓBKA DANYCH ---")
print(df3.head())