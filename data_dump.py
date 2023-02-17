import pymongo
import pandas as pd
import json


username = input("Enter MongoDB username : ")
password = input("Enter Password : ")
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.27vjcn4.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"/config/workspace/insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PREMIUM_PREDICTION"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")

    df.reset_index(drop = True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many((json_record))

