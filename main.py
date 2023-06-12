from typing import Union, List
from pydantic import BaseModel
from ersilia import ErsiliaModel

from fastapi import FastAPI

app = FastAPI()


class ModelId(BaseModel):
    model_id: str


class InputData(BaseModel):
    input: List[str]


@app.get("/")
def read_root():
    return {"Welcome": "To Ersilia!"}


@app.post("/info")
def info_ersilia(model_id: ModelId):
    with ErsiliaModel(model_id) as mdl:
        info = mdl.info()
    return info


@app.post("/run")
def run_ersilia(model_id: ModelId, input_data: InputData):
    # input_data = ["C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]", "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"]
    with ErsiliaModel(model_id) as mdl:
        results = mdl.run(input_data)
    return results
