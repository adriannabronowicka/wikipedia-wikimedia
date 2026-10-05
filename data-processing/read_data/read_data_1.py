import pandas as pd

df1 = pd.read_csv("../csv_files/1-ogladalnosc_monthly.csv")

pd.set_option('display.expand_frame_repr', False)


print("OGLADANOSC")
print("--- SHAPE ---")
print(df1.shape)

print("\n--- TYPY I BRAKI ---")
print(df1.info())

print("\n--- PRÓBKA DANYCH ---")
print(df1.head())

print(df1["agent"].unique())