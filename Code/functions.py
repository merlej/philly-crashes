import pandas as pd

# Create a function to replace empty string with 'NA'
def replace_empty_strings(df, val):
    for c in df.columns:
        if df[str(c)].dtype == 'object':
            df[str(c)].replace(' ', val, inplace=True)
    return df