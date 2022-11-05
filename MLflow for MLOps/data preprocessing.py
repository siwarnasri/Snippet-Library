# Training data preprocessing function

def train_preprocessing(df,
                 numeric_columns,
                 categorical_columns,
                 scaler):

     new_churn = df[set(numeric_columns + categorical_columns)].copy()
     new_churn[numeric_columns] = scaler.fit_transform(new_churn[numeric_columns])
     churn_dummies = pd.get_dummies(new_churn[categorical_columns], drop_first=True)
     new_churn = pd.concat([new_churn, churn_dummies], axis=1)
     new_churn.drop(categorical_columns, axis=1, inplace = True)

     return new_churn  
