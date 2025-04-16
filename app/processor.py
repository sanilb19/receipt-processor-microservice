import math
from app.models import Receipt

def calculate_points(receipt: Receipt) -> int:
    points = 0
    # One point for every alphanumeric character in the retailer name.
    points += sum(c.isalnum() for c in receipt.retailer)

    # 50 points if the total is a round dollar amount with no cents.
    total = float(receipt.total)
    if total.is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25.
    if total % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt.
    points += (len(receipt.items) // 2) * 5

    # If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer. 
    # The result is the number of points earned.
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    # 6 points if the day in the purchase date is odd.
    if int(receipt.purchaseDate.split("-")[2]) % 2 == 1:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm
    hour = int(receipt.purchaseTime.split(":")[0])
    minute = int(receipt.purchaseTime.split(":")[1])
    if 14 <= hour < 16:
        points += 10

    return points
