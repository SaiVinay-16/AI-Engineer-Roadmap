import logging

# Configure logging
# Configuration = Settings
logging.basicConfig(
    filename="app.log",      # Log file name
    level=logging.INFO,      # Minimum log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log messages
logging.info("This is an INFO message.")
logging.warning("This is a WARNING message.")
logging.error("This is an ERROR message.")

print("Log messages have been saved to app.log")