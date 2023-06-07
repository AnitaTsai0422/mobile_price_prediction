import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, data_file: str):
        self.data_file = data_file

    def read(self):
        df = pd.read_csv(self.data_file)
        return df

    def data_split(self, df: pd.DataFrame):
        train_df, val_df = train_test_split(df, test_size=0.2, random_state=24)

        return train_df, val_df
    
    def save_data(self, df, file_path: str):
        df.to_csv(file_path, index=False) 