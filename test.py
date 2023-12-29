from datetime import datetime, timedelta

# Define the start and end times
start_time_str = "14:40"
end_time_str = "20:00"

# Convert string times to datetime objects
start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

# Calculate the duration
duration = end_time - start_time

# Print the result
print(f"You worked for {duration}")
