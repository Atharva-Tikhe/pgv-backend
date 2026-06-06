from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import json
from datetime import datetime


class MetadataRequest(BaseModel):
    target: str


class InterpretationRequest(BaseModel):
    sample_id: str
    interpretation: str


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:5173",  # Your Vite React app's local address
    "http://daedalus.ncl.ac.uk:5173",
    "http://daedalus.ncl.ac.uk:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/version")
def send_ver():
    return JSONResponse({"version": "0.0.1"})


@app.post("/sample/metadata")
def send_meta(target: MetadataRequest):
    print(target)
    df = pd.read_csv("./b1_CIMS.csv")
    meta = df[df["RegId"] == int(target.target)].to_json()
    return {"meta": meta}


@app.get("/samples")
def send_sample():
    df = pd.read_csv("./b1_CIMS.csv")
    meta = df["RegId"].unique().tolist()
    print(meta)
    return {"samples": meta}


@app.get("/samples/batch/1")
def send_batch_wise():
    return JSONResponse(json.load(open("./samples_b1.json", "r")))


@app.post("/samples/interpretation/")
def get_interpretation(req: InterpretationRequest):
    sample = req.sample_id
    data = req.interpretation
    print(data, sample)

    with open(f"./static/interpretations/{sample}.txt", "a") as f:
        f.writelines([str(datetime.now()), "\t", data, str("\n")])

    return JSONResponse({"status": "ok"})
