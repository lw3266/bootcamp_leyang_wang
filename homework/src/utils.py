def get_summary_stats(df):
    if 'category' in df.columns:
        return df.groupby(['category']).describe()
    else:
        print('dataframe does not contain column: "category"')

# source: stage04 notebook by Prof. Jason Yarmish
def validate_df(df: pd.DataFrame, required_cols: List[str], dtypes_map: Dict[str, str]) -> Dict[str, str]:
    msgs = {}
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        msgs['missing_cols'] = f"Missing columns: {missing}"
    for col, dtype in dtypes_map.items():
        if col in df.columns:
            try:
                if dtype == 'datetime64[ns]':
                    pd.to_datetime(df[col])
                elif dtype == 'float':
                    pd.to_numeric(df[col])
            except Exception as e:
                msgs[f'dtype_{col}'] = f"Failed to coerce {col} to {dtype}: {e}"
    na_counts = df.isna().sum().sum()
    msgs['na_total'] = f"Total NA values: {na_counts}"
    return msgs