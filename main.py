from typing import Union, List
from pydantic import BaseModel
from ersilia import ErsiliaModel
from ersilia.hub.fetch import ModelFetcher
from ersilia.hub.content import ModelCatalog

from fastapi import FastAPI

app = FastAPI()


class ModelId(BaseModel):
    model_id: str


class InputData(BaseModel):
    input: List[str]


class IntegerData(BaseModel):
    number: int


@app.get("/")
def read_root():
    return {"Welcome": "To Ersilia!"}


@app.get("/catalog")
def catalog_ersilia():
    mc = ModelCatalog()
    return mc.get()


@app.post("/serve")
def serve_ersilia(model_id: ModelId):
    return

@app.get("/close")
def close_ersilia():
    return


@app.get("/current")
def current_ersilia():
    return ["foo"]

@app.post("/fetch")
def fetch_ersilia(model_id: ModelId):
    mf = ModelFetcher()
    mf.fetch(model_id)


@app.post("/info")
def info_ersilia(model_id: ModelId):
    with ErsiliaModel(model_id) as mdl:
        info = mdl.info()
    return info


@app.post("/example")
def example_ersilia(model_id: ModelId, n_samples: IntegerData):
    with ErsiliaModel(model_id) as mdl:
        samples = mdl.example()
    return samples


@app.post("/run")
def run_ersilia(model_id: ModelId, input_data: InputData):
    with ErsiliaModel(model_id) as mdl:
        results = mdl.run(input_data)
    return results
