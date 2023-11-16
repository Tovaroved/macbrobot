from datetime import datetime

# Define the start and end times
start_time_str = "12:35"
end_time_str = "20:20"

# Convert string times to datetime objects
start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

# Calculate the duration
duration = end_time - start_time

# Print the result
print(f"You worked for {duration}")