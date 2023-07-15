# Import Libries
import os
import joblib
import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

# Get Argument
if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", type=str, default=os.getenv("SM_CHANNEL_TRAIN"))
    parser.add_argument("--test", type=str, default=os.getenv("SM_CHANNEL_TEST"))
    parser.add_argument("--model-dir", type=str, default=os.getenv("SM_MODEL_DIR"))
    
    args, _ = parser.parse_known_args()
    
    # Get dataset for model training
    df_train = pd.read_csv(os.path.join(args.train, "train.csv"))
    df_test = pd.read_csv(os.path.join(args.test, "test.csv"))
    
    # Split dataset into features and labels
    x_train = df_train.drop("Loan_Status",axis=1)
    x_test = df_test.drop("Loan_Status", axis=1)
    
    y_train = df_train["Loan_Status"]
    y_test = df_test["Loan_Status"]
    
    # Initialize random forest
    clf = RandomForestClassifier()
    clf.fit(x_train, y_train)
    
    # Display prediction
    y_pred = clf.predict(x_test)
    
    print(f"\n\nAccuracy_score: {round(accuracy_score(y_test, y_pred),3)}")
    print(f"f1 score: {round(f1_score(y_test, y_pred), 3)}")
    print(f"Recal score: {round(recall_score(y_test, y_pred),3)}")
    print(f"Precision score: {round(precision_score(y_test, y_pred),3)}\n\n")

    # Save model
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))