from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Payment API")

class Payment(BaseModel):
    amount: float
    currency: str = "HKD"
    description: str | None = None

# In-memory store for skeleton (replace with Postgres later)
payments = {}

@app.post("/payments")
def create_payment(payment: Payment):
    payment_id = len(payments) + 1
    payments[payment_id] = payment.model_dump()
    return {"id": payment_id, "status": "created"}

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    if payment_id not in payments:
        raise HTTPException(status_code=404, detail="Not found")
    return payments[payment_id]

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
