import ldclient
from ldclient.config import Config
import time
import json
from datetime import datetime
import os

# Get SDK key from environment variable
sdk_key = os.getenv('LAUNCHDARKLY_SDK_KEY')
if not sdk_key:
    print("Error: LAUNCHDARKLY_SDK_KEY environment variable is not set")
    exit(1)

# Initialize the LaunchDarkly client
ldclient.set_config(Config(sdk_key))

# Get the client instance
ld_client = ldclient.get()

# Wait for client to initialize
if ld_client.is_initialized():
    print("LaunchDarkly client initialized")
else:
    print("LaunchDarkly client failed to initialize")
    exit(1)

# Read context keys from file
with open('context_keys.txt', 'r') as f:
    context_keys = [line.strip() for line in f.readlines()]

# Create or append to log file
log_filename = f'variation_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

try:
    for context_key in context_keys:
        # Create context object
        context = {
            "kind": "user",
            "key": context_key
        }

        # Get variation detail for boolean flag
        detail = ld_client.variation_detail("hero-image", context, False)

        # Create log entry
        log_entry = {
            "timestamp": int(time.time() * 1000),
            "context_key": context_key,
            "flag_key": "hero-image",
            "value": detail.value,
            "variation_index": detail.variation_index,
            "reason": detail.reason
        }

        # Write to log file
        with open(log_filename, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        # Sleep for a few microseconds (1000 microseconds = 1 millisecond)
        time.sleep(0.001)  # 1 millisecond delay

    print(f"Completed testing variations. Results written to {log_filename}")

finally:
    # Close the LaunchDarkly client
    ld_client.close()
