from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities



#validation using pydantic
class UserInput(BaseModel):
    
    age: Annotated[int, Field(..., gt=0, lt=70, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=10, description="Weight of the User in Kg")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user in meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Anual income of the user in lpa")]
    smoker: Annotated[bool, Field(..., description="Is the user a smoker")]
    city: Annotated[str, Field(..., description="The city user lives in")]
    occupation: Annotated[Literal["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job" ], Field(..., description="Occupation of the user")]
    
    
    
    
    @field_validator("city")
    @classmethod
    def normalize_city(cls, value: str) -> str:
        value = value.strip().title()
        return value
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    
    @computed_field
    @property
    def lifeStyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low" 
        
    @computed_field
    @property
    def ageGroup(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
  