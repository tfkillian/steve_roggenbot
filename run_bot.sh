#!/bin/bash
#
# run_bot.sh
#
# This script waits a random number of seconds (up to 24 hours),
# then activates a Python virtual environment and runs bot.py.

# 1. Generate a random number of seconds to sleep (0 - 86,399 = 24 hours)
SLEEP_SECONDS=$((RANDOM % 86400))
echo "Sleeping for $SLEEP_SECONDS seconds before running bot.py..."
sleep $SLEEP_SECONDS

# 2. Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3. Run the Python bot
echo "Running bot.py..."
python stevenrogganbot.py

# 4. (Optional) Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Done."
