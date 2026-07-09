import pickle
import pandas as pd



#import the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


#model version --> this usually comes from MLFlow
MODEL_VERSION = "1.0.0"


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    output = model.predict(df)[0]
    return output