from typing import Union
from ersilia import ErsiliaModel

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict")
def predict_ersilia():
    input = [
        "C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]",
        "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
    ]
    
    with ErsiliaModel("eos2v11") as mdl:
        results = mdl.predict(input)

    return results
