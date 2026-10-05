import pandas as pd

df4 = pd.read_csv("../csv_files/4-aktywni_edytorzy_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df4.shape)

print("\n--- TYPY I BRAKI ---")
print(df4.info())

print("\n--- PRÓBKA DANYCH ---")
print(df4.head())