import pickle
import pandas as pd



#import the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


#model version --> this usually comes from MLFlow
MODEL_VERSION = "1.0.0"

# Getting class labels from model  this is important for matching probabilities to class names
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    #creating data frame
    df = pd.DataFrame([user_input])
    
    #predict the class
    predicted_class = model.predict(df)[0]
    
    # gettng proba for all classes
    probailities = model.predict_proba(df)[0]
    confidence = max(probailities)
    
    #creating map -> {class_name: proba}
    class_proba = dict(zip(class_labels, map(lambda p: round(p,4), probailities)))
    
    return {
        "predicted_category": predicted_class,
        'confidence': round(confidence, 4),
        "class_probabilities": class_proba
    }