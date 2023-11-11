from datetime import datetime

# Define the start and end times
start_time_str = "13:15"
end_time_str = "23:50"

# Convert string times to datetime objects
start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

# Calculate the duration
duration = end_time - start_time

# Print the result
print(f"You worked for {duration}")