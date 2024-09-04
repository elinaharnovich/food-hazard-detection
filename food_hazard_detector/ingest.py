import os
import pandas as pd
import minsearch

DATA_PATH = os.getenv("DATA_PATH", "../data/incidents_train.csv")

def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path, index_col=False, dtype=str)
    df = df.rename(columns={"Unnamed: 0": "id", "hazard-category": "hazard_category", "product-category": "product_category"})

    documents = df.to_dict(orient='records')

    index = minsearch.Index(
        text_fields=['title', 'hazard_category', 'product_category', 'hazard', 'product'],
        keyword_fields=['id']
    )
    index.fit(documents)
    return index
