from src.Project4.utils.common import save_bin, logger
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from src.Project4.entity.config_entity import Model_Trainer_Config
import os


class Model_Trainer:
    def __init__(self, config: Model_Trainer_Config):
        self.config = config
        self.models = {
            'LogisticRegression': LogisticRegression(),
            'KNeighborsClassifier': KNeighborsClassifier(),
            'GaussianNB': GaussianNB(),
            'DecisionTreeClassifier': DecisionTreeClassifier(),
            'RandomForestClassifier': RandomForestClassifier(),
            'SVC': SVC(),
            'GradientBoostingClassifier': GradientBoostingClassifier()
        }

    def finetune_best_model(self, best_model, model_name, X_train, y_train):
        logger.info(f'Finetuning Best Model')
        param_grid = getattr(self.config.params, model_name)
        searcher = GridSearchCV(best_model, param_grid=param_grid)
        searcher.fit(X_train, y_train)
        best_params = searcher.best_params_
        logger.info("best params are:")
        logger.info(best_params)
        logger.info("best score is:", searcher.best_score_)
        finetuned_model = best_model.set_params(**best_params)
        return finetuned_model

    def train_model(self):
        train_data_path = self.config.train_path
        test_data_path = self.config.test_path

        df_train = pd.read_csv(train_data_path)
        X_train = df_train.iloc[:, :-1]
        y_train = df_train.iloc[:, -1]

        df_test = pd.read_csv(test_data_path)
        X_test = df_test.iloc[:, :-1]
        y_test = df_test.iloc[:, -1]

        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        report = {}
        for i in self.models:
            logger.info(f'Training on Model: {i}')
            self.models[i].fit(X_train_scaled, y_train)
            logger.info(f'Finished Training Model: {i}')
            preds = self.models[i].predict(X_test_scaled)
            accuracy = accuracy_score(y_test, preds)
            report[i] = accuracy
            logger.info(f'Successfully Finised Evaluating Model: {i}')
            logger.info(f'Model: {i}, Accuracy: {accuracy}')
            logger.info('--------------------------------------------')

        best_model_score = max(sorted(report.values()))
        best_model_name = list(self.models.keys())[list(
            report.values()).index(best_model_score)]
        best_model = self.models[best_model_name]
        # fine_tuned = False
        # fine_tuned_model = self.finetune_best_model(best_model, best_model_name, X_train=X_train, y_train=y_train)
        # fine_tuned = True
        # if not fine_tuned:
        #     fine_tuned_model = best_model
        
        joblib.dump(best_model, os.path.join(
            self.config.root_dir, 'model.joblib'))
        
        print(f'Best Model: {best_model_name}, Accuracy: {best_model_score}')
