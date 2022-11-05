# Define and do run

with mlflow.start_run(run_name="Churn Prediction model run 2") as run:

     #Define model parameters

     n_estimators = 1500
     learning_rate = 0.1
     max_depth = 4

     # Define model

     xgb_model = XGBClassifier(learning_rate=learning_rate,
                               n_estimators=n_estimators,
                               max_depth=max_depth)

     xgb_model.fit(X_train, y_train)

     y_pred_model = xgb_model.predict(X_test)
     predictions_test= xgb_model.predict_proba(X_test)[:,1]

     accuracy = accuracy_score(y_pred_model, y_test)
     auc_score = roc_auc_score(y_test, predictions_test)

     # Log parameters

     mlflow.log_param("n_estimators", n_estimators)
     mlflow.log_param("learning_rate", learning_rate)
     mlflow.log_param("max_depth", max_depth)

     # Log metrics

     mlflow.log_metric("accuracy", accuracy)
     mlflow.log_metric("auc_score", auc_score)

     # log model with all objects referenced

     pyfunc.log_model(
         artifact_path = "churn_pyfunc",
         python_model = Churn_Model(model=xgb_model),
         conda_env = mlflow_env)

     # Save run_id and experiment_id

     run_id = run.info.run_uuid
     experiment_id = run.info.experiment_id

     # End run

     mlflow.end_run()  
