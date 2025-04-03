from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))

print("Data e hora em Oslo:", data_oslo)