path="/Users/kimseunghyuck/.kaggle/competitions/titanic/"
file=["gender_submission.csv","test.csv","train.csv"]
import pandas as pd
import numpy as np
file1pd=pd.read_csv(path+file[2])
file1pd[:5]
file1pd.shape #(891,12)
file1pd.columns.values
#array(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 
#'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], dtype=object)

