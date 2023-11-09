from datetime import datetime

def calculate_fine(return_date):
    current_time = datetime.utcnow()
    difference = current_time - return_date

    days_overdue = difference.days

    fine_amount = max(0, days_overdue) * 0.20

    return fine_amount