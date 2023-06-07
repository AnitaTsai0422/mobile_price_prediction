class Prediction:
    def __init__(self, model, feature):
        self.model = model
        self.feature = feature
    
    def predict(self, df):
        X = df[self.feature]
        df['pred'] = self.model.predict(X)
        return df
    
    def save(df, path):
        df.to_csv(f'{path}/prediction.csv')