import pandas as pd

def fill_missing_median(df, cols):
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(df[col].median(numeric_only=True))

    return df

def drop_missing(df, threshold):
    df.dropna()
    return df

def normalize_data(df, cols):
    for col in cols:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df