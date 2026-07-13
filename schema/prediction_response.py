from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    prediction : int = Field(
        ...,
        description='indicate Applicant default risk'
    ) 

    risk : str = Field(
        ...,
    )

    confidence : float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)"
    )

    class_probabilities : dict = Field(
        ...,
        description="Probability distribution across all possible classes"
    )