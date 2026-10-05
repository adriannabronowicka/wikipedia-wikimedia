import pandas as pd

df7 = pd.read_csv("../csv_files/7-top_100_najczesciej_edytowanych_artykulow_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("--- SHAPE ---")
print(df7.shape)

print("\n--- TYPY I BRAKI ---")
print(df7.info())

print("\n--- PRÓBKA DANYCH ---")
print(df7.head())