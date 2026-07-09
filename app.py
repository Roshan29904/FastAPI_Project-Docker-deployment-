from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

# make a FastAPI instance
app = FastAPI()

        
# creating a root endpoint
@app.get("/")
def home():
    return {
        "message": "Insurance Premium Prediction API",
    }



# health check endpoint -> it is for machine readable
@app.get("/health")
def health_check():
     return {
         "status": "ok",
         "version": MODEL_VERSION,
         "model_loaded": model is not None
     }


# creating predict endpoint         
@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    
    user_input = {
            "bmi": data.bmi,
            "age_group": data.ageGroup,
            "lifestyle_risk": data.lifeStyle_risk,
            "city_tier": data.city_tier,  
            "income_lpa": data.income_lpa,
            "occupation": data.occupation
        }
    try:
        prediction = predict_output(user_input)
            
        return JSONResponse(status_code=200, content={"response": prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
        
   
   

# to run fastapi ---> uvicorn app:app --reload 