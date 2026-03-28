import pandas as pd

try:
    df = pd.read_excel('Data.xlsx')
    print(df.head())
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
except Exception as e:
    print(f"Error: {e}")
