import pandas as pd

def get_summary_stats(df):
    if 'category' in df.columns:
        return df.groupby(['category']).describe()
    else:
        print('dataframe does not contain column: "category"')