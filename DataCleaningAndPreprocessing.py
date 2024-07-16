import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

def clean_and_preprocess(df):
    df = df.dropna(subset=['A', 'B'])

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df.loc[:, numeric_cols] = scaler.fit_transform(df[numeric_cols])

    categorical_cols = df.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(sparse_output=False)
    encoded_cols = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_cols))

    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df.reset_index(drop=True), encoded_df], axis=1)

    return df

# Example DataFrame
data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': ['cat', 'dog', 'cat', 'dog']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

cleaned_df = clean_and_preprocess(df)
print("Cleaned and Preprocessed DataFrame:")
print(cleaned_df)
