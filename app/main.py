from fastapi import FastAPI, HTTPException
from app.models import Receipt
from app.store import save_receipt, get_points
from app.processor import calculate_points


app = FastAPI()


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = save_receipt(receipt)
    return {"id": receipt_id}

@app.get("/receipts/{receipt_id}/points")
def get_receipt_points(receipt_id: str):
    receipt = get_points(receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    points = calculate_points(receipt)
    return {"points": points}
