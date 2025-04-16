import uuid

store = {}

def save_receipt(receipt):
    receipt_id = str(uuid.uuid4())
    store[receipt_id] = receipt
    return receipt_id

def get_points(receipt_id):
    receipt = store.get(receipt_id)
    return receipt
