import pandas as pd

df6 = pd.read_csv("../csv_files/6-polskie_artykuly_w_top_1000_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df6.shape)

print("\n--- TYPY I BRAKI ---")
print(df6.info())

print("\n--- PRÓBKA DANYCH ---")
print(df6.head())