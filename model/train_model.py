import joblib
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


class PipeModel:
    def __init__(self, estimator, feature, target) -> None:
        #  TODO:check the correct error type
        if not isinstance(estimator, Pipeline):

            raise ValueError('must be pipeline object of skleran')

        self.estimator = estimator # pipeline
        self.feature = feature
        self.target = target
    
    def train_model(self, df):
        X_train = df[self.feature]
        y_train = df[self.target]
        self.estimator = self.estimator.fit(X_train, y_train)

    def save(self, path):
        joblib.dump(self.estimator, f'{path}/pipelineobj.joblib') 

    @staticmethod
    def load(file_path):
        obj = joblib.load(file_path)
        return obj

    def evaluate(self, df):
        X_val = df[self.feature]
        y_val = df[self.target]
        pred = self.estimator.predict(X_val)
        eval_accuracy = accuracy_score(y_val, pred)
        return eval_accuracy