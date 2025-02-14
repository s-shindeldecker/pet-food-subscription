import uuid
import time

# Number of records to generate
NUM_RECORDS = 100

# Generate data
data = []
context_keys = set()

for _ in range(NUM_RECORDS):
    context_key = str(uuid.uuid4())
    context_keys.add(context_key)
    timestamp = int(time.time() * 1000)  # Current time in milliseconds
    
    # Create the line with exact formatting - no spaces between fields, commas between all fields
    line = f'"convert_to_paid","user","{context_key}","",{timestamp}'
    data.append(line)

# Write the main file
with open('event_data.csv', 'w') as f:
    for line in data:
        f.write(f"{line}\n")

print(f"Generated {NUM_RECORDS} records in event_data.csv")

# Write the unique context keys to a separate file
with open('context_keys.txt', 'w') as f:
    for key in context_keys:
        f.write(f"{key}\n")

print(f"Saved {len(context_keys)} unique context keys to context_keys.txt")

# Show sample of generated data
print("\nSample data format:")
print(data[0])
