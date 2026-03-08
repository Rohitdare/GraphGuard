from fastapi import FastAPI
from fraud_detection.path_tracer import trace_money_flow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {"message": "GraphGuard Backend Running"}

@app.get("/trace/{account_id}")
def trace_account(account_id: str):

    graph = trace_money_flow(account_id)

    return graph