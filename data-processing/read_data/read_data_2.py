import pandas as pd

df2 = pd.read_csv("../csv_files/2-nowe_artykuly_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df2.shape)

print("\n--- TYPY I BRAKI ---")
print(df2.info())

print("\n--- PRÓBKA DANYCH ---")
print(df2.head())

print(df2["total.content"].sum())