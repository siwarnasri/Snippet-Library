# Define and do run

with mlflow.start_run(run_name="Churn Prediction model run 1") as run:
     # Define model parameters
     penalty = "l2"

     # Define model

     log_reg_model = LogisticRegression(solver='lbfgs', penalty=penalty)
     log_reg_model.fit(X_train, y_train)

     y_pred_model = log_reg_model.predict(X_test)
     predictions_test= log_reg_model.predict_proba(X_test)[:,1]

     accuracy = accuracy_score(y_pred_model, y_test)
     auc_score = roc_auc_score(y_test, predictions_test)

     # Log parameters

     mlflow.log_param("penalty", penalty)

     # Log metrics

     mlflow.log_metric("accuracy", accuracy)
     mlflow.log_metric("auc_score", auc_score)


     # log model with all objects referenced

     pyfunc.log_model(
         artifact_path = "churn_pyfunc",
         python_model = Churn_Model(model=log_reg_model),
         conda_env = mlflow_env)

     # Save run_id and experiment_id

     run_id = run.info.run_uuid
     experiment_id = run.info.experiment_id

     # End run

     mlflow.end_run()  
