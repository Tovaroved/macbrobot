from datetime import datetime, timedelta

start_time_str = "12:50"
end_time_str = "23:30"

start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

duration = end_time - start_time

print(f"{duration}")
