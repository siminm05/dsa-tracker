from datetime import date, timedelta

INTERVALS = [1, 3, 7, 14, 30]  # days to wait before each review

def next_review_date(review_count, from_date=None):
    from_date = from_date or date.today()
    index = min(review_count, len(INTERVALS) - 1)
    return from_date + timedelta(days=INTERVALS[index])

if __name__ == "__main__":
    print(next_review_date(0))   # tomorrow
    print(next_review_date(1))   # 3 days from today
    print(next_review_date(99))  # 30 days from today